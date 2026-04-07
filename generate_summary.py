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
    "and resolution times for customer-facing issues.",
    [
        "Designed and deployed AI-powered diagnostic agents for ACA incident resolution \u2014 ICM Summarization Agent, "
        "CoreDNS Agent, Sessions Agent, and Billing Subagent.",
        "Shifted architecture from workflow-based to investigative prompts, dramatically improving AI-aligned RCA accuracy; "
        "closed 20+ agent backlog items through targeted ICM analysis.",
        "Evolving agent toward autonomous auto-repair \u2014 automatically comparing agent-generated RCA vs actual RCA, "
        "creating repair items, and auto-resolving qualifying incidents.",
        "Enabled Foundry Control Plane (FCP) support so all agents created on ACA are visible on the Foundry Control Plane.",
        "Presented the RCA Agent at the IDC Pinnacle event, showcasing its impact on incident diagnostics and reliability.",
    ],
    "Reduced ACA incident P50 time-to-mitigate by 97% (185\u2009\u2192\u20096 min) and P50 time-to-resolve by 64% "
    "(269\u2009\u2192\u200998 min). Targets reduction of ~99 monthly CRIs through accelerated root cause analysis.",
)

# --- Section 2: ACA Sessions ---
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

# --- Section 3: Azure Functions on ACA ---
add_section(
    story,
    "Azure Functions on Azure Container Apps (2025\u2013Present)",
    "Azure Functions on ACA lacked feature parity with native Azure Functions, missing key management, "
    "diagnostics, and scaling capabilities.",
    [
        "Implemented function keys management commands for ACA Functions.",
        "Added invocation tracing/summary and durable-events logging for diagnostics.",
        "Authored API spec for Function ARM APIs.",
        "Added support for editing KEDA scaling rules in Azure Functions on ACA.",
        "Implemented drain functionality for Azure Functions on ACA.",
        "Working on closing feature parity gaps between Azure Functions on ACA and native Azure Functions.",
    ],
    "Enhancements benefit ~1,322 external ACA Functions apps, improving security, observability, and operational efficiency.",
)

# --- Section 4: Dapr OSS Contributions ---
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

# --- Section 5: CI/CD, Internal Fork & Release Engineering ---
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

# --- Section 6: Dapr AKS Extension ---
add_section(
    story,
    "Dapr AKS Extension \u2014 Security &amp; Multi-Region Rollouts (2022\u2013Present)",
    "Dapr AKS Extension customers needed secure, up-to-date versions across all Azure regions with fast "
    "CVE remediation and reliable rollouts.",
    [
        "Led Dapr 1.15 and 1.16 rollouts across all Azure regions.",
        "Fixed multiple CVE/security vulnerabilities; remediated issues across ~400 AKS clusters.",
        "Expanded AKS extension availability to new regions based on customer demand.",
        "Integrated CodeQL into AKS Extension pipeline for security and code quality.",
        "Consolidated multiple pipelines into a single OneBranch-compliant pipeline to expedite releases.",
        "Resolved customer-reported AKS extension ICMs promptly.",
    ],
    "Upgraded ~260 subscriptions and ~400 AKS clusters to secure Dapr versions, strengthening security posture "
    "and ensuring reliable Dapr experiences for enterprise customers.",
)

# --- Section 7: On-Call & DRI ---
add_section(
    story,
    "On-Call Reliability &amp; DRI Operations (2024\u2013Present)",
    "Azure Container Apps required consistent, high-quality on-call coverage to maintain service uptime "
    "and resolve customer-impacting incidents rapidly.",
    [
        "Served as on-call DRI, resolving 200+ incidents including 27+ CRIs, outperforming team baselines.",
        "Handled 36 Sev2 LSIs (P50 TTM 1h, P50 TTR 25h vs ACA baseline 3.9h/60h) and 6 Sev3 CRIs.",
        "Delivered repair items to address root causes, reducing incident recurrence and improving system resilience.",
        "Improved alert fidelity by updating 5 LSI alerts based on investigation findings.",
    ],
    "Ensured high service uptime and reduced operational noise through proactive issue resolution, "
    "consistently exceeding ACA on-call baselines.",
)

# --- Section 8: Security & Key Vault Integration ---
add_section(
    story,
    "Azure Key Vault Integration &amp; Security Posture (2025)",
    "ACA Managed Environment Storage API was handling raw connection strings in ~27K daily API calls, "
    "creating a security risk.",
    [
        "Integrated Azure Key Vault with Managed Environment Storage API, enabling secure secret handling.",
        "Eliminated raw connection strings in storage create API calls.",
        "Resolved CodeQL violations across container apps, improving code security and compliance.",
    ],
    "Provided a secure alternative to raw account keys for ~27K daily storage API calls, "
    "strengthening security posture and aligning with enterprise-grade standards.",
)

doc.build(story)
print("Generated Work-Summary.pdf successfully.")
