import offline_guard
import json,os,copy,contextlib,io,time
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock,patch
import yaml
from rql_xql.pipeline.translator import TranslationService,_pipeline_cache
from rql_xql.engine.core import SemanticTranslator,_normalize_rql
from rql_xql.domain.models import TranslationMethod,TranslationResult
from rql_xql.infra.config import get_settings

OUT=[]
def record(name,fn):
 try:OUT.append({'name':name,'observed':fn()})
 except Exception as e:OUT.append({'name':name,'probe_error':str(e)})
def engine(meta=None):
 e=MagicMock();e.translate.return_value=('dataset = asset_inventory | fields xdm.asset.id',{'translation_method':'rule_engine','query_type':'config','complexity':'easy',**(meta or {})});return e
def service(e=None):
 s=TranslationService(rule_engine=e or engine());s._unified_validate=lambda q:SimpleNamespace(valid=True,issues=[]);s._check_semantic_intent=lambda *a:None;s._enforce_leak_gate=lambda *a:None;return s

def missing_live():
 s=service();r=s.translate('config from cloud.resource',use_cache=False)
 return {'live_validation_passed':r.metadata.get('live_validation_passed'),'is_valid':r.is_valid,'credentials_supplied':False}
record('missing_credentials_report_live_success',missing_live)

def cache_context():
 _pipeline_cache.clear();s=service();calls=[]
 def check(*a,**kw):calls.append(kw['cc_api_url']);return []
 s._check_cortex_execution=check
 a=s.translate('config from cloud.resource',cc_url='https://tenant-a.invalid',cc_api_key='synthetic-A',cc_api_key_id='1')
 b=s.translate('config from cloud.resource',disable_llm=True,cc_url='https://tenant-b.invalid',cc_api_key='synthetic-B',cc_api_key_id='2')
 return {'validation_targets':calls,'second_cache_hit':b.cache_hit,'same_result_object':a is b,'first_result_also_mutated_to_cache_hit':a.cache_hit}
record('cache_reuses_tenant_and_policy_context',cache_context)

def review_lost():
 s=service(engine({'requires_review':True,'confidence':0.1,'unknown_fields':['example.unknown'],'dropped_conditions':['synthetic condition']}));r=s.translate('config from cloud.resource',use_cache=False)
 return {'engine_requires_review':True,'engine_confidence':0.1,'api_needs_review':r.needs_review,'pipeline_confidence':r.confidence}
record('compiler_review_signal_lost',review_lost)

def ephemeral():
 from training.ephemeral_sft import EphemeralSFTRunner
 try:EphemeralSFTRunner('gs://synthetic-never-used').run(dry_run=True)
 except Exception as e:return {'exception':type(e).__name__,'message':str(e),'cloud_called':False}
 return {'unexpected':'dry run completed'}
record('ephemeral_sft_loader_contract',ephemeral)

def new_pairs():
 from training.ephemeral_sft import EphemeralSFTRunner
 with patch.object(EphemeralSFTRunner,'_load_last_run_timestamp',return_value=time.time()+86400):n=EphemeralSFTRunner().count_new_pairs()
 return {'new_pairs_with_future_last_run_marker':n}
record('untimestamped_examples_recounted',new_pairs)

def blind():
 t=SemanticTranslator();first=next(iter(t._gold_index.values()));t.gold_standard=[]
 q,m=t.translate(first['rql'],use_cache=False)
 return {'gold_standard_list_length':len(t.gold_standard),'private_index_length':len(t._gold_index),'translation_method':m['translation_method'],'matches_reference':q==first['xql']}
record('blind_fixture_retains_gold_lookup',blind)

def norm():
 a="config from cloud.resource where json.rule = name equals 'Prod'";b=a.replace('Prod','prod')
 return {'case_distinct_literal_queries_collide':_normalize_rql(a)==_normalize_rql(b)}
record('gold_normalization_folds_literal_case',norm)

def bulk():
 from fastapi.testclient import TestClient
 from rql_xql.api import server
 from tests.unit.test_api import _make_translation_result
 svc=MagicMock();svc.translate.return_value=_make_translation_result();parser=MagicMock();parser.parse.return_value=SimpleNamespace(valid=True,issues=[],errors=[])
 with patch.object(server,'_get_service',return_value=svc),patch.object(server,'_get_parser',return_value=parser),patch('rql_xql.infra.security.encryption.decrypt_encrypted_credentials',return_value={'cc_url':'https://synthetic.invalid','cc_api_key':'synthetic-key','cc_api_key_id':'1'}):
  c=TestClient(server.create_app());r=c.post('/translate/bulk',json={'queries':[{'id':'1','rql':'config from cloud.resource'}],'encrypted_credentials':'synthetic-encrypted-placeholder'})
  encrypted={'status':r.status_code,'credential_kwargs':{k:v for k,v in svc.translate.call_args.kwargs.items() if k.startswith('cc_')}}
  svc.reset_mock();r=c.post('/translate/bulk',json={'queries':[{'id':'1','rql':'config from cloud.resource'}],'cc_api_url':'https://synthetic.invalid','cc_api_key':'synthetic-key','cc_api_key_id':'1'})
  return {'encrypted':encrypted,'plaintext_status':r.status_code,'plaintext_forwarded':svc.translate.call_args.kwargs.get('cc_api_key')=='synthetic-key'}
record('bulk_credential_contract',bulk)

def shadow():
 s=service();s._cognitive=MagicMock();r=s.translate('config from cloud.resource',shadow_mode=True,use_cache=False);s._shadow_executor.shutdown(wait=True)
 return {'cognitive_called':s._cognitive.translate.called}
record('shadow_keyword_mismatch',shadow)

def evaluation():
 from eval.vertex_eval import EvalRunner
 s=service();svc=MagicMock();svc.translate.return_value=TranslationResult(source_query='synthetic',translated_query='dataset = asset_inventory',method=TranslationMethod.GOLD_STANDARD)
 runner=EvalRunner(enable_live_validation=False,use_vertex_eval=False);runner._service=svc
 sample=runner.evaluate_single({'rql':'synthetic','xql':'dataset = asset_inventory'},blind=True)
 return {'service_kwargs':svc.translate.call_args.kwargs,'method':sample.method}
record('blind_evaluator_does_not_disable_lookup',evaluation)

def parity_empty():
 from rql_xql.verification.unified_validator import ResultMatcher
 return {'match_rate':ResultMatcher().compare([],[]).match_rate}
record('empty_results_count_as_full_match',parity_empty)

orig=Path('/Users/justyntemme/Documents/code/RQL_XQL_Translator')
gold=yaml.safe_load((orig/'backend/gold_standard.yaml').read_text())['examples']
summary={'gold_pairs':len(gold),'gold_without_timestamp':sum(not(e.get('timestamp') or e.get('added')) for e in gold),'probes':OUT}
Path('/private/tmp/rql-xql-review/probes.json').write_text(json.dumps(summary,indent=2,default=str))
print(json.dumps(summary,indent=2,default=str))
