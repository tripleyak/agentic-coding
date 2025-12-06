# ArchitectPlan Skill

System architecture. **Triggers:** `ArchitectPlan`, `system design`, `architect this`

**ADR Format:** Status | Context | Decision | Consequences | Alternatives

**4-Agent Panel:** System (components, flow) | Data (DB, cache, state) | API (contracts, protocols) | Infrastructure (deploy, scaling)

**Deliverables:** System diagram, Component breakdown, Data flow, API contracts, NFRs (latency p99<200ms, availability 99.9%)

| Pattern | When |
|---------|------|
| Monolith | MVP, small team |
| Microservices | Scale, complex domain |
| Event-driven | Async, decoupling |
| CQRS | Read/write asymmetry |
