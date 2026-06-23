from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

doc = SimpleDocTemplate(
    "Work-Summary.pdf",
    pagesize=A4,
    topMargin=0.6 * inch,
    bottomMargin=0.6 * inch,
    leftMargin=0.75 * inch,
    rightMargin=0.75 * inch,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "ProjectTitle",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12,
    spaceAfter=6,
    spaceBefore=14,
)

label_style = ParagraphStyle(
    "Label",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10,
    spaceAfter=2,
    spaceBefore=6,
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=13,
    spaceAfter=2,
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=13,
    leftIndent=18,
    spaceAfter=2,
    bulletIndent=6,
    bulletFontName="Helvetica",
)


def add_section(story, title, problem, bullets, impact):
    story.append(Paragraph(title, title_style))
    story.append(Paragraph("<b>Problem:</b> " + problem, body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>What I Did:</b>", label_style))
    for b in bullets:
        story.append(Paragraph("\u2022  " + b, bullet_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Impact:</b> " + impact, body_style))


story = []

# --- Section 1: AI-Powered SRE Agents ---
add_section(
    story,
    "AI-Powered SRE Agents for Azure Container Apps (2025\u2013Present)",
    "Azure Container Apps incidents required manual root cause analysis, leading to long mitigation "
    "and resolution times for customer-facing issues; agent accuracy, deployment reliability, and "
    "auto-remediation coverage needed sustained investment.",
    [
        "Designed and deployed AI-powered diagnostic agents for ACA incident resolution \u2014 ICM Summarization Agent, "
        "CoreDNS Agent, Sessions Agent, and Billing Subagent.",
        "Shifted architecture from workflow-based to investigative prompts, dramatically improving AI-aligned RCA accuracy; "
        "closed 20+ agent backlog items through targeted ICM analysis.",
        "Drove a series of experiments lifting RCA accuracy and visibility \u2014 agent now posts an RCA on "
        "~99% of incidents; on-call rates root cause correct on ~76% over a 30-day window.",
        "Auto-resolved 57 of ~400 CRIs and authored ~132 repair items in a six-month window through evolving "
        "auto-repair capabilities (compare agent-generated RCA vs actual RCA, create repair items, auto-resolve qualifying incidents).",
        "Extended subagent skills with concrete customer-incident patterns: SAL-deletion, Geneva 503, "
        "env-delete with orphaned load balancers.",
        "Stood up the Ev2 deployment pipeline for the agent itself, shipping through standard Azure release "
        "machinery instead of manual updates that previously caused conflicts when changes landed close together.",
        "Presented the RCA Agent at the IDC Pinnacle event; squad won the IDC Pinnacle FY\u201926 "
        "<b>best AI success story award</b> among ~200+ teams.",
    ],
    "Reduced ACA incident P50 time-to-mitigate by 97% (185\u2009\u2192\u20096 min) and P50 time-to-resolve by 64% "
    "(269\u2009\u2192\u200998 min). Sustained ~99% RCA coverage with ~76% on-call-rated accuracy; auto-resolved "
    "57 CRIs and produced 132 repair items in six months. Recognized as a hero example across the org.",
)

# --- Section 2: Foundry Control Plane (FCP) Integration with ACA ---
add_section(
    story,
    "Foundry Control Plane Integration with ACA (2026)",
    "Agentic apps hosted on ACA were not discoverable or manageable from the Foundry Control Plane, "
    "making ACA a second-class hosting target for agents in Foundry.",
    [
        "Designed and shipped the integration that lets Foundry Control Plane (FCP) discover and surface "
        "agentic apps on ACA \u2014 wired through a <b>new preview API across clouds, CP, and CRD</b>.",
        "Supported both <b>customer-declared</b> and <b>auto-detection</b> modes so customers retain control "
        "while coverage still extends to apps that don't self-declare.",
        "Covered ~1,200\u20132,000+ potential agentic apps on ACA, making ACA a first-class hosting target "
        "for agents in Foundry.",
        "Although the upstream Foundry integration was later shelved due to Foundry re-architecture, the "
        "ACA-side foundation laid significant observability into agentic workload patterns on ACA.",
    ],
    "Established the integration surface and agent-workload observability that positions ACA as the canonical "
    "hosting target for agentic apps; design decisions (declared + auto modes) preserved customer control "
    "while maximizing coverage.",
)

# --- Section 3: Express Apps on ADC ---
add_section(
    story,
    "Express Apps on Azure Dev Compute (ADC) \u2014 Public Preview Enablement (2026)",
    "ACA Express Apps (sub-500ms ephemeral sandbox offering on the new ADC platform layer) was blocked from "
    "Public Preview by missing parity with standard ACA \u2014 specifically ephemeral volume support and "
    "Log Analytics customer-log delivery for the 100K\u2013250K ACA environments using LA today.",
    [
        "Closed two of the largest gaps holding back Express Public Preview \u2014 <b>ephemeral volume support</b> "
        "and <b>Log Analytics customer-log delivery</b> \u2014 by landing changes on both the ADC and ACA sides "
        "so the end-to-end flow works through a single customer-facing surface.",
        "Drove a detailed design discussion with the ADC team on the correct way to add LA Collector API support "
        "\u2014 evaluating ADC-native vs an ACA-specific sidecar model \u2014 and got sign-off from ADC and other "
        "key stakeholders <b>before any code landed</b>, avoiding future churn.",
        "Reused ADC's existing volume infrastructure for ACA ephemeral-storage parity instead of adding a new "
        "kind, keeping the integration small and shipping in-window.",
        "Adapted design across multiple iterations as the underlying ADC architecture changed, maintaining "
        "best customer experience.",
    ],
    "LA delivery is the migration path for the ~100K\u2013250K ACA environments using LA today, and the P0 "
    "migration blocker for Express Public Preview (June 2026). Express migration targets <b>~$40M annual "
    "COGs savings</b> through core reclaim.",
)

# --- Section 4: ACA Sessions ---
add_section(
    story,
    "Azure Container Apps Sessions (2024\u20132025)",
    "ACA Sessions lacked observability, had critical async execution bugs, and needed data-plane APIs "
    "for internal and external customers.",
    [
        "Built Session Management APIs (Delete, List, Get) to improve session observability and control.",
        "Fixed critical async execution bugs in code interpreter sessions and Node.js session-specific issues.",
        "Enabled early session deletion \u2014 a key requirement from the Fabric Team \u2014 reducing billing and costs.",
        "Added performance tests for ACA Sessions, identifying code execution regressions.",
        "Enabled .NET code interpreter support for the Security Copilot Team.",
        "Implemented Geneva actions to manage upgrades for Node.js sessions.",
    ],
    "Improved session stability and experience for ~300 external customers actively using ACA Sessions. "
    "Enabled cost optimization for ACA session customers through early deletion support.",
)

# --- Section 5: Azure Functions on ACA ---
add_section(
    story,
    "Azure Functions on Azure Container Apps \u2014 Reliability &amp; Platform Capability (2025\u2013Present)",
    "Azure Functions on ACA lacked feature parity with native Azure Functions and had reliability gaps "
    "around graceful shutdown, trigger fidelity, and authentication \u2014 surfacing as multiple CRIs with "
    "the same error across ~5K active apps.",
    [
        "Designed and shipped <b>graceful drain</b> for managed function apps so in-flight executions complete "
        "cleanly during scale-in \u2014 retired three separate CRIs that all stemmed from the same underlying error.",
        "Delivered <b>queueLength override</b> for queue triggers and a broader <b>scale-rule override</b> path, "
        "lifting trigger fidelity for managed Function and Logic apps.",
        "Added <b>JWT clock-skew leeway</b> to harden auth stability for managed Function and Logic apps.",
        "Implemented function keys management commands for ACA Functions.",
        "Added invocation tracing/summary and durable-events logging for diagnostics.",
        "Added support for editing KEDA scaling rules in Azure Functions on ACA.",
        "Authored API spec for Function ARM APIs.",
        "Closing feature-parity gaps between Azure Functions on ACA and native Azure Functions on an ongoing basis.",
    ],
    "Stabilized ~5K active Functions-on-ACA apps and ~1,322 external Functions apps to the point where the "
    "most frequent CRIs are gone; lifted trigger fidelity and auth stability across managed Function and Logic apps.",
)

# --- Section 6: Functions Observability in Central Kusto ---
add_section(
    story,
    "Functions Observability Migration to Central Kusto (2026)",
    "Functions telemetry was emitted to the legacy waws Kusto clusters owned by App Service, creating storage "
    "pressure on the old clusters and fragmenting the query surface used by alerting, customer detectors, "
    "and agent skills.",
    [
        "Routed <b>FunctionsLogs</b>, <b>FunctionsMetrics</b>, and <b>DurableFunctionsEvents</b> from the "
        "legacy waws Kusto clusters into the modern <b>capps</b> clusters.",
        "Persisted through a non-trivial issue on the <b>Legion</b> side for consumption function apps where "
        "logs were not flowing, going deeper into the problem until it was resolved.",
        "Unblocked alerting, customer detectors, and many agent skills through a single query surface.",
    ],
    "Resolved storage pressure on the legacy App Service Kusto clusters and consolidated the query surface "
    "for alerting, customer detectors, and SRE-agent skills.",
)

# --- Section 7: Dapr OSS Contributions ---
add_section(
    story,
    "Open-Source Contributions to Dapr \u2014 CNCF Project (2021\u20132024)",
    "Dapr, a CNCF open-source project for distributed applications, needed components upgraded to stable, "
    "new features, improved developer experience, and active community support.",
    [
        "Upgraded MQTT PubSub component from alpha to stable; contributed fix to upstream library; added certification tests.",
        "Marked Azure CosmosDB state store, Configuration API building block, and Redis/PostgreSQL configuration stores to stable.",
        "Implemented cascade terminate and purge for Dapr Workflows \u2014 changes spanning runtime and multiple SDKs.",
        "Added bulk subscribe support in Azure Event Hubs and Dapr Workflow performance tests; identified several P0 bugs.",
        "Enabled airgap installation support; built MSI installer; made Dapr available in winget with automated package updates.",
        "Published combined coverage reports for conformance and certification tests.",
        "Resolved customer issues across GitHub (Runtime, Components-Contrib, SDKs) and Discord.",
    ],
    "Accelerated Dapr component maturity and improved developer experience, driving broader adoption of Dapr "
    "across Azure and the open-source community.",
)

# --- Section 8: CI/CD, Internal Fork & Release Engineering ---
add_section(
    story,
    "Dapr Internal Fork &amp; CI/CD Infrastructure (2021\u20132024)",
    "Microsoft\u2019s internal services (AKS, Container Apps) needed a reliable internal fork of Dapr with "
    "fast release turnaround, compliance, and multi-architecture support.",
    [
        "Architected and maintained Dapr internal fork across 5 repositories (dapr, cli, dashboard, components-contrib, kit) "
        "with build, code-signing, and release pipelines.",
        "Automated OSS-to-internal merge pipeline, achieving internal releases within &lt;1 day SLA of OSS release.",
        "Re-designed internal repository to a patch-based model with separate per-service images for faster, targeted releases.",
        "Migrated CI/CD pipelines to 1ES (OneBranch) for compliance; integrated Ev2 deployment for Standard Deployment Practices.",
        "Added multi-arch support (ARM64, ARM, AMD64), Mariner and distroless images; handled 1P Container Registry migration.",
        "Delivered nightly builds for Azure Container Apps.",
    ],
    "Enabled AKS and Container Apps to reliably consume internal Dapr images with rapid turnaround, "
    "supporting seamless adoption of Dapr across Azure distributed services.",
)

# --- Section 9: Dapr AKS Extension ---
add_section(
    story,
    "Dapr AKS Extension \u2014 Security &amp; Multi-Region Rollouts (2022\u20132026)",
    "Dapr AKS Extension customers needed secure, up-to-date versions across all Azure regions with fast "
    "CVE remediation, reliable rollouts, and fresh artifacts.",
    [
        "Led Dapr 1.15 and 1.16 rollouts across all Azure regions; shipped additional security-vulnerability fix releases.",
        "Drove subsequent extension version through prod and added a <b>daily extension-only rollout</b> "
        "so artifacts stay fresh.",
        "Fixed multiple CVE/security vulnerabilities; remediated issues across ~400 AKS clusters.",
        "Expanded AKS extension availability to new regions (e.g., AustriaEast) based on customer demand.",
        "Integrated CodeQL into AKS Extension pipeline for security and code quality.",
        "Consolidated multiple pipelines into a single OneBranch-compliant pipeline to expedite releases.",
        "Resolved customer-reported AKS extension ICMs promptly.",
    ],
    "Upgraded ~260 subscriptions and ~400 AKS clusters to secure Dapr versions; sustained fresh-artifact "
    "delivery via daily rollouts. Workstream subsequently offloaded to allow focus on higher-impact areas.",
)

# --- Section 10: On-Call & DRI ---
add_section(
    story,
    "On-Call Reliability &amp; DRI Operations (2024\u2013Present)",
    "Azure Container Apps required consistent, high-quality on-call coverage to maintain service uptime "
    "and resolve customer-impacting incidents rapidly across CRIs and LSIs.",
    [
        "Served as on-call DRI across multiple rotations \u2014 resolved <b>38 CRIs and 84 LSIs (36 Sev2s)</b> "
        "in the most recent 6-month window alone, on top of <b>200+ prior incidents including 27+ CRIs</b>.",
        "Handled 36 Sev2 LSIs (P50 TTM 1h, P50 TTR 25h vs ACA baseline 3.9h/60h) and 6 Sev3 CRIs in earlier windows, "
        "consistently outperforming team baselines.",
        "Delivered repair items to address root causes, reducing incident recurrence and improving system resilience.",
        "Improved alert fidelity by updating 5 LSI alerts based on investigation findings.",
        "Fed agent feedback and skill updates back from incidents the agent struggled on so its accuracy "
        "keeps improving \u2014 actively listening in weekly IcM discussions even off-shift.",
    ],
    "Ensured high service uptime and reduced operational noise through proactive issue resolution, "
    "consistently exceeding ACA on-call baselines while closing the agent\u2192incident feedback loop.",
)

# --- Section 11: Security & Key Vault Integration ---
add_section(
    story,
    "Azure Key Vault Integration &amp; Security Posture (2025\u20132026)",
    "ACA Managed Environment Storage API was handling raw connection strings in ~27K daily API calls, "
    "creating a security risk; the Dapr repo also needed proactive vulnerability scanning.",
    [
        "Integrated Azure Key Vault with Managed Environment Storage API, enabling secure secret handling.",
        "Eliminated raw connection strings in storage create API calls.",
        "Resolved CodeQL violations across container apps, improving code security and compliance.",
        "Used <b>Argus security-scan tool</b> to scan the Dapr repo for vulnerabilities; shared the report "
        "with the team along with action items to fix the highest-risk ones.",
    ],
    "Provided a secure alternative to raw account keys for ~27K daily storage API calls, "
    "strengthening security posture and aligning with enterprise-grade standards; proactively surfaced "
    "Dapr-repo vulnerabilities for team remediation.",
)

# --- Section 12: AI-Augmented Engineering & Craft ---
add_section(
    story,
    "AI-Augmented Engineering &amp; Craft (2026)",
    "As Copilot accelerated authoring, the engineering bottleneck shifted to <b>verification</b> \u2014 "
    "behavioural diffs in a multi-tenant platform can have wide blast radius, and a drain feature regression "
    "(revision regression + nil-dereference Sev3) reinforced the need for disciplined self-review and "
    "end-to-end validation before merge.",
    [
        "Incorporated <b>Copilot self-review</b> on PRs with three parallel perspectives \u2014 "
        "<i>Advocate</i> defending intent, <i>Skeptic</i> hunting regressions and edge cases, "
        "<i>Architect</i> evaluating direction \u2014 to catch issues before peer review. Used the same skill on "
        "peer PRs as a deeper second-opinion pass.",
        "Used Copilot across the full flow \u2014 design \u2192 implementation \u2192 PR review \u2014 and made "
        "<b>e2e validation on a private stamp</b> a standard step before merging any meaningful feature change.",
        "Adopted a \u201cwhat does this change for every existing customer\u201d lens on every PR after the "
        "drain-feature regression, reasoning blast radius up-front instead of relying on post-merge detection.",
        "Delivered <b>62 PRs</b> across Functions, Sessions, and AKS-extension components in a single review "
        "cycle, sustained by AI-augmented authoring and review.",
        "Kept the codebase tidy: removed dead types, aligned client contracts with service changes, and added "
        "docs in the same PR as design changes.",
        "Shared learnings on AI tooling with the broader AppPlat team to lift team-wide AI fluency.",
    ],
    "Shifted personal engineering practice to match the AI-augmented era \u2014 author fast, verify deeply. "
    "Sustained high PR throughput (62 PRs / cycle) while improving the quality of self-review and reducing "
    "post-merge surprises.",
)

# --- Section 13: Mentoring & Cross-Team Leadership ---
add_section(
    story,
    "Mentoring &amp; Cross-Team Leadership (2025\u20132026)",
    "Sustaining team velocity at SDE2 level requires unblocking newer engineers, building cross-team "
    "relationships that make follow-on features easier to ship, and absorbing on-call asymmetry when "
    "teammates need coverage.",
    [
        "Mentored new hires <b>Khushi and Divyansh</b> through their first on-call rotations \u2014 helping "
        "with faster customer resolution and unblocking issues during both on-call and dev flows.",
        "Continued mentoring Khushi separately on agent-platform and scaling-rules PRs, and gave a junior "
        "engineer space to learn and own parts of the Functions-on-ACA feature set.",
        "Built durable cross-team relationships with <b>ADC, Functions, FCP, and SRE-Agent teams</b> to land "
        "cross-org features end-to-end \u2014 those review relationships make the next feature easier to ship.",
        "Collaborated with the Playwright testing team on a proof of concept using ACA Sessions.",
        "Took ad-hoc on-call shifts to support the China team during new-year leave and to cover teammates "
        "whose plans changed; stayed engaged in CRI/LSI discussions off-shift.",
        "Presented the ACA RCA Agent at the IDC Pinnacle event; squad won the FY\u201926 best AI success "
        "story award among ~200+ teams.",
    ],
    "Multiplied team impact by unblocking first-time on-call engineers, building review relationships across "
    "ADC/Functions/FCP/SRE-Agent that compound over time, and absorbing on-call coverage gaps proactively.",
)

doc.build(story)
print("Generated Work-Summary.pdf successfully.")
