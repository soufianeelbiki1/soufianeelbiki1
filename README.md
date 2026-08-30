# Soufiane Elbiki

## Payments & Distributed Systems · Data Analytics & Decision Science · Applied AI/ML

I build systems where correctness, explicit failure handling, measurable quality, and defensible data interpretation matter more than demo-only feature count. This GitHub is one coherent portfolio for engineering and data roles rather than a collection of unrelated tutorials.

## Flagship systems

| Project | Portfolio role | Merged evidence |
|---|---|---|
| [AtlasPay](https://github.com/soufianeelbiki1/AtlasPay) | Payments, distributed systems, analytics | ISO 8583/EMV/ISO 20022 boundaries, issuer routing, timeout/reversal semantics, durable idempotency, double-entry ledger, transactional outbox, reconciliation, observability, and CI-tested PostgreSQL analytics marts |
| [Nexus](https://github.com/soufianeelbiki1/Nexus) | AtlasPay operator/control plane | Strict typed operational contracts, authenticated AtlasPay API consumption, fail-closed live configuration, explicit unavailable data, and fixture-only richer network views until durable network history exists |
| [AtlasRAG](https://github.com/soufianeelbiki1/AtlasRAG) | Production AI/LLM system | Durable ingestion, citation-first retrieval, hybrid rank fusion/reranking contracts, regression evaluation, and provider token/cost/latency accounting |
| [ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) | Applied ML / CV evaluation | Explainable passport-photo policy, versioned inference contracts, quality/geometry rules, held-out evaluation infrastructure, and privacy-conscious estimator boundaries |
| [portfolio](https://github.com/soufianeelbiki1/portfolio) | Public case-study surface | Role-specific evidence for Data Analyst, Analytics Engineer, Data Scientist, Payments, Backend, Distributed Systems, and AI/ML roles |

## Data analytics & decision science

### Payments Analytics Warehouse — implemented foundation

AtlasPay now contains a first analytics layer over its durable PostgreSQL schema:

- daily payment creation cohorts by currency;
- gross amount and average ticket in integer minor units;
- current durable status composition with an explicit warning that current state is **not** historical funnel data;
- capture/refund/reversal lifecycle timing with average, p50, and p95 elapsed time;
- transactional-outbox reliability: published, unpublished, retry-limit events, average/p95 publish latency;
- daily debit-credit ledger control totals and imbalance signals;
- CI tests that execute every analytics mart against the migrated PostgreSQL schema.

The analytical rules are deliberate: currencies are never combined in monetary KPIs, operation timing is not mislabeled as issuer latency, unavailable network history is not turned into fake zeroes, and synthetic/dev data is not presented as production merchant evidence.

### Next deep analytics projects

1. **Payments Analytics Warehouse v2**  
   Persist a privacy-conscious authorization/network fact table with event time, route ID, disposition, response code family, latency, timeout/late classification, and reversal linkage. Build decline taxonomy, authorization rate by issuer/time band, timeout/reversal cohorts, anomaly checks, dimensional marts, and a decision dashboard. Never store PAN/DE55 in analytics facts.

2. **Product Experimentation Lab**  
   Model users/sessions/events/experiment assignments. Validate randomization with sample-ratio-mismatch checks, build funnel and retention cohorts, estimate treatment effects using difference in proportions plus bootstrap intervals and CUPED, add guardrails and multiple-testing/sequential-look caveats, then produce a reproducible ship/no-ship decision memo.

3. **Retail Decision Intelligence**  
   Build orders, customers, products, promotions, returns, inventory snapshots, purchase orders, and suppliers into a star schema. Analyze RFM/cohorts, gross-margin decomposition, promotion lift, stockout/overstock risk, supplier lead-time variability, and demand forecasts with time-based validation. End with reorder recommendations and scenario analysis rather than a decorative dashboard.

4. **Risk & Fraud Monitoring**  
   Use time-ordered transaction data with leakage-safe splits. Compare a rules baseline with interpretable ML, evaluate precision-recall, expected monetary cost, calibration, and threshold trade-offs, then add PSI/drift monitoring, segment diagnostics, explainability, and an analyst investigation queue. Avoid accuracy as the headline metric on imbalanced data.

5. **Public Data Operations Case Study**  
   Ingest a real open government/economic/transport dataset with source provenance, incremental loads, schema-change checks, and data-quality tests. Add SQL/Python time-series or geospatial analysis where justified, produce 3–5 reproducible findings with limitations, and publish a concise stakeholder decision brief.

Every analytics project should include the business question, provenance, data dictionary, analytical grain, data model, advanced SQL, Python/statistics, data-quality checks, reproducible pipeline, dashboard/report, quantified findings only when supported, and limitations.

## Engineering evidence

### AtlasPay

AtlasPay combines payment-protocol and distributed-systems work with durable state. It includes strict ISO 8583 codecs, canonical authorization mapping, issuer/acquirer routing, STAN/RRN correlation, explicit timeout/late/duplicate outcomes, timeout-triggered reversal correlation, DE55 BER-TLV/EMV parsing, and a scoped ISO 8583 → canonical → ISO 20022 projection with documented loss boundaries.

PostgreSQL durability includes request and operation idempotency, append-only balanced double-entry accounting, atomic capture/refund/reversal state transitions, transactional outbox persistence, at-least-once publication, idempotent consumption, reconciliation, bounded replay, operator aggregation, and analytics marts. External delivery is never described as exactly-once.

### AtlasRAG

AtlasRAG is evaluation-first rather than chat-UI-first: deterministic retrieval baselines, citation-first answers, weak-evidence abstention, durable replay-safe ingestion, PostgreSQL constraints, reciprocal-rank fusion across retriever ports, reranking contracts, RAG regression datasets, and provider usage/cost/latency accounting. A semantic/vector adapter is not called measured until it is actually evaluated.

### Nexus

Nexus is a strict Next.js/React/TypeScript AtlasPay operator application. When AtlasPay API configuration is present, it uses the authenticated `/v1/ops/snapshot` source and fails closed on configuration, authentication, transport, or contract failure instead of silently substituting fixture numbers. Live mode renders only durable fields AtlasPay actually exposes; richer issuer/transaction views remain fixture-only until durable network facts exist. No live deployment is claimed.

### ForecastLab

ForecastLab separates explainable compliance policy from future pixel estimators. It has versioned geometry/quality rules, estimator interfaces, precomputed-signal FastAPI evaluation, synthetic regression coverage, and held-out evaluation infrastructure with precision/recall/confusion metrics and named slices. It does not claim certification or unmeasured real-world computer-vision accuracy.

## Role lenses

- **Data Analyst:** AtlasPay analytics → Payments Warehouse v2 → experimentation / retail decision projects
- **Analytics Engineer:** AtlasPay PostgreSQL grains + CI-tested marts → dimensional/fact modeling → data quality and metric contracts
- **Data Scientist:** AtlasRAG / ForecastLab evaluation discipline → experimentation → forecasting / fraud cost modeling / calibration
- **Payments / FinTech:** AtlasPay → Nexus
- **Backend / Distributed Systems:** AtlasPay → Nexus → AtlasRAG durability
- **AI / LLM:** AtlasRAG → ForecastLab → AtlasPay engineering discipline

## Principles

- Fix failing lint, tests, types, builds, security, and data contracts before adding features.
- Define metric grain, time semantics, currency semantics, and unavailable data explicitly.
- Prefer explicit invariants and real failure states over happy-path demos.
- Never imply vague exactly-once behavior across external boundaries.
- Use validation strategy, confidence intervals, calibration, and expected cost where they fit the decision.
- Back claims with tests, CI, datasets, metrics, reproducible analysis, or ADRs.
- Never publish fake production traffic, fabricated live telemetry, unsupported business impact, model accuracy without held-out evidence, or unverified live URLs.

## Current build order

1. Persist AtlasPay authorization/network facts and use them for real issuer/authorization analytics in AtlasPay + Nexus.
2. Build the Product Experimentation Lab as a dedicated, reproducible analytics project.
3. Build Retail Decision Intelligence with dimensional modeling, forecasting, and inventory decisions.
4. Continue AtlasRAG measured semantic retrieval and ForecastLab real estimator/evaluation work.
5. Keep portfolio/profile claims synchronized with merged evidence and verified deployments only.
