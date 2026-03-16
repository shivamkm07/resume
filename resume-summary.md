# Resume Summary — Extracted Key Items from Work History

**Role:** Software Development Engineer, Microsoft (July 2021 – Present)
- SDE 1: July 2021 – July 2024
- SDE 2: July 2024 – Present

**Team:** Azure Container Apps / Dapr, Microsoft (IDC)

---

## SDE2-Level Resume Expectations
- Ownership of features end-to-end (design → ship → operate)
- Cross-team collaboration & influence
- Quantifiable business impact (customers, clusters, latency, uptime)
- Technical leadership signals — mentoring, leading rollouts, on-call reliability
- Open-source contributions (high signal for infra/platform roles)
- Format: `[Action verb] + [What you did] + [Resulting quantifiable impact]`

---

## 🥇 Priority 1 — Strongest Resume Items

### ACA RCA / SRE Agent (AI-Powered Diagnostics)
> *Highest signal item — AI/LLM agents with dramatic quantifiable impact*

- Designed and deployed **AI-powered RCA agents** for Azure Container Apps to accelerate incident resolution — ICM Summarization Agent, CoreDNS Agent, Sessions Agent, and Billing Subagent.
- Shifted architecture from workflow-based to **investigative prompts**, dramatically improving AI-aligned RCA accuracy; closed 20+ agent backlog items through targeted analysis.
- Reduced ACA incident **P50 time-to-mitigate by 97% (185 → 6 min)** and **P50 time-to-resolve by 64% (269 → 98 min)**.
- Targets reduction of **~99 monthly CRIs** and P50 mitigation time of 88 hours by accelerating root cause analysis.
- **[NEW]** Evolving agent into **auto-repair mode** — automatically comparing agent-generated RCA vs actual RCA, creating repair items, and auto-resolving incidents that meet criteria.
- **Presented** the RCA Agent at the **IDC Pinnacle event**, showcasing impact on incident diagnostics and reliability.

### Open-Source Contributions to Dapr (CNCF Project)
> *Strong differentiator — sustained OSS contributions to a major CNCF project*

- Upgraded **MQTT PubSub** component from alpha to stable; contributed fix to upstream library; added certification tests.
- Marked **Azure CosmosDB state store** to stable; marked **Configuration API building block** stable (Dapr 1.11).
- Upgraded **Redis and PostgreSQL** configuration stores to stable with conformance/certification tests.
- Added **bulk subscribe support** in Azure Event Hubs.
- Implemented **cascade terminate and purge** for Dapr Workflows — changes spanning runtime and multiple SDKs.
- Added **Dapr Workflow performance tests**; identified several P0 bugs and collaborated on fixes.
- Enabled **airgap installation support** in Dapr; collaborated with external open-source contributor for CLI change.
- Made Dapr available in **winget** with automated package updates; built **MSI installer** for Dapr CLI.
- Published **combined coverage reports** for conformance and certification tests.
- Resolved customer issues across GitHub (Runtime, Components-Contrib, SDKs) and Discord.

---

## 🥈 Priority 2 — Strong Supporting Items

### CI/CD, Internal Fork & Release Engineering
> *Shows infra/platform ownership and automation depth*

- Architected and maintained Dapr **internal fork across 5 repositories** (dapr, cli, dashboard, components-contrib, kit) with build, code-signing, and release pipelines.
- Automated **OSS-to-internal merge** pipeline (`automerge`), achieving internal releases within **<1 day SLA** of OSS release.
- Re-designed internal repository to a **patch-based model** with separate per-service images for faster, targeted releases.
- Migrated Dapr CI/CD pipelines to **1ES (OneBranch)** for compliance; integrated **Ev2 deployment** for Standard Deployment Practices.
- Consolidated multiple Dapr pipelines into a **single OneBranch pipeline** to expedite releases.
- Added **multi-arch support** (ARM64, ARM, AMD64) for Dapr and dashboard images.
- Added **Mariner** and **distroless** images; handled **1P Container Registry migration**.
- Delivered **62 PRs** across Functions, Sessions, and AKS extension components in a single review cycle.

### Azure Container Apps Sessions — Feature Development
> *Feature ownership with clear customer-facing impact*

- Developed **Session Management APIs** (Delete, List, Get) improving observability for **~300 external customers**.
- Fixed critical **async execution bugs** in code interpreter sessions and Node.js session-specific issues.
- Enabled **early session deletion** — key requirement from the Fabric Team, reducing billing/costs for customers.
- Added **performance tests** for ACA Sessions, identifying code execution regressions.
- Enabled **.NET code interpreter support** for the Security Copilot Team.
- Developed multiple **data-plane APIs** for sessions based on internal team feedback.
- Implemented **Geneva actions** to manage upgrades for Node.js sessions.

