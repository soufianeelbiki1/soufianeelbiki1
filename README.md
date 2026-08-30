# Soufiane Elbiki

## Payments & Distributed Systems · Applied AI/ML · Full-Stack Product Engineering

I build systems where correctness, explicit failure handling, observability, and measurable quality matter more than demo-only feature count. This GitHub is one coherent engineering portfolio rather than a collection of unrelated tutorials.

## Flagship systems

| Project | Role in the portfolio | Engineering direction |
|---|---|---|
| [AtlasPay](https://github.com/soufianeelbiki1/AtlasPay) | Payments & distributed-systems flagship | ISO 8583/EMV/ISO 20022 interoperability, correlation/routing, durable idempotency, double-entry ledger, outbox/eventing, replay, reconciliation, observability and failure testing |
| [Nexus](https://github.com/soufianeelbiki1/Nexus) | AtlasPay operator/control plane | Operational UI for transaction flows, issuer latency, auth rates, reversals, ledger/reconciliation, event lag, incidents, topology and diagnostics |
| [AtlasRAG](https://github.com/soufianeelbiki1/AtlasRAG) | Production AI/LLM system | Ingestion, hybrid retrieval, reranking, evaluation datasets, groundedness metrics, provider abstraction, tracing, cost/latency, tenancy, jobs and security |
| [ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) | Applied ML flagship in transition | Reproducible data/model lifecycle, explainable evaluation, versioned experiments and deployable inference |
| [portfolio](https://github.com/soufianeelbiki1/portfolio) | Public product surface | Architecture stories, role-specific hiring lenses, verified engineering evidence and synchronized project links |

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

The strict ISO 8583 message-body codec is merged to `main`, including primary/secondary bitmaps, fixed and LLVAR/LLLVAR fields, binary DE55 support, malformed-input tests, Hypothesis round-trip coverage, and CI quality gates.

The next switch-architecture slice is also merged: AtlasPay now has a protocol-independent canonical authorization model, explicit ISO 8583 ↔ canonical mapping for the supported purchase profile, numeric/alpha currency mapping, and response correlation using expected MTI plus the STAN/RRN pair. The mapping fails closed when required fields, field widths, processing codes, or currencies are unsupported.

The next network-behavior slice is now merged: a transport-independent coordinator makes timeout, late-response, duplicate, and mismatched-response outcomes explicit with deterministic tests. Next high-value slices: issuer/acquirer routing, reversal linkage, and expanded EMV/DE55 support.

### AtlasRAG

The repository has a deterministic retrieval contract and typed query/evidence models. CI and contract tests cover dependency consistency, Ruff lint/format, compilation, retrieval ranking behavior, and Pydantic bounds.

The first evaluation slice is now merged: a deterministic evaluator reports precision@k, recall@k, and MRR, rejects empty datasets, and is covered by CI. Next high-value slices: ingestion/chunking contracts, then hybrid retrieval/reranking before adding heavier infrastructure.

### Portfolio

The portfolio repository now contains a responsive, dependency-free engineering case-study site instead of an empty placeholder. It presents the same projects through payments, backend, distributed-systems, AI, platform/SRE, and ML hiring lenses while explicitly labeling early-stage work.

Its CI contract checks required case-study sections, flagship repository links, local assets, truthful early-stage status labels, and placeholder/unverified demo links. A public deployment is **not** claimed yet; a live URL will be added only after deployment is verified.

### Nexus and ForecastLab

These remain early-stage and will be advanced in rotation after their foundations, CI, and truthful transition/product documentation are established. Nexus will follow meaningful AtlasPay operational data rather than inventing a decorative control plane. ForecastLab will be rebuilt around a measurable ML lifecycle rather than notebook-only work.

## Role lenses

- **Payments / FinTech:** AtlasPay → Nexus → AtlasRAG
- **Backend:** AtlasPay → Nexus → AtlasRAG
- **Distributed Systems:** AtlasPay → Nexus → AtlasRAG
- **Platform / SRE:** Nexus + AtlasPay operational architecture
- **AI / LLM:** AtlasRAG → AtlasPay engineering discipline
- **ML:** ForecastLab → AtlasRAG → AtlasPay

## Build order

1. Deepen AtlasPay vertically into the flagship payments platform.
2. Keep the portfolio and profile synchronized with merged, verifiable work.
3. Advance AtlasRAG evaluation-first toward production retrieval and LLM operations.
4. Build Nexus once AtlasPay exposes meaningful operational data and diagnostics.
5. Rebuild ForecastLab around a reproducible, explainable ML lifecycle.
6. Add deployment links only after successful, verifiable deployments.
