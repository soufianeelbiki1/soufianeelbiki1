# Soufiane El Biki

## Payments & Distributed Systems · Applied AI/ML · Full-Stack Product Engineering

I build production-minded systems where correctness, measurable quality, and clear operational behavior matter more than demo polish. This GitHub is one coherent flagship portfolio—not a collection of unrelated tutorials.

## Flagship systems

| Project | Focus | Evidence I am building |
|---|---|---|
| [AtlasPay](https://github.com/soufianeelbiki1/AtlasPay) | Payment infrastructure | ISO 8583/EMV/ISO 20022 interoperability, idempotency, double-entry ledger, outbox/eventing, reconciliation, observability |
| [AtlasRAG](https://github.com/soufianeelbiki1/AtlasRAG) | Production AI/RAG | Ingestion, hybrid retrieval, reranking, groundedness/hallucination evaluation, provider abstraction, tenancy, tracing, cost/latency |
| [ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) | Computer vision | Passport-photo compliance signals, segmentation, explainable rule scores, heatmaps, datasets, model/version tracking, FastAPI inference |
| [Nexus](https://github.com/soufianeelbiki1/Nexus) | Operator control plane | Live transaction flows, issuer latency/auth rates, reversals, ledger/reconciliation, Kafka lag, incidents, topology, diagnostics |
| [portfolio](https://github.com/soufianeelbiki1/portfolio) | Product presentation | Clear narratives, verified demos, architecture trade-offs, synchronized links |

## Engineering operating contract

Every iteration starts with repository state and CI inspection. Regressions in lint, tests, types, builds, security, deployment, or architecture are fixed before feature work. Distributed-system claims must name their delivery semantics and failure boundaries; exactly-once is never implied across external systems. Prefer modular monoliths, explicit invariants, durable data, property-based/adversarial tests, fault injection, measurable quality, and ADRs. Never publish fake scale, fake production traffic, or unverified live URLs.

## Delivery order

AtlasPay is built vertically first: protocol codecs → payment correlation and failure handling → canonical model and interoperability → durable ledger/outbox → streaming, replay, reconciliation, and operations. Nexus starts once AtlasPay exposes meaningful operational data. AtlasRAG and ForecastLab advance in parallel with evaluation-first milestones. All READMEs and portfolio links must stay synchronized.

## Current status

- Active working branch: portfolio-build-20260829 (local development context).
- No deployment claimed: live URLs are added only after verification.
- Next highest-value milestone: strict ISO 8583 codec layer with secondary bitmap, LLVAR/LLLVAR validation, and property-based round-trip tests.

See the individual repositories for implementation details, test commands, ADRs, and verified CI/deployment evidence.