### Dapr AKS Extension — Security & Multi-Region Rollouts
> *Production-at-scale ownership*

- Led **Dapr 1.15 and 1.16 rollouts** across all Azure regions.
- Fixed multiple **CVE/security vulnerabilities**; upgraded **~260 subscriptions** and **~400 AKS clusters** to secure versions.
- Expanded AKS extension availability to **new regions** (AustriaEast, etc.) based on customer demand.
- Integrated **CodeQL** into AKS Extension pipeline for security and code quality.
- Resolved customer-reported AKS extension ICMs promptly.

---

## 🥉 Priority 3 — Good Supplementary Items

### Azure Container Apps Functions
> *Scope expansion into a new product area*

- Implemented **function keys management commands** for ACA Functions.
- Added **invocation tracing/summary** and **durable-events logging** for diagnostics.
- Authored **API spec for Function ARM APIs**.
- Improvements benefit **~1,322 external ACA Functions apps**.
- **[NEW]** Added support for **editing KEDA scaling rules** in Azure Functions on ACA.
- **[NEW]** Implementing **drain functionality** for Azure Functions on ACA.
- **[NEW]** Working on **feature parity** between Azure Functions on ACA and native Azure Functions — closing gaps in missing capabilities.

### Foundry Control Plane (FCP) Integration for ACA Agents [NEW]
> *New area — AI platform enablement*

- **[NEW]** Enabled **Foundry Control Plane support** for agents created on ACA — all ACA-created agents now surfaced on the Foundry Control Plane, improving discoverability and management.

### Azure Key Vault Integration & Security
- Integrated **Azure Key Vault with Managed Environment Storage API**, eliminating raw connection strings in **~27K daily API calls**.
- Resolved **CodeQL violations** across container apps codebase, strengthening security posture and compliance.

### On-Call / Livesite Reliability (DRI)
> *Shows operational maturity expected at SDE2 level*

- Resolved **90+ ICMs including 13 CRIs** in a single on-call rotation.
- Handled **36 Sev2 LSIs** (P50 TTM 1h, P50 TTR 25h — outperforming ACA baselines of 3.9h/60h).
- Handled **6 Sev3 CRIs** with strong mitigation metrics.
- Resolved **~14 CRIs and ~150 LSIs** (including ~58 Sev2 alerts) in another cycle.
- Delivered **repair items** to address root causes, reducing incident recurrence.
- Improved **5 LSI alert fidelity** based on investigation findings.

---

## 🏅 Leadership & Mentoring Signals

- **Mentored new hire** Khushi, unblocking her across tasks.
- Took **ad-hoc on-call shifts** to support China team during new year leave.
- Collaborated with **Playwright testing team** on proof-of-concept using ACA Sessions.
- **Presented** ACA RCA Agent at **IDC Pinnacle event**.

---

## Skills to Highlight (based on work)

| Category | Skills |
|----------|--------|
| Languages | Go, Python, C#/.NET, JavaScript/TypeScript |
| Cloud & Azure | Azure Container Apps (ACA), AKS, Azure Functions, Azure Key Vault, Azure Event Hubs, Azure CosmosDB |
| Infrastructure | Kubernetes, Docker, Dapr (CNCF), Helm, Container Registries (MCR) |
| CI/CD | OneBranch (1ES), Ev2, ADO Pipelines, GitHub Actions |
| AI/Agents | LLM-based RCA Agents, AI-powered diagnostics, Auto-repair agents |
| Observability | Geneva, ICM, CodeQL, KEDA |
| Open Source | Dapr (CNCF) — runtime, CLI, SDKs, components-contrib |
| Practices | On-call DRI, Incident management, Security (CVE remediation), Multi-region rollouts |

---

## New Items Added (After Nov 2025) — Summary

1. **KEDA Rules Editing** — Azure Functions on ACA now supports editing KEDA scaling rules.
2. **Foundry Control Plane (FCP) for ACA Agents** — Agents created on ACA are now surfaced in the Foundry Control Plane for unified management.
3. **Drain Functionality** — Adding drain support for Azure Functions on ACA for graceful shutdowns.
4. **SRE Agent → Auto-Repair** — Evolving RCA agent to automatically compare generated vs actual RCA, create repair items, and auto-resolve qualifying incidents.
5. **Azure Functions Parity** — Closing feature gaps between Azure Functions on ACA and native Azure Functions.
