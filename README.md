# Soufiane Elbiki

## Payments & Distributed Systems · Applied AI/ML · Full-Stack Product Engineering

I build systems where correctness, explicit failure handling, observability, and measurable quality matter more than demo-only feature count. This GitHub is one coherent engineering portfolio rather than a collection of unrelated tutorials.

## Flagship systems

| Project | Role in the portfolio | Verified direction |
|---|---|---|
| [AtlasPay](https://github.com/soufianeelbiki1/AtlasPay) | Payments & distributed-systems flagship | ISO 8583/canonical interoperability, issuer/acquirer routing, reversal correlation, durable idempotency, atomic double-entry ledger flows, transactional outbox, reconciliation/replay, and explicit network failure semantics |
| [Nexus](https://github.com/soufianeelbiki1/Nexus) | AtlasPay operator/control plane | Typed provenance-aware operational snapshots, degraded-source handling, issuer health, incidents, STAN/RRN transaction drill-down and reversal correlation |
| [AtlasRAG](https://github.com/soufianeelbiki1/AtlasRAG) | Production AI/LLM system | Deterministic retrieval/evaluation, citation-first query service, weak-evidence abstention, provider boundary, and replay-safe deterministic ingestion identity |
| [ForecastLab](https://github.com/soufianeelbiki1/ForecastLab) | Applied ML flagship | Explainable passport-photo compliance policy, synthetic evaluation data, rule-level metrics, and privacy-conscious estimator boundaries |
| [portfolio](https://github.com/soufianeelbiki1/portfolio) | Public product surface | Architecture stories, hiring lenses, verified engineering evidence and synchronized truth boundaries |

## Engineering principles

- Fix broken lint, tests, types, builds, security, deployment and architecture before feature work.
- Prefer explicit invariants and real failure states over happy-path demos.
- Use modular monoliths unless a service boundary has a concrete operational reason to exist.
- Treat timeouts, retries, duplicates, reversals, reconciliation and replay as first-class behavior.
- Never imply vague “exactly once” behavior across external boundaries; state the actual semantics and failure boundaries.
- Back claims with tests, CI, metrics, load/fault experiments, datasets or ADRs.
- Never publish fake scale, fake production traffic, fabricated live telemetry, model accuracy without held-out evidence, or unverified live URLs.

## Current verified progress

### AtlasPay

AtlasPay now includes a strict ISO 8583 codec and canonical authorization mapping, durable PostgreSQL request and business-operation idempotency, an append-only balanced double-entry ledger, and capture/refund/reversal operations that commit business state and ledger journals atomically.

Domain events are persisted through a transactional outbox. The reference publisher is explicitly **at least once**, consumers can deduplicate durably, failed deliveries retain retry/error state, and poison messages are not silently discarded. Deterministic reconciliation reports cross-check payments, operations, journals, entries and outbox linkage; replay controls are bounded and do not silently rewrite accounting history.

A transport-independent network coordinator makes accepted, timeout, late-response, duplicate and correlation-mismatch outcomes explicit. Issuer/acquirer routing and one-to-one reversal correlation are merged with deterministic specificity and ambiguity handling. Strict DE55 BER-TLV parsing, constructed-template recursion, duplicate preservation, EMV tag metadata and five-byte TVR decoding are also merged. A byte-oriented transport port and ISO 8583 network adapter now separate message encoding from sockets/TLS/framing; response, timeout, and local transport failure are distinct, and timeout explicitly preserves unknown external-delivery status. The merged authorization network flow now enforces canonical/wire STAN-RRN equality, routes before registration, links a timeout-triggered reversal without claiming delivery, classifies a later original response as late, and permits correlation reuse only after a known-local transport failure. Scoped ISO 20022 interoperability is the next protocol boundary.

### AtlasRAG

AtlasRAG has a deterministic lexical retriever plus precision@k, recall@k and MRR evaluation primitives. A citation-first application service filters weak evidence, abstains when support is insufficient, and exposes a credential-free FastAPI reference query path through a provider/generator boundary.

Deterministic ingestion identity is also merged: normalized SHA-256 document fingerprints, stable content-derived chunk IDs, exact replay semantics and explicit document-ID conflicts. Durable PostgreSQL document/chunk persistence with unique constraints, transaction-scoped advisory locking, replay reconstruction, and explicit content conflicts is now merged. Hybrid retrieval orchestration is also merged: reciprocal-rank fusion combines heterogeneous retriever ports without comparing uncalibrated raw backend scores, and reranking sits behind a separate contract. A measured semantic/vector adapter is still not claimed.

### Nexus

Nexus is no longer a placeholder. It is a strict Next.js/React/TypeScript operator application with typed AtlasPay operational contracts, source provenance, explicit ready/stale/partial/unavailable loading states, runtime snapshot validation, and a hard rule that invalid or unavailable source integrity renders no telemetry values.

The operator view includes authorization/outbox/ledger summaries, issuer-route health, incidents and transaction-level STAN/RRN drill-down with coordinator disposition, latency availability and linked reversal correlation/reason. Search/outcome filtering and read-only reconciliation/outbox checks are merged with explicit no-auto-repair/no-poison-discard guidance. The current source is deliberately fixture-backed rather than advertised as live telemetry.

### ForecastLab

ForecastLab now has an explainable passport-photo compliance policy over measured observations for dimensions, face count, head pose, background uniformity and occlusion. Thresholds are versionable, evidence is returned per rule, and invalid measurement ranges fail explicitly.

A versioned synthetic observation dataset provides fixed train/validation/test-style regression splits with no photographs or personal identity data. Rule-level confusion counts, precision, recall and accuracy are implemented. Privacy-conscious estimator interfaces and an observation pipeline for pose/background/occlusion plus quality signals are merged with deterministic doubles and integration tests. A separate versioned quality policy now evaluates normalized blur, compression, illumination and shadow scores with explainable thresholds and synthetic rule-level regression metrics. A FastAPI precomputed-signal endpoint returns combined geometric/quality rule evidence plus policy and estimator version metadata; it explicitly does not decode raw photos. No real-world computer-vision accuracy or certification is claimed.

### Portfolio

The portfolio case-study site is synchronized with these verified boundaries. CI checks required sections, flagship links, local assets, truthful status labels and placeholder/unverified links. A public deployment is **not** claimed until a live URL is independently verified.

## Role lenses

- **Payments / FinTech:** AtlasPay → Nexus → AtlasRAG
- **Backend:** AtlasPay → Nexus → AtlasRAG
- **Distributed Systems:** AtlasPay → Nexus → AtlasRAG
- **Platform / SRE:** Nexus + AtlasPay operational architecture
- **AI / LLM:** AtlasRAG → AtlasPay engineering discipline
- **ML:** ForecastLab → AtlasRAG → AtlasPay

## Build order

1. Keep deepening AtlasPay while preserving explicit payment/network failure boundaries.
2. Keep the portfolio and profile synchronized with merged, verifiable work.
3. Advance AtlasRAG from hybrid orchestration to a regression dataset and measured semantic/vector retrieval adapter.
4. Move Nexus from fixture-backed validated workflows to a verified AtlasPay data endpoint.
5. Move ForecastLab from signal-only inference to held-out evaluation adapters and raw-image inference behind versioned estimators.
6. Add deployment links only after successful, verifiable deployments.
