# Soufiane Elbiki

## Payments & Distributed Systems · Applied AI/ML · Full-Stack Product Engineering

I build systems where correctness, explicit failure handling, observability, and measurable quality matter more than demo-only feature count. This GitHub is one coherent engineering portfolio rather than a collection of unrelated tutorials.

## Flagship systems

| Project | Role in the portfolio | Engineering direction |
|---|---|---|
| [AtlasPay](https://github.com/soufianeelbiki1/AtlasPay) | Payments & distributed-systems flagship | ISO 8583/EMV/ISO 20022 interoperability, correlation/routing, durable idempotency, double-entry ledger, outbox/eventing, replay, reconciliation, observability and failure testing |
| [Nexus](https://github.com/soufianeelbiki1/Nexus) | AtlasPay operator/control plane | Next.js/TypeScript operational UI for transaction flows, issuer latency, auth rates, reversals, ledger/reconciliation, Kafka lag, incidents, topology and diagnostics |
| [AtlasRAG](https://github.com/soufianeelbiki1/AtlasRAG) | Production AI/LLM system | Ingestion, hybrid retrieval, reranking, evaluation datasets, groundedness metrics, provider abstraction, tracing, cost/latency, tenancy, jobs and security |
| [ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) | Applied CV/ML flagship in transition | ICAO-style passport-photo compliance signals, pose/quality/illumination/background checks, segmentation, explainable rule scores, evaluation/versioning and FastAPI inference |
| [portfolio](https://github.com/soufianeelbiki1/portfolio) | Public product surface | Architecture stories, verified demos, engineering trade-offs and synchronized project links |

## Engineering principles

- Fix broken lint, tests, types, builds, security, deployment and architecture before feature work.
- Prefer explicit invariants and real failure states over happy-path demos.
- Use modular monoliths unless a service boundary has a concrete operational reason to exist.
- Treat timeouts, retries, duplicates, reversals, reconciliation and replay as first-class behavior.
- Never imply vague “exactly once” behavior across external boundaries; state the actual semantics and failure boundaries.
- Back claims with tests, CI, metrics, load/fault experiments, datasets or ADRs.
- Never publish fake scale, fake production traffic or unverified live URLs.

## Current verified progress

### AtlasPay

The strict ISO 8583 message-body codec is now merged to `main`, including primary/secondary bitmaps, fixed and LLVAR/LLLVAR fields, binary DE55 support, malformed-input tests, Hypothesis round-trip coverage, stronger CI checks, and an ADR defining at-least-once/idempotent delivery semantics and external failure boundaries.

Next high-value slices: durable persistence/idempotency, payment state/correlation, timeout and late-response handling, reversals, then ledger/outbox foundations.

### AtlasRAG

The repository has a deterministic retrieval contract and typed query/evidence models. CI and contract tests now cover Python 3.11/3.12, dependency consistency, Ruff lint/format, compilation, retrieval ranking behavior, and Pydantic bounds.

Next high-value slices: ingestion/chunking contracts, retrieval evaluation metrics, then hybrid retrieval/reranking before adding heavier infrastructure.

### Nexus, ForecastLab and portfolio

These remain early-stage and will be advanced in rotation after their foundations, CI and truthful transition/product documentation are established. Deployment links will appear only after successful, verifiable deployments.

## Build order

1. Deepen AtlasPay vertically into the flagship payments platform.
2. Build Nexus once AtlasPay exposes meaningful operational data and diagnostics.
3. Advance AtlasRAG evaluation-first toward production retrieval and LLM operations.
4. Rebuild ForecastLab around explainable passport-photo compliance CV/ML.
5. Keep this profile and the portfolio synchronized with shipped, verifiable work.
