# Soufiane Elbiki

### Backend-first software engineer · Java / Spring Boot · TypeScript / React

I build backend services, the interfaces people use to operate them, and the
data workflows that help teams make decisions.

Based in Morocco. ENSIAS engineering graduate. Open to international remote
roles and scoped freelance projects.

[Live Nexus console](https://nexus-soufiane15.vercel.app/) ·
[Engineering case studies](https://github.com/soufianeelbiki1/portfolio/blob/3cf7187537d6e52e2a52304c66dbf9f983192bae/docs/CASE_STUDIES.md) ·
[LinkedIn](https://www.linkedin.com/in/soufiane-elbiki/) ·
[Email](mailto:elbikisoufiane@gmail.com)

---

## Selected work

### 01 / Payment operations — AtlasPay + Nexus

What happens when a payment request times out, a retry arrives, or an operator
needs to reconcile the ledger?

**AtlasPay** explores these questions through a Java 21 / Spring Boot
authorization service, a Python payment API, PostgreSQL persistence, a
double-entry ledger and transactional outbox delivery. **Nexus** provides the
Next.js / TypeScript operations console, including explicit stale, partial and
unavailable states.

[Backend and architecture](https://github.com/soufianeelbiki1/AtlasPay) ·
[Operator console](https://github.com/soufianeelbiki1/Nexus) ·
[Live read-only dashboard](https://nexus-soufiane15.vercel.app/) ·
[Run the integrated demo](https://github.com/soufianeelbiki1/Nexus/blob/65c72e204c0fb6b3b281483ffd35872c05335df4/docs/LOCAL_DEMO.md)

### 02 / Inventory decisions — RetailIntel

Which products need attention, how much should be reordered, and what evidence
supports that decision?

A DuckDB retail workflow with point-in-time demand features, transparent
replenishment calculations and visible forecast error. Its generated dashboard
records the synthetic-data seed, sample size, date range and decision cutoffs.

[Repository](https://github.com/soufianeelbiki1/RetailIntel) ·
[Decision walkthrough](https://github.com/soufianeelbiki1/RetailIntel/blob/878526db1753ecca415f4f06dc717e8d90a1f9b9/docs/DECISION_WALKTHROUGH.md)

### 03 / Answers with evidence — AtlasRAG

How should a retrieval system respond when its sources are incomplete?

A Python/PostgreSQL retrieval backend with stable citations, weak-evidence
abstention and deterministic regression evaluation. Its diagnostics separate
false abstentions from unsafe evidence responses and prevent duplicate citations
from inflating recall.

[Repository and evaluation](https://github.com/soufianeelbiki1/AtlasRAG) ·
[Merged diagnostics](https://github.com/soufianeelbiki1/AtlasRAG/pull/12)

These are personal engineering projects. Payment flows are simulated; generated
datasets and evaluation limits are documented in each repository.

## Inspectable engineering evidence

- **Published personal project · TypeScript/platform:**
  [Nexus #26](https://github.com/soufianeelbiki1/Nexus/pull/26) is merged. Its
  Node 24 locked build, 22 tests, container checks, dependency audit, authenticated
  runtime smoke and outage/recovery demo pass. The live console was browser-tested
  from desktop down to 320 px without layout overflow or WCAG A/AA axe findings.
- **Merged · data product:**
  [RetailIntel #6](https://github.com/soufianeelbiki1/RetailIntel/pull/6) adds
  auditable provenance and keyboard-accessible report tables. CI passes 35 tests
  on Python 3.11/3.12, Ruff and installed-wheel execution.
- **Merged · applied AI:**
  [AtlasRAG #12](https://github.com/soufianeelbiki1/AtlasRAG/pull/12) adds
  failure-specific evidence diagnostics. Its post-merge Python/PostgreSQL CI
  passes 44 tests on Python 3.11 and 3.12.
- **Ready for review · Java/Spring Boot:**
  [AtlasPay #38](https://github.com/soufianeelbiki1/AtlasPay/pull/38) verifies
  idempotent retries, payload conflicts, concurrent requests and rollback against
  PostgreSQL. The review head passes 36 Java/PostgreSQL and 105
  Python/PostgreSQL tests plus container checks; it is not merged or presented as
  a deployed Java release.

Status labels are deliberate: merged evidence is stable on `main`; AtlasPay's
review branch is not presented as published production behavior. Test counts
describe these repositories, not real-world traffic, adoption or scale.

## What I can help with

- **Backend development:** Java / Spring Boot services, REST APIs, PostgreSQL and
  integration work.
- **Full-stack delivery:** React / Next.js interfaces connected to backend
  workflows.
- **Delivery and operations:** Docker, CI/CD, observability and failure handling.
- **Data workflows:** SQL transformations, analytical dashboards and applied AI
  integrations.

My professional background includes public-sector platforms and enterprise
application delivery. This GitHub contains public project code and demonstrations.

## Further exploration

[AtlasAnalytics](https://github.com/soufianeelbiki1/AtlasAnalytics) — payments
analytics and risk evaluation  
[ExperimentLab](https://github.com/soufianeelbiki1/ExperimentLab) — experiment
validity and decision tooling  
[ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) — passport-photo
compliance policy evaluation

## Get in touch

For a remote engineering role or a scoped freelance project,
[email me](mailto:elbikisoufiane@gmail.com) with the problem, the team and the
expected outcome.
