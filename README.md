# Soufiane Elbiki

Backend and full-stack engineer interested in payment systems, distributed systems, data platforms and applied AI.

I use this GitHub for projects where I can test failure handling, data contracts and system behavior rather than only the happy path.

## Projects

### [AtlasPay](https://github.com/soufianeelbiki1/AtlasPay)
Payment-processing reference system with ISO 8583/EMV boundaries, routing, timeout and reversal handling, PostgreSQL idempotency, double-entry accounting, a transactional outbox, reconciliation and operational metrics. Its Java 21/Spring Boot 3 authorization module adds validated REST, transactional PostgreSQL persistence, idempotency and outbox delivery beside the Python API.

### [Nexus](https://github.com/soufianeelbiki1/Nexus)
Next.js/TypeScript operations console for AtlasPay. It validates the live API contract at runtime and shows degraded/unavailable states instead of silently replacing failed live data with fixtures.

### [AtlasRAG](https://github.com/soufianeelbiki1/AtlasRAG)
FastAPI RAG backend with durable PostgreSQL ingestion, citation-aware responses, weak-evidence abstention, rank fusion, reranking hooks and regression evaluation.

### [ForecastLab](https://github.com/soufianeelbiki1/ForecastLab)
Passport-photo compliance evaluation prototype with versioned rules, estimator interfaces, FastAPI signal evaluation and held-out evaluation tooling.

### [AtlasAnalytics](https://github.com/soufianeelbiki1/AtlasAnalytics)
DuckDB payments warehouse with separate payment/authorization grains, issuer and decline analysis, rolling baselines, chronological risk evaluation, calibration and PSI monitoring.

### [ExperimentLab](https://github.com/soufianeelbiki1/ExperimentLab)
A/B-testing toolkit covering SRM, treatment-effect estimation, CUPED, bootstrap intervals, power/MDE planning and rule-based ship/hold decisions.

### [RetailIntel](https://github.com/soufianeelbiki1/RetailIntel)
Retail warehouse and inventory analysis with margin/returns, supplier reliability, RFM/cohorts, dense SKU-day demand, forecast baselines and replenishment recommendations.

## Current focus

- making AtlasPay + Nexus runnable as a compact end-to-end demo;
- improving CI/CD, security scanning and observability around the projects;
- adding interactive dashboards to the analytics repositories;
- keeping evaluation and performance claims tied to reproducible tests or datasets.

The [portfolio repository](https://github.com/soufianeelbiki1/portfolio) contains a visual index of the projects.
