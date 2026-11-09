# Lesson 21: Use VS Code and JetBrains security plugins

Week 3 · Lesson 21 of 45 · Objective/exercise 5.4

[Course start](../README.md) · [Previous lesson](20-cli-b-cli-b-track-a-scan-through-output-and-platform-results.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 5.4. **Practice mode:** Implement at least one and rehearse both.

**Read first:** [Visual Studio (VS) Code and VS Code compatible IDEs](https://cortex-docs.paloaltonetworks.com/application-security/code-security/ide/visual-studio-vs-code-and-vs-code-compatible-ides); [JetBrains](https://cortex-docs.paloaltonetworks.com/application-security/code-security/ide/jetbrains).

1. Check each plugin’s documented host architecture, runtime dependencies, AppSec entitlement, and CLI permissions before installing.
2. Generate a suitably scoped Standard API key and retrieve its ID and tenant API URL. Use the documented authentication fields rather than assuming an Advanced key works.
3. Install the official Cortex plugin in VS Code, configure authentication, open the lab project, and scan a known fixture. Read the finding’s explanation and apply a correction; rescan.
4. Repeat in JetBrains if installed. Otherwise, walk through its actual configuration screens from the documentation and record the required fields and dependencies.
5. Compare IDE results with the repository/CLI scan of the same commit and configuration. Investigate path exclusions or scanner differences before assuming results must be identical.

**Verify and save:** A successful IDE scan and remediation, plus configuration evidence or a complete walkthrough for the second IDE.

**Explain without notes:** What would you check when authentication works elsewhere but IDE scanning fails?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [22. Deploy AppSec rules, policies, and guardrails](22-5-2-deploy-appsec-rules-policies-and-guardrails.md)**
