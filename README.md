# Soufiane Elbiki

## Payments & Distributed Systems · Data Analytics & Decision Science · Applied AI/ML · Full-Stack Product Engineering

I build systems where correctness, explicit failure handling, measurable quality, and defensible data interpretation matter more than demo-only feature count. This GitHub is one coherent portfolio for engineering and data roles rather than a collection of unrelated tutorials.

## Flagship projects

| Project | Best fit | Merged evidence |
|---|---|---|
| [AtlasPay](https://github.com/soufianeelbiki1/AtlasPay) | Payments / Backend / Distributed Systems | ISO 8583 + EMV boundaries, scoped ISO 20022 projection, routing, timeout/late/reversal semantics, durable idempotency, double-entry ledger, transactional outbox, reconciliation, observability, fault injection, PostgreSQL analytics |
| [AtlasAnalytics](https://github.com/soufianeelbiki1/AtlasAnalytics) | Data Analyst / Analytics Engineer / Data Scientist | DuckDB payments warehouse, explicit fact grains, issuer/decline marts, rolling baselines, synthetic executive findings, leakage-safe fraud/risk evaluation, cost-sensitive thresholds, calibration, PSI |
| [ExperimentLab](https://github.com/soufianeelbiki1/ExperimentLab) | Product Analyst / Data Scientist | Experiment warehouse, SRM, two-proportion inference, CUPED, bootstrap uncertainty, ship/hold policy, power and minimum-detectable-effect planning |
| [RetailIntel](https://github.com/soufianeelbiki1/RetailIntel) | Data Analyst / Analytics Engineer | Retail warehouse, margin/returns, supplier reliability, RFM/cohorts, descriptive promotion economics, dense SKU-day demand, time-safe forecast baseline, safety stock and reorder decisions |
| [AtlasRAG](https://github.com/soufianeelbiki1/AtlasRAG) | AI / LLM Engineer | Citation-first RAG, abstention, durable PostgreSQL ingestion, hybrid rank fusion, reranking contract, versioned regression evaluation, provider token/cost/latency accounting |
| [ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) | Applied ML / CV Engineering | Explainable passport-photo policy, geometry/quality rules, estimator interfaces, FastAPI signal inference, synthetic regression evaluation, licensed held-out evaluation contract |
| [Nexus](https://github.com/soufianeelbiki1/Nexus) | Full-Stack / Platform Engineering | Strict Next.js/TypeScript operator plane, authenticated AtlasPay API consumption, runtime validation, fail-closed live behavior, unavailable-state semantics, transaction/reconciliation workflows |

The [portfolio](https://github.com/soufianeelbiki1/portfolio) repository is the public case-study surface for these projects rather than a standalone technical project to list on a CV.

## Data analytics & decision science

### AtlasAnalytics

The dedicated payments analytics flagship separates monetary payment facts from authorization-attempt operational facts so retries cannot inflate volume. Current evidence includes:

- reproducible synthetic payment warehouse in DuckDB;
- payment, authorization, reversal, reconciliation, issuer and currency grains;
- payment/issuer/decline marts with advanced SQL window logic;
- rolling issuer baselines and anomaly scoring;
- synthetic executive findings with explicit evidence labels;
- chronological fraud/risk splits to prevent future-to-past leakage;
- precision, recall, FPR, alert-rate and amount-sensitive expected-cost evaluation;
- cost-optimal threshold selection, calibration bins and PSI monitoring.

No synthetic finding is presented as a production merchant, issuer or fraud-loss result.

### ExperimentLab

ExperimentLab shows experimentation reasoning beyond a p-value:

- assignment integrity and Sample Ratio Mismatch checks;
- two-proportion treatment-effect estimation with confidence intervals;
- CUPED adjustment using pre-treatment covariates;
- deterministic bootstrap intervals for skewed outcomes;
- explicit `ship`, `hold` and `do_not_ship` decision policy;
- sample-size and minimum-detectable-effect planning;
- fixed-horizon, sequential-look and business-impact caveats.

All current experiment observations are reproducibly synthetic.

### RetailIntel

RetailIntel turns a commercial warehouse into concrete inventory and merchandising decisions:

- product-day gross/net sales, returns, COGS and margin;
- latest-SKU inventory actions and supplier reliability;
- customer RFM and acquisition cohorts;
- descriptive promotion/category economics without causal-lift claims;
- dense SKU × calendar-day demand including zero-demand days;
- seven-day trailing forecasts using prior observations only;
- demand volatility and forecast error;
- explicit 95% service-level assumption, safety stock, reorder point, inventory position and recommended reorder quantity.

## Engineering evidence

### AtlasPay

AtlasPay models payment-system failure modes rather than a CRUD happy path. It combines ISO 8583/EMV boundaries, canonical authorization mapping, issuer/acquirer routing, STAN/RRN correlation, timeout/late/duplicate outcomes, reversal correlation, PostgreSQL idempotency, append-only double-entry accounting, transactional outbox delivery, reconciliation, operator aggregation and deterministic fault injection. External delivery is never described as exactly-once.

### Nexus

Nexus is the typed operator plane for AtlasPay. A configured live source is authenticated and runtime-validated. Configuration, authentication, transport or contract failure renders unavailable state rather than silently substituting fixture telemetry. Richer issuer/network views remain fixture-only until AtlasPay exposes durable network-history contracts.

### AtlasRAG

AtlasRAG is evaluation-first rather than chat-UI-first: citation-first responses, weak-evidence abstention, replay-safe durable ingestion, PostgreSQL constraints, reciprocal-rank fusion across retriever ports, reranking contracts, versioned RAG regression data and provider usage/cost/latency accounting. A semantic/vector retriever is not called measured until it is actually evaluated.

### ForecastLab

ForecastLab separates explainable compliance policy from future raw-image estimators. It has versioned geometry/quality rules, estimator interfaces, FastAPI signal evaluation, synthetic regression coverage and licensed held-out evaluation infrastructure. It does not claim ICAO certification or unmeasured real-world CV accuracy.

## Role lenses

- **Data Analyst:** AtlasAnalytics → RetailIntel → ExperimentLab
- **Analytics Engineer:** AtlasAnalytics → RetailIntel → AtlasPay analytics
- **Data Scientist:** ExperimentLab → AtlasAnalytics risk evaluation → ForecastLab / AtlasRAG evaluation
- **Payments / FinTech:** AtlasPay → Nexus
- **Backend / Distributed Systems:** AtlasPay → AtlasRAG durability → Nexus
- **Full Stack:** Nexus → AtlasPay
- **AI / LLM / ML:** AtlasRAG → ForecastLab

## Principles

- Fix failing lint, tests, types, builds, security and data contracts before adding features.
- Define analytical grain, time semantics, currency semantics and unavailable data explicitly.
- Prefer durable invariants and explicit failure states over happy-path claims.
- Never imply vague exactly-once behavior across external boundaries.
- Use confidence intervals, experiment-integrity checks, leakage control, calibration, expected cost and validation strategy where they fit the decision.
- Back claims with tests, CI, datasets, metrics, reproducible analysis or architecture decisions.
- Never publish fake production traffic, fabricated live telemetry, unsupported business impact, unmeasured model accuracy or unverified live URLs.

## What I would put on a CV

I would select 3–5 projects based on the role rather than listing every repository. The strongest current combinations are:

- **Data roles:** AtlasAnalytics, RetailIntel, ExperimentLab, AtlasPay analytics.
- **Backend / payments:** AtlasPay, Nexus, AtlasRAG.
- **AI / ML:** AtlasRAG, ForecastLab, plus AtlasPay as reliability evidence.
