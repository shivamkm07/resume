# Work Summary — Shivam Kumar

> **Master reference of all work done.** This is the complete, exhaustive record of contributions, data points, and metrics — the superset from which the resume is curated. Sourced from `work.txt` (semester Connects, Nov 2021 → May 2026), the manually-curated `importnat things from wor.md`, and the current resume. Organized by **area** for quick lookup, followed by **technical deep-dives**, **decision/conflict examples**, **recognition**, a **chronological Connect appendix**, and a **metrics quick-reference**.

**Role:** Software Development Engineer II, Microsoft — Azure Container Apps (Hyderabad, India)
**SDE2:** Jul 2024 – Present · **SDE1:** Jul 2021 – Jul 2024
**Manager:** Rajneesh Mitharwal

---

## Contents

- [1. Dapr — OSS, Internal Fork & AKS Extension](#1-dapr--oss-internal-fork--aks-extension)
- [2. ACA Sessions](#2-aca-sessions)
- [3. Core ACA Platform](#3-core-aca-platform)
- [4. Azure Functions on ACA](#4-azure-functions-on-aca)
- [5. Express Apps on ADC (Azure Dev Compute)](#5-express-apps-on-adc-azure-dev-compute)
- [6. FCP Integration with ACA](#6-fcp-integration-with-aca)
- [7. ACA RCA / SRE Agent](#7-aca-rca--sre-agent)
- [8. Live-Site / DRI / On-Call](#8-live-site--dri--on-call)
- [9. Craft & AI-Augmented Engineering](#9-craft--ai-augmented-engineering)
- [10. Direction & Design Leadership](#10-direction--design-leadership)
- [11. People, Mentoring & Collaboration](#11-people-mentoring--collaboration)
- [12. Setbacks & Learnings](#12-setbacks--learnings)
- [13. Goals (Upcoming Period)](#13-goals-upcoming-period)
- [Technical Deep-Dive Examples (interview-ready)](#technical-deep-dive-examples-interview-ready)
- [Decision / Conflict Examples](#decision--conflict-examples)
- [Recognition & Awards](#recognition--awards)
- [Chronological Connect Appendix](#chronological-connect-appendix)
- [Metrics Quick-Reference](#metrics-quick-reference)

---

## 1. Dapr — OSS, Internal Fork & AKS Extension

### 1.1 Dapr OSS Contributions (CNCF)
- **MQTT PubSub component**: upgraded from alpha → **Stable**; added MQTT certification test; contributed a fix to one of the upstream libraries used by the component.
- **Azure CosmosDB state store**: marked **Stable**.
- **Configuration API building block**: marked **Stable** (1.11 release); upgraded **Redis** and **PostgreSQL** configuration stores to stable; added API + component conformance tests; updated SDK implementations to conform to the accepted uniform spec.
- **Bulk subscribe** support added in **Azure Event Hubs**.
- **Dapr Workflows**:
  - Implemented **Cascade Terminate** and **Cascade Purge** — changes across runtime *and* SDKs.
  - Collaborated with an external contributor to add **metrics** for workflows.
  - Logging enhancements in workflow runtime and SDK for better debugging.
  - Bug fixes in the **DurableTask framework** (the orchestrator powering workflows).
  - Added **performance tests** that surfaced several **P0 bugs**; collaborated to resolve some.
  - **Scalability defect**: diagnosed and fixed workflows not running on more than 2 instances (see [deep-dive](#technical-deep-dive-examples-interview-ready)).
- **Dapr CLI**:
  - **Airgap installation** support (worked with an external contributor on the CLI change).
  - **Mariner image** support, **MSI installer**, **winget** availability (incl. automation to update the winget packages repo).
  - Created/managed/maintained the **installer-bundle repo**; shipped a bundle release at every dapr/cli release.
- Resolved numerous customer issues across **runtime, components-contrib, and SDKs** on GitHub and Discord.
- Published **combined coverage reports** for conformance + certification tests.
- Collaborated with IDC + Redmond teams to resolve **P0 items** in the 1.7 release.

### 1.2 Dapr Internal Fork (built & owned solo)
- Implemented the **complete internal-fork setup** across **5 forked repos**: `dapr`, `cli`, `dashboard`, `components-contrib`, `kit`.
- Built **build, codesigning, and release pipelines** from scratch; automated upgrade to latest OSS releases; e2e tests for unintended bugs.
- Re-designed the internal repo to a **patch-based model** for faster/cleaner releases (vs full repo clone — see [decision examples](#decision--conflict-examples)).
- **Separate internal images per service** to enable service-specific patches.
- **Multi-arch** support (ARM64, ARM, AMD64) for all Dapr images *and* dashboard images — for **all supported Dapr versions from a single pipeline**.
- Finalized branching + merge strategy; automated most of the internal release process as an **`automerge` pipeline**.
- Achieved **Dapr internal releases within a 1-day SLA** of OSS release.
- **1P Container Registry migration** for Dapr; added **Mariner** images; added missing **distroless** images to MCR; **nightly builds** for ACA.
- Added a separate component for **k8se-envoy-specific name resolution** (Dapr ↔ ACA integration).
- Backported patches/fixes into the internal repo to stay consistent with OSS (1.11.* / 1.12.* internal releases).

### 1.3 Dapr AKS Extension
- Contributed to **AKS Extension GA requirements**.
- Migrated Dapr CI/CD pipelines to **1ES** (compliance) and consolidated multiple pipelines into a **single OneBranch pipeline**; integrated **Ev2** deployment for **SDP** compliance.
- **Dapr 1.15** rollout across all regions + hotfixes; **Dapr 1.16** rollout; **AustriaEast** region enablement based on customer demand.
- Multiple **CVE / security-vulnerability** fix releases; resolved **S360** image vulnerabilities; resolved customer-reported AKS extension ICMs.
- **CodeQL** integration in the Dapr AKS Extension pipeline.
- Added a **daily extension-only rollout** so artifacts stay fresh.
- **Impact:** upgraded **~260 subscriptions / ~400 AKS clusters** to secure Dapr versions.
- *(Workstream later offloaded to focus on higher-impact areas.)*

---

## 2. ACA Sessions

- Helped **launch ACA Sessions Public Preview**.
- **Code interpreters:**
  - **Node.js** code-interpreter support — owned end-to-end.
  - **.NET** code-interpreter support — **adopted by the Security Copilot team**.
  - Fixed critical **async execution bugs** in code-interpreter sessions; resolved Python + Node.js session-specific bugs; fixed Node.js Sessions **test failures**.
- **Session Management data-plane APIs**: **Delete, List, Get** (+ create) — improving session observability and control.
- **Geneva actions** to manage upgrades + monitoring for Node.js sessions.
- Collaborated with the **Playwright testing team** on a POC using ACA Sessions.
- Added **performance tests** that identified regressions in code execution.
- **Early session deletion** — key requirement from the **Fabric team**; reduces billing and optimizes costs.
- **Impact:** improved stability/experience for **~300 external customers** actively using ACA Sessions.

---

## 3. Core ACA Platform

- **Azure Key Vault integration** with the **Managed Environment Storage API** — secure secret handling, eliminating raw connection strings in API calls.
  - **Impact:** secure alternative to raw account keys across **~27K daily storage-create API calls**; strengthened enterprise-grade security posture.
- Resolved **CodeQL violations** across container apps (security + compliance); cleaned up *all* container-app CodeQL violations.

---

## 4. Azure Functions on ACA

> Component scale: **~5K active managed apps**, **~1,322 external apps**. Stabilized to the point that the most frequent CRIs are gone.

- **Graceful drain** for managed function apps — in-flight executions complete cleanly during scale-in. Addressed an active pain point that surfaced as **3 separate CRIs with the same error**. (Implemented via the **postExecute API** — see [deep-dive](#technical-deep-dive-examples-interview-ready).)
- **Trigger fidelity / scaling overrides:**
  - **queueLength override** for queue triggers.
  - **scale-rule override**.
  - **KEDA rules edit** support.
- **JWT clock-skew leeway** — auth stability for managed Function *and* Logic apps.
- **Function keys management** commands (implemented using a **debug container** — see deep-dive).
- **Diagnostics / observability:**
  - **Invocation tracing / summary**.
  - **Durable-events logging** support.
  - **API spec** for Function ARM APIs.
- **Functions observability — central Kusto migration:**
  - Routed **FunctionsLogs, FunctionsMetrics, DurableFunctionsEvents** from legacy **waws** Kusto clusters → modern **capps** clusters.
  - Resolved storage pressure on old App Service clusters; unblocked **alerting, customer detectors, and many agent skills** through a single query surface.
  - Required solving a **non-trivial Legion-side issue** for consumption function apps where logs were not flowing.
- **Impact:** enhancements benefit ~1,322 external ACA Functions apps — improved security, observability, operational efficiency; gave a **junior engineer space to learn and own** parts of this feature set.

---

## 5. Express Apps on ADC (Azure Dev Compute)

> ADC = internal service providing ephemeral sandbox offering at **<500 ms**. Express Apps Public Preview targeted **June 2026**.

- Closed **two of the largest gaps** holding back Express Public Preview, landing changes on **both ADC and ACA** sides so the end-to-end flow works through a single customer-facing surface:
  1. **Ephemeral volume support** — reused ADC's **existing volume infrastructure** for ACA ephemeral-storage parity (no new volume kind), keeping the integration small and shipping in-window.
  2. **Log Analytics customer-log delivery** — the **P0 migration blocker**; drove design of the **LA Collector API** support (ADC-native vs ACA-specific sidecar — see [decision examples](#decision--conflict-examples)) with stakeholder sign-off before any code landed.
- **Impact:** LA delivery is the migration path for **~100K+ ACA environments** (~250K using LA today) evaluating Express; manager-stated **~$40M annual COGs savings** target.
- Adapted across **multiple architecture iterations** as underlying design changed.

---

## 6. FCP Integration with ACA

- Designed and shipped the integration that lets **Foundry Control Plane (FCP)** discover and surface **agentic apps on ACA**.
- Supports **customer-declared** *and* **auto-detection** modes — wired through a **new preview API across clouds, Control Plane (CP), and CRD**.
- **Auto-detection** uses **privileged host-process inspection** (telapp / procpid) to identify whether a running process is an agentic app — see [deep-dive](#technical-deep-dive-examples-interview-ready).
- **Coverage:** **~1,200** (manager: **~2K+**) potential agentic apps on ACA — making ACA a first-class hosting target for agents in Foundry.
- *(Foundry-side integration later shelved due to Foundry re-architecture; ACA-side foundation laid significant **observability** for agentic-workload patterns.)*

---

## 7. ACA RCA / SRE Agent

### 7.1 Agents & Architecture
- **RCA Agent** with multiple **subagents**:
  - **ICM Summarization Agent** — automates extraction of key insights from ICMs.
  - **CoreDNS Agent** — analysis/debugging of CoreDNS issues.
  - **Sessions Agent** — investigates session ICMs (code interpreter + custom container).
  - **Billing subagent**.
- **Auto-repair agent** — compares agent-generated RCA vs actual RCA and **creates repair items** for the incident.
- **Auto-resolve** — automatically resolves incidents that can be resolved.
- **End-to-end setup** for the ACA RCA Agent.
- **Ev2 deployment pipeline** — agent ships through standard Azure release machinery instead of manual updates (which previously caused conflicts when changes landed close together).
- Shifted from **workflow-based** prompts → **investigative** prompts.
- Extended subagent skills with concrete customer-incident patterns: **SAL-deletion, Geneva 503, env-delete with orphaned LBs**.

### 7.2 Metrics & Impact
- **P50 TTM: 185 → 6 min** (~97% reduction); **P50 TTR: 269 → 98** (~64% reduction).
- Posts an RCA on **~99% of incidents**; on-call rates root cause correct on **~76%** (last 30 days).
- In six months: **auto-resolved 57 of ~400 CRIs**; authored **~132 repair items**.
- Closed **20+ agent backlog items** via targeted ICM analysis + updates across agent and subagents.
- Presented at **IDC Pinnacle**; squad won **best AI success story at IDC Pinnacle FY'26** among **~200+ teams**. Hero example across the org; inspired other teams to build autonomous systems.

---

## 8. Live-Site / DRI / On-Call

> Cumulative DRI ownership across rotations as both primary and backup.

| Period | CRIs | LSIs | Notes |
|---|---|---|---|
| Nov 2024 | 13 | 90+ ICMs total | 2-week rotation, primary + backup |
| May 2025 | ~14 | ~150 (incl. ~58 Sev2) | repair items reducing recurrence |
| Nov 2025 | 6 Sev3 | 36 Sev2 LSIs | P50 TTM 1h / TTR 25h (vs ACA 3.9h/60h); Sev3 TTM 19h / TTR 243h (vs 24.25/123h) |
| May 2026 | 38 | 84 (incl. 36 Sev2) | fed agent feedback back from incidents |

- Delivered **repair items** addressing root causes; reduced incident recurrence and operational noise.
- Improved **alert fidelity** — updated **5 LSI alerts** based on investigation findings.
- Stayed engaged in **CRI/LSI discussions off-shift**; fed skill updates back to the RCA Agent from incidents it struggled on.

---

## 9. Craft & AI-Augmented Engineering

- **Copilot self-review** on PRs with three parallel perspectives — **Advocate** (defends intent), **Skeptic** (hunts regressions/edge cases), **Architect** (evaluates direction) — to catch issues before review. Same skill used on peer PRs as a deeper second-opinion pass.
- Used **Copilot across the full flow** — design → implementation → PR review.
- Made **e2e validation on a private stamp** a standard step before merging any meaningful feature change.
- Used **Argus** security-scan tool to scan the Dapr repo for vulnerabilities; shared report + action items for highest-risk ones.
- **Codebase hygiene:** removed dead types, aligned client contracts with service changes, added docs in the same PR as design changes. Code typically requires little review time.
- **Throughput:** **62 PRs** delivered across Functions, Sessions, and AKS extension (Nov 2025 period).
- **CodeQL** integration + violation cleanup for secure, maintainable code.

---

## 10. Direction & Design Leadership

- **LA integration in ADC:** drove a detailed design discussion with the ADC team on the correct way to add **LA Collector API** support — evaluating **ADC-native vs ACA-specific sidecar** model; got sign-off from ADC + key stakeholders **before any code landed**, avoiding future churn. Following the same process for other key ADC design changes.
- **Ephemeral storage:** reused ADC's existing volume infrastructure instead of adding a new kind — kept the integration small, shipped in-window.
- **FCP:** supported both **auto-detection** and **customer-declared** modes so customers retain control while coverage extends to apps that don't self-declare.
- Shaped implementation for **Functions keys-management** commands.
- Guided **stability/security** choices via timely Dapr hotfixes, CVE fixes, and region expansion.

---

## 11. People, Mentoring & Collaboration

- Mentored **Khushi** and **Divyansh** — both doing on-call for the first time — helping with faster customer resolution and unblocking during on-call + dev flows. Continued mentoring Khushi on agent-platform and scaling-rules PRs.
- Worked closely with **ADC, Functions, FCP, and SRE-Agent** teams to land cross-org features end-to-end.
- Took **ad-hoc on-call shifts** when teammates' plans changed (incl. covering the **China team** during New Year leave).
- Shared learnings on **AI tooling** with the **AppPlat team**, lifting teammates' AI fluency.
- Described by peers as approachable, deeply knowledgeable, and a clear explainer.

---

## 12. Setbacks & Learnings

- The **drain feature** shipped early in the period was followed by two unintended consequences:
  1. A **revision regression** — unrelated edits started creating new revisions.
  2. A **nil-dereference** that fired a **Sev3 ICM**.
- Both fixes were small; the lesson was big: **in a multi-tenant platform every PR is a behavioural diff, not just a code diff** — blast radius must be reasoned through up-front. The system caught the regression in early regions, allowing proactive measures.
- **Changed behavior:** walk through each change with a "what does this change for every existing customer" lens; validate e2e on a private stamp before merging; run the Advocate-Skeptic-Architect review skill on own PRs first — especially as Copilot makes authoring fast and the bottleneck shifts to **verification, not writing**.

---

## 13. Goals (Upcoming Period)

1. **Increase Adoption for ACA** — Express reliability & parity with standard ACA apps; ACA on-call; deliver on prioritized ACA initiatives.
2. **Drive ACA Agent Harness for a Toil-Free Dev-to-Deploy Loop** — stitch the full PR lifecycle (review → merge → deploy → monitor) with automated regression correlation; bake recurring SRE work (health sweeps, config-drift detection, stale-resource cleanup) into the agent; expose SRE intelligence via **MCP**; partner with the landing intern.
3. **Sustain ACA Key Surfaces** — Functions on ACA, Dapr AKS Extension, SRE Agent (fixes/hotfixes, version bumps, region/cloud enablement, skills/prompts).
4. **Empower DevDiv India** — culture of belonging/teamwork; org-wide efforts (Giving, Learning Days, Hackathon, MS Poll); complete required trainings on time.

---

## Technical Deep-Dive Examples (interview-ready)

These are flagged as strong technical narratives for interviews / system-design discussions:

1. **Dapr Workflows not scaling beyond 2 instances** — the full story of how workflows failed to run on more than 2 instances, how it was identified (performance testing), root-caused in the DurableTask orchestration layer, and resolved with metrics + logging enhancements.
2. **Functions key management via debug container** — using a debug container to implement function-keys management commands.
3. **Drain support in Functions via postExecute API** — graceful drain so in-flight executions finish during scale-in.
4. **Auto-detection of agents on ACA via telapp** — privileged host-process inspection using procpid information to determine whether a running process is an agentic app (FCP integration).
5. **RCA Agent** — multi-subagent architecture, investigative-vs-workflow prompting, auto-repair / auto-resolve loops.

---

## Decision / Conflict Examples

- **Internal fork: Git patch model vs full repo clone** — chose a **patch-based** model (which I supported) over full clone. Benefits: intelligent Git patching/merging, smoother Go-modules updates, scripted automation, fewer merge conflicts, service-specific patches. *(Worth validating the precise usefulness framing of git patch before citing.)*
- **LA Collector API: ADC-native vs ACA-specific sidecar** — evaluated both; secured stakeholder sign-off on the chosen approach before code landed.
- **etcd for Dapr scheduler** *(optional/secondary example)* — potential conflict example around using etcd; various issues currently surfacing in etcd. Not a first-choice example since not yet acted on, but usable.

---

## Recognition & Awards

- **Microsoft RockStar Award** — '22 and '23, for exceptional contributions.
- **IDC Pinnacle FY'26 — Best AI Success Story** (ACA RCA Agent squad, among ~200+ teams).
- **Academic Excellence Award (×2)**, IIT Kanpur.
- JEE Advanced **AIR 715** · JEE Mains **AIR 348** · KVPY Scholar · NSE Physics **Top 1%** · Ram Prakash Chopra Scholarship.

---

## Chronological Connect Appendix

### Nov 2021 — Dapr Internal Fork & ACA Integration (foundational)
- Complete internal-fork setup: 5 repos (dapr, cli, dashboard, components-contrib, kit); build/codesigning/release pipelines; automated OSS upgrades; e2e tests.
- Dapr ↔ ACA integration: separate component for k8se-envoy-specific name resolution.
- **Why:** Dapr supportability for Microsoft internal services; internal-only changes; Dapr as advanced Azure offering.
- **Impact:** AKS + ACA running internal Dapr images from pipelines; fast OSS upgradability; supported AKS + ACA adoption.

### May 2022 — Dapr OSS Components + Fork Maturity
- MQTT PubSub → stable + certification test + upstream lib fix; airgap install (external contributor); installer-bundle repo.
- Fork: multi-arch (ARM64/ARM/AMD64) for images + dashboard; branching/merge strategy; `automerge` pipeline; AKS Extension GA reqs.
- Collaborated with IDC + Redmond on 1.7 P0 items.

### Nov 2022 — Releases within SLA + 1P Migration
- Internal releases within **1-day SLA**; patch-based redesign; per-service images.
- 1P Container Registry migration; Mariner images; missing distroless images in MCR; nightly ACA builds.
- CosmosDB state store → stable; Mariner + MSI for CLI; winget availability + automation; bug fixes.

### May 2023 — Configuration API & Stores
- Configuration API → stable (1.11); Redis + PostgreSQL config stores → stable; API + component tests; SDK conformance; combined coverage reports.
- Pipeline reliability; internal images within 1-day SLA.

### Nov 2023 — Workflows Perf + Event Hubs
- Internal 1.11.*/1.12.* releases within SLA; backported patches.
- Scoped Dapr service invocation in ACI.
- Bulk subscribe in Azure Event Hubs; workflow performance tests → identified several P0 bugs; workflow logging enhancements; resolved GitHub/Discord customer issues.

### May 2024 — Workflows Cascade + Pipelines + Sessions PP
- Cascade Terminate/Purge in Workflows (runtime + SDKs); external-contributor metrics; DurableTask bug fixes; logging.
- Migrated Dapr CI/CD to 1ES; resolved AKS extension ICMs; S360 image vulnerability fixes.
- ACA Sessions PP: perf tests (identified regressions); Python code-interpreter backend bug fixes.

### Nov 2024 — Reliability + Node.js Sessions + OneBranch/Ev2
- On-call: 2-week rotation, **90+ ICMs incl. 13 CRIs**.
- Node.js ACA Sessions critical bug fixes to prod; Geneva actions for Node.js upgrades; Playwright POC; data-plane APIs (in dev).
- Dapr CVE fixes (AKS extension + ACA); consolidated to single OneBranch pipeline; Ev2 deployment for SDP.

### May 2025 — Sessions APIs, AKV, RCA Agent v1, DRI
- Sessions: Session Management APIs (Delete/List/Get); async execution + Node.js fixes; **~300 external customers**; early session deletion (Fabric team).
- Core ACA: Azure Key Vault + Managed Env Storage API (~27K daily calls); CodeQL violations resolved.
- DRI: **~14 CRIs, ~150 LSIs (~58 Sev2)**; repair items.
- RCA Agent: ICM Summarization, CoreDNS, Sessions agents built/deployed.
- Dapr AKS: security fixes; 1.15 rollout all regions; new-region expansion → **~260 subs / ~400 clusters** upgraded.
- Presented RCA Agent at IDC Pinnacle.

### Nov 2025 — RCA Accuracy, Functions Capability, Security
- **62 PRs** across Functions, Sessions, AKS extension.
- RCA Agent: **P50 TTM 185→6, TTR 269→98**; Sessions/Billing subagents; investigative prompts; closed 20+ backlog items.
- Functions: keys-management commands; invocation tracing/summary; durable-events logging; ARM API spec — **~1,322 external apps**.
- Sessions: .NET code interpreter (Security Copilot); Node.js test-failure fixes.
- AKS Extension: 1.15 hotfixes; 1.16 rollout; CVE fixes; AustriaEast enablement.
- Security/Quality: CodeQL integration + cleanup.
- DRI: 36 Sev2 LSIs (P50 TTM 1h/TTR 25h) + 6 Sev3 CRIs.
- People: mentored Khushi; ad-hoc shifts for China team.

### May 2026 — Express, Functions Reliability, RCA Agent, FCP, Kusto
- **Express on ADC:** ephemeral volume support + Log Analytics customer-log delivery (P0 PP blocker; ~100K+ envs; ~$40M COGs).
- **Functions reliability:** graceful drain (retired 3 CRIs); queueLength + scale-rule overrides; JWT clock-skew leeway; **~5K active apps** stabilized.
- **RCA Agent:** ~99% RCA coverage; ~76% accuracy; auto-resolved 57/~400 CRIs; ~132 repair items; SAL-deletion / Geneva-503 / orphaned-LB skills; Ev2 pipeline. **IDC Pinnacle FY'26 best-AI-success-story** (~200+ teams).
- **FCP:** discover/surface agentic apps; preview API across clouds/CP/CRD; auto-detection via telapp; **~1,200–2K+ apps** (later shelved Foundry-side; ACA observability foundation retained).
- **Functions observability:** waws → capps Kusto migration (FunctionsLogs/Metrics/DurableFunctionsEvents); solved Legion-side consumption-app log issue.
- **Dapr AKS (contributor):** security-fix release; next version through prod; daily extension-only rollout. *(Now offloaded.)*
- **DRI:** 38 CRIs, 84 LSIs (36 Sev2).
- **Craft/Direction/People/Setback:** see sections [9](#9-craft--ai-augmented-engineering)–[12](#12-setbacks--learnings).

---

## Metrics Quick-Reference

| Metric | Value | Area |
|---|---|---|
| RCA Agent P50 TTM | 185 → 6 min (~97% ↓) | RCA Agent |
| RCA Agent P50 TTR | 269 → 98 (~64% ↓) | RCA Agent |
| RCA coverage | ~99% of incidents | RCA Agent |
| RCA on-call accuracy | ~76% (30 days) | RCA Agent |
| CRIs auto-resolved | 57 of ~400 (6 mo) | RCA Agent |
| Repair items authored | ~132 | RCA Agent |
| Agent backlog items closed | 20+ | RCA Agent |
| Express / ACA envs (LA migration path) | ~100K+ (~250K using LA) | Express/ADC |
| Express COGs savings target | ~$40M / yr | Express/ADC |
| FCP agentic apps covered | ~1,200 (~2K+ per mgr) | FCP |
| Functions on ACA — managed apps | ~5K active | Functions |
| Functions on ACA — external apps | ~1,322 | Functions |
| Functions drain — CRIs retired | 3 | Functions |
| Sessions external customers | ~300 | Sessions |
| AKV-secured daily API calls | ~27K | Core ACA |
| Dapr AKS — clusters upgraded | ~400 (~260 subs) | Dapr AKS |
| Dapr internal release SLA | <1 day of OSS | Dapr Fork |
| Dapr repos forked | 5 | Dapr Fork |
| PRs (Nov 2025 period) | 62 | Throughput |
| DRI (May 2026) | 38 CRIs / 84 LSIs (36 Sev2) | Live-site |
| DRI (May 2025) | ~14 CRIs / ~150 LSIs (~58 Sev2) | Live-site |
| DRI (Nov 2024) | 13 CRIs / 90+ ICMs | Live-site |
| LSI alerts improved | 5 | Live-site |

---

*Last updated: 2026-06-22. Source of truth: `work.txt` + `importnat things from wor.md` + current resume (`cv-jake-format-v3.tex`).*
