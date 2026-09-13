# Soufiane Elbiki

### Backend-first software engineer · Java / Spring Boot · TypeScript / React

I build backend services, the interfaces people use to operate them, and the data workflows that help teams make decisions.

Based in Morocco. ENSIAS engineering graduate. Open to international remote roles and freelance projects.

[Explore my work](https://soufiane-portfolio-delta.vercel.app) · [LinkedIn](https://www.linkedin.com/in/soufiane-elbiki/) · [Email](mailto:elbikisoufiane@gmail.com)

---

## Selected work

### 01 / Payment operations — AtlasPay + Nexus

What happens when a payment request times out, a retry arrives, or an operator needs to reconcile the ledger?

**AtlasPay** explores these questions through a Java 21 / Spring Boot authorization service, a Python payment API, PostgreSQL persistence, a double-entry ledger and transactional outbox delivery. **Nexus** provides the Next.js / TypeScript operations console, including explicit stale, partial and unavailable states.

[Backend & architecture](https://github.com/soufianeelbiki1/AtlasPay) · [Operator console](https://github.com/soufianeelbiki1/Nexus) · [Run the integrated demo](https://github.com/soufianeelbiki1/Nexus/blob/main/docs/LOCAL_DEMO.md)

### 02 / Inventory decisions — RetailIntel

Which products need attention, how much should be reordered, and how reliable are the suppliers?

A DuckDB retail warehouse with demand history, margin analysis, customer cohorts and transparent replenishment calculations. Includes a browser dashboard generated from reproducible synthetic data.

[Repository & dashboard setup](https://github.com/soufianeelbiki1/RetailIntel)

### 03 / Answers with evidence — AtlasRAG

How should a retrieval system respond when its sources are incomplete?

A Python retrieval backend with PostgreSQL ingestion, citation-aware responses, weak-evidence abstention and regression evaluation.

[Repository & evaluation](https://github.com/soufianeelbiki1/AtlasRAG)

These are personal engineering projects. Payment flows are simulated; generated datasets and evaluation limits are documented in each repository.

## Inspectable engineering evidence

- **Merged · applied AI:** AtlasRAG’s evaluation distinguishes grounded answers from clean abstention and includes a counterexample that catches excessive abstention. [Review the merged change](https://github.com/soufianeelbiki1/AtlasRAG/pull/11) · [42-test Python/PostgreSQL CI](https://github.com/soufianeelbiki1/AtlasRAG/actions/runs/34744313209)
- **Ready for review · Java/Spring Boot:** AtlasPay verifies idempotent retries, payload conflicts, concurrent requests and transaction rollback against PostgreSQL. [Review the implementation and tests](https://github.com/soufianeelbiki1/AtlasPay/pull/38)
- **Ready for review · TypeScript/platform:** Nexus locks dependencies, aligns Node 24 across CI and Docker, and tests healthy → outage → recovery without fabricated fallback data. [Review the implementation and checks](https://github.com/soufianeelbiki1/Nexus/pull/26)
- **Draft · data product:** RetailIntel compares forecast baselines and exposes uncertainty beside the inventory queue; source tests pass, while browser QA is still open. [Review the honest work in progress](https://github.com/soufianeelbiki1/RetailIntel/pull/6)

Status labels are deliberate: merged evidence is stable on `main`; review branches are not presented as published production behavior.

## What I can help with

- **Backend development:** Java / Spring Boot services, REST APIs, PostgreSQL and integration work.
- **Full-stack delivery:** React / Next.js interfaces connected to backend workflows.
- **Delivery and operations:** Docker, CI/CD, observability and failure handling.
- **Data workflows:** SQL transformations, analytical dashboards and applied AI integrations.

My professional background includes public-sector platforms and enterprise application delivery. This GitHub contains public project code and demonstrations.

## Further exploration

[AtlasAnalytics](https://github.com/soufianeelbiki1/AtlasAnalytics) — payments analytics and risk evaluation  
[ExperimentLab](https://github.com/soufianeelbiki1/ExperimentLab) — experiment validity and decision tooling  
[ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) — passport-photo compliance policy evaluation

## Get in touch

For a remote engineering role or a freelance project, [email me](mailto:elbikisoufiane@gmail.com) with the problem, the team and the expected scope.
