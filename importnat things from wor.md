Dapr OSS:

MQTT Pubsub - Fixed bugs and stabilised for production with tests(don't mention tests specifically)
Airgap Installation support in Dapr CLI, Mariner image support, MSI installer
Azure cosmosDB statestore stable
Config API stable
Redis and Postgresql config store stable
Bulk subscribe support in Azure eventhubs
Dapr workflows performance improvement: Identifying performance of workflows(using test but again do not mention tests), limitations, idneitifying and fixing the bugs, logging enhancements
Cascade Terminate/Purge for dapr workflows support, add required emtrics, bugfixes in durabletask framework which was used for workflows
- This whole Dapr workflows story of how it was not running on more than 2 instances, how you idntified and how you reslved the issue could be a god technical example again. 







Dapr Internal fork

Internal fork - Maiantained internal fork of Dapr using patch for lesser merge conflicts and created entire framework, pipelines, repo all ownself. - You can mention this in the conflic scenario: patch (you supported) vs the (full repo clone), metion benefits like git intelligent patching, merging, go modules update etc, using scripts etc for that. Check usefulness of git patch. Handled complicated scenario for producing multi arch images for all suppryed versions of dapr and for all dap rimages all with a single pipeline

Ev2/onebranch pipeline migration, etc


ACA Service

Sesions - Resolved issues in code interpreter, perf tests addition. Nodejs sessions addition, own end to end, Geneva actions for noejs upgrades and monitoring, playwright testing team colaboration for using sessions, data plane apis for sessions like get/create/delete etc. , session management apis delete list get, code interpreter fixes, bigs async execution, 
• Sessions: Enabled customer adoption and usage via .NET code interpreter support for Security Copilot Team and fixing Node.js Sessions test failures.


Core ACA - AKV integration with Envirnment storage api
FCP Integration with ACA- surface agentic apps on ACA to FCP - you can mention telapp process for a complex technical problem, how it uses privileged access on host to find the process information using procpid things and then uses that information to find whether it's an agentic app - Good example for technical problem


SRE Agent
Several agents as part of RCA Agent
• ACA RCA Agent: Improved AI-aligned RCA accuracy and reduced ACA ICM timelines (P50 TTM 185→6, TTR 269→98) by introducing Sessions/Billing subagents and shifting from workflow-based to investigative prompts. Increased correctness by closing 20+ agent backlog items through targeted ICM analysis and updates across agent and subagents.
Auto repair agent
End to end setup for ACA RCA agent
Agent ev2 deployment pipeline




• ACA Functions: Expanded core platform capabilities via function keys management commands and strengthened diagnostics via invocation tracing/summary and support for durable-events logging. Also added API spec for function ARM apis. These enhancements benefit ~1,322 external ACA Functions apps, improving security, observability, and operational efficiency.
Drain functionality support 
Keda rules edit support
Queue Length override, scale rule override


ADC
Ephemeral volume support, Log Analytics support


Other points:
1. Conflict example: Using etcd for dapr in scheduler, you can mention differenet issues happening rn in etcd, but then you haven't so might not be fist choice, still a good conflict example if you want
2


Technical problesm:
1. Dapr workflows
2. Functions key management using debug container
2. Drain support in Functions using postExecute api
3. Auto detection of agents on ACA using telapp
4. RCA Agenyt


End to end journey for 

resume summary top for someone else for sample:
Software Engineer II at Microsoft, specializing in distributed systems, backend infrastructure, and scalable AI-powered platforms. I design, optimize, and scale services that handle millions of daily requests, improve GraphQL API latency by 270%, and accelerate provisioning latency by 60%, driving measurable impact across global customers.

At Microsoft, I’ve led initiatives in Kubernetes-based microservices, GraphQL APIs, Redis caching frameworks, observability pipelines, and security automation, collaborating across teams to deliver resilient, production-grade solutions.

With a strong foundation from IIT Kanpur (CSE), I bring a blend of deep technical expertise, system-level thinking, and cross-team leadership, thriving in high-scale, high-impact environments. Passionate about backend systems, infra reliability, and applied AI, I aim to build platforms that empower both developers and end-users at global scale.

