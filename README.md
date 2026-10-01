# HUMMBL Universal Agent Skills (v1.0.0)

A curated, open-source library of **1,283 universal AI agent skills**, workflows, evaluation harnesses, and cognitive tools.

Compatible with **Cursor, Claude Code, Antigravity CLI, OpenCode, and Codex**.

## Quick Install

### Install for Claude Code (~/.claude/skills)
```bash
git clone https://github.com/hummbl-io/agent-skills.git ~/.claude/skills/hummbl
```

### Install for Cursor (.cursor/skills)
```bash
git clone https://github.com/hummbl-io/agent-skills.git .cursor/skills/hummbl
```

## Official Base120 skill

[Base120 0.2.0](skills/base120/SKILL.md) includes all 120 reasoning operators,
an offline snapshot of SDK 3.0.0, source hashes, full license texts, and a
stdlib verifier. Use the entire `skills/base120/` directory so references stay
alongside the instructions. Lookup does not require MCP or provider access.

```bash
python skills/base120/scripts/verify_reference.py
```

[Distribution provenance](skills/base120/distribution.json) pins the canonical
skill commit and every copied file. Upstream source and maintenance repositories
may require access; this public bundle includes the complete lookup reference.
Skill and SDK versions are independent. Hash checks verify agreement with the
bundled metadata and do not establish empirical reasoning effectiveness.

## HUMMBL implementation sources

The [public source map](docs/public-sources.md) links HUMMBL's Python packages,
embedded Rust and TypeScript tuple references, Lean formalization tree, and
service-specific MCP adapters. Each entry includes its source and maturity
boundary. It also identifies the Node Base120 technical canary and its release
hold. The official skill above retains its own versioned offline snapshot.

## Skills Catalog (1,283 Total)

| Skill | Author / Upstream | License | Description |
|:---|:---|:---|:---|
| [`_index`](skills/_index/SKILL.md) | HUMMBL | Apache-2.0 | Skill index -- generated catalog of every local skill under ~/.agents/skills so agents can d... |
| [`a11y-audit`](skills/a11y-audit/SKILL.md) | HUMMBL | Apache-2.0 | Web accessibility audit against WCAG 2.1 AA standards |
| [`a11y-fix`](skills/a11y-fix/SKILL.md) | HUMMBL | Apache-2.0 | Generate specific fixes for accessibility audit findings with code patches |
| [`aar`](skills/aar/SKILL.md) | HUMMBL | Apache-2.0 | Generate an After Action Report with Base120 references and receipts. |
| [`aar-followthrough`](skills/aar-followthrough/SKILL.md) | HUMMBL | Apache-2.0 | "Run AFTER [aar] completes to elaborate and plan every §7 recommendation into an owned, veri... |
| [`ab-test-analyzer`](skills/ab-test-analyzer/SKILL.md) | HUMMBL | Apache-2.0 | "Analyze A/B test results for statistical significance, effect size, and practical importanc... |
| [`absence-audit`](skills/absence-audit/SKILL.md) | HUMMBL | Apache-2.0 | Find what's MISSING from a system -- unhandled cases, missing tests, absent monitoring, sile... |
| [`accelerated-computing-cudf`](skills/accelerated-computing-cudf/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Official NVIDIA-authored guidance for NVIDIA cuDF GPU DataFrames, pandas acceleration, dask-... |
| [`adapter-status`](skills/adapter-status/SKILL.md) | HUMMBL | Apache-2.0 | Check which service adapters are wired and operational. |
| [`admission-gate`](skills/admission-gate/SKILL.md) | HUMMBL | Apache-2.0 | Redaction gate for publishing fleet artifacts to external remotes. Hard-fails on local paths... |
| [`adr-review`](skills/adr-review/SKILL.md) | HUMMBL | Apache-2.0 | Review Architecture Decision Records for staleness, superseded decisions, missing outcomes, ... |
| [`agent`](skills/agent/SKILL.md) | HUMMBL | Apache-2.0 | Initialize any agent by name -- looks up the dispatch table and runs the right primitive (sk... |
| [`agent-audit`](skills/agent-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit a specific agent's bus activity, commit history, trust score, and guardrail compliance. |
| [`agent-browser`](skills/agent-browser/SKILL.md) | HUMMBL | Apache-2.0 | Browser automation CLI for AI agents. Use when the user needs to interact with websites, inc... |
| [`agent-compare`](skills/agent-compare/SKILL.md) | HUMMBL | Apache-2.0 | Side-by-side comparison of agent outputs on identical tasks — quality, speed, cost, accuracy |
| [`agent-cost-track`](skills/agent-cost-track/SKILL.md) | HUMMBL | Apache-2.0 | Track per-agent token usage and API costs with budget alerts and cost attribution |
| [`agent-design`](skills/agent-design/SKILL.md) | HUMMBL | Apache-2.0 | Design agentic workflows -- tool selection, loop structure, guardrails, memory, termination ... |
| [`agent-grade`](skills/agent-grade/SKILL.md) | HUMMBL | Apache-2.0 | Grade an agent's work on a 100-point rubric that scores verified, authorized state change — ... |
| [`agent-guardrail`](skills/agent-guardrail/SKILL.md) | HUMMBL | Apache-2.0 | Configure and test agent guardrails for input/output validation, tool-use constraints, and s... |
| [`agent-memory`](skills/agent-memory/SKILL.md) | HUMMBL | Apache-2.0 | Design agent memory systems with short-term, long-term, episodic, and semantic memory and re... |
| [`agent-metrics`](skills/agent-metrics/SKILL.md) | HUMMBL | Apache-2.0 | Aggregate agent performance metrics from bus, git, and CI history |
| [`agent-roster`](skills/agent-roster/SKILL.md) | HUMMBL | Apache-2.0 | Live probe of all known agents and models -- registry, bus activity, process status, model t... |
| [`agent-trace`](skills/agent-trace/SKILL.md) | HUMMBL | Apache-2.0 | Trace and debug agentic workflows by logging tool calls, decision points, and state transitions |
| [`agent-usage-report`](skills/agent-usage-report/SKILL.md) | HUMMBL | Apache-2.0 | Report named-agent usage telemetry, citation counts, first/last use, and backfill coverage f... |
| [`agents-sdk`](skills/agents-sdk/SKILL.md) | HUMMBL | Apache-2.0 | "Build Cloudflare Workers agents with Agents SDK: stateful agents, WebSockets, MCP servers, ... |
| [`ai-cost-optimize`](skills/ai-cost-optimize/SKILL.md) | HUMMBL | Apache-2.0 | Reduce AI API costs through caching, batching, model downsizing, prompt compression, and res... |
| [`ai-policy-review`](skills/ai-policy-review/SKILL.md) | HUMMBL | Apache-2.0 | Review and grade an existing internal AI use policy against NIST AI RMF, ISO 42001, and EU A... |
| [`ai-regulation`](skills/ai-regulation/SKILL.md) | HUMMBL | Apache-2.0 | Track AI-specific regulations -- EU AI Act, US executive orders, state bills, sector-specifi... |
| [`ai-risk-assessment`](skills/ai-risk-assessment/SKILL.md) | HUMMBL | Apache-2.0 | Full AI system risk assessment aligned to NIST AI RMF. Maps risks across GOVERN/MAP/MEASURE/... |
| [`ai-safety-check`](skills/ai-safety-check/SKILL.md) | HUMMBL | Apache-2.0 | Validate AI outputs for safety, bias, and robustness with comprehensive testing. [Maps to P9.] |
| [`aiq-deploy`](skills/aiq-deploy/SKILL.md) | HUMMBL | Apache-2.0 | Use when asked to install, deploy, run, validate, troubleshoot, or stop NVIDIA AI-Q Blueprin... |
| [`aiq-research`](skills/aiq-research/SKILL.md) | HUMMBL | Apache-2.0 | Use when asked to run deep research or AI-Q research through a reachable NVIDIA AI-Q Bluepri... |
| [`alert-digest`](skills/alert-digest/SKILL.md) | HUMMBL | Apache-2.0 | Summarize and deduplicate recent alerts, identify fatigue patterns |
| [`alert-noise-reduce`](skills/alert-noise-reduce/SKILL.md) | HUMMBL | Apache-2.0 | Deduplicate and correlate alerts to reduce noise. Groups similar alerts by signature, suppre... |
| [`alert-rule`](skills/alert-rule/SKILL.md) | HUMMBL | Apache-2.0 | Create and manage alert rules for health probes, cost thresholds, and CI failures |
| [`alert-triage`](skills/alert-triage/SKILL.md) | HUMMBL | Apache-2.0 | Triage incoming alerts, suppress duplicates, correlate related alerts, route to the right re... |
| [`algorithmic-art`](skills/algorithmic-art/SKILL.md) | HUMMBL | Apache-2.0 | "Create original, self-contained, and verified p5.js generative art from an algorithmic phil... |
| [`alignment-check`](skills/alignment-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify agent outputs align with stated goals — detect goal drift, reward hacking, specificat... |
| [`alphafold-database-fetch-and-analyze`](skills/alphafold-database-fetch-and-analyze/SKILL.md) | HUMMBL | Apache-2.0 | Retrieve and analyze AlphaFold predicted structures for a protein. Use when the user provide... |
| [`alphagenome-single-variant-analysis`](skills/alphagenome-single-variant-analysis/SKILL.md) | HUMMBL | Apache-2.0 | Analyzes genetic variant effects on gene expression (RNA-seq), chromatin accessibility (DNAS... |
| [`amazon-bedrock`](skills/amazon-bedrock/SKILL.md) | HUMMBL | Apache-2.0 | Builds generative AI applications on Amazon Bedrock. Covers model invocation (Converse API, ... |
| [`amberteam`](skills/amberteam/SKILL.md) | HUMMBL | Apache-2.0 | Supply chain security -- security of dependencies, third-party libraries, build pipelines, a... |
| [`amc-run-rtsp-calibration`](skills/amc-run-rtsp-calibration/SKILL.md) | HUMMBL | "Apache-2.0" | "Calibrate a new dataset from live RTSP camera streams via the AutoMagicCalib REST API. Use ... |
| [`amc-run-sample-calibration`](skills/amc-run-sample-calibration/SKILL.md) | HUMMBL | "Apache-2.0" | "Run end-to-end calibration on the shipped sample dataset (sdg_08_2_sample_data_010926.zip) ... |
| [`amc-run-video-calibration`](skills/amc-run-video-calibration/SKILL.md) | HUMMBL | "Apache-2.0" | "Calibrates pre-recorded `cam_*.mp4` datasets through the AutoMagicCalib REST API. Use for u... |
| [`amc-setup-calibration-stack`](skills/amc-setup-calibration-stack/SKILL.md) | HUMMBL | "Apache-2.0" | "Launch AutoMagicCalib microservice and web UI from NGC release images via Docker Compose. U... |
| [`anthropic-watch`](skills/anthropic-watch/SKILL.md) | HUMMBL | Apache-2.0 | Track bleeding-edge Anthropic announcements -- model releases, API changes, Claude Code upda... |
| [`apex`](skills/apex/SKILL.md) | HUMMBL | Apache-2.0 | Recon-first assessment mode — think before acting, produce a plan, delegate execution to the... |
| [`api-design`](skills/api-design/SKILL.md) | HUMMBL | Apache-2.0 | Design REST/HTTP APIs with consistent patterns -- endpoints, errors, pagination, auth. |
| [`api-docs`](skills/api-docs/SKILL.md) | HUMMBL | Apache-2.0 | Generate API documentation from FastAPI/Flask endpoints or Python function signatures |
| [`api-test`](skills/api-test/SKILL.md) | HUMMBL | Apache-2.0 | Generate and run HTTP API tests against live or mocked endpoints |
| [`apply-review`](skills/apply-review/SKILL.md) | HUMMBL | Apache-2.0 | Review application materials (resume, cover letter, LinkedIn copy, portfolio one-pager, outr... |
| [`arcana-peer-review`](skills/arcana-peer-review/SKILL.md) | HUMMBL | Apache-2.0 | Simulate independent non-author review by dispatching ARCANA-archetype subagents, each apply... |
| [`arcana-review`](skills/arcana-review/SKILL.md) | HUMMBL | Apache-2.0 | Multi-agent peer review using diverse epistemological lenses. Dispatches N subagents (subage... |
| [`arcana-to-pitch`](skills/arcana-to-pitch/SKILL.md) | HUMMBL | Apache-2.0 | Transform ARCANA multi-lens synthesis outputs into HUMMBL pitch materials. Converts philosop... |
| [`arch-diagram`](skills/arch-diagram/SKILL.md) | HUMMBL | Apache-2.0 | Generate interactive architecture diagrams as self-contained HTML/SVG files. |
| [`aria-label-audit`](skills/aria-label-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit ARIA labels and accessibility attributes for correctness and completeness. [Maps to P9.] |
| [`artifact-compiler-benchmark`](skills/artifact-compiler-benchmark/SKILL.md) | HUMMBL | Apache-2.0 | Run multi-dimensional latency, memory, and scaling benchmarks for the Compatibility-Aware Ar... |
| [`ask-the-stack`](skills/ask-the-stack/SKILL.md) | HUMMBL | Apache-2.0 | Query the full knowledge stack (CLP + bibliography + bus + evidence docs) for research-groun... |
| [`assessment-report`](skills/assessment-report/SKILL.md) | HUMMBL | Apache-2.0 | Generate governance assessment report from checklist results and scores. |
| [`assumption-audit`](skills/assumption-audit/SKILL.md) | HUMMBL | Apache-2.0 | Surface hidden assumptions in code, architecture, or decisions — list what must be true for ... |
| [`async-update`](skills/async-update/SKILL.md) | HUMMBL | Apache-2.0 | Quick 3-sentence async update for any stakeholder. Where things stand, what's next, what the... |
| [`audit-prep`](skills/audit-prep/SKILL.md) | HUMMBL | Apache-2.0 | Prepare for external audit -- evidence checklist, gap identification, document organization,... |
| [`auth-audit`](skills/auth-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit authentication and authorization patterns including token handling, session management... |
| [`auto-ship`](skills/auto-ship/SKILL.md) | HUMMBL | Apache-2.0 | "Alias for the lfg skill (compound-engineering plugin). Full autonomous shipping pipeline: p... |
| [`autofix`](skills/autofix/SKILL.md) | HUMMBL | Apache-2.0 | Safely review and apply CodeRabbit PR review-thread feedback from GitHub with per-change app... |
| [`automation-roi`](skills/automation-roi/SKILL.md) | HUMMBL | Apache-2.0 | Calculate ROI for automating a manual workflow -- time saved, break-even, payback period. |
| [`autoresearch-mode`](skills/autoresearch-mode/SKILL.md) | HUMMBL | Apache-2.0 | Governed, receipt-producing autonomous research mode with scheduled cadence and operator-fac... |
| [`autoresearch-tui`](skills/autoresearch-tui/SKILL.md) | HUMMBL | Apache-2.0 | Real-time observability TUI for the autoresearch overnight GPU training loop. One file, stdl... |
| [`autotile-rule-compiler`](skills/autotile-rule-compiler/SKILL.md) | HUMMBL | Apache-2.0 | Generates 2D auto-tiling rulesets from minimal input. Supports 2x2 corner-based, 3x3 minimal... |
| [`aws-ai-ml`](skills/aws-ai-ml/SKILL.md) | HUMMBL | Apache-2.0 | Selects, deploys, and customizes AI models on Amazon SageMaker. Fine-tuning (SFT, DPO, RLVR,... |
| [`aws-auth`](skills/aws-auth/SKILL.md) | HUMMBL | Apache-2.0 | Adds user authentication to web and mobile apps with Amazon Cognito (user pools and identity... |
| [`aws-billing-and-cost-management`](skills/aws-billing-and-cost-management/SKILL.md) | HUMMBL | Apache-2.0 | Analyze AWS costs, find savings, manage budgets, evaluate Savings Plans and Reserved Instanc... |
| [`aws-blocks`](skills/aws-blocks/SKILL.md) | HUMMBL | Apache-2.0 | Guides building full-stack applications with AWS Blocks — an Infrastructure-from-Code framew... |
| [`aws-cdk`](skills/aws-cdk/SKILL.md) | HUMMBL | Apache-2.0 | Authors, deploys, and troubleshoots AWS infrastructure using CDK with TypeScript or Python. ... |
| [`aws-cloudformation`](skills/aws-cloudformation/SKILL.md) | HUMMBL | Apache-2.0 | Authors, validates, and troubleshoots AWS CloudFormation templates. Covers template authorin... |
| [`aws-compute`](skills/aws-compute/SKILL.md) | HUMMBL | Apache-2.0 | Provisions, scales, and operates Amazon EC2 virtual-machine workloads: instance-type selecti... |
| [`aws-containers`](skills/aws-containers/SKILL.md) | HUMMBL | Apache-2.0 | Builds and deploys containerized workloads on Elastic Kubernetes Service (EKS), Elastic Cont... |
| [`aws-database`](skills/aws-database/SKILL.md) | HUMMBL | Apache-2.0 | Routes any task involving AWS databases — choosing, comparing, recommending, getting started... |
| [`aws-deployment`](skills/aws-deployment/SKILL.md) | HUMMBL | Apache-2.0 | Configures CI/CD pipelines using AWS CodePipeline, CodeBuild, CodeDeploy, CodeConnections, a... |
| [`aws-iam`](skills/aws-iam/SKILL.md) | HUMMBL | Apache-2.0 | Provides verified corrections for IAM behaviors that AI agents frequently get wrong — policy... |
| [`aws-messaging-and-streaming`](skills/aws-messaging-and-streaming/SKILL.md) | HUMMBL | Apache-2.0 | Guides general use of AWS messaging and streaming services. Covers Amazon SQS, Amazon SNS, A... |
| [`aws-networking`](skills/aws-networking/SKILL.md) | HUMMBL | Apache-2.0 | Routes AWS networking requests to the correct service skill for implementation. Covers Route... |
| [`aws-observability`](skills/aws-observability/SKILL.md) | HUMMBL | Apache-2.0 | Builds, configures, debugs, and optimizes AWS observability with CloudWatch (Log Insights, M... |
| [`aws-sdk-js-v3-usage`](skills/aws-sdk-js-v3-usage/SKILL.md) | HUMMBL | Apache-2.0 | AWS SDK for JavaScript v3 development patterns. Use when writing JavaScript or TypeScript co... |
| [`aws-sdk-python-usage`](skills/aws-sdk-python-usage/SKILL.md) | HUMMBL | Apache-2.0 | AWS SDK for Python (boto3/botocore) development patterns. You MUST use this skill when writi... |
| [`aws-sdk-swift-usage`](skills/aws-sdk-swift-usage/SKILL.md) | HUMMBL | Apache-2.0 | AWS SDK for Swift development patterns. Use when writing Swift code that uses AWS services v... |
| [`aws-security`](skills/aws-security/SKILL.md) | HUMMBL | Apache-2.0 | Covers AWS security services and workflows — Security Hub V2 (OCSF) findings, connectors, ag... |
| [`aws-serverless`](skills/aws-serverless/SKILL.md) | HUMMBL | Apache-2.0 | Builds, deploys, manages, debugs, configures, and optimizes serverless applications on AWS u... |
| [`aws-storage`](skills/aws-storage/SKILL.md) | HUMMBL | Apache-2.0 | Selects, investigates, and compares AWS object, file, and block storage services, and answer... |
| [`base120`](skills/base120/SKILL.md) | HUMMBL | MIT OR Apache-2.0 | Official 0.2.0 skill: all 120 operators, a pinned offline reference, and optional stdlib verification. |
| [`base120-compose`](skills/base120-compose/SKILL.md) | HUMMBL | Apache-2.0 | "The Synthesist. Composition transformation of Base120 (CO1-CO20). Build the whole the parts... |
| [`base120-decompose`](skills/base120-decompose/SKILL.md) | HUMMBL | Apache-2.0 | "The Anatomist. Decomposition transformation of Base120 (DE1-DE20). Break wholes until each ... |
| [`base120-infrastructure`](skills/base120-infrastructure/SKILL.md) | HUMMBL | Apache-2.0 | Infrastructure for adding --base120 cognitive structuring to skill scripts at fleet scale. P... |
| [`base120-invert`](skills/base120-invert/SKILL.md) | HUMMBL | Apache-2.0 | "The Contrarian. Inversion transformation of Base120 (IN1-IN20). Negate assumptions, find th... |
| [`base120-perspect`](skills/base120-perspect/SKILL.md) | HUMMBL | Apache-2.0 | "The Framer. Perspective transformation of Base120 (P1-P20). Name what is before anyone touc... |
| [`base120-recurse`](skills/base120-recurse/SKILL.md) | HUMMBL | Apache-2.0 | "The Iterator. Recursion transformation of Base120 (RE1-RE20). Apply patterns across scales ... |
| [`base120-systema`](skills/base120-systema/SKILL.md) | HUMMBL | Apache-2.0 | "The Steward. Systems transformation of Base120 (SY1-SY20). Hold the whole — find the levera... |
| [`base120-verify`](skills/base120-verify/SKILL.md) | HUMMBL | Apache-2.0 | Grade Base120 alignment reports as draft or receipt using artifact evidence fields — rejecte... |
| [`basen`](skills/basen/SKILL.md) | HUMMBL | Apache-2.0 | BaseN-tier multi-variant operator catalog. Lookup / search / apply / recommend across regist... |
| [`bg-agent`](skills/bg-agent/SKILL.md) | HUMMBL | Apache-2.0 | Manage background subagents with tier-routed models, stripped tool contexts, lifecycle pruni... |
| [`bibliometric`](skills/bibliometric/SKILL.md) | HUMMBL | Apache-2.0 | Bibliometric analysis - publication counts, h-index, citation impact, co-authorship networks... |
| [`bio-energy-physical-aggregator-research`](skills/bio-energy-physical-aggregator-research/SKILL.md) | HUMMBL | Apache-2.0 | Domain research skill for Bio, Energy & Physical aggregator discovery. Catalogs canonical ag... |
| [`biocognitive-assessment`](skills/biocognitive-assessment/SKILL.md) | HUMMBL | Apache-2.0 | Administer and score the HUMMBL Biocognitive OS Assessment — an 18-question diagnostic instr... |
| [`bki-cite-audit`](skills/bki-cite-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit the BKI corpus bibliography — verify each citation exists, check claim-source match, f... |
| [`bki-evidence-flywheel`](skills/bki-evidence-flywheel/SKILL.md) | HUMMBL | Apache-2.0 | Search for new empirical evidence supporting BKI propositions (belonging, cognitive science,... |
| [`bki-reframe`](skills/bki-reframe/SKILL.md) | HUMMBL | Apache-2.0 | Capture and classify somatic-linguistic belonging reframes ("have to" vs "get to"). Names th... |
| [`bki-session-export`](skills/bki-session-export/SKILL.md) | HUMMBL | Apache-2.0 | Package BKI session insights (new questions, corrections, theory updates) as a structured am... |
| [`blocker-scanner`](skills/blocker-scanner/SKILL.md) | HUMMBL | Apache-2.0 | Scan local fleet surfaces for P0-P3 blockers — git, bus, rules, skills, tests, security, gov... |
| [`blog-draft`](skills/blog-draft/SKILL.md) | HUMMBL | Apache-2.0 | Draft technical blog post with outline, code samples, SEO metadata, and CTA |
| [`blueteam`](skills/blueteam/SKILL.md) | HUMMBL | Apache-2.0 | Defensive analysis — for a given asset, system, change, or red-team report, identify existin... |
| [`board-meeting-orchestrator`](skills/board-meeting-orchestrator/SKILL.md) | HUMMBL | Apache-2.0 | Run an AI Board of Directors meeting. Reads the Board Constitution Registry, gathers live co... |
| [`bokka`](skills/bokka/SKILL.md) | HUMMBL | MIT | Cavewoman character: BOKKA, the scout. Nervous, quick, speaks in short bursts. Always lookin... |
| [`brainstorm`](skills/brainstorm/SKILL.md) | HUMMBL | Apache-2.0 | Design-first exploration -- no code until the user approves a design. |
| [`branch-strategy`](skills/branch-strategy/SKILL.md) | HUMMBL | Apache-2.0 | Visualize branch topology, find stale/diverged branches, suggest cleanup. |
| [`brand`](skills/brand/SKILL.md) | HUMMBL | Apache-2.0 | "DEPRECATED: Use brand-guidelines instead. This skill is retired as of 2026-08-19 and kept o... |
| [`brand-admission`](skills/brand-admission/SKILL.md) | HUMMBL | Apache-2.0 | Brand-specific admission gate overlay that adds palette-token, visual-asset, and brand-guide... |
| [`brand-factory`](skills/brand-factory/SKILL.md) | HUMMBL | Apache-2.0 | Generate novel brand name candidates from etymological roots, verify domain availability via... |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | HUMMBL | Apache-2.0 | Applies HUMMBL's official design system tokens (two-tone green system with Grove and Verdere... |
| [`brew-audit`](skills/brew-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit Homebrew packages for outdated, unused, and security issues |
| [`briefing-history`](skills/briefing-history/SKILL.md) | HUMMBL | Apache-2.0 | List, search, compare, and show past morning briefings. |
| [`budget-plan`](skills/budget-plan/SKILL.md) | HUMMBL | Apache-2.0 | Monthly/quarterly budget allocation with variance tracking against actuals |
| [`build`](skills/build/SKILL.md) | HUMMBL | Apache-2.0 | Implementation surge mode — TDD-first, coverage-verified, deslop-checked. For feature builds... |
| [`bulk-edit`](skills/bulk-edit/SKILL.md) | HUMMBL | Apache-2.0 | Apply the same edit across many files safely -- find, preview, apply, verify. |
| [`burn-rate-track`](skills/burn-rate-track/SKILL.md) | HUMMBL | Apache-2.0 | Track monthly burn rate with trend analysis. Monitors spend velocity, forecasts runway, and ... |
| [`bus`](skills/bus/SKILL.md) | HUMMBL | Apache-2.0 | Read or post to the coordination bus (append-only TSV message log). |
| [`bus-analytics`](skills/bus-analytics/SKILL.md) | HUMMBL | Apache-2.0 | Analyze coordination bus message patterns, frequency, and agent activity. |
| [`bus-audit`](skills/bus-audit/SKILL.md) | HUMMBL | Apache-2.0 | Parse the fleet bus TSV and produce a Rumsfeldian epistemological map -- known knowns, known... |
| [`bus-forensics`](skills/bus-forensics/SKILL.md) | HUMMBL | Apache-2.0 | Forensically analyze the coordination bus — reconstruct event timelines, trace response chai... |
| [`business-review`](skills/business-review/SKILL.md) | HUMMBL | Apache-2.0 | Review an external business using source-traceable evidence, explicit uncertainty, commercia... |
| [`canary-deploy`](skills/canary-deploy/SKILL.md) | HUMMBL | Apache-2.0 | Gradual rollout verification -- deploy to subset, compare metrics, promote or rollback |
| [`canvas-design`](skills/canvas-design/SKILL.md) | HUMMBL | Apache-2.0 | Create beautiful visual art in .png and .pdf documents using design philosophy. You should u... |
| [`cap-table`](skills/cap-table/SKILL.md) | HUMMBL | Apache-2.0 | Build or update an equity cap table. Founders, investors, option pool. Shows ownership %, di... |
| [`case-study`](skills/case-study/SKILL.md) | HUMMBL | Apache-2.0 | Generate a structured case study from project data with metrics and outcomes |
| [`cashflow-project`](skills/cashflow-project/SKILL.md) | HUMMBL | Apache-2.0 | Project cash flow scenarios (base/bull/bear). Models inflows, outflows, and runway under mul... |
| [`catalog-write`](skills/catalog-write/SKILL.md) | HUMMBL | Apache-2.0 | Orchestrate catalog-style research writeups — individual pieces first, index last, git-track... |
| [`caveman-bespoke`](skills/caveman-bespoke/SKILL.md) | HUMMBL | MIT | Combined token-saver + code-maximizer. Mouth small (caveman prose) AND code full (enterprise... |
| [`caveman-mode`](skills/caveman-mode/SKILL.md) | HUMMBL | Apache-2.0 | Caveman voice adapter for HUMMBL communication profiles. Equivalent to --voice=caveman with ... |
| [`caveman-ponytail`](skills/caveman-ponytail/SKILL.md) | HUMMBL | MIT | Combined token-saver + code-minimizer. Mouth small (caveman prose) AND code small (lazy seni... |
| [`cd-monitor`](skills/cd-monitor/SKILL.md) | HUMMBL | Apache-2.0 | Monitor deployment, rollout, promotion, and post-release health status. Use when the user as... |
| [`cert-tracker`](skills/cert-tracker/SKILL.md) | HUMMBL | Apache-2.0 | Track certification progress with deadlines, study hours, and requirements |
| [`chain-evolve`](skills/chain-evolve/SKILL.md) | HUMMBL | Apache-2.0 | Validate skill-chains.md against actual usage sequences — find emergent chains, dead chains,... |
| [`chain-validate`](skills/chain-validate/SKILL.md) | HUMMBL | Apache-2.0 | Verify every skill referenced in Skill Chains sections actually exists in the registry. Catc... |
| [`changelog`](skills/changelog/SKILL.md) | HUMMBL | Apache-2.0 | Generate changelog between two refs using conventional commits. |
| [`changelog-digest`](skills/changelog-digest/SKILL.md) | HUMMBL | Apache-2.0 | Generate a human-readable digest of changes for non-technical stakeholders. |
| [`changelog-post`](skills/changelog-post/SKILL.md) | HUMMBL | Apache-2.0 | Turn a git changelog into a polished "What's New" blog post or social announcement |
| [`changelog-rss`](skills/changelog-rss/SKILL.md) | HUMMBL | Apache-2.0 | Publish changelog as RSS/Atom feed for external subscribers |
| [`changelog-subscribe`](skills/changelog-subscribe/SKILL.md) | HUMMBL | Apache-2.0 | Watch upstream dependencies for breaking changes and security advisories |
| [`chaos-test`](skills/chaos-test/SKILL.md) | HUMMBL | Apache-2.0 | Run controlled chaos tests to verify circuit breakers and kill switch behavior |
| [`chart`](skills/chart/SKILL.md) | HUMMBL | Apache-2.0 | Generate ASCII or SVG charts from data (bar, line, scatter, histogram, pie) |
| [`chatgpt-handoff`](skills/chatgpt-handoff/SKILL.md) | HUMMBL | Apache-2.0 | Ingest a ChatGPT response, route to downstream skills based on category tag, confirm scope, ... |
| [`chembl-database`](skills/chembl-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved ... |
| [`cherry-pick-safe`](skills/cherry-pick-safe/SKILL.md) | HUMMBL | Apache-2.0 | Cherry-pick commits with conflict detection, test verification, and bus notification. |
| [`churn-analysis`](skills/churn-analysis/SKILL.md) | HUMMBL | Apache-2.0 | Analyze client churn signals including engagement drops, support spikes, and renewal risk sc... |
| [`ci-monitor`](skills/ci-monitor/SKILL.md) | HUMMBL | Apache-2.0 | Monitor GitHub Actions -- list runs, check status, view logs, retry failed jobs. |
| [`ci-wait`](skills/ci-wait/SKILL.md) | HUMMBL | Apache-2.0 | Watch a CI run until completion and report pass/fail. |
| [`circuit-status`](skills/circuit-status/SKILL.md) | HUMMBL | Apache-2.0 | Show circuit breaker state per adapter. |
| [`citation-network`](skills/citation-network/SKILL.md) | HUMMBL | Apache-2.0 | Analyze citation networks - build directed graphs of citations, identify influential works, ... |
| [`claim-verify`](skills/claim-verify/SKILL.md) | HUMMBL | Apache-2.0 | Extract all factual claims from text, verify against web sources, produce verdict table with... |
| [`claims-review`](skills/claims-review/SKILL.md) | HUMMBL | Apache-2.0 | Structured peer review of a claim set from an artifact or tool. Dual-mode (artifact claims -... |
| [`claude-api`](skills/claude-api/SKILL.md) | HUMMBL | Apache-2.0 | "Build, debug, migrate, or optimize Claude API / Anthropic SDK apps, including prompt cachin... |
| [`cli-design`](skills/cli-design/SKILL.md) | HUMMBL | Apache-2.0 | Design CLI interfaces with consistent flags, help text, and subcommands |
| [`cli-harness`](skills/cli-harness/SKILL.md) | HUMMBL | Apache-2.0 | Build and run test harnesses for CLI tools — captures exit code, stdout/stderr, filesystem m... |
| [`client-report`](skills/client-report/SKILL.md) | HUMMBL | Apache-2.0 | Generate periodic client progress report from time logs, deliverables, and milestones |
| [`clinical-trials-database`](skills/clinical-trials-database/SKILL.md) | HUMMBL | Apache-2.0 | Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by condition, dru... |
| [`clinvar-database`](skills/clinvar-database/SKILL.md) | HUMMBL | Apache-2.0 | Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Ben... |
| [`cloud-estate-manager`](skills/cloud-estate-manager/SKILL.md) | HUMMBL | Apache-2.0 | Inventory, reconcile, and record provenance for the HUMMBL cloud-estate against the closed-w... |
| [`cloudflare`](skills/cloudflare/SKILL.md) | HUMMBL | Apache-2.0 | "Build or debug Cloudflare platform work across Workers, Pages, KV, D1, R2, Workers AI, Vect... |
| [`cloudflare-email-service`](skills/cloudflare-email-service/SKILL.md) | HUMMBL | Apache-2.0 | "Build or debug Cloudflare Email Sending/Routing in Workers or apps, including bindings, RES... |
| [`code-review`](skills/code-review/SKILL.md) | HUMMBL | Apache-2.0 | AI-powered code review using CodeRabbit. Default code-review skill. Trigger for any explicit... |
| [`codebase-tour`](skills/codebase-tour/SKILL.md) | HUMMBL | Apache-2.0 | Generate a guided tour of a codebase with entry points, key modules, data flow, and start-he... |
| [`codegen-eval`](skills/codegen-eval/SKILL.md) | HUMMBL | Apache-2.0 | Evaluate AI-generated code for correctness, style, security, and maintainability. Run static... |
| [`coding-scheme`](skills/coding-scheme/SKILL.md) | HUMMBL | Apache-2.0 | Develop and apply qualitative coding schemes - deductive, inductive, or abductive coding wit... |
| [`coffee-chat`](skills/coffee-chat/SKILL.md) | HUMMBL | Apache-2.0 | Informal networking call prep. Who is this person, what to learn (not pitch), 3 questions, 3... |
| [`cognitive-load`](skills/cognitive-load/SKILL.md) | HUMMBL | Apache-2.0 | Estimate cognitive load of UI elements using task complexity, information density, and Hick'... |
| [`color-contrast`](skills/color-contrast/SKILL.md) | HUMMBL | Apache-2.0 | Check and suggest color contrast ratios for WCAG compliance. [Maps to P9.] |
| [`color-team-engine`](skills/color-team-engine/SKILL.md) | HUMMBL | Apache-2.0 | Full-spectrum color team registry and dispatcher for security wargames. Reads color-registry... |
| [`commerce-travel-culture-aggregator-research`](skills/commerce-travel-culture-aggregator-research/SKILL.md) | HUMMBL | Apache-2.0 | Domain research skill for Commerce, Travel & Culture aggregator discovery. Catalogs canonica... |
| [`commit`](skills/commit/SKILL.md) | HUMMBL | Apache-2.0 | Stage and commit changes with Conventional Commits format and co-author attribution. |
| [`competitive-intel`](skills/competitive-intel/SKILL.md) | HUMMBL | Apache-2.0 | Research and compare competitors, alternatives, and market positioning. |
| [`complexity-score`](skills/complexity-score/SKILL.md) | HUMMBL | Apache-2.0 | Cyclomatic and cognitive complexity scoring per function with hotspot ranking and simplifica... |
| [`compliance-calendar`](skills/compliance-calendar/SKILL.md) | HUMMBL | Apache-2.0 | Generate and track compliance deadlines, audit windows, certification expirations |
| [`concept-map`](skills/concept-map/SKILL.md) | HUMMBL | Apache-2.0 | Generate concept maps from code or docs — dependency graphs as Mermaid or ASCII diagrams |
| [`config-drift`](skills/config-drift/SKILL.md) | HUMMBL | Apache-2.0 | Detect configuration drift across machines in the mesh |
| [`config-matrix`](skills/config-matrix/SKILL.md) | HUMMBL | Apache-2.0 | Systematically test configuration combinations -- env vars, feature flags, provider settings... |
| [`conflict-resolve`](skills/conflict-resolve/SKILL.md) | HUMMBL | Apache-2.0 | Guided merge conflict resolution with context from both sides and semantic understanding. |
| [`container-scan`](skills/container-scan/SKILL.md) | HUMMBL | Apache-2.0 | Scan container images for vulnerabilities, bloat, unnecessary packages, and hardening issues |
| [`content-calendar`](skills/content-calendar/SKILL.md) | HUMMBL | Apache-2.0 | Plan and track content across channels (blog, social, newsletter) with publish dates |
| [`content-design`](skills/content-design/SKILL.md) | HUMMBL | Apache-2.0 | Design product microcopy, labels, onboarding text, empty states, error messages, help text, ... |
| [`content-review`](skills/content-review/SKILL.md) | HUMMBL | Apache-2.0 | Review outbound content (blog posts, one-pagers, social, docs) for accuracy, tone, brand, an... |
| [`context-budget`](skills/context-budget/SKILL.md) | HUMMBL | Apache-2.0 | Monitor and optimize context window usage -- suggest compaction, trim bloat, manage token bu... |
| [`context-evolve`](skills/context-evolve/SKILL.md) | HUMMBL | Apache-2.0 | Measure token cost of every auto-injected file — rank by cost-per-relevance, suggest compres... |
| [`context-export`](skills/context-export/SKILL.md) | HUMMBL | Apache-2.0 | Export live machine context as a pasteable block for claude.ai conversations |
| [`contract-drift`](skills/contract-drift/SKILL.md) | HUMMBL | Apache-2.0 | Detect drift in structured contracts from SKILL.md frontmatter against a frozen baseline; va... |
| [`contract-negotiate`](skills/contract-negotiate/SKILL.md) | HUMMBL | Apache-2.0 | Review contract/SOW terms, flag risky clauses, and suggest alternatives |
| [`contract-review`](skills/contract-review/SKILL.md) | HUMMBL | Apache-2.0 | Review and validate contract schemas for breaking changes and compatibility. |
| [`contract-test`](skills/contract-test/SKILL.md) | HUMMBL | Apache-2.0 | Verify service responses against contract schemas in contracts/ directory |
| [`contractor-agreement`](skills/contractor-agreement/SKILL.md) | HUMMBL | Apache-2.0 | Draft an Independent Contractor Agreement (ICA). Covers scope, rate, IP assignment, confiden... |
| [`contributor-guide`](skills/contributor-guide/SKILL.md) | HUMMBL | Apache-2.0 | Generate CONTRIBUTING.md with dev setup, PR process, code style, and testing requirements fr... |
| [`control-catalog`](skills/control-catalog/SKILL.md) | HUMMBL | Apache-2.0 | Manage a catalog of governance controls mapped to multiple frameworks (NIST, ISO, SOC 2). |
| [`coronal-mission-pack`](skills/coronal-mission-pack/SKILL.md) | HUMMBL | Apache-2.0 | The Coronal Agent's pre-loaded skill set — everything an overnight/multi-PR coordination shi... |
| [`cost-forecast`](skills/cost-forecast/SKILL.md) | HUMMBL | Apache-2.0 | Predict next month API spend from usage trends — daily burn rate, projections, budget exhaus... |
| [`cost-governor`](skills/cost-governor/SKILL.md) | HUMMBL | Apache-2.0 | "Set and enforce spending limits across cloud infrastructure, AI/LLM API calls, and agent fl... |
| [`cost-status`](skills/cost-status/SKILL.md) | HUMMBL | Apache-2.0 | Query costs.db for budget, spend, and governor decisions. |
| [`counterfactual`](skills/counterfactual/SKILL.md) | HUMMBL | Apache-2.0 | Explore "what if we'd chosen differently" for past decisions. Maps to IN17. |
| [`coverage`](skills/coverage/SKILL.md) | HUMMBL | Apache-2.0 | Run pytest with coverage and report uncovered modules. |
| [`coverage-gate`](skills/coverage-gate/SKILL.md) | HUMMBL | Apache-2.0 | Enforce per-PR coverage deltas and fail builds on coverage regression. CI-integrable coverag... |
| [`crab`](skills/crab/SKILL.md) | HUMMBL | Apache-2.0 | Mandatory multi-agent turn execution protocol -- CRAWL/Check, Reason, Act, Bus. Run before a... |
| [`crab-loop`](skills/crab-loop/SKILL.md) | HUMMBL | Apache-2.0 | CRAB-wrapped bounded iteration -- one WIP_START, a /loop converge/retry/watch body, one WIP_... |
| [`crisis-mode`](skills/crisis-mode/SKILL.md) | HUMMBL | Apache-2.0 | Calm-first crisis response — stabilize before you solve, preserve evidence, postmortem manda... |
| [`crm`](skills/crm/SKILL.md) | HUMMBL | Apache-2.0 | Manage your CRM (e.g., Google Sheets) -- contacts, pipelines, interactions, and digest |
| [`cross-agent`](skills/cross-agent/SKILL.md) | HUMMBL | Apache-2.0 | Chief synthesis officer for multi-agent analysis. Use this after two or more agents, lanes, ... |
| [`cross-pr-conflict-scan`](skills/cross-pr-conflict-scan/SKILL.md) | HUMMBL | Apache-2.0 | Detect semantic and merge conflicts BETWEEN open sibling PRs — same-file collisions, merge-o... |
| [`cross-repo-grep`](skills/cross-repo-grep/SKILL.md) | HUMMBL | Apache-2.0 | Search pattern across all PROJECTS/ repos with repo-level grouping |
| [`cross-runtime-bridge`](skills/cross-runtime-bridge/SKILL.md) | HUMMBL | Apache-2.0 | Delegate tasks from Devin to opencode (background execution runtime). One-shot delegation, p... |
| [`cross-runtime-validation`](skills/cross-runtime-validation/SKILL.md) | Devin (GLM-5.2) | Apache-2.0 | Cross-runtime epistemic validation protocol. Run the same task against multiple independent ... |
| [`crucible-telemetry`](skills/crucible-telemetry/SKILL.md) | HUMMBL | Apache-2.0 | Agent lifecycle metrics, guardrail violations, and fleet health. |
| [`csv-analyze`](skills/csv-analyze/SKILL.md) | HUMMBL | Apache-2.0 | Load CSV, compute stats (mean, median, std dev, outliers, correlations), generate summary |
| [`cudaq-guide`](skills/cudaq-guide/SKILL.md) | CUDA-Q Team <cuda-qua... | "Apache-2.0" | "Use for CUDA-Q setup, simulation targets, QPU access, and @cudaq.kernel authoring guidance." |
| [`cudaq-importing`](skills/cudaq-importing/SKILL.md) | CUDA-Q Team <cuda-qua... | "Apache-2.0" | "Use when porting circuits from another framework (e.g. Qiskit) into CUDA-Q kernels while pr... |
| [`cultural-adapt`](skills/cultural-adapt/SKILL.md) | HUMMBL | Apache-2.0 | Adapt communication, docs, and UX for different audiences -- technical vs business, US vs in... |
| [`cuopt-developer`](skills/cuopt-developer/SKILL.md) | HUMMBL | Apache-2.0 | Modify, build, test, debug, and contribute to NVIDIA cuOpt (C++/CUDA, Python, server, CI). U... |
| [`cuopt-install`](skills/cuopt-install/SKILL.md) | HUMMBL | Apache-2.0 | Install cuOpt for Python, C, or server via pip, conda, or Docker; verify the install. For bu... |
| [`cuopt-multi-objective-exploration`](skills/cuopt-multi-objective-exploration/SKILL.md) | HUMMBL | Apache-2.0 | Trace, complete, and interpret the Pareto frontier across competing objectives using repeate... |
| [`cuopt-numerical-optimization-api`](skills/cuopt-numerical-optimization-api/SKILL.md) | HUMMBL | Apache-2.0 | LP, MILP, and QP (beta) with cuOpt — Python, C, and CLI. Use when the user is solving LP, MI... |
| [`cuopt-numerical-optimization-formulation`](skills/cuopt-numerical-optimization-formulation/SKILL.md) | HUMMBL | Apache-2.0 | LP, MILP, QP — concepts, problem-text parsing, and formulation patterns (parameters, constra... |
| [`cuopt-routing-api-python`](skills/cuopt-routing-api-python/SKILL.md) | HUMMBL | Apache-2.0 | Vehicle routing (VRP, TSP, PDP) with cuOpt — Python API only. Use when the user is building ... |
| [`cuopt-server-api-python`](skills/cuopt-server-api-python/SKILL.md) | HUMMBL | Apache-2.0 | cuOpt REST server — start server, endpoints, Python/curl client examples. Use when the user ... |
| [`cybersec-research-discipline`](skills/cybersec-research-discipline/SKILL.md) | HUMMBL | Apache-2.0 | 'Cybersecurity threat research self-checks: IOC defanging before output, curl --fail in moni... |
| [`daily-grade`](skills/daily-grade/SKILL.md) | HUMMBL | Apache-2.0 | Grade the operator's day on a 100-point rubric that scores meaningful state change, not acti... |
| [`daily-research`](skills/daily-research/SKILL.md) | HUMMBL | Apache-2.0 | Daily evidence collection — find, evaluate, and ingest the best research into the knowledge ... |
| [`daily-standup`](skills/daily-standup/SKILL.md) | HUMMBL | Apache-2.0 | Async daily standup from git commits, bus activity, calendar, and blockers. |
| [`dali-dynamic-mode`](skills/dali-dynamic-mode/SKILL.md) | HUMMBL | Apache-2.0 | "DALI imperative dynamic mode (`nvidia.dali.experimental.dynamic`, ndd): use when working on... |
| [`dashboard-check`](skills/dashboard-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify dashboard API + frontend health, SSE streaming, and data freshness |
| [`dashboard-qt`](skills/dashboard-qt/SKILL.md) | HUMMBL | Apache-2.0 | Summon the HUMMBL fleet Qt/QML dashboard — Quickshell panel with agent grid, bus stream, tas... |
| [`dashboard-tui`](skills/dashboard-tui/SKILL.md) | HUMMBL | Apache-2.0 | Launch the HUMMBL fleet TUI dashboard — Textual-based terminal interface showing agents, bus... |
| [`data-archive`](skills/data-archive/SKILL.md) | HUMMBL | Apache-2.0 | Archive research or operational data for reproducibility and compliance with checksums and m... |
| [`data-catalog`](skills/data-catalog/SKILL.md) | HUMMBL | Apache-2.0 | Build and query a data catalog with metadata, schema, access policies, and lineage links |
| [`data-designer`](skills/data-designer/SKILL.md) | HUMMBL | Apache-2.0 | Use when the user wants to create a dataset, generate synthetic data, or build a data genera... |
| [`data-export`](skills/data-export/SKILL.md) | HUMMBL | Apache-2.0 | Export data from SQLite/JSONL/TSV to CSV, JSON, or Markdown tables. |
| [`data-govern`](skills/data-govern/SKILL.md) | HUMMBL | Apache-2.0 | Implement data governance policies for access control, retention, classification, and compli... |
| [`data-lineage`](skills/data-lineage/SKILL.md) | HUMMBL | Apache-2.0 | Trace data lineage from source through transforms to sink for impact analysis and compliance |
| [`data-masking`](skills/data-masking/SKILL.md) | HUMMBL | Apache-2.0 | Apply data masking (tokenization, generalization, suppression, differential privacy) for saf... |
| [`data-profile`](skills/data-profile/SKILL.md) | HUMMBL | Apache-2.0 | Profile datasets for column types, nullability, cardinality, distributions, outliers, and qu... |
| [`data-quality`](skills/data-quality/SKILL.md) | HUMMBL | Apache-2.0 | Validate data completeness, consistency, freshness, and schema conformance |
| [`data-schema-infer`](skills/data-schema-infer/SKILL.md) | HUMMBL | Apache-2.0 | Infer schema from raw data files (CSV/JSON/JSONL). Detects column names, types, nullability,... |
| [`dataset-card`](skills/dataset-card/SKILL.md) | HUMMBL | Apache-2.0 | Generate a dataset card documenting provenance, composition, quality metrics, known biases, ... |
| [`dbsnp-database`](skills/dbsnp-database/SKILL.md) | HUMMBL | Apache-2.0 | Use when you want to look up, map, and search for short genetic variants (SNPs, indels) in N... |
| [`dead-code`](skills/dead-code/SKILL.md) | HUMMBL | Apache-2.0 | Find and report unused code -- functions, imports, variables, files. |
| [`deal-memo`](skills/deal-memo/SKILL.md) | HUMMBL | Apache-2.0 | Write an internal deal memo after a promising prospect or partner conversation. Captures sig... |
| [`debug-test`](skills/debug-test/SKILL.md) | HUMMBL | Apache-2.0 | Isolate and fix a failing test -- reproduce, diagnose root cause, patch, verify. |
| [`decision-fatigue`](skills/decision-fatigue/SKILL.md) | HUMMBL | Apache-2.0 | Identify and reduce decision points in workflows to combat decision fatigue |
| [`decision-log`](skills/decision-log/SKILL.md) | HUMMBL | Apache-2.0 | Record architectural or process decisions as ADRs with context and consequences. |
| [`decision-reversal-track`](skills/decision-reversal-track/SKILL.md) | HUMMBL | Apache-2.0 | Track decisions that were later reversed and why. Records the reversal context, trigger, and... |
| [`deep-research`](skills/deep-research/SKILL.md) | HUMMBL | Apache-2.0 | Fork an isolated research agent without polluting context. |
| [`deep-research-mode`](skills/deep-research-mode/SKILL.md) | HUMMBL | Apache-2.0 | Wide-aperture research with evidence quality enforcement — source tiering, claim honesty, un... |
| [`deepstream-dev`](skills/deepstream-dev/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | NVIDIA DeepStream SDK development with Python pyservicemaker API. Use when building video an... |
| [`deepstream-generate-pipeline`](skills/deepstream-generate-pipeline/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Build DeepStream GStreamer pipelines interactively. Use when the user asks about pipelines f... |
| [`deepstream-import-vision-model`](skills/deepstream-import-vision-model/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Use this skill to bring a supported object-detection vision model from HuggingFace or NVIDIA... |
| [`deepstream-profile-pipeline`](skills/deepstream-profile-pipeline/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | "Profile a DeepStream pipeline with Nsight Systems and derive its configs from the measureme... |
| [`deepstream-run-mv3dt`](skills/deepstream-run-mv3dt/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | "Run and operate the DeepStream Multi-View 3D Tracking reference app, also known as MV3DT. U... |
| [`deepstream-sop`](skills/deepstream-sop/SKILL.md) | HUMMBL | "CC-BY-4.0 AND Apache-2.0" | Use this skill when building, deploying, evaluating, debugging, or measuring latency for the... |
| [`delegate`](skills/delegate/SKILL.md) | HUMMBL | Apache-2.0 | Prepare a task for delegation to another agent (Codex, Gemini, human) with full context and ... |
| [`deliverable-check`](skills/deliverable-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify SOW deliverables are complete before invoicing — checklist against contract |
| [`delphi-study`](skills/delphi-study/SKILL.md) | HUMMBL | Apache-2.0 | Delphi method expert consensus study - iterative surveys with anonymous feedback rounds unti... |
| [`demo-record`](skills/demo-record/SKILL.md) | HUMMBL | Apache-2.0 | Record terminal demos with asciinema — scripted, reproducible, shareable |
| [`demo-script`](skills/demo-script/SKILL.md) | HUMMBL | Apache-2.0 | Scripted product demo with timing, talking points, fallback plans for failures |
| [`dep-check`](skills/dep-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify zero third-party runtime dependencies -- scan imports including conditional try/excep... |
| [`dep-update`](skills/dep-update/SKILL.md) | HUMMBL | Apache-2.0 | Check for outdated dependencies, preview breaking changes, and generate update plan or PR |
| [`dependency-graph`](skills/dependency-graph/SKILL.md) | HUMMBL | Apache-2.0 | Map module dependencies, find circular imports, calculate coupling metrics. |
| [`dependency-health`](skills/dependency-health/SKILL.md) | HUMMBL | Apache-2.0 | Monitor upstream dependency health including CVE history, maintenance activity, bus factor, ... |
| [`deploy-canary`](skills/deploy-canary/SKILL.md) | HUMMBL | Apache-2.0 | Post-deploy endpoint verification loop — polls endpoints after git push, posts BLOCKED or ST... |
| [`deploy-checklist`](skills/deploy-checklist/SKILL.md) | HUMMBL | Apache-2.0 | Environment-specific deploy verification -- tests, health, changelog, tag. |
| [`deploy-health`](skills/deploy-health/SKILL.md) | HUMMBL | Apache-2.0 | Run post-deploy smoke and health validation for a service, environment, or release. Use afte... |
| [`deprecation-track`](skills/deprecation-track/SKILL.md) | HUMMBL | Apache-2.0 | Track deprecated APIs, functions, and config with expiry dates, migration paths, and usage c... |
| [`design-qa`](skills/design-qa/SKILL.md) | HUMMBL | Apache-2.0 | Verify implemented UI against design intent, specifications, screenshots, or acceptance crit... |
| [`design-tokens`](skills/design-tokens/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL design token system — colors, typography, spacing, status colors. Generate TCSS, QML ... |
| [`deslop`](skills/deslop/SKILL.md) | HUMMBL | Apache-2.0 | Remove AI-generated code slop -- verbose comments, unnecessary abstractions, over-engineering. |
| [`dev-case-study`](skills/dev-case-study/SKILL.md) | HUMMBL | Apache-2.0 | Generate, draft, or finalize developer portfolio case studies for hummbl-io/hummbl-io. Three... |
| [`devin-cli-runtime`](skills/devin-cli-runtime/SKILL.md) | HUMMBL | Apache-2.0 | Complete Devin CLI runtime reference for agents — permission modes, agent modes, subagents, ... |
| [`dialectical-analysis`](skills/dialectical-analysis/SKILL.md) | HUMMBL | Apache-2.0 | Sequential Hegelian dialectical analysis and debate using Thesis, Antithesis, and Synthesis ... |
| [`dicom-metadata-extract`](skills/dicom-metadata-extract/SKILL.md) | HUMMBL | Apache-2.0 | Used for extracting selected metadata from one DICOM file and flagging standard-tag PHI pres... |
| [`dicom-series-preflight`](skills/dicom-series-preflight/SKILL.md) | HUMMBL | Apache-2.0 | Used for header-only preflight of one DICOM series folder before conversion or inference. No... |
| [`dicom-series-to-volume`](skills/dicom-series-to-volume/SKILL.md) | HUMMBL | Apache-2.0 | Used for converting one CT DICOM series folder to a HU NIfTI volume with affine evidence. No... |
| [`diff-explain`](skills/diff-explain/SKILL.md) | HUMMBL | Apache-2.0 | Explain any git diff in plain English for non-technical stakeholders, PR reviewers, or onboa... |
| [`diff-report`](skills/diff-report/SKILL.md) | HUMMBL | Apache-2.0 | Rich diff between two data files (CSV, JSON, JSONL) with statistical summary of changes |
| [`digital-health-clinical-asr-build`](skills/digital-health-clinical-asr-build/SKILL.md) | Ben Randoing <brandoi... | Apache-2.0 | "Stage 2 of the Clinical ASR Flywheel. Use when curating clinical terms, tagging IPA, and sy... |
| [`digital-health-clinical-asr-eval`](skills/digital-health-clinical-asr-eval/SKILL.md) | Ben Randoing <brandoi... | Apache-2.0 | "Stage 3 of Clinical ASR Flywheel. Score a NeMo manifest, produce the five-section KER leade... |
| [`digital-health-clinical-asr-finetune`](skills/digital-health-clinical-asr-finetune/SKILL.md) | Ben Randoing <brandoi... | Apache-2.0 | "Stage 4 of the Clinical ASR Flywheel. Use when priority KER is above 0.3 to run stock NeMo ... |
| [`digital-health-clinical-asr-setup`](skills/digital-health-clinical-asr-setup/SKILL.md) | Ben Randoing <brandoi... | Apache-2.0 | "Stage 1 of Clinical ASR Flywheel. Use when bootstrapping a cycle: NVCF+MW disclosure, NVIDI... |
| [`dimension-reduce`](skills/dimension-reduce/SKILL.md) | HUMMBL | Apache-2.0 | Simplify complex data by finding the few variables that matter most. Maps to DE5. |
| [`disaster-recovery`](skills/disaster-recovery/SKILL.md) | HUMMBL | Apache-2.0 | "Define RTO/RPO objectives, design failover procedures, document recovery runbooks, and run ... |
| [`discord-read`](skills/discord-read/SKILL.md) | HUMMBL | Apache-2.0 | Read Discord channel history via Bot API — stdlib only, read-only, no writes |
| [`discovery-call`](skills/discovery-call/SKILL.md) | HUMMBL | Apache-2.0 | Pre-call research on prospect with question list, note template, and follow-up draft |
| [`dispatch`](skills/dispatch/SKILL.md) | HUMMBL | Apache-2.0 | Spawn parallel subagents for decomposable work. |
| [`dns-check`](skills/dns-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify DNS records (A, AAAA, MX, SPF, DKIM, DMARC, CNAME) and propagation status |
| [`doc-coauthoring`](skills/doc-coauthoring/SKILL.md) | HUMMBL | Apache-2.0 | "Guide collaborative writing of docs, proposals, specs, RFCs, or decision docs through conte... |
| [`doc-drift`](skills/doc-drift/SKILL.md) | HUMMBL | Apache-2.0 | Detect documentation drift — cross-reference canonical docs (AGENTS.md, rules-index.md, DOTF... |
| [`doc-harden`](skills/doc-harden/SKILL.md) | HUMMBL | Apache-2.0 | Harden research markdown by extracting claims, suggesting evidence grades, and generating ve... |
| [`doc-self-check`](skills/doc-self-check/SKILL.md) | HUMMBL | Apache-2.0 | Pre-publish self-check for research docs — contradiction scan, pip-show verification, ledger... |
| [`doca-aes-gcm`](skills/doca-aes-gcm/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA AES-GCM work on a BlueField DPU or Conne... |
| [`doca-argp`](skills/doca-argp/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill for hands-on DOCA Arg Parser CLI work on a shipped sample or new DOCA-using a... |
| [`doca-argus`](skills/doca-argus/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is deploying or operating the DOCA Argus Service — the packaged... |
| [`doca-bare-metal-deployment`](skills/doca-bare-metal-deployment/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill for launching, supervising, debugging, OR platform lifecycle on a BlueField —... |
| [`doca-bench`](skills/doca-bench/SKILL.md) | HUMMBL | Apache-2.0 | Run `doca_bench` (DOCA 2.7.0 or newer) to measure throughput, bulk latency, precision latenc... |
| [`doca-bench-extension`](skills/doca-bench-extension/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the operator is authoring, building, loading, or debugging a custom doca... |
| [`doca-bf3-deployment`](skills/doca-bf3-deployment/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill for BlueField-3 (BF3) day-1 platform bring-up via the classic RShim/BFB path:... |
| [`doca-bf4-deployment`](skills/doca-bf4-deployment/SKILL.md) | HUMMBL | Apache-2.0 | WARNING: guides potentially IRREVERSIBLE BlueField-4 hardware operations (PLDM firmware burn... |
| [`doca-caps`](skills/doca-caps/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user wants to invoke the read-only doca_caps CLI to ask what DOCA se... |
| [`doca-collectx-deployment`](skills/doca-collectx-deployment/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill to deploy and operate a CollectX (clx) based DOCA telemetry collector on a ho... |
| [`doca-comch`](skills/doca-comch/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA Comch work on a host + BlueField pair — ... |
| [`doca-comm-channel-admin`](skills/doca-comm-channel-admin/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill to enumerate host↔DPU DOCA comch (formerly Comm Channel) servers and connecti... |
| [`doca-common`](skills/doca-common/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill whenever the user is doing hands-on DOCA programming on a BlueField DPU or Co... |
| [`doca-compress`](skills/doca-compress/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill for hands-on DOCA Compress programming on a BlueField DPU, ConnectX NIC, or h... |
| [`doca-container-deployment`](skills/doca-container-deployment/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is hands-on deploying an in-bundle DOCA service container (Argu... |
| [`doca-debug`](skills/doca-debug/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is debugging any DOCA symptom — a build that won't compile, a l... |
| [`doca-devemu`](skills/doca-devemu/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA Device Emulation on a BlueField DPU — ex... |
| [`doca-dma`](skills/doca-dma/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA DMA programming — bringing up a doca_dma... |
| [`doca-dms`](skills/doca-dms/SKILL.md) | HUMMBL | Apache-2.0 | Operate NVIDIA DOCA Management Service (`dmsd` + `dmspe`) on a BlueField, Arm/x86 host, or K... |
| [`doca-dpa`](skills/doca-dpa/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA DPA host-side work on a BlueField — crea... |
| [`doca-dpa-hl-tracer`](skills/doca-dpa-hl-tracer/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user runs doca_dpa_hl_tracer to capture/decode DPA-side traces at th... |
| [`doca-dpdk-bridge`](skills/doca-dpdk-bridge/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user has an existing DPDK application and is adding DOCA capabilitie... |
| [`doca-erasure-coding`](skills/doca-erasure-coding/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA Erasure Coding programming on a BlueFiel... |
| [`doca-eth`](skills/doca-eth/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill for hands-on DOCA Ethernet packet-queue work on a BlueField DPU or ConnectX N... |
| [`doca-firefly`](skills/doca-firefly/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is operating the DOCA Firefly Service container on BlueField — ... |
| [`doca-flow`](skills/doca-flow/SKILL.md) | HUMMBL | Apache-2.0 | Build and debug DOCA Flow applications on supported NVIDIA NICs/DPUs: define match/action pi... |
| [`doca-flow-dpa-perf`](skills/doca-flow-dpa-perf/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is invoking doca_flow_dpa_perf on DPA-capable hardware (Connect... |
| [`doca-flow-dpa-provider`](skills/doca-flow-dpa-provider/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA Flow DPA Provider work — exporting a `do... |
| [`doca-flow-grpc-server`](skills/doca-flow-grpc-server/SKILL.md) | HUMMBL | Apache-2.0 | PLAINTEXT-ONLY: the shipped `doca_flow_grpc` server uses `grpc::InsecureServerCredentials()`... |
| [`doca-flow-perf`](skills/doca-flow-perf/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is measuring the host or DPU-CPU control-plane rate of a DOCA F... |
| [`doca-flow-tune`](skills/doca-flow-tune/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is tuning a live or captured `doca-flow` pipeline with `doca_fl... |
| [`doca-gpi`](skills/doca-gpi/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill for hands-on DOCA GPI programming — wiring a GPU-Packet-Initiator context so ... |
| [`doca-gpunetio`](skills/doca-gpunetio/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA GPUNetIO programming — wiring a CUDA ker... |
| [`doca-gpunetio-ib-write-bw`](skills/doca-gpunetio-ib-write-bw/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is building, running, or interpreting the doca/tools/gpunetio_i... |
| [`doca-gpunetio-ib-write-lat`](skills/doca-gpunetio-ib-write-lat/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is measuring GPU-kernel-initiated RDMA WRITE latency through do... |
| [`doca-hardware-safety`](skills/doca-hardware-safety/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill whenever the agent is about to recommend or apply a change that touches DPU /... |
| [`doca-mgmt`](skills/doca-mgmt/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA Management programming against BlueField... |
| [`doca-pcc`](skills/doca-pcc/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on host-side DOCA PCC work to load a CUSTOM Prog... |
| [`doca-pcc-counters`](skills/doca-pcc-counters/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is invoking the DOCA PCC Counters tool — the `pcc_counters.sh` ... |
| [`doca-pcc-ztr-rttcc-algo`](skills/doca-pcc-ztr-rttcc-algo/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on deployment, tuning, or evaluation of the DOCA... |
| [`doca-programming-guide`](skills/doca-programming-guide/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is writing their first DOCA app or asking a library-agnostic pr... |
| [`doca-public-knowledge-map`](skills/doca-public-knowledge-map/SKILL.md) | HUMMBL | Apache-2.0 AND CC-BY-4.0 | Use this skill when the user needs to locate authoritative information about NVIDIA DOCA wit... |
| [`doca-rdma`](skills/doca-rdma/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA RDMA programming on a BlueField DPU, Con... |
| [`doca-rdmi`](skills/doca-rdmi/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA RDMI (RDMA Initiator) programming — pick... |
| [`doca-rmax`](skills/doca-rmax/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA Rivermax work on a BlueField DPU or Conn... |
| [`doca-setup`](skills/doca-setup/SKILL.md) | HUMMBL | Apache-2.0 AND CC-BY-4.0 | Use this skill when the user is dealing with the DOCA environment around their workload — ve... |
| [`doca-sha`](skills/doca-sha/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA SHA programming — offloading SHA-1, SHA-... |
| [`doca-sha-offload-engine`](skills/doca-sha-offload-engine/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when wiring the DOCA SHA Offload Engine (an OpenSSL ENGINE) into an existing ... |
| [`doca-socket-relay`](skills/doca-socket-relay/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the operator is driving the DOCA Socket Relay to bridge a socket-oriente... |
| [`doca-spcx-cc`](skills/doca-spcx-cc/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is invoking `doca_spcx_cc` (the host-side CLI under /opt/mellan... |
| [`doca-sta`](skills/doca-sta/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on NVMe-over-Fabrics storage-target work on a Bl... |
| [`doca-structured-tools-contract`](skills/doca-structured-tools-contract/SKILL.md) | HUMMBL | Apache-2.0 AND CC-BY-4.0 | Use this skill whenever another DOCA skill says "prefer the structured tool per doca-structu... |
| [`doca-telemetry`](skills/doca-telemetry/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill to read DOCA hardware-counter events from a `doca_dev` through the per-domain... |
| [`doca-telemetry-exporter`](skills/doca-telemetry-exporter/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA Telemetry Exporter programming on a host... |
| [`doca-telemetry-utils`](skills/doca-telemetry-utils/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is invoking `doca_telemetry_utils` on a host with DOCA installe... |
| [`doca-upgrade`](skills/doca-upgrade/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is contemplating a DOCA upgrade or downgrade — moving a host to... |
| [`doca-urom`](skills/doca-urom/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing hands-on DOCA UROM library work from the host side — w... |
| [`doca-urom-svc`](skills/doca-urom-svc/SKILL.md) | HUMMBL | Apache-2.0 | Operate the DOCA UROM Service container on BlueField Arm for remote memory operations (puts,... |
| [`doca-verbs`](skills/doca-verbs/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is dropping below the higher-level DOCA libraries (doca-rdma / ... |
| [`doca-version`](skills/doca-version/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when the user is doing DOCA version handling — detecting the installed releas... |
| [`docgen`](skills/docgen/SKILL.md) | HUMMBL | Apache-2.0 | Generate documents (docx, pptx, xlsx, pdf) via Python tooling. |
| [`docker-manage`](skills/docker-manage/SKILL.md) | HUMMBL | Apache-2.0 | Inspect and manage Docker resources, including a non-mutating post-update verification check... |
| [`docstring-audit`](skills/docstring-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit docstring coverage, style consistency (Google/NumPy/Sphinx), and parameter accuracy ag... |
| [`docx`](skills/docx/SKILL.md) | HUMMBL | Apache-2.0 | "Create, read, edit, format, or convert Word documents. Use for .docx files, Word reports, t... |
| [`dod`](skills/dod/SKILL.md) | HUMMBL | Apache-2.0 | Definition of Done — per-task-type checklist enforcing what "complete" means. Soft gate befo... |
| [`dream`](skills/dream/SKILL.md) | HUMMBL | Apache-2.0 | HULE capture mode — divergent synthesis, Option C Hypnagogic. Closes HRSI Gap 4. Requires AV... |
| [`drift-detect`](skills/drift-detect/SKILL.md) | HUMMBL | Apache-2.0 | Detect behavioral drift in agent outputs over time — trending analysis of bus messages, comm... |
| [`dual-agent`](skills/dual-agent/SKILL.md) | HUMMBL | Apache-2.0 | Structured two-agent workflow — Push-dominant agent (Claude) advises; Pull-dominant agent (C... |
| [`dune`](skills/dune/SKILL.md) | HUMMBL | Apache-2.0 | "Use Dune CLI/DuneSQL for on-chain analytics, decoded contract tables, saved queries, visual... |
| [`durable-objects`](skills/durable-objects/SKILL.md) | HUMMBL | Apache-2.0 | "Build or review Cloudflare Durable Objects for stateful coordination, RPC, SQLite storage, ... |
| [`dx-audit`](skills/dx-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit developer experience including build time, test time, and docs quality |
| [`dynamo-interconnect-check`](skills/dynamo-interconnect-check/SKILL.md) | HUMMBL | Apache-2.0 | Validate that a Dynamo deployment's NIXL/UCX/NCCL interconnect is ready for disaggregated se... |
| [`dynamo-recipe-runner`](skills/dynamo-recipe-runner/SKILL.md) | HUMMBL | Apache-2.0 | Select, validate, patch, and deploy existing NVIDIA Dynamo Kubernetes recipes. Use for model... |
| [`dynamo-router-starter`](skills/dynamo-router-starter/SKILL.md) | HUMMBL | Apache-2.0 | Start or patch Dynamo router modes and run router endpoint smoke checks. Use for round-robin... |
| [`dynamo-troubleshoot`](skills/dynamo-troubleshoot/SKILL.md) | HUMMBL | Apache-2.0 | Diagnose failed or unhealthy Dynamo deployments. Use when pods, model-cache jobs, PVCs, work... |
| [`earth2studio-create-datasource`](skills/earth2studio-create-datasource/SKILL.md) | HUMMBL | Apache-2.0 | Create and validate Earth2Studio data source wrappers (DataSource, ForecastSource, DataFrame... |
| [`earth2studio-create-diagnostic`](skills/earth2studio-create-diagnostic/SKILL.md) | HUMMBL | Apache-2.0 | Create Earth2Studio diagnostic model wrappers for single-step data transformations, includin... |
| [`earth2studio-create-prognostic`](skills/earth2studio-create-prognostic/SKILL.md) | HUMMBL | Apache-2.0 | Create Earth2Studio prognostic (time-stepping forecast) model wrappers. Do NOT use for diagn... |
| [`earth2studio-data-fetch`](skills/earth2studio-data-fetch/SKILL.md) | HUMMBL | Apache-2.0 | Fetch weather/climate data via Earth2Studio data sources for specific variables and times. D... |
| [`earth2studio-deterministic-forecast`](skills/earth2studio-deterministic-forecast/SKILL.md) | HUMMBL | Apache-2.0 | Build deterministic forecast scripts with Earth2Studio (model, data source, IO, inference). ... |
| [`earth2studio-discover`](skills/earth2studio-discover/SKILL.md) | HUMMBL | Apache-2.0 | Find Earth2Studio models, data sources, and examples for a weather/climate use case. Do NOT ... |
| [`earth2studio-install`](skills/earth2studio-install/SKILL.md) | HUMMBL | Apache-2.0 | Guide installing Earth2Studio via uv or pip, selecting model extras, and configuring the env... |
| [`economics-mode`](skills/economics-mode/SKILL.md) | HUMMBL | Apache-2.0 | Governed financial decision support — every allocation has thesis, downside, and exit. |
| [`edc-review`](skills/edc-review/SKILL.md) | HUMMBL | Apache-2.0 | Derive an agent's Everyday Carry (EDC) skill set from usage telemetry, score concentration, ... |
| [`email-sequence`](skills/email-sequence/SKILL.md) | HUMMBL | Apache-2.0 | Draft a 3-5 email nurture or outreach sequence. Goal-driven, audience-specific, with subject... |
| [`embedding-index`](skills/embedding-index/SKILL.md) | HUMMBL | Apache-2.0 | Build and manage vector embedding indices — HNSW, IVF, or flat indices with metadata filtering |
| [`embl-ebi-ols`](skills/embl-ebi-ols/SKILL.md) | HUMMBL | Apache-2.0 | Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, d... |
| [`empathy-map`](skills/empathy-map/SKILL.md) | HUMMBL | Apache-2.0 | Map the emotional, cognitive, and experiential landscape of the humans the agent serves — wh... |
| [`encode-ccres-database`](skills/encode-ccres-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API, or ... |
| [`end-session`](skills/end-session/SKILL.md) | HUMMBL | Apache-2.0 | Disciplined session closeout. Run before signing off. |
| [`energy-map`](skills/energy-map/SKILL.md) | HUMMBL | Apache-2.0 | Track energy levels across the day to optimize task scheduling and identify peak hours |
| [`engagement-tracker`](skills/engagement-tracker/SKILL.md) | HUMMBL | Apache-2.0 | Track active client engagements with milestones, health status, risk indicators, and renewal... |
| [`ensembl-database`](skills/ensembl-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or pr... |
| [`entropy-catalog`](skills/entropy-catalog/SKILL.md) | HUMMBL | Apache-2.0 | Look up public true-RNG, beacon, and clone sites from the HUMMBL entropy catalog. Refuse sec... |
| [`env-doc`](skills/env-doc/SKILL.md) | HUMMBL | Apache-2.0 | Document all environment variables in a project with purpose, type, default, sensitivity, an... |
| [`env-parity`](skills/env-parity/SKILL.md) | HUMMBL | Apache-2.0 | Compare environment configs across dev/staging/prod for drift, missing vars, and type mismat... |
| [`env-setup`](skills/env-setup/SKILL.md) | HUMMBL | Apache-2.0 | One-command dev environment bootstrap — venv, deps, hooks, config, verification |
| [`epistemic-crucible-mode`](skills/epistemic-crucible-mode/SKILL.md) | HUMMBL | Apache-2.0 | A composable, multi-agent sandbox for rigorous, non-destructive trial and error utilizing LL... |
| [`epistemic-stance`](skills/epistemic-stance/SKILL.md) | HUMMBL | Apache-2.0 | Pre-delegation epistemic triage — names the truth-related intent before tool selection. Sits... |
| [`error-catalog`](skills/error-catalog/SKILL.md) | HUMMBL | Apache-2.0 | Catalog all exception types, error codes, and handling patterns in the codebase |
| [`error-message`](skills/error-message/SKILL.md) | HUMMBL | Apache-2.0 | Audit and improve error messages for clarity and actionability |
| [`escalation-policy`](skills/escalation-policy/SKILL.md) | HUMMBL | Apache-2.0 | Define and manage escalation chains for alerts and incidents |
| [`ethnography-plan`](skills/ethnography-plan/SKILL.md) | HUMMBL | Apache-2.0 | Plan ethnographic research - field site selection, access negotiation, observation protocols... |
| [`etl-design`](skills/etl-design/SKILL.md) | HUMMBL | Apache-2.0 | Design data pipelines with extraction, validation, transformation, loading, error handling, ... |
| [`eval-forge`](skills/eval-forge/SKILL.md) | HUMMBL | Apache-2.0 | Forge self-validating eval suites for side-effecting agent skills. Three modes: forge (build... |
| [`eval-suite`](skills/eval-suite/SKILL.md) | HUMMBL | Apache-2.0 | Design and run LLM evaluation suites -- accuracy, latency, cost, format compliance across te... |
| [`evening-touchdown`](skills/evening-touchdown/SKILL.md) | HUMMBL | Apache-2.0 | Evening landing sequence -- time-aware twin of morning-kickoff. Day log (UTC-correct for ET)... |
| [`evidence-grade`](skills/evidence-grade/SKILL.md) | HUMMBL | Apache-2.0 | Grade evidence quality — source credibility, recency, methodology, reproducibility, relevance |
| [`evidence-pack`](skills/evidence-pack/SKILL.md) | HUMMBL | Apache-2.0 | Bundle bus logs, guardrails, ADRs, and governance artifacts into a shareable evidence pack f... |
| [`evidence-review`](skills/evidence-review/SKILL.md) | HUMMBL | Apache-2.0 | Structured review of an evidence corpus for completeness, provenance, gaps, and fleet-readin... |
| [`evidence-triangulate`](skills/evidence-triangulate/SKILL.md) | HUMMBL | Apache-2.0 | Triangulate a claim from 3+ independent sources. Cross-references evidence to establish conf... |
| [`exception-flow`](skills/exception-flow/SKILL.md) | HUMMBL | Apache-2.0 | Map exception flow through code — trace raise/catch/propagate paths, identify swallowed erro... |
| [`exec-summary`](skills/exec-summary/SKILL.md) | HUMMBL | Apache-2.0 | Produce 1-page executive summary from any long-form document or analysis. |
| [`expense-log`](skills/expense-log/SKILL.md) | HUMMBL | Apache-2.0 | Track business expenses for tax and runway analysis |
| [`experiment-track`](skills/experiment-track/SKILL.md) | HUMMBL | Apache-2.0 | Track ML experiments and hyperparameters with versioning and comparison. [Maps to CO7.] |
| [`explore-mode`](skills/explore-mode/SKILL.md) | HUMMBL | Apache-2.0 | Canary-first swarm exploration for Phase -1 Discovery. 1 canary maps territory, then N swarm... |
| [`factory-batch-run`](skills/factory-batch-run/SKILL.md) | HUMMBL | Apache-2.0 | Run Phase 0 HUAOMP/MTSMU scoring on a batch of candidates in parallel. Wrapper around the sc... |
| [`factory-telemetry-populate`](skills/factory-telemetry-populate/SKILL.md) | HUMMBL | Apache-2.0 | Populate skill_invocations telemetry across fleet runtimes so lean-set-review has evidence f... |
| [`fastapi`](skills/fastapi/SKILL.md) | HUMMBL | Apache-2.0 | FastAPI best practices and conventions. Use when working with FastAPI APIs, Pydantic models,... |
| [`fastapi-templates`](skills/fastapi-templates/SKILL.md) | HUMMBL | Apache-2.0 | Create production-ready FastAPI projects with async patterns, dependency injection, and comp... |
| [`feature-flag`](skills/feature-flag/SKILL.md) | HUMMBL | Apache-2.0 | Manage feature flags -- list, toggle, audit stale flags, clean up shipped features |
| [`feature-store`](skills/feature-store/SKILL.md) | HUMMBL | Apache-2.0 | Manage ML feature stores and data pipelines for consistent training and serving. [Maps to CO... |
| [`field-research`](skills/field-research/SKILL.md) | HUMMBL | Apache-2.0 | Field research methodology - site selection, data collection (observation/interviews/artifac... |
| [`file-transfer`](skills/file-transfer/SKILL.md) | HUMMBL | Apache-2.0 | Transfer files between local machine and a remote host via SCP/rsync. |
| [`finance-legal-aggregator-research`](skills/finance-legal-aggregator-research/SKILL.md) | HUMMBL | Apache-2.0 | Domain research skill for Finance & Legal aggregator discovery. Catalogs canonical aggregato... |
| [`financial-model`](skills/financial-model/SKILL.md) | HUMMBL | Apache-2.0 | Build a 3-statement financial model (P&L, cash flow, balance sheet) with assumptions labeled... |
| [`find-skills`](skills/find-skills/SKILL.md) | HUMMBL | Apache-2.0 | "Discover and install agent skills when the user asks how to do something, wants a skill for... |
| [`find-work`](skills/find-work/SKILL.md) | HUMMBL | Apache-2.0 | Discover what needs doing -- scan bus, git, tests, health, tech debt, and open items to surf... |
| [`fine-tune-prep`](skills/fine-tune-prep/SKILL.md) | HUMMBL | Apache-2.0 | Prepare training data for LLM fine-tuning -- format validation, dedup, cost estimation, qual... |
| [`first-principles`](skills/first-principles/SKILL.md) | HUMMBL | Apache-2.0 | Propose first principles from primitives, invariants, purpose, constraints, and authority. P... |
| [`fitness`](skills/fitness/SKILL.md) | HUMMBL | Apache-2.0 | Administer and score the HUMMBL Fitness Profile, the compatibility-preserving name for the e... |
| [`fitness-assessment`](skills/fitness-assessment/SKILL.md) | HUMMBL | Apache-2.0 | Administer and score the HUMMBL Fitness Assessment — an 18-question diagnostic instrument th... |
| [`flake-hunter`](skills/flake-hunter/SKILL.md) | HUMMBL | Apache-2.0 | Identify flaky tests by pattern -- re-run suspicious tests, categorize causes, suggest fixes |
| [`flashcard`](skills/flashcard/SKILL.md) | HUMMBL | Apache-2.0 | Generate Q&A flashcards from docs, notes, or topic for study and review |
| [`fleet-coverage-map`](skills/fleet-coverage-map/SKILL.md) | HUMMBL | Apache-2.0 | Map task categories to skills and find capability gaps — tasks that no skill covers. Surface... |
| [`fleet-curator`](skills/fleet-curator/SKILL.md) | HUMMBL | Apache-2.0 | Reconcile skills, rules, roster, and memory sources into an evidence-backed fleet knowledge ... |
| [`fleet-health-check`](skills/fleet-health-check/SKILL.md) | HUMMBL | Apache-2.0 | Composite fleet health check that runs all 4 validation skills — fleet-skill-smoke (schema),... |
| [`fleet-llm`](skills/fleet-llm/SKILL.md) | HUMMBL | Apache-2.0 | Multi-provider LLM gateway — Aperture (unfunded 2026-09-27), Cloudflare Workers AI, Groq, Nv... |
| [`fleet-skill-baseline-manager`](skills/fleet-skill-baseline-manager/SKILL.md) | HUMMBL | Apache-2.0 | Manage all-skills baseline snapshots with deterministic diff summaries and controlled updates. |
| [`fleet-skill-headline-audit`](skills/fleet-skill-headline-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit SKILL.md readability signals and detect heading drift for fleet-wide quality. |
| [`fleet-skill-health`](skills/fleet-skill-health/SKILL.md) | HUMMBL | Apache-2.0 | Validate fleet SKILL.md inventory structure through frontmatter smoke checks, declared-root ... |
| [`fleet-skill-health-pulse`](skills/fleet-skill-health-pulse/SKILL.md) | HUMMBL | Apache-2.0 | Emit a compact fleet-health signal combining smoke, drift, and bus-lane activity. |
| [`fleet-skill-intel-surge-router`](skills/fleet-skill-intel-surge-router/SKILL.md) | HUMMBL | Apache-2.0 | Convert all-skills findings into low-friction routing actions for Intel-Surge/triage. |
| [`fleet-skill-placeholder-cleanup`](skills/fleet-skill-placeholder-cleanup/SKILL.md) | HUMMBL | Apache-2.0 | Classify unresolved placeholders across SKILL.md files and emit severity-ranked remediation ... |
| [`fleet-skill-rootset-scan`](skills/fleet-skill-rootset-scan/SKILL.md) | HUMMBL | Apache-2.0 | Build a canonical root coverage matrix and report missing or duplicate fleet skill scopes. |
| [`fleet-skill-smoke`](skills/fleet-skill-smoke/SKILL.md) | HUMMBL | Apache-2.0 | Fast smoke validation for all SKILL.md files across known skill roots, with explicit hard-fa... |
| [`fleet-skill-test-router`](skills/fleet-skill-test-router/SKILL.md) | HUMMBL | Apache-2.0 | Convert all-skills test findings into low-friction routing actions for fleet skill triage an... |
| [`fleet-status`](skills/fleet-status/SKILL.md) | HUMMBL | Apache-2.0 | Unified view of all machines (MBP, Windows desktop, $REMOTE_HOST) -- health, sync state, too... |
| [`fleet-tools`](skills/fleet-tools/SKILL.md) | HUMMBL | Apache-2.0 | Query the HUMMBL fleet tool catalog — discover which Python packages, dashboards, and Omarch... |
| [`focus-block`](skills/focus-block/SKILL.md) | HUMMBL | Apache-2.0 | Start a timed deep work block with goal, distraction logging, and end-of-block review |
| [`foldseek-structural-search`](skills/foldseek-structural-search/SKILL.md) | HUMMBL | Apache-2.0 | Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH,... |
| [`follow-up`](skills/follow-up/SKILL.md) | HUMMBL | Apache-2.0 | Check CRM for stale leads and consulting contacts needing follow-up, draft emails |
| [`font-craft`](skills/font-craft/SKILL.md) | HUMMBL | Apache-2.0 | Design, engineer, and compile bespoke vector typefaces and typography assets programmaticall... |
| [`forensic-index`](skills/forensic-index/SKILL.md) | HUMMBL | Apache-2.0 | Build and query a local SQLite index over captured session-forensic JSON artifacts (session_... |
| [`forensic-recommendations`](skills/forensic-recommendations/SKILL.md) | HUMMBL | Apache-2.0 | Act on recommendations from session forensic reports and cross-session analysis. Implements ... |
| [`forensic-telemetry-sidecar`](skills/forensic-telemetry-sidecar/SKILL.md) | HUMMBL | Apache-2.0 | Emits and validates the machine-readable forensic telemetry sidecar (forensic_telemetry.json... |
| [`foundationpose-pipeline`](skills/foundationpose-pipeline/SKILL.md) | HUMMBL | Apache-2.0 | Adapt BOP datasets, run the FoundationPose perception pipeline with TAO depth, and evaluate ... |
| [`foundationpose-setup`](skills/foundationpose-setup/SKILL.md) | HUMMBL | Apache-2.0 | Install or repair the FoundationPose perception pipeline and build its FoundationStereo Tens... |
| [`founder-check`](skills/founder-check/SKILL.md) | HUMMBL | Apache-2.0 | 'Am I doing founder work? 5-question diagnostic. Revenue-moving, building vs maintaining, cu... |
| [`frame-audit`](skills/frame-audit/SKILL.md) | HUMMBL | Apache-2.0 | "Audit metaphor or framing choices before pitches, positioning, architecture narratives, cat... |
| [`framework-compare`](skills/framework-compare/SKILL.md) | HUMMBL | Apache-2.0 | Compare two governance frameworks side-by-side with control overlap analysis |
| [`free-apis`](skills/free-apis/SKILL.md) | HUMMBL | Apache-2.0 | Free API wrappers for OpenAlex, NVD, OSV, PubMed, and other no-cost data sources. Use when y... |
| [`freemodel-generate`](skills/freemodel-generate/SKILL.md) | HUMMBL | Apache-2.0 | Zero-cost text, vision, and image generation via free endpoints on NVIDIA NIM, OpenRouter, a... |
| [`freemodel-marketplace-cards`](skills/freemodel-marketplace-cards/SKILL.md) | HUMMBL | Apache-2.0 | Marketplace-ready product visuals (main image, secondaries, A+ modules) via free endpoints w... |
| [`freemodel-product-photoshoot`](skills/freemodel-product-photoshoot/SKILL.md) | HUMMBL | Apache-2.0 | Brand-quality product imagery via free endpoints (HF FLUX.1-schnell primary) with locally-as... |
| [`frontend`](skills/frontend/SKILL.md) | HUMMBL | Apache-2.0 | Design and build frontend UI -- HTML/CSS/JS, React, responsive. |
| [`frontend-design`](skills/frontend-design/SKILL.md) | HUMMBL | Apache-2.0 | "Create distinctive, production-grade web UI: components, pages, dashboards, landing pages, ... |
| [`full-audit`](skills/full-audit/SKILL.md) | HUMMBL | Apache-2.0 | Comprehensive codebase audit -- chains dep-check, dead-code, try-except-audit, absence-audit... |
| [`fullstack-development`](skills/fullstack-development/SKILL.md) | HUMMBL | Apache-2.0 | Design, implement, and verify a production-oriented full-stack web application from requirem... |
| [`gameboard-ops`](skills/gameboard-ops/SKILL.md) | HUMMBL | Apache-2.0 | "ARCHIVED 2026-08-27: Use ops-gameboard instead. This is a redirect stub; the canonical cont... |
| [`gap-analysis`](skills/gap-analysis/SKILL.md) | HUMMBL | Apache-2.0 | Compare current controls against target framework requirements, quantify gaps, prioritize re... |
| [`garage`](skills/garage/SKILL.md) | HUMMBL | Apache-2.0 | Generate agent performance visuals — watch faces, API gauges, failure states, livery presets... |
| [`gdpr-check`](skills/gdpr-check/SKILL.md) | HUMMBL | Apache-2.0 | GDPR compliance audit -- data inventory, consent mechanisms, retention policies, right to er... |
| [`gemini-audit`](skills/gemini-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit Gemini-authored artifacts using adopt/adapt/avoid triage. Produces a structured verdic... |
| [`gen-image`](skills/gen-image/SKILL.md) | HUMMBL | Apache-2.0 | Vendor-neutral image and text generation over free OpenAI-compatible endpoints (NVIDIA, Open... |
| [`gen-marketplace-cards`](skills/gen-marketplace-cards/SKILL.md) | HUMMBL | Apache-2.0 | Marketplace-ready product listing visuals (main image, secondaries, A+ modules) on free vend... |
| [`gen-photoshoot`](skills/gen-photoshoot/SKILL.md) | HUMMBL | Apache-2.0 | Brand-quality product photoshoots on free vendor-neutral endpoints. Local mode-specific prom... |
| [`general-manager`](skills/general-manager/SKILL.md) | HUMMBL | Apache-2.0 | Reconcile scoped work, owners, dependencies, and ledger evidence into a coordination brief. ... |
| [`git-archaeology`](skills/git-archaeology/SKILL.md) | HUMMBL | Apache-2.0 | Deep history exploration -- find when and why something changed, trace the evolution of code. |
| [`git-bisect`](skills/git-bisect/SKILL.md) | HUMMBL | Apache-2.0 | Binary search for the commit that introduced a bug using automated test verification. |
| [`git-blame-analysis`](skills/git-blame-analysis/SKILL.md) | HUMMBL | Apache-2.0 | Analyze code ownership, churn rate, and hotspots by file and function using git blame and log. |
| [`git-forensics`](skills/git-forensics/SKILL.md) | HUMMBL | Apache-2.0 | Forensically analyze git repositories across the fleet — reconstruct commit timelines, trace... |
| [`git-identity-check`](skills/git-identity-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify git author identity matches the agent guardrails per repo. Checks that commits are at... |
| [`github-repository-architect`](skills/github-repository-architect/SKILL.md) | HUMMBL | Apache-2.0 | Complete GitHub repository setup with production-grade standards including community health ... |
| [`github-tricks`](skills/github-tricks/SKILL.md) | HUMMBL | Apache-2.0 | GitHub URL tricks of the trade -- domain swaps (gitingest, gitdiagram, deepwiki, gitmcp), na... |
| [`gm`](skills/gm/SKILL.md) | HUMMBL | Apache-2.0 | Canonical good-morning and day-start launcher with a technical pulse, business pipeline, cal... |
| [`gn`](skills/gn/SKILL.md) | HUMMBL | Apache-2.0 | Goodnight ritual for the founder. Personal accountability close — intent audit, one honest s... |
| [`gnomad-database`](skills/gnomad-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the Genome Aggregation Database (gnomAD). Use when determining the rarity or allele fr... |
| [`goal-cycle`](skills/goal-cycle/SKILL.md) | HUMMBL | Apache-2.0 | Persistent goal-loop harness for selecting, completing, and immediately reselecting agent go... |
| [`goal-selection`](skills/goal-selection/SKILL.md) | HUMMBL | Apache-2.0 | "Use this whenever the user says to pick/choose/select your own goal, find productive work, ... |
| [`goldplate-bespoke`](skills/goldplate-bespoke/SKILL.md) | HUMMBL | MIT | Combined token-expander + code-maximizer. Mouth full (academic prose) AND code full (enterpr... |
| [`goldplate-ponytail`](skills/goldplate-ponytail/SKILL.md) | HUMMBL | MIT | Combined token-expander + code-minimizer. Mouth full (academic prose) AND code small (lazy s... |
| [`govern`](skills/govern/SKILL.md) | HUMMBL | Apache-2.0 | Governance surge mode — assess, map to frameworks, generate evidence artifacts, report. For ... |
| [`governance-audit`](skills/governance-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit governance bus integrity -- format, fields, timeline, retention. |
| [`governance-maturity`](skills/governance-maturity/SKILL.md) | HUMMBL | Apache-2.0 | Score an organization's AI governance maturity on a 5-level scale with actionable roadmap. |
| [`governance-report`](skills/governance-report/SKILL.md) | HUMMBL | Apache-2.0 | Generate periodic governance health report for client leadership or board -- status, metrics... |
| [`governance-scorecard`](skills/governance-scorecard/SKILL.md) | HUMMBL | Apache-2.0 | Traffic-light scorecard of governance posture across all domains and frameworks |
| [`governed-compression`](skills/governed-compression/SKILL.md) | HUMMBL | Apache-2.0 | Governed compression experiments — quantization and approximation primitives with governance... |
| [`graph-build`](skills/graph-build/SKILL.md) | HUMMBL | Apache-2.0 | Build or refresh Graphify knowledge-graph artifacts for HUMMBL corpora (projects, bki, arcan... |
| [`graphify`](skills/graphify/SKILL.md) | HUMMBL | Apache-2.0 | any input (code, docs, papers, images) → knowledge graph → clustered communities → HTML + JS... |
| [`grayteam`](skills/grayteam/SKILL.md) | HUMMBL | Apache-2.0 | SOC operations -- 24/7 monitoring, alert triage, SOC shift work. Blue team operational front... |
| [`greenteam`](skills/greenteam/SKILL.md) | HUMMBL | Apache-2.0 | Secure development and DevSecOps -- interaction between defenders and builders. Blue teaches... |
| [`grokk`](skills/grokk/SKILL.md) | HUMMBL | MIT | Caveman character: GROKK, the chieftain. Gruff, decisive, speaks in commands. Few words. The... |
| [`grounded-theory`](skills/grounded-theory/SKILL.md) | HUMMBL | Apache-2.0 | Grounded theory qualitative research methodology - iterative coding, categorization, and the... |
| [`growth-model`](skills/growth-model/SKILL.md) | HUMMBL | Apache-2.0 | Analyze network effects, growth loops, and go-to-market dynamics. Maps to CO7. |
| [`gsp`](skills/gsp/SKILL.md) | HUMMBL | Apache-2.0 | Administer and score the HUMMBL Governance Sense-Making Profile (GSP), the compatibility-pre... |
| [`gtex-database`](skills/gtex-database/SKILL.md) | HUMMBL | Apache-2.0 | Use when you want to retrieve quantitative RNA expression data and variant eQTL information ... |
| [`guardrail-design`](skills/guardrail-design/SKILL.md) | HUMMBL | Apache-2.0 | Design input/output guardrails for LLM applications -- content filters, format validators, s... |
| [`habit-track`](skills/habit-track/SKILL.md) | HUMMBL | Apache-2.0 | Track daily habits and routines with streak counting, trends, and consistency scores |
| [`hallucination-check`](skills/hallucination-check/SKILL.md) | HUMMBL | Apache-2.0 | Cross-reference LLM output against source documents for factual accuracy and grounding. |
| [`handoff`](skills/handoff/SKILL.md) | HUMMBL | Apache-2.0 | Generate a structured handoff for agent or session transitions. |
| [`harness-watch`](skills/harness-watch/SKILL.md) | HUMMBL | Apache-2.0 | Track releases and breaking changes across agentic harnesses and runtimes — claude-code, cod... |
| [`headroom`](skills/headroom/SKILL.md) | HUMMBL | Apache-2.0 | Proxy-level context compression for AI agents. Compresses tool outputs, logs, RAG chunks, fi... |
| [`health`](skills/health/SKILL.md) | HUMMBL | Apache-2.0 | Run the HUMMBL governance kernel health CLI and report its observed state. |
| [`healthcare-ai-watch`](skills/healthcare-ai-watch/SKILL.md) | HUMMBL | Apache-2.0 | Track Healthcare AI regulation — ONC HTI-1, FDA PCCP, HIPAA, EU AI Act medical-device clause... |
| [`heraldry`](skills/heraldry/SKILL.md) | HUMMBL | Apache-2.0 | Generate heraldic arms for HUMMBL agents — SVG shields, Unicode renderings, blazon text from... |
| [`hf-watch`](skills/hf-watch/SKILL.md) | HUMMBL | Apache-2.0 | Track Hugging Face ecosystem -- new models, trending repos, leaderboard shifts, dataset rele... |
| [`higgsfield-brandkit`](skills/higgsfield-brandkit/SKILL.md) | HUMMBL | Apache-2.0 | Create and extend complete visual brand systems through the Higgsfield CLI and bundled deter... |
| [`higgsfield-generate`](skills/higgsfield-generate/SKILL.md) | HUMMBL | Apache-2.0 | Generate images/videos/3D assets/audio via Higgsfield AI. Defaults: GPT Image 2 for image/de... |
| [`higgsfield-marketplace-cards`](skills/higgsfield-marketplace-cards/SKILL.md) | HUMMBL | Apache-2.0 | Generate marketplace product image cards through Higgsfield: compliant main image, secondary... |
| [`higgsfield-product-photoshoot`](skills/higgsfield-product-photoshoot/SKILL.md) | HUMMBL | Apache-2.0 | Generate brand-quality product images through Higgsfield product-photoshoot prompt enhanceme... |
| [`higgsfield-soul-id`](skills/higgsfield-soul-id/SKILL.md) | HUMMBL | Apache-2.0 | Train a Soul Character — a personalized model on a person's face that Higgsfield uses for id... |
| [`higgsfield-video-explainer`](skills/higgsfield-video-explainer/SKILL.md) | HUMMBL | Apache-2.0 | Build a complete non-photoreal narrated explainer or story video from ordered 10-second bloc... |
| [`higgsfield-websites`](skills/higgsfield-websites/SKILL.md) | HUMMBL | Apache-2.0 | Build, edit, and deploy full-stack websites, apps and games via the Higgsfield CLI (`higgsfi... |
| [`higgsfield-youtube-thumbnail`](skills/higgsfield-youtube-thumbnail/SKILL.md) | HUMMBL | Apache-2.0 | Create high-click-through YouTube thumbnails and vertical video covers through the Higgsfiel... |
| [`hipaa-map`](skills/hipaa-map/SKILL.md) | HUMMBL | Apache-2.0 | HIPAA control mapping for healthcare workloads. Maps system controls to HIPAA Security Rule ... |
| [`holohub-app-lifecycle`](skills/holohub-app-lifecycle/SKILL.md) | HUMMBL | Apache-2.0 | "Use for non-failing HoloHub app work with ./holohub: scaffold, build, run, test, visual evi... |
| [`holohub-debug-build-run`](skills/holohub-debug-build-run/SKILL.md) | HUMMBL | Apache-2.0 | "Use when a concrete ./holohub command fails, hangs, regresses, or returns wrong output and ... |
| [`holohub-module-lifecycle`](skills/holohub-module-lifecycle/SKILL.md) | HUMMBL | Apache-2.0 | "Use for reusable Holoscan Module work with ./holohub: scaffold, tests, editable install, DE... |
| [`holoscan-install-conda`](skills/holoscan-install-conda/SKILL.md) | HUMMBL | Apache-2.0 | "Install Holoscan SDK v4.3+ via Conda in a CUDA 13 environment. Use for Conda installs; redi... |
| [`holoscan-install-container`](skills/holoscan-install-container/SKILL.md) | HUMMBL | Apache-2.0 | "Install Holoscan SDK via the NGC Docker container. Use for container-based installs; not fo... |
| [`holoscan-install-debian`](skills/holoscan-install-debian/SKILL.md) | HUMMBL | Apache-2.0 | "Install Holoscan SDK natively on Ubuntu via apt. Use for C++ installs on Ubuntu; pair with ... |
| [`holoscan-install-source`](skills/holoscan-install-source/SKILL.md) | HUMMBL | Apache-2.0 | "Build Holoscan SDK from source via the in-tree ./run script. Use only when published packag... |
| [`holoscan-install-wheel`](skills/holoscan-install-wheel/SKILL.md) | HUMMBL | Apache-2.0 | "Install Holoscan SDK Python wheel via pip into a venv. Use for Python installs; not for nat... |
| [`holoscan-setup`](skills/holoscan-setup/SKILL.md) | HUMMBL | Apache-2.0 | "Guides Holoscan SDK installation: inspects the host, assesses platform compatibility, recom... |
| [`hsb-app`](skills/hsb-app/SKILL.md) | Holoscan Team <holosc... | "Apache-2.0" | Discover and run Holoscan Sensor Bridge example applications on a connected devkit. Filters ... |
| [`hsb-flash`](skills/hsb-flash/SKILL.md) | Holoscan Team <holosc... | "Apache-2.0" | Flash the FPGA on an HSB board connected to an NVIDIA devkit. Supports HSB Lattice boards (F... |
| [`hsb-ip-create-top`](skills/hsb-ip-create-top/SKILL.md) | Holoscan Team <holosc... | Apache-2.0 | Create or explain fixed-format HSB FPGA_top.sv wrappers from validated HOLOLINK_def.svh file... |
| [`hsb-ip-def`](skills/hsb-ip-def/SKILL.md) | Holoscan Team <holosc... | Apache-2.0 | Generate, validate, compare, or explain HSB HOLOLINK_def.svh macros. Do not use for FPGA_top... |
| [`hsb-ip-packetizer`](skills/hsb-ip-packetizer/SKILL.md) | Holoscan Team <holosc... | Apache-2.0 | Choose or explain HSB Sensor RX packetizer fields for HOLOLINK_def.svh. Do not use for full ... |
| [`hsb-setup`](skills/hsb-setup/SKILL.md) | Holoscan Team <holosc... | "Apache-2.0" | Clone the latest NVIDIA Holoscan Sensor Bridge repo, ask which supported devkit is being use... |
| [`hsb-test`](skills/hsb-test/SKILL.md) | Holoscan Team <holosc... | "Apache-2.0" | Execute QA test plans on Holoscan Sensor Bridge hardware. Reads a user-provided test documen... |
| [`huaomp`](skills/huaomp/SKILL.md) | HUMMBL | Apache-2.0 | Maximum epistemic breadth -- 6 analytical lenses (Holistic, Universal, Absolute, Omni, Meta,... |
| [`human-protein-atlas-database`](skills/human-protein-atlas-database/SKILL.md) | HUMMBL | Apache-2.0 | Use when you want to retrieve semi-quantitative protein expression and spatial localisation ... |
| [`hummbl`](skills/hummbl/SKILL.md) | HUMMBL | Apache-2.0 | Structured reasoning framework for AI agents — turns plans, hypotheses, observations, evalua... |
| [`hummbl-axis`](skills/hummbl-axis/SKILL.md) | HUMMBL | Apache-2.0 | Ladder that selects which Atlas contradiction to act on |
| [`hummbl-bif`](skills/hummbl-bif/SKILL.md) | HUMMBL | Apache-2.0 | Batch Ingestion Framework - systematic methodology for technical knowledge acquisition using... |
| [`hummbl-bus`](skills/hummbl-bus/SKILL.md) | HUMMBL | Apache-2.0 | Secure append-only TSV coordination bus for multi-agent systems |
| [`hummbl-business-review`](skills/hummbl-business-review/SKILL.md) | HUMMBL | Apache-2.0 | "Create evidence-backed internal business reviews of HUMMBL across strategy, offers, funnels... |
| [`hummbl-cognition`](skills/hummbl-cognition/SKILL.md) | HUMMBL | Apache-2.0 | Cognitive Ledger Protocol (CLP) and Open Brain server for HUMMBL agent reasoning |
| [`hummbl-compass`](skills/hummbl-compass/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL Directional Navigation & Multi-Agent Routing Algorithms |
| [`hummbl-contracts`](skills/hummbl-contracts/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL contract schemas and stdlib-only JSON Schema validator |
| [`hummbl-edge-mesh`](skills/hummbl-edge-mesh/SKILL.md) | HUMMBL | Apache-2.0 | Provision, operate, monitor, recover, and deploy HUMMBL edge nodes across meshtastic + Raspb... |
| [`hummbl-framework`](skills/hummbl-framework/SKILL.md) | HUMMBL | Apache-2.0 | Complete HUMMBL Base120 mental models framework with all 120 models across 6 transformations... |
| [`hummbl-free-models`](skills/hummbl-free-models/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL Open-Weights & Free-Tier Model Registry Generator |
| [`hummbl-governance`](skills/hummbl-governance/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL governance primitives — kill switch, circuit breaker, cost governor, delegation token... |
| [`hummbl-intel`](skills/hummbl-intel/SKILL.md) | HUMMBL | Apache-2.0 | INT taxonomy framework for agent intelligence collection |
| [`hummbl-kernel`](skills/hummbl-kernel/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL orchestration kernel — lightweight workflow execution with security, compliance, and ... |
| [`hummbl-lattice`](skills/hummbl-lattice/SKILL.md) | HUMMBL | Apache-2.0 | Domain-specific reasoning operator lattices for the Domain120 framework |
| [`hummbl-lint-config`](skills/hummbl-lint-config/SKILL.md) | HUMMBL | Apache-2.0 | Shared ruff lint configuration for the HUMMBL fleet |
| [`hummbl-research-institute-foundations`](skills/hummbl-research-institute-foundations/SKILL.md) | HUMMBL | Apache-2.0 | Session-start context grounding for HUMMBL, LLC. Scans all hummbl-io repos, research coverag... |
| [`hummbl-rubric-templates`](skills/hummbl-rubric-templates/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL Standard Evaluation Rubric Templates & Automated Validators |
| [`hummbl-taxonomy`](skills/hummbl-taxonomy/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL Governed Intelligence Tier Taxonomy & Classifier |
| [`hummbl-tuples`](skills/hummbl-tuples/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL Typed Tuples governance model |
| [`hummbl-validation`](skills/hummbl-validation/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL validation framework — invariant checks, schema validation, external validation tests... |
| [`hummbl-validation-framework`](skills/hummbl-validation-framework/SKILL.md) | HUMMBL | Apache-2.0 | HUMMBL Validation Framework — external validation tests for the design system |
| [`hyperfocus-enter`](skills/hyperfocus-enter/SKILL.md) | HUMMBL | Apache-2.0 | Enter hyperfocus mode — transition cogstate to HYPERFOCUS, silence non-critical interrupts, ... |
| [`hyperfocus-exit`](skills/hyperfocus-exit/SKILL.md) | HUMMBL | Apache-2.0 | Exit hyperfocus mode — transition cogstate to TRANSITION then RECOVERY, restore interrupt av... |
| [`i18n-check`](skills/i18n-check/SKILL.md) | HUMMBL | Apache-2.0 | Find hardcoded strings and i18n readiness issues in code |
| [`i4h-lerobot-viz`](skills/i4h-lerobot-viz/SKILL.md) | HUMMBL | Apache-2.0 | Serve and visually inspect a converted LeRobot dataset in the browser. Use for videos and st... |
| [`i4h-workflow`](skills/i4h-workflow/SKILL.md) | HUMMBL | Apache-2.0 | Orient users to the i4h workflow runtime and route them to the correct stage skill. Use for ... |
| [`i4h-workflow-create`](skills/i4h-workflow-create/SKILL.md) | HUMMBL | Apache-2.0 | Create a minimal blank Workflow scaffold with a Scene containing ground and light plus an id... |
| [`i4h-workflow-dataset-annotate`](skills/i4h-workflow-dataset-annotate/SKILL.md) | HUMMBL | Apache-2.0 | Grade or filter workflow HDF5 episodes with an OpenAI-compatible vision model. Use for visua... |
| [`i4h-workflow-dataset-convert`](skills/i4h-workflow-dataset-convert/SKILL.md) | HUMMBL | Apache-2.0 | Convert workflow HDF5 recordings to LeRobot datasets for training or browser inspection. Use... |
| [`i4h-workflow-dataset-mimic`](skills/i4h-workflow-dataset-mimic/SKILL.md) | HUMMBL | Apache-2.0 | Expand workflow HDF5 demonstrations with action jitter, optionally scoped to node segments. ... |
| [`i4h-workflow-dataset-replay`](skills/i4h-workflow-dataset-replay/SKILL.md) | HUMMBL | Apache-2.0 | Replay a workflow HDF5 episode through its original Scene. Use for visual trajectory and rec... |
| [`i4h-workflow-dataset-teleop`](skills/i4h-workflow-dataset-teleop/SKILL.md) | HUMMBL | Apache-2.0 | Record demonstrations through a workflow's teleop Task into workflow HDF5. Use for keyboard,... |
| [`i4h-workflow-e2e`](skills/i4h-workflow-e2e/SKILL.md) | HUMMBL | Apache-2.0 | Run the maintained workflow data-to-policy pipeline from recording through checkpoint valida... |
| [`i4h-workflow-finetune`](skills/i4h-workflow-finetune/SKILL.md) | HUMMBL | Apache-2.0 | Fine-tune a manifest-backed GR00T or openpi remote Task on compatible LeRobot data. Use for ... |
| [`i4h-workflow-scene-edit`](skills/i4h-workflow-scene-edit/SKILL.md) | HUMMBL | Apache-2.0 | Edit an existing workflow Scene or task contract. Use for assets, layout, cameras, randomiza... |
| [`i4h-workflow-setup`](skills/i4h-workflow-setup/SKILL.md) | HUMMBL | Apache-2.0 | Preflight and set up the root-level workflow runtime. Use for installation, missing componen... |
| [`i4h-workflow-train-rl`](skills/i4h-workflow-train-rl/SKILL.md) | HUMMBL | Apache-2.0 | Use when training, evaluating, or exporting Workflow policies with online RSL-RL or RLinf, i... |
| [`i4h-workflow-validate`](skills/i4h-workflow-validate/SKILL.md) | HUMMBL | Apache-2.0 | Run the root-level workflow runtime policy or rule-based rollouts and verify simulator succe... |
| [`icp-profile`](skills/icp-profile/SKILL.md) | HUMMBL | Apache-2.0 | Build a detailed Ideal Customer Profile with firmographic, psychographic, and trigger event ... |
| [`idea-pack`](skills/idea-pack/SKILL.md) | HUMMBL | Apache-2.0 | Create a structured IDEA PACK at Phase C of the Intent-to-Spec pipeline. Generates a schema-... |
| [`identity`](skills/identity/SKILL.md) | HUMMBL | Apache-2.0 | Unified HUMMBL agent identity facade — integrates design-tokens, heraldry, and garage into o... |
| [`identity-map`](skills/identity-map/SKILL.md) | HUMMBL | Apache-2.0 | Map how identities shape system behavior -- agent roles, user personas, org context. Maps to... |
| [`idp-inspect`](skills/idp-inspect/SKILL.md) | HUMMBL | Apache-2.0 | Query IDP governance JSONL and delegation state. |
| [`idp-spec`](skills/idp-spec/SKILL.md) | HUMMBL | Apache-2.0 | Intelligent Delegation Profile — deterministic delegation for multi-agent systems |
| [`import-sort`](skills/import-sort/SKILL.md) | HUMMBL | Apache-2.0 | Audit and fix import ordering (stdlib -> third-party -> local) with isort-compatible rules |
| [`inbox-zero`](skills/inbox-zero/SKILL.md) | HUMMBL | Apache-2.0 | Process all pending items to zero -- open PRs, stale issues, unanswered bus messages, dirty ... |
| [`incentive-design`](skills/incentive-design/SKILL.md) | HUMMBL | Apache-2.0 | Design reward structures that align individual agent/user actions with system goals. Maps to... |
| [`incident`](skills/incident/SKILL.md) | HUMMBL | Apache-2.0 | Run non-mutating incident triage with explicit health, bus, kill-switch, repository-bound CI... |
| [`incident-commander`](skills/incident-commander/SKILL.md) | HUMMBL | Apache-2.0 | "Take command during an active incident — coordinate responders, track timeline, manage comm... |
| [`incident-response-plan`](skills/incident-response-plan/SKILL.md) | HUMMBL | Apache-2.0 | Build an AI-specific incident response plan — detection, classification, containment, notifi... |
| [`incident-timeline-reconstruct`](skills/incident-timeline-reconstruct/SKILL.md) | HUMMBL | Apache-2.0 | Reconstruct an incident timeline from logs, bus messages, and alerts. Correlates timestamps ... |
| [`inclusive-design`](skills/inclusive-design/SKILL.md) | HUMMBL | Apache-2.0 | Apply inclusive design principles and practices for accessible, equitable user experiences. ... |
| [`industry-watch`](skills/industry-watch/SKILL.md) | HUMMBL | Apache-2.0 | Track bleeding-edge AI announcements from NVIDIA, Google, Apple, Microsoft, AWS, Cloudflare,... |
| [`inference-optimize`](skills/inference-optimize/SKILL.md) | HUMMBL | Apache-2.0 | Optimize ML inference with KV-cache, batching, speculative decoding, and attention optimization |
| [`information-architecture`](skills/information-architecture/SKILL.md) | HUMMBL | Apache-2.0 | Structure navigation, taxonomy, page hierarchy, content grouping, labels, and findability. U... |
| [`insight-capture`](skills/insight-capture/SKILL.md) | HUMMBL | Apache-2.0 | Structured insight capture from sessions into the cognitive ledger. Distills a non-obvious f... |
| [`intel-ingest`](skills/intel-ingest/SKILL.md) | HUMMBL | Apache-2.0 | Ingest intelligence into the Cognitive Ledger, Open Brain, Bus, and all other intel ingestio... |
| [`interaction-design`](skills/interaction-design/SKILL.md) | HUMMBL | Apache-2.0 | Design or review user flows, interaction states, transitions, feedback loops, empty/loading/... |
| [`internal-comms`](skills/internal-comms/SKILL.md) | HUMMBL | Apache-2.0 | "Write internal communications in preferred company formats: status reports, leadership upda... |
| [`interpro-database`](skills/interpro-database/SKILL.md) | HUMMBL | Apache-2.0 | Identify domains, families, and sites in proteins; find all proteins in a family or sharing ... |
| [`investor-update`](skills/investor-update/SKILL.md) | HUMMBL | Apache-2.0 | Draft monthly investor/stakeholder update from metrics, milestones, and roadmap. |
| [`invoice-generate`](skills/invoice-generate/SKILL.md) | HUMMBL | Apache-2.0 | Generate invoice from hours, rate, and client details with sequence tracking. |
| [`ip-valuation`](skills/ip-valuation/SKILL.md) | HUMMBL | Apache-2.0 | Find all IP assets (repositories, packages, domains) and rank them by estimated market value. |
| [`isaac-mission-control-showcase`](skills/isaac-mission-control-showcase/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Run and validate an end-to-end Mission Control showcase with a locally installed Isaac Sim l... |
| [`iso-crosswalk`](skills/iso-crosswalk/SKILL.md) | HUMMBL | Apache-2.0 | Cross-reference controls across ISO 27001, ISO 42001, NIST CSF, SOC 2 |
| [`issue-triage`](skills/issue-triage/SKILL.md) | HUMMBL | Apache-2.0 | Triage GitHub issues -- auto-label, prioritize by severity/type, identify stale issues, sugg... |
| [`jaspar-database`](skills/jaspar-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the JASPAR database for Transcription Factor (TF) binding profiles. Use when retrievin... |
| [`jetson-build-source`](skills/jetson-build-source/SKILL.md) | HUMMBL | "Apache-2.0" | Use when you need to rebuild the BSP overlay — DT, OOT modules, or kernel — from changes und... |
| [`jetson-customize-camera`](skills/jetson-customize-camera/SKILL.md) | HUMMBL | "Apache-2.0" | Enable MIPI/GMSL camera sensors on a Jetson Thor or Orin custom carrier by rendering a kerne... |
| [`jetson-customize-clocks`](skills/jetson-customize-clocks/SKILL.md) | HUMMBL | "Apache-2.0" | Use to lock/cap Jetson CPU/GPU/EMC clocks, toggle EMC/CPU DVFS, or change cpufreq governors ... |
| [`jetson-customize-fan`](skills/jetson-customize-fan/SKILL.md) | HUMMBL | "Apache-2.0" | Use when you need to add, remove, edit, list, or change the boot default of an nvfancontrol ... |
| [`jetson-customize-mgbe`](skills/jetson-customize-mgbe/SKILL.md) | HUMMBL | "Apache-2.0" | Enable Jetson Thor 25G/10G/1G MGBE QSFP via kernel-DT overlay. Do NOT use for UPHY lane allo... |
| [`jetson-customize-nvpmodel`](skills/jetson-customize-nvpmodel/SKILL.md) | HUMMBL | "Apache-2.0" | Use when you need to add, remove, edit, list, or change the boot default of an nvpmodel powe... |
| [`jetson-customize-pcie`](skills/jetson-customize-pcie/SKILL.md) | HUMMBL | "Apache-2.0" | Per-controller PCIe enable / disable / lanes / link-speed for a Jetson Thor or Orin custom c... |
| [`jetson-customize-pinmux`](skills/jetson-customize-pinmux/SKILL.md) | HUMMBL | "Apache-2.0" | Per-pin SFIO / direction / initial-state configurator for a Jetson Orin or Thor custom carri... |
| [`jetson-customize-uphy`](skills/jetson-customize-uphy/SKILL.md) | HUMMBL | "Apache-2.0" | Configure Jetson UPHY lane allocation (uphy0/uphy1-config) on Orin/Thor custom carriers. Do ... |
| [`jetson-customize-usb`](skills/jetson-customize-usb/SKILL.md) | HUMMBL | "Apache-2.0" | Enable/disable Jetson USB2/USB3 SS ports via kernel-DT overlay. Do NOT use for UPHY lane all... |
| [`jetson-derive-carrier`](skills/jetson-derive-carrier/SKILL.md) | HUMMBL | "Apache-2.0" | Bootstrap a custom carrier board by forking carrier files and scaffolding a DT overlay from ... |
| [`jetson-diagnostic`](skills/jetson-diagnostic/SKILL.md) | HUMMBL | "Apache-2.0" | Read-only Jetson health snapshot for identity, memory, GPU, thermal, power, storage, service... |
| [`jetson-download-bsp`](skills/jetson-download-bsp/SKILL.md) | HUMMBL | "Apache-2.0" | Download NVIDIA Jetson Linux BSP artifacts (BSP tarball, sample rootfs, public_sources, x-to... |
| [`jetson-flash-image`](skills/jetson-flash-image/SKILL.md) | HUMMBL | "Apache-2.0" | Use to flash a promoted BSP image to a Jetson DUT in RCM mode via flash.sh or l4t_initrd_fla... |
| [`jetson-generate-kb`](skills/jetson-generate-kb/SKILL.md) | HUMMBL | "Apache-2.0" | Build a per-target knowledge-base markdown next to the active profile by walking the BSP roo... |
| [`jetson-headless-mode`](skills/jetson-headless-mode/SKILL.md) | HUMMBL | "Apache-2.0" | Plan and apply safe Jetson headless-mode changes to reclaim GUI and daemon memory. |
| [`jetson-inference-mem-tune`](skills/jetson-inference-mem-tune/SKILL.md) | HUMMBL | "Apache-2.0" | Pick the serving stack and per-runtime memory flags (vLLM, SGLang, llama.cpp, TensorRT Edge-... |
| [`jetson-init-image`](skills/jetson-init-image/SKILL.md) | HUMMBL | "Apache-2.0" | Extract Jetson Linux + sample-rootfs tarballs and run apply_binaries.sh for the active targe... |
| [`jetson-init-source`](skills/jetson-init-source/SKILL.md) | HUMMBL | "Apache-2.0" | Set up the BSP source workspace: Linux_for_Tegra overlay tracker, bsp_sources, Crosstool-NG ... |
| [`jetson-init-target`](skills/jetson-init-target/SKILL.md) | HUMMBL | "Apache-2.0" | Author a new Jetson target-platform profile (reference_devkit + optional custom_carrier) and... |
| [`jetson-link-docs`](skills/jetson-link-docs/SKILL.md) | HUMMBL | "Apache-2.0" | Bind pre-downloaded Jetson reference docs (developer guide, design guide, pinmux, schematics... |
| [`jetson-llm-benchmark`](skills/jetson-llm-benchmark/SKILL.md) | HUMMBL | "Apache-2.0" | Benchmark Jetson LLM/VLM serving performance across vLLM, llama.cpp, and Ollama with structu... |
| [`jetson-llm-serve`](skills/jetson-llm-serve/SKILL.md) | HUMMBL | "Apache-2.0" | Stand up vLLM or SGLang serving on Jetson, using upstream vLLM on Thor and Orin JetPack 7.2+... |
| [`jetson-package`](skills/jetson-package/SKILL.md) | HUMMBL | "Apache-2.0" | Pick Jetson-compatible containers, vLLM runtime images, and Jetson AI Lab PyPI indexes; maps... |
| [`jetson-print-bsp-info`](skills/jetson-print-bsp-info/SKILL.md) | HUMMBL | "Apache-2.0" | Use when you need to print Jetson BSP info (L4T version, board configs, rootfs state) from a... |
| [`jetson-print-device-info`](skills/jetson-print-device-info/SKILL.md) | HUMMBL | "Apache-2.0" | Use when you need to print Jetson device info (module model, L4T version, kernel, OS version... |
| [`jetson-promote-image`](skills/jetson-promote-image/SKILL.md) | HUMMBL | "Apache-2.0" | Use to promote overlay files and built artifacts into the staged BSP image. Do NOT use to fl... |
| [`jetson-quick-start`](skills/jetson-quick-start/SKILL.md) | HUMMBL | "Apache-2.0" | Entry skill for Jetson / IGX BSP customization. Asks one core click-to-select setup question... |
| [`jetson-set-target`](skills/jetson-set-target/SKILL.md) | HUMMBL | "Apache-2.0" | Switch the active Jetson target-platform pointer to an existing profile YAML. Use before cus... |
| [`jetson-speculative-decoding`](skills/jetson-speculative-decoding/SKILL.md) | HUMMBL | "Apache-2.0" | Add EAGLE-3 or draft-model speculative decoding to a Jetson vLLM server when TPOT is the bot... |
| [`jetson-validate-image`](skills/jetson-validate-image/SKILL.md) | HUMMBL | "Apache-2.0" | Use after jetson-flash-image to run static BSP checks, on-target smoke/regression tests on a... |
| [`jetson-video-benchmark`](skills/jetson-video-benchmark/SKILL.md) | HUMMBL | "Apache-2.0" | Use when measuring Jetson Video Codec SDK or PyNvVideoCodec encode/decode throughput, compar... |
| [`jetson-video-capability`](skills/jetson-video-capability/SKILL.md) | HUMMBL | "Apache-2.0" | Use when Jetson codec, profile, chroma, bit-depth, dimension, engine-count, or operational s... |
| [`jetson-video-pipeline`](skills/jetson-video-pipeline/SKILL.md) | HUMMBL | "Apache-2.0" | Use when executing and verifying Jetson Video Codec SDK or PyNvVideoCodec encode/decode, tra... |
| [`jetson-video-recipe`](skills/jetson-video-recipe/SKILL.md) | HUMMBL | "Apache-2.0" | Use when turning a Jetson encoder use case into one validated surface-neutral recipe with na... |
| [`jetson-video-setup`](skills/jetson-video-setup/SKILL.md) | HUMMBL | "Apache-2.0" | Use when installing, repairing, probing, or verifying native NVIDIA Video Codec SDK or PyNvV... |
| [`job-description`](skills/job-description/SKILL.md) | HUMMBL | Apache-2.0 | Write a job description / job posting. Role summary, responsibilities, requirements (must-ha... |
| [`job-hunt`](skills/job-hunt/SKILL.md) | HUMMBL | Apache-2.0 | Daily job application tracker -- streak, targets, follow-ups, platform links, and proof pack... |
| [`json-explore`](skills/json-explore/SKILL.md) | HUMMBL | Apache-2.0 | Navigate complex JSON/JSONL structures, extract paths, compare versions, show schema |
| [`jsonl-validate`](skills/jsonl-validate/SKILL.md) | HUMMBL | Apache-2.0 | Validate JSONL files against schemas, detect corruption, report line-level errors. |
| [`jump-physics-calculator`](skills/jump-physics-calculator/SKILL.md) | HUMMBL | Apache-2.0 | Calculates exact kinematic formulas (gravity, jump velocity, coyote time, air control) from ... |
| [`kai-email-management`](skills/kai-email-management/SKILL.md) | HUMMBL | Apache-2.0 | AI Chief of Staff email management for Kai - autonomous email triage, draft response generat... |
| [`kaizen`](skills/kaizen/SKILL.md) | HUMMBL | Apache-2.0 | Continuous-improvement ritual — capture one small improvement, attribute the object that act... |
| [`kermt-add-cmim-pretrain`](skills/kermt-add-cmim-pretrain/SKILL.md) | HUMMBL | Apache-2.0 | Convert a grover_base checkpoint (encoder-only or encoder + vocab heads) into a hybrid check... |
| [`kermt-continue-pretrain`](skills/kermt-continue-pretrain/SKILL.md) | HUMMBL | Apache-2.0 | Continue KERMT pretraining on a custom SMILES corpus with a grover_base, cmim, or hybrid che... |
| [`kermt-embed`](skills/kermt-embed/SKILL.md) | HUMMBL | Apache-2.0 | Extract per-molecule embeddings from any encoder-bearing KERMT checkpoint. Use a local check... |
| [`kermt-finetune`](skills/kermt-finetune/SKILL.md) | HUMMBL | Apache-2.0 | Finetune a pretrained KERMT encoder on a labeled CSV. Validate the checkpoint and data, prep... |
| [`kermt-infer`](skills/kermt-infer/SKILL.md) | HUMMBL | Apache-2.0 | Run predictions with a finetuned KERMT checkpoint on a SMILES-only CSV. The skill validates ... |
| [`kermt-monitor`](skills/kermt-monitor/SKILL.md) | HUMMBL | Apache-2.0 | Check progress for a detached KERMT run (pretrain, finetune, or any kermt_run_detached invoc... |
| [`kermt-pretrain-scratch`](skills/kermt-pretrain-scratch/SKILL.md) | HUMMBL | Apache-2.0 | Pretrain a fresh KERMT model from scratch on a user-provided corpus. Builds a new vocabulary... |
| [`kermt-setup`](skills/kermt-setup/SKILL.md) | HUMMBL | Apache-2.0 | Bootstrap the KERMT agent environment — verify host docker + nvidia-container-toolkit, build... |
| [`keyboard-nav`](skills/keyboard-nav/SKILL.md) | HUMMBL | Apache-2.0 | Test keyboard navigation and focus management for accessibility compliance. [Maps to P9.] |
| [`kill-switch`](skills/kill-switch/SKILL.md) | HUMMBL | Apache-2.0 | Inspect kill switch state (read-only by default, engage with explicit command). |
| [`knowledge-map`](skills/knowledge-map/SKILL.md) | HUMMBL | Apache-2.0 | "Map who-knows-what across teams, agents, docs, and code ownership. Use for silos, gaps, doc... |
| [`kpi-track`](skills/kpi-track/SKILL.md) | HUMMBL | Apache-2.0 | Define and track KPIs with thresholds, trend direction, and alerting |
| [`krak`](skills/krak/SKILL.md) | HUMMBL | MIT | Caveman character: KRAK, the warrior. Aggressive, loyal, boastful. Quick to anger, quick to ... |
| [`landing-page-copy`](skills/landing-page-copy/SKILL.md) | HUMMBL | Apache-2.0 | Write landing page copy — hero, problem/solution, benefits, social proof, FAQ, and CTA secti... |
| [`latency-percentile`](skills/latency-percentile/SKILL.md) | HUMMBL | Apache-2.0 | Analyze latency distributions — p50/p90/p95/p99/p99.9 with tail latency identification and S... |
| [`launch-antigravity`](skills/launch-antigravity/SKILL.md) | HUMMBL | Apache-2.0 | Skill to launch the Antigravity desktop application on Windows host. |
| [`launch-nemo-rl`](skills/launch-nemo-rl/SKILL.md) | HUMMBL | Apache-2.0 | Playbook for launching, monitoring, stopping, and debugging NeMo-RL recipes on a Kubernetes ... |
| [`launch-with-aws`](skills/launch-with-aws/SKILL.md) | HUMMBL | Apache-2.0 | Migrates vibe-coded web applications to AWS. Handles the full workflow from analysis through... |
| [`lavenderteam`](skills/lavenderteam/SKILL.md) | HUMMBL | Apache-2.0 | AI/ML security -- adversarial ML, prompt injection defense, model security, AI governance. S... |
| [`ldtk-type-generator`](skills/ldtk-type-generator/SKILL.md) | HUMMBL | Apache-2.0 | Parses .ldtk project files and auto-generates type-safe structs/classes for all entity field... |
| [`lead-intake`](skills/lead-intake/SKILL.md) | HUMMBL | Apache-2.0 | Process new leads from Cal.com, Linktree, or manual entry into CRM and send acknowledgment |
| [`ledger`](skills/ledger/SKILL.md) | HUMMBL | Apache-2.0 | Post, query, search, and reindex the Cognitive Ledger (CLP shared memory). |
| [`legal-ai-precedent-watch`](skills/legal-ai-precedent-watch/SKILL.md) | HUMMBL | Apache-2.0 | "Research legal-AI ethics, privilege, confidentiality, hallucination sanctions, court rules,... |
| [`legal-check`](skills/legal-check/SKILL.md) | HUMMBL | Apache-2.0 | Review code, docs, and configs for license compliance, IP exposure, and legal risks. |
| [`library`](skills/library/SKILL.md) | HUMMBL | Apache-2.0 | HUAOMP Library — acquire, catalog, query, and curate knowledge across 20 departments. Receip... |
| [`license-audit`](skills/license-audit/SKILL.md) | HUMMBL | Apache-2.0 | Deep license compatibility check across all dependencies, flag GPL contamination, generate S... |
| [`literature-search-arxiv`](skills/literature-search-arxiv/SKILL.md) | HUMMBL | Apache-2.0 | Search for scientific papers, preprints, and publications on arXiv. Extract metadata, abstra... |
| [`literature-search-biorxiv`](skills/literature-search-biorxiv/SKILL.md) | HUMMBL | Apache-2.0 | Browse, filter, and download life sciences, biology, and medical preprints from bioRxiv and ... |
| [`literature-search-europepmc`](skills/literature-search-europepmc/SKILL.md) | HUMMBL | Apache-2.0 | Search Europe PMC for scientific literature and download open-access full texts and PDFs. Re... |
| [`literature-search-openalex`](skills/literature-search-openalex/SKILL.md) | HUMMBL | Apache-2.0 | Query the OpenAlex scholarly database for research papers, authors, institutions, topics, so... |
| [`llms-txt`](skills/llms-txt/SKILL.md) | HUMMBL | Apache-2.0 | Generate or update llms.txt and llms-full.txt for LLM-optimized site discovery |
| [`load-test`](skills/load-test/SKILL.md) | HUMMBL | Apache-2.0 | Generate and run HTTP load tests with stdlib urllib and concurrent.futures |
| [`loc-report`](skills/loc-report/SKILL.md) | HUMMBL | Apache-2.0 | Lines of code report by directory, language, and change velocity |
| [`log-analyze`](skills/log-analyze/SKILL.md) | HUMMBL | Apache-2.0 | Pattern recognition in log files -- error clusters, timing anomalies, frequency analysis |
| [`log-tail`](skills/log-tail/SKILL.md) | HUMMBL | Apache-2.0 | Tail and search logs -- local services, launchd agents, bus, governance. |
| [`long-running-loop`](skills/long-running-loop/SKILL.md) | HUMMBL | Apache-2.0 | Governed execution protocol for relentless, long-running autonomous agent operations. |
| [`longrun`](skills/longrun/SKILL.md) | HUMMBL | Apache-2.0 | Orchestrates long-running Devin CLI sessions in --sandbox --permission-mode autonomous. Bund... |
| [`loop`](skills/loop/SKILL.md) | HUMMBL | Apache-2.0 | Repeat a command or skill with structure -- watch, retry, iterate, converge. |
| [`loot-table-linter`](skills/loot-table-linter/SKILL.md) | HUMMBL | Apache-2.0 | Audits drop tables and RNG configs (JSON, CSV, YAML) for rounding errors, unreachable loot t... |
| [`machine-health`](skills/machine-health/SKILL.md) | HUMMBL | Apache-2.0 | Verify local and fleet health with layered SSH, Tailscale route, Docker, resource, and compa... |
| [`machine-inventory`](skills/machine-inventory/SKILL.md) | HUMMBL | Apache-2.0 | Hardware and software inventory across all machines with diff capability |
| [`marathon-runner`](skills/marathon-runner/SKILL.md) | HUMMBL | MIT | Long-term coding mode. Optimize for maintainability over 6+ months. Test suite first, code s... |
| [`market-gap-finder`](skills/market-gap-finder/SKILL.md) | HUMMBL | Apache-2.0 | Scan a market category for unmet needs and whitespace opportunities that HUMMBL is uniquely ... |
| [`mcnamara-fallacy`](skills/mcnamara-fallacy/SKILL.md) | HUMMBL | Apache-2.0 | Audit decisions and metric systems for the McNamara fallacy — the four-step collapse where o... |
| [`mcore-create-issue`](skills/mcore-create-issue/SKILL.md) | HUMMBL | Apache-2.0 | Investigate a failing GitHub Actions run or job and create a GitHub issue for the failure. |
| [`mcore-linting-and-formatting`](skills/mcore-linting-and-formatting/SKILL.md) | HUMMBL | Apache-2.0 | Linting and formatting for Megatron-LM. Covers running autoformat.sh, tools (ruff, black, is... |
| [`mcore-run-on-slurm`](skills/mcore-run-on-slurm/SKILL.md) | HUMMBL | Apache-2.0 | How to launch distributed Megatron-LM training jobs on a SLURM cluster. Covers a minimal sba... |
| [`mcore-split-pr`](skills/mcore-split-pr/SKILL.md) | HUMMBL | Apache-2.0 | Split a PR into multiple PRs to reduce the number of required CODEOWNERS reviewer groups. |
| [`mcore-testing`](skills/mcore-testing/SKILL.md) | HUMMBL | Apache-2.0 | Test system for Megatron-LM. Covers test layout, recipe YAML structure, adding and running u... |
| [`mcp-builder`](skills/mcp-builder/SKILL.md) | HUMMBL | Apache-2.0 | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to int... |
| [`mcp-fleet-config-12server`](skills/mcp-fleet-config-12server/SKILL.md) | HUMMBL | Apache-2.0 | Configures and validates the 12-server MCP fleet standard for HUMMBL agents. Manages both lo... |
| [`mcp-fleet-ops`](skills/mcp-fleet-ops/SKILL.md) | HUMMBL | Apache-2.0 | Cross-machine MCP fleet operations — rolling health checks, config drift detection, version ... |
| [`mcp-server-developer`](skills/mcp-server-developer/SKILL.md) | HUMMBL | Apache-2.0 | Model Context Protocol (MCP) server implementation specialist for Claude Desktop integration... |
| [`mcp-test`](skills/mcp-test/SKILL.md) | HUMMBL | Apache-2.0 | Test MCP server implementations with tool discovery, schema validation, invocation testing, ... |
| [`medtech-model-evidence-export`](skills/medtech-model-evidence-export/SKILL.md) | HUMMBL | Apache-2.0 | Exports sanitized metadata, parameters, reproducibility details, quality metrics, and option... |
| [`meeting-capture`](skills/meeting-capture/SKILL.md) | HUMMBL | Apache-2.0 | Post-meeting agent — fetches Gemini transcript from Google Drive, extracts decisions/actions... |
| [`meeting-prep`](skills/meeting-prep/SKILL.md) | HUMMBL | Apache-2.0 | Prepare agenda, context, and action items for a meeting with stakeholders. |
| [`meeting-review`](skills/meeting-review/SKILL.md) | HUMMBL | Apache-2.0 | Review meeting context, open action items, recent decisions, and last meeting summary. |
| [`memory-dedup`](skills/memory-dedup/SKILL.md) | HUMMBL | Apache-2.0 | Compact MEMORY.md back under the auto-load limit by truncating long index lines, splitting c... |
| [`memory-evolve`](skills/memory-evolve/SKILL.md) | HUMMBL | Apache-2.0 | Score memory files for staleness, relevance, duplication — prune/update/consolidate recommen... |
| [`memory-registry`](skills/memory-registry/SKILL.md) | HUMMBL | Apache-2.0 | Manage the active Codex memory registry, rollout summaries, and explicit ad hoc update notes. |
| [`mental-model`](skills/mental-model/SKILL.md) | HUMMBL | Apache-2.0 | Catalog and apply mental models (Occam's razor, second-order thinking, inversion, etc.) to p... |
| [`mesh-audit`](skills/mesh-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit local .agents Git provenance, cleanliness, and alignment with origin/main without chan... |
| [`mesh-sync`](skills/mesh-sync/SKILL.md) | HUMMBL | Apache-2.0 | Sync .agents/ content across the fleet via hummbl-io/agents GitHub remote. Git-based — push ... |
| [`meta-analysis`](skills/meta-analysis/SKILL.md) | HUMMBL | Apache-2.0 | PRISMA-compliant systematic review pipeline — search, screen, extract, synthesize. Produces ... |
| [`meta-synthesis`](skills/meta-synthesis/SKILL.md) | HUMMBL | Apache-2.0 | Qualitative meta-synthesis - aggregate findings across qualitative studies using meta-ethnog... |
| [`metal-scaffold`](skills/metal-scaffold/SKILL.md) | HUMMBL | Apache-2.0 | Scaffold a new project in the hummbl-io/metal repo under the correct language directory with... |
| [`metric-define`](skills/metric-define/SKILL.md) | HUMMBL | Apache-2.0 | Define business and technical metrics with collection method, baseline, target, alert thresh... |
| [`migrate`](skills/migrate/SKILL.md) | HUMMBL | Apache-2.0 | Plan and execute data or schema migrations -- ledger format, bus format, config changes, dat... |
| [`migration-check`](skills/migration-check/SKILL.md) | HUMMBL | Apache-2.0 | Pre-migration validation — schema compatibility, data integrity, rollback plan |
| [`mission-abort`](skills/mission-abort/SKILL.md) | HUMMBL | Apache-2.0 | Exit a mission-mode session with partial-work receipt. |
| [`mission-declare`](skills/mission-declare/SKILL.md) | HUMMBL | Apache-2.0 | Declare a new mission-mode session with structured packet schema. |
| [`ml-bias-audit`](skills/ml-bias-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit a model for demographic and performance bias. Tests for disparate impact across protec... |
| [`ml-train`](skills/ml-train/SKILL.md) | HUMMBL | Apache-2.0 | Train and validate machine learning models with experiment tracking. [Maps to CO7.] |
| [`mlops-deploy`](skills/mlops-deploy/SKILL.md) | HUMMBL | Apache-2.0 | Deploy and monitor ML models in production with validation and rollback capabilities. [Maps ... |
| [`mobile-bus`](skills/mobile-bus/SKILL.md) | HUMMBL | Apache-2.0 | Write to the coordination bus from any execution context (local or remote). Auto-detects loc... |
| [`mock-server`](skills/mock-server/SKILL.md) | HUMMBL | Apache-2.0 | Spin up a mock HTTP server from API schema or example responses using stdlib http.server |
| [`model-card`](skills/model-card/SKILL.md) | HUMMBL | Apache-2.0 | Generate ML model cards documenting capabilities, limitations, training data, and ethical co... |
| [`model-compare`](skills/model-compare/SKILL.md) | HUMMBL | Apache-2.0 | Side-by-side model comparison on identical inputs with structured scoring. |
| [`model-drift`](skills/model-drift/SKILL.md) | HUMMBL | Apache-2.0 | Detect and monitor model performance drift over time with statistical validation. [Maps to C... |
| [`model-lifecycle`](skills/model-lifecycle/SKILL.md) | HUMMBL | Apache-2.0 | Track new model releases, vendor deprecations/sunsets, and component topologies (kernels, ha... |
| [`model-router`](skills/model-router/SKILL.md) | HUMMBL | Apache-2.0 | Design multi-model routing -- select optimal model per task based on cost, quality, latency,... |
| [`model-serve`](skills/model-serve/SKILL.md) | HUMMBL | Apache-2.0 | Serve ML models via REST/gRPC with batching, autoscaling, and health checks |
| [`mog`](skills/mog/SKILL.md) | HUMMBL | MIT | Caveman character: MOG, the hunter. Patient, sensory, speaks in terms of smell, track, and p... |
| [`mono-diff`](skills/mono-diff/SKILL.md) | HUMMBL | Apache-2.0 | Show changes across multiple repos since a date with commit summaries |
| [`morning-brief`](skills/morning-brief/SKILL.md) | HUMMBL | Apache-2.0 | Unified fleet+news briefing emailed to Proton every 4 hours — action-required probes, fleet ... |
| [`mtsmu-debug`](skills/mtsmu-debug/SKILL.md) | HUMMBL | Apache-2.0 | "Evidence-first debugging for failures, regressions, flaky tests, broken scripts, and runtim... |
| [`mtsmu-orchestrator`](skills/mtsmu-orchestrator/SKILL.md) | HUMMBL | Apache-2.0 | "Evidence-first orchestration for high-rigor coding, debugging, review, and ops work with la... |
| [`mtsmu-research`](skills/mtsmu-research/SKILL.md) | HUMMBL | Apache-2.0 | "High-rigor research with source weighting, temporal checks, fact/inference separation, unce... |
| [`mtsmu-review`](skills/mtsmu-review/SKILL.md) | HUMMBL | Apache-2.0 | Bug-first review for code, configs, scripts, and operational changes. Use when the user asks... |
| [`mtsmu-swarm`](skills/mtsmu-swarm/SKILL.md) | HUMMBL | Apache-2.0 | Swarm-style coordination for high-rigor implementation, debugging, review, and operations wo... |
| [`multimodal-brief`](skills/multimodal-brief/SKILL.md) | HUMMBL | Apache-2.0 | Synthesize information from multiple data types -- text, screenshots, logs, metrics, diagram... |
| [`mutation-manage`](skills/mutation-manage/SKILL.md) | HUMMBL | Apache-2.0 | Run and analyze mutation testing results, track kill rate over time, identify weak test areas |
| [`nala`](skills/nala/SKILL.md) | HUMMBL | MIT | Cavewoman character: NALA, the firekeeper. Wise, observant, speaks in metaphors about fire a... |
| [`ncbi-sequence-fetch`](skills/ncbi-sequence-fetch/SKILL.md) | HUMMBL | Apache-2.0 | Retrieve protein and nucleotide sequences from NCBI databases using E-utilities. Supports di... |
| [`nda-check`](skills/nda-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify NDA/confidentiality status before sharing sensitive info with a client or partner |
| [`nda-draft`](skills/nda-draft/SKILL.md) | HUMMBL | Apache-2.0 | Draft a Non-Disclosure Agreement (NDA). Mutual or one-way. Covers confidentiality, term, gov... |
| [`nemo-automodel-distributed-training`](skills/nemo-automodel-distributed-training/SKILL.md) | HUMMBL | Apache-2.0 | Guide for selecting and configuring distributed training strategies in NeMo AutoModel, inclu... |
| [`nemo-automodel-launcher-config`](skills/nemo-automodel-launcher-config/SKILL.md) | HUMMBL | Apache-2.0 | Configure NeMo AutoModel job launches for interactive runs, Slurm clusters, and SkyPilot clo... |
| [`nemo-automodel-model-onboarding`](skills/nemo-automodel-model-onboarding/SKILL.md) | HUMMBL | Apache-2.0 | Guide for onboarding new model architectures into NeMo AutoModel, including architecture dis... |
| [`nemo-automodel-recipe-development`](skills/nemo-automodel-recipe-development/SKILL.md) | HUMMBL | Apache-2.0 | Create and modify NeMo AutoModel training and evaluation recipes, including YAML structure, ... |
| [`nemo-fabric-build-adapter`](skills/nemo-fabric-build-adapter/SKILL.md) | HUMMBL | Apache-2.0 | Build, migrate, review, and maintain third-party NVIDIA NeMo Fabric adapters against the pub... |
| [`nemo-fabric-integrate`](skills/nemo-fabric-integrate/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when integrating NVIDIA NeMo Fabric into a consumer application, service, eva... |
| [`nemo-mbridge-mlm-bridge-training`](skills/nemo-mbridge-mlm-bridge-training/SKILL.md) | HUMMBL | Apache-2.0 | Run Megatron-LM (MLM) and Megatron Bridge training with mock or real data. Covers correlatio... |
| [`nemo-mbridge-multi-node-slurm`](skills/nemo-mbridge-multi-node-slurm/SKILL.md) | HUMMBL | Apache-2.0 | Convert single-node scripts to multi-node Slurm sbatch jobs and debug common multi-node fail... |
| [`nemo-mbridge-perf-activation-recompute`](skills/nemo-mbridge-perf-activation-recompute/SKILL.md) | HUMMBL | Apache-2.0 | Validate and use selective and full activation recompute in Megatron Bridge to reduce GPU me... |
| [`nemo-mbridge-perf-cuda-graphs`](skills/nemo-mbridge-perf-cuda-graphs/SKILL.md) | HUMMBL | Apache-2.0 | Validate and use CUDA graph capture in Megatron Bridge, including local full-iteration graph... |
| [`nemo-mbridge-perf-expert-parallel-overlap`](skills/nemo-mbridge-perf-expert-parallel-overlap/SKILL.md) | HUMMBL | Apache-2.0 | Validate and use MoE expert-parallel communication overlap in Megatron-Bridge, including ove... |
| [`nemo-mbridge-perf-hierarchical-context-parallel`](skills/nemo-mbridge-perf-hierarchical-context-parallel/SKILL.md) | HUMMBL | Apache-2.0 | Operational guide for enabling hierarchical context parallelism in Megatron-Bridge, includin... |
| [`nemo-mbridge-perf-megatron-fsdp`](skills/nemo-mbridge-perf-megatron-fsdp/SKILL.md) | HUMMBL | Apache-2.0 | Operational guide for enabling Megatron FSDP in Megatron-Bridge, including config knobs, cod... |
| [`nemo-mbridge-perf-memory-tuning`](skills/nemo-mbridge-perf-memory-tuning/SKILL.md) | HUMMBL | Apache-2.0 | Techniques for reducing peak GPU memory in Megatron Bridge — expandable segments, PEFT + SP ... |
| [`nemo-mbridge-perf-moe-comm-overlap`](skills/nemo-mbridge-perf-moe-comm-overlap/SKILL.md) | HUMMBL | Apache-2.0 | MoE expert-parallel communication overlap in Megatron Bridge. Covers dispatch/combine overla... |
| [`nemo-mbridge-perf-moe-hardware-configs`](skills/nemo-mbridge-perf-moe-hardware-configs/SKILL.md) | HUMMBL | Apache-2.0 | Representative, point-in-time MoE training playbooks by hardware and model family. Use them ... |
| [`nemo-mbridge-perf-moe-long-context`](skills/nemo-mbridge-perf-moe-long-context/SKILL.md) | HUMMBL | Apache-2.0 | Long-context MoE training guidance for Megatron Bridge. Covers CP sizing, selective recomput... |
| [`nemo-mbridge-perf-moe-optimization-workflow`](skills/nemo-mbridge-perf-moe-optimization-workflow/SKILL.md) | HUMMBL | Apache-2.0 | Evidence-gated workflow for MoE performance optimization in Megatron Bridge. Covers measurem... |
| [`nemo-mbridge-perf-moe-vlm-training`](skills/nemo-mbridge-perf-moe-vlm-training/SKILL.md) | HUMMBL | Apache-2.0 | Practical guidance for training MoE VLMs in Megatron Bridge. Compares FSDP and 3D-parallel a... |
| [`nemo-mbridge-perf-parallelism-strategies`](skills/nemo-mbridge-perf-parallelism-strategies/SKILL.md) | HUMMBL | Apache-2.0 | Operational guide for choosing and combining parallelism strategies in Megatron Bridge, incl... |
| [`nemo-mbridge-perf-sequence-packing`](skills/nemo-mbridge-perf-sequence-packing/SKILL.md) | HUMMBL | Apache-2.0 | Validate and use packed sequences and long-context training in Megatron-Bridge, including of... |
| [`nemo-mbridge-perf-tp-dp-comm-overlap`](skills/nemo-mbridge-perf-tp-dp-comm-overlap/SKILL.md) | HUMMBL | Apache-2.0 | Operational guide for enabling TP, DP, and PP communication overlap in Megatron-Bridge, incl... |
| [`nemo-mbridge-recipe-recommender`](skills/nemo-mbridge-recipe-recommender/SKILL.md) | HUMMBL | Apache-2.0 | Recommend and customize Megatron Bridge library and benchmark recipes for a user's model, GP... |
| [`nemo-mbridge-resiliency`](skills/nemo-mbridge-resiliency/SKILL.md) | HUMMBL | Apache-2.0 | Resiliency features in Megatron Bridge including fault tolerance, straggler detection, in-pr... |
| [`nemo-relay-debug-runtime-integration`](skills/nemo-relay-debug-runtime-integration/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when NeMo Relay is installed or imported but application-side runtime behavio... |
| [`nemo-relay-get-started`](skills/nemo-relay-get-started/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when first-time NeMo Relay users want to try Relay, choose the least-complex ... |
| [`nemo-relay-install`](skills/nemo-relay-install/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when choosing or running NeMo Relay installation for the CLI, Python, Node.js... |
| [`nemo-relay-instrument-calls`](skills/nemo-relay-instrument-calls/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when an application owns tool or LLM/provider call sites and needs to wrap th... |
| [`nemo-relay-instrument-context-isolation`](skills/nemo-relay-instrument-context-isolation/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when concurrent requests, async tasks, threads, workers, goroutines, or agent... |
| [`nemo-relay-instrument-typed-wrappers`](skills/nemo-relay-instrument-typed-wrappers/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when adding NeMo Relay typed wrappers, domain types, or provider codecs while... |
| [`nemo-relay-migrate-from-flow`](skills/nemo-relay-migrate-from-flow/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when migrating applications, examples, integrations, documentation, manifests... |
| [`nemo-relay-plugin-adaptive-tuning`](skills/nemo-relay-plugin-adaptive-tuning/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when baseline NeMo Relay instrumentation exists and the user wants to configu... |
| [`nemo-relay-plugin-build`](skills/nemo-relay-plugin-build/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when building or packaging reusable NeMo Relay runtime behavior as an embedde... |
| [`nemo-relay-plugin-observability`](skills/nemo-relay-plugin-observability/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when choosing or configuring NeMo Relay 0.6 or 0.7 observability through the ... |
| [`nemo-retriever`](skills/nemo-retriever/SKILL.md) | HUMMBL | Apache-2.0 | Use when searching, extracting, ingesting, or querying a document collection with the NeMo R... |
| [`nemo-retriever-mcp`](skills/nemo-retriever-mcp/SKILL.md) | HUMMBL | Apache-2.0 | Use when a task needs to search or add documents through NeMo Retriever MCP. |
| [`nemo-rl-auto-research`](skills/nemo-rl-auto-research/SKILL.md) | HUMMBL | Apache-2.0 | "Autonomous NeMo-RL research agent workflow for directed hypothesis testing and open-ended d... |
| [`nemo-rl-brev-etiquette`](skills/nemo-rl-brev-etiquette/SKILL.md) | HUMMBL | Apache-2.0 | Brev instance operating guidance for NeMo-RL agents working in ~/RL with limited workspace d... |
| [`nemo-rl-docs`](skills/nemo-rl-docs/SKILL.md) | HUMMBL | Apache-2.0 | "Documentation conventions for NeMo-RL. Covers docs/index.md updates and docstring format. D... |
| [`nemo-rl-session-memory`](skills/nemo-rl-session-memory/SKILL.md) | HUMMBL | Apache-2.0 | "Manage durable working-session memory for coding agents. Use when a user asks to preserve o... |
| [`nemoclaw-user-guide`](skills/nemoclaw-user-guide/SKILL.md) | HUMMBL | "Apache-2.0" | "Guides human users' AI agents to the NemoClaw docs MCP server and canonical Fern documentat... |
| [`nemotron-asr-finetune`](skills/nemotron-asr-finetune/SKILL.md) | HUMMBL | Apache-2.0 | Orchestration skill for NVIDIA Nemotron Speech (Riva) / NeMo ASR domain and language adaptat... |
| [`nemotron-customize`](skills/nemotron-customize/SKILL.md) | HUMMBL | Apache-2.0 | "Plan, configure, and chain repo-native Nemotron customization steps into single-step or mul... |
| [`nemotron-policy-generator`](skills/nemotron-policy-generator/SKILL.md) | HUMMBL | "Apache-2.0 AND CC-BY-4.0" | "Generates BYO custom safety policies for NVIDIA Nemotron content-safety guardrails — Nemotr... |
| [`nemotron-retrieval-recipes`](skills/nemotron-retrieval-recipes/SKILL.md) | NVIDIA Nemotron Team ... | Apache-2.0 | Use when planning, debugging, tuning, evaluating, exporting, or deploying public Nemotron `e... |
| [`nemotron-speech`](skills/nemotron-speech/SKILL.md) | HUMMBL | Apache-2.0 | Routes NVIDIA Nemotron Speech (Formerly Riva) NIM tasks — deploys, runs, and tests ASR, TTS,... |
| [`nemotron-voice-agent-builder`](skills/nemotron-voice-agent-builder/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Create, refine, or fix NVIDIA voice agents (Cascaded or Omni) with Pipecat or LiveKit. Use w... |
| [`neon`](skills/neon/SKILL.md) | HUMMBL | Apache-2.0 | Overview of Neon, a complete set of cloud backend primitives for apps and agents, spanning L... |
| [`neon-postgres`](skills/neon-postgres/SKILL.md) | HUMMBL | Apache-2.0 | Guides and best practices for working with Lakebase Postgres on Neon: connections, pooled vs... |
| [`nested-story`](skills/nested-story/SKILL.md) | HUMMBL | Apache-2.0 | Structure complex information as layered narratives -- executive summary nesting into techni... |
| [`news-brief`](skills/news-brief/SKILL.md) | HUMMBL | Apache-2.0 | Morning news digest — HuggingNews AI wire, Hacker News front page, Hugging Face trending mod... |
| [`newsletter-submit`](skills/newsletter-submit/SKILL.md) | HUMMBL | Apache-2.0 | Prepare and track newsletter submissions to Python Weekly, PyCoders, and awesome lists |
| [`nexus`](skills/nexus/SKILL.md) | HUMMBL | Apache-2.0 | Canonical-surface scanner for governance and operator context before `/apex` plans. |
| [`nist-map`](skills/nist-map/SKILL.md) | HUMMBL | Apache-2.0 | Map controls to NIST CSF 2.0 and AI RMF categories with gap analysis |
| [`note`](skills/note/SKILL.md) | HUMMBL | Apache-2.0 | Ultra-fast thought capture to the Cognitive Ledger. One command, no ceremony. Tags route the... |
| [`novelty-quest`](skills/novelty-quest/SKILL.md) | HUMMBL | Apache-2.0 | Generate novel hypotheses, cross-domain analogies, and contrarian claims that don't fit any ... |
| [`novelty-surge`](skills/novelty-surge/SKILL.md) | HUMMBL | Apache-2.0 | Bounded external intelligence sweep (Intel Surge) feeding divergent hypothesis generation (N... |
| [`nsight-frame-profiler`](skills/nsight-frame-profiler/SKILL.md) | HUMMBL | Apache-2.0 | Profiles D3D12/Vulkan/CUDA executables using NVIDIA Nsight CLI (nsys/ncu), isolates GPU vs C... |
| [`nv-generate-ct-rflow`](skills/nv-generate-ct-rflow/SKILL.md) | HUMMBL | Apache-2.0 | Used for generating synthetic CT volumes and masks with NV-Generate-CTMR rflow-ct. Not for p... |
| [`nv-generate-mr`](skills/nv-generate-mr/SKILL.md) | HUMMBL | Apache-2.0 | Used for generating synthetic body MRI volumes with NV-Generate-CTMR rflow-mr. Not for paire... |
| [`nv-generate-mr-brain`](skills/nv-generate-mr-brain/SKILL.md) | HUMMBL | Apache-2.0 | Used for generating synthetic T1, T2, FLAIR, SWI, or MRA brain MRI volumes with NV-Generate-... |
| [`nv-generate-mr-brain-finetune`](skills/nv-generate-mr-brain-finetune/SKILL.md) | HUMMBL | Apache-2.0 | Used for finetuning NV-Generate-CTMR MR-Brain v1 for T1, T2, FLAIR, SWI, or MRA data from a ... |
| [`nv-generate-vae-finetune`](skills/nv-generate-vae-finetune/SKILL.md) | HUMMBL | Apache-2.0 | Used for finetuning the NV-Generate-CTMR MAISI VAE from CT/MRI NIfTI datalists. Not for clin... |
| [`nv-reason-cxr`](skills/nv-reason-cxr/SKILL.md) | HUMMBL | Apache-2.0 | Used for command-shape or live NV-Reason-CXR chest X-ray reasoning smoke tests. Not for diag... |
| [`nv-segment-ct`](skills/nv-segment-ct/SKILL.md) | HUMMBL | Apache-2.0 | Used for running NV-Segment-CT VISTA3D on CT NIfTI volumes and recording label-map evidence. |
| [`nv-segment-ct-finetune`](skills/nv-segment-ct-finetune/SKILL.md) | HUMMBL | Apache-2.0 | Runs standard or fixed-channel softmax finetuning of NV-Segment-CT VISTA3D on CT NIfTI image... |
| [`nv-segment-ctmr`](skills/nv-segment-ctmr/SKILL.md) | HUMMBL | Apache-2.0 | Used for running NV-Segment-CTMR on CT or MRI NIfTI volumes and recording label-map evidence... |
| [`nvflare-autofl`](skills/nvflare-autofl/SKILL.md) | HUMMBL | Apache-2.0 | "Use for agent-assisted Auto-FL optimization of an existing NVFLARE job in simulation, POC, ... |
| [`nvflare-autofl-report`](skills/nvflare-autofl-report/SKILL.md) | HUMMBL | Apache-2.0 | "Generate a reproducible final report, literature-outcome synthesis, JSON summary, and refre... |
| [`nvflare-convert-huggingface`](skills/nvflare-convert-huggingface/SKILL.md) | HUMMBL | Apache-2.0 | "Convert existing Hugging Face Transformers Trainer or TRL SFTTrainer training code into an ... |
| [`nvflare-convert-lightning`](skills/nvflare-convert-lightning/SKILL.md) | HUMMBL | Apache-2.0 | "Convert existing PyTorch Lightning training code into an NVFLARE federated job using the Li... |
| [`nvflare-convert-pytorch`](skills/nvflare-convert-pytorch/SKILL.md) | HUMMBL | Apache-2.0 | "Convert existing plain or manual PyTorch training code into an NVFLARE federated job using ... |
| [`nvflare-diagnose-job`](skills/nvflare-diagnose-job/SKILL.md) | HUMMBL | Apache-2.0 | "Use when the user asks why a reported NVFLARE job failure signal occurred: the job failed, ... |
| [`nvflare-fed-stats`](skills/nvflare-fed-stats/SKILL.md) | HUMMBL | Apache-2.0 | "Compute federated statistics over tabular data (count, sum, mean, stddev, var, histogram, q... |
| [`nvflare-orient`](skills/nvflare-orient/SKILL.md) | HUMMBL | Apache-2.0 | "Route open-ended NVFLARE advice and only conversion requests whose preliminary source inspe... |
| [`nvflare-shared`](skills/nvflare-shared/SKILL.md) | HUMMBL | Apache-2.0 | Internal NVFLARE conversion references and templates. Use only when another NVFLARE skill di... |
| [`nvidia-skill-finder`](skills/nvidia-skill-finder/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Use for NVIDIA-related requests where an NVIDIA skill might help, even if the user did not a... |
| [`observability-audit`](skills/observability-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit logging, metrics, and alerting coverage across services. |
| [`observability-setup`](skills/observability-setup/SKILL.md) | HUMMBL | Apache-2.0 | Instrument a service with distributed tracing, metrics, and structured logging. Set up OpenT... |
| [`offer-letter`](skills/offer-letter/SKILL.md) | HUMMBL | Apache-2.0 | Draft an employment offer letter. Covers title, comp, equity, start date, benefits, at-will ... |
| [`okr`](skills/okr/SKILL.md) | HUMMBL | Apache-2.0 | Set, track, and score OKRs with progress tracking |
| [`omni-meta-aggregator-discovery`](skills/omni-meta-aggregator-discovery/SKILL.md) | HUMMBL | Apache-2.0 | Phase -1 Discovery skill for the HUMMBL Omni-Meta Sovereign Mesh (HUAOMP ⊗ MTSMU). Formalize... |
| [`omni-researcher`](skills/omni-researcher/SKILL.md) | HUMMBL | Apache-2.0 | Adaptive and dynamic agentic researcher swarm using poly-agent. Classifies input, dynamicall... |
| [`omniverse-cad-to-simready`](skills/omniverse-cad-to-simready/SKILL.md) | HUMMBL | Apache-2.0 | "Coordinate the end-to-end CAD/source-asset to SimReady workflow. Use for broad requests suc... |
| [`omniverse-realtime-viewer`](skills/omniverse-realtime-viewer/SKILL.md) | HUMMBL | Apache-2.0 | "Use as the top-level router for Omniverse Realtime Viewer USD app requests and focused view... |
| [`omniverse-usd-performance-tuning`](skills/omniverse-usd-performance-tuning/SKILL.md) | HUMMBL | Apache-2.0 | "Top-level workflow skill for USD performance diagnosis and optimization. Handles slow loadi... |
| [`on-call`](skills/on-call/SKILL.md) | HUMMBL | Apache-2.0 | On-call rotation setup with schedule, runbooks, and handoff notes |
| [`onboard-client`](skills/onboard-client/SKILL.md) | HUMMBL | Apache-2.0 | Client onboarding — environment setup, access provisioning, kickoff agenda, deliverable expe... |
| [`onboard-dev`](skills/onboard-dev/SKILL.md) | HUMMBL | Apache-2.0 | Generate dev environment setup guide from repo analysis |
| [`onboard-human`](skills/onboard-human/SKILL.md) | HUMMBL | Apache-2.0 | Onboard a new human team member -- dev environment, access, context, first tasks. |
| [`one-pager`](skills/one-pager/SKILL.md) | HUMMBL | Apache-2.0 | One-page brief synthesized from scratch. Headline, problem, solution, why now, proof, ask. E... |
| [`opencode-forensic-brief`](skills/opencode-forensic-brief/SKILL.md) | HUMMBL | Apache-2.0 | Generates a concise forensic briefing for OpenCode (or any downstream auditor) from a comple... |
| [`openfda-database`](skills/openfda-database/SKILL.md) | HUMMBL | Apache-2.0 | Query, search, and download data from the openFDA API for drugs, devices, foods, tobacco, co... |
| [`opentargets-database`](skills/opentargets-database/SKILL.md) | HUMMBL | Apache-2.0 | Query Open Targets Platform for target-disease associations, drug target discovery, tractabi... |
| [`operating-agreement`](skills/operating-agreement/SKILL.md) | HUMMBL | Apache-2.0 | Draft a complete LLC Operating Agreement. Single-member or multi-member. Georgia default, mu... |
| [`operator-discovery`](skills/operator-discovery/SKILL.md) | HUMMBL | Apache-2.0 | Discover the human operator who owns and controls the agent fleet — their cognitive profile,... |
| [`operator-execute`](skills/operator-execute/SKILL.md) | HUMMBL | Apache-2.0 | Walk operator through executing one specific operator-owned item (NOW or SCHEDULED). Capture... |
| [`operator-mode`](skills/operator-mode/SKILL.md) | HUMMBL | Apache-2.0 | Constitutional Tier 0 — human authority is supreme. All agent authority is delegated, not in... |
| [`operator-queue`](skills/operator-queue/SKILL.md) | HUMMBL | Apache-2.0 | Add to or list the operator-owned work queue. Items the agent is structurally blocked from d... |
| [`operator-status`](skills/operator-status/SKILL.md) | HUMMBL | Apache-2.0 | Read-only snapshot of operator-owned queue. State counts, this-week SCHEDULED, GATED items w... |
| [`operator-triage`](skills/operator-triage/SKILL.md) | HUMMBL | Apache-2.0 | Walk operator through QUEUED items, assign state (NOW/SCHEDULED/GATED/CLARIFY/DEFERRED/DROPP... |
| [`ops`](skills/ops/SKILL.md) | HUMMBL | Apache-2.0 | Operations surge mode — health-first, diagnose-then-fix, bus-visible at every state change. ... |
| [`ops-gameboard`](skills/ops-gameboard/SKILL.md) | HUMMBL | Apache-2.0 | Label, categorize, and produce an actionable gameboard view of open issues, PRs, and branch ... |
| [`org-mutation-precheck`](skills/org-mutation-precheck/SKILL.md) | HUMMBL | Apache-2.0 | Pre-check branch protection and signing requirements before bulk API mutations across repos.... |
| [`org-pr-board-scan`](skills/org-pr-board-scan/SKILL.md) | HUMMBL | Apache-2.0 | Cross-repo inventory of every open PR in the org — grouped by repo/author, sized by addition... |
| [`orphan-scan`](skills/orphan-scan/SKILL.md) | HUMMBL | Apache-2.0 | Detect orphan files in any directory that maintains an index — files exist on disk but no in... |
| [`orthogonal-check`](skills/orthogonal-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify that system components vary independently -- no hidden coupling or unintended correla... |
| [`oss-graduation`](skills/oss-graduation/SKILL.md) | HUMMBL | Apache-2.0 | Checklist and gate for graduating a local HUMMBL package to the hummbl-io/oss monorepo for p... |
| [`oss-health`](skills/oss-health/SKILL.md) | HUMMBL | Apache-2.0 | Assess open source project health -- contributors, commit frequency, issue response time, bu... |
| [`outreach-strategy`](skills/outreach-strategy/SKILL.md) | HUMMBL | Apache-2.0 | Build a 30/60/90-day outreach strategy for a segment — channel selection, message architectu... |
| [`overengineering-audit`](skills/overengineering-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit a codebase or file path for architectural over-engineering, deep indirection, redundan... |
| [`paidf-augmentation`](skills/paidf-augmentation/SKILL.md) | HUMMBL | Apache-2.0 | Use when authoring or validating PAIDF augmentation YAML configs, or running remote Cosmos T... |
| [`paidf-auto-labeling`](skills/paidf-auto-labeling/SKILL.md) | NVIDIA <opensource@nv... | Apache-2.0 | Use when a user needs to get started with PAIDF Auto-Labeling, plan a scenario, run or debug... |
| [`paidf-curation-and-retrieval`](skills/paidf-curation-and-retrieval/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Use when operating PAIDF Curation and Retrieval or NVIDIA Cosmos Curator pipelines (split, f... |
| [`paidf-orchestration-setup`](skills/paidf-orchestration-setup/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Audit, prepare, and deploy PAIDF Orchestration on a Kubernetes GPU cluster - single-GPU H100... |
| [`paidf-orchestration-write-dag`](skills/paidf-orchestration-write-dag/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Use when a user describes a custom PAIDF Orchestration pipeline — a specific ordered combina... |
| [`pair-mode`](skills/pair-mode/SKILL.md) | HUMMBL | Apache-2.0 | Structured pair programming with driver/navigator roles, rotation timer, shared context note... |
| [`paper`](skills/paper/SKILL.md) | HUMMBL | Apache-2.0 | Work with research papers and TeX documents -- read, edit, compile, review. |
| [`paper-chat`](skills/paper-chat/SKILL.md) | HUMMBL | Apache-2.0 | Interactive CLI to talk to a PDF using long-context models, with automatic Cognitive Ledger ... |
| [`paper-review`](skills/paper-review/SKILL.md) | HUMMBL | Apache-2.0 | Structured review of research papers — methodology, findings, relevance, limitations |
| [`paranoid`](skills/paranoid/SKILL.md) | HUMMBL | MIT | Defensive coding mode. Guard every input. Assert every assumption. Handle every error specif... |
| [`partnership-brief`](skills/partnership-brief/SKILL.md) | HUMMBL | Apache-2.0 | Build a one-pager partnership brief for a channel, integration, or co-sell conversation. Cov... |
| [`pattern-tile`](skills/pattern-tile/SKILL.md) | HUMMBL | Apache-2.0 | Identify repeating patterns in code/architecture and extract reusable templates. Maps to CO11. |
| [`payment-track`](skills/payment-track/SKILL.md) | HUMMBL | Apache-2.0 | Track invoice payments, aging, outstanding balances, and payment history per client |
| [`pdb-database`](skills/pdb-database/SKILL.md) | HUMMBL | Apache-2.0 | Use when you want to search for or download experimentally-determined 3D structures for biom... |
| [`pdf`](skills/pdf/SKILL.md) | HUMMBL | Apache-2.0 | "Read, extract, merge, split, rotate, watermark, create, fill, secure, OCR, or convert PDF f... |
| [`performance-review`](skills/performance-review/SKILL.md) | HUMMBL | Apache-2.0 | Draft a performance review with competency ratings, narrative, and development plan. Calibra... |
| [`pet`](skills/pet/SKILL.md) | HUMMBL | Apache-2.0 | Governed digital companion — a small ASCII pet that adapts to your check-ins and (optionally... |
| [`physical-ai-defect-image-generation`](skills/physical-ai-defect-image-generation/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Use when the user wants to orchestrate defect image generation with NVIDIA Cosmos AnomalyGen... |
| [`physical-ai-event-video-generation`](skills/physical-ai-event-video-generation/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Run the PAIDF Orchestration Event Video Generation DAG on Kubernetes - image-to-video anomal... |
| [`physical-ai-image-attribute-augmentation`](skills/physical-ai-image-attribute-augmentation/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Run the PAIDF Orchestration Image Attribute Augmentation DAG on Kubernetes - person-crop clo... |
| [`physical-ai-infrastructure-setup-and-resilient-scaling`](skills/physical-ai-infrastructure-setup-and-resilient-scaling/SKILL.md) | HUMMBL | Apache-2.0 | Use when the user wants to set up, scale, validate, or harden NVIDIA physical AI infrastruct... |
| [`physical-ai-neural-reconstruction`](skills/physical-ai-neural-reconstruction/SKILL.md) | HUMMBL | Apache-2.0 | "Router for NVIDIA NuRec/NRE: USDZ rendering, NCore conversion, 3DGS, gRPC sensor sim, carli... |
| [`physical-ai-video-data-augmentation`](skills/physical-ai-video-data-augmentation/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Use when running video data augmentation and auto-labeling workflows on OSMO: flow selection... |
| [`physicsnemo-discover`](skills/physicsnemo-discover/SKILL.md) | HUMMBL | Apache-2.0 | Official NVIDIA-authored guidance for navigating PhysicsNeMo — pick the model, datapipe, or ... |
| [`physicsnemo-shard-tensor`](skills/physicsnemo-shard-tensor/SKILL.md) | HUMMBL | Apache-2.0 | Official NVIDIA-authored guidance for PhysicsNeMo ShardTensor domain parallelism — integrate... |
| [`pii-discover`](skills/pii-discover/SKILL.md) | HUMMBL | Apache-2.0 | Discover PII in datasets, logs, and code before processing. Scans for common PII patterns (S... |
| [`pin-code-resy`](skills/pin-code-resy/SKILL.md) | HUMMBL | Apache-2.0 | "Adversarial semantic wargame. The Operator and Agent battle to deconstruct a fuzzy concept ... |
| [`pipeline-lineage-map`](skills/pipeline-lineage-map/SKILL.md) | HUMMBL | Apache-2.0 | Map data lineage from source through transforms to sink. Builds a dependency graph of data f... |
| [`pipeline-review`](skills/pipeline-review/SKILL.md) | HUMMBL | Apache-2.0 | Full sales funnel snapshot. Stage counts, conversion rates, stale contacts, action items. We... |
| [`pitch`](skills/pitch/SKILL.md) | HUMMBL | Apache-2.0 | Draft and refine pitch materials -- elevator pitch, one-pager, deck outline, demo script. |
| [`pivot-table`](skills/pivot-table/SKILL.md) | HUMMBL | Apache-2.0 | Aggregate tabular data with groupby, sum, avg, count, and pivot operations |
| [`plaidteam`](skills/plaidteam/SKILL.md) | HUMMBL | Apache-2.0 | Multi-team coordinator -- coordinates simultaneous exercises across multiple color teams. Th... |
| [`plan`](skills/plan/SKILL.md) | HUMMBL | Apache-2.0 | Structured planning for multi-item task lists. Produces a tiered, actionable plan that separ... |
| [`plausibility-audit`](skills/plausibility-audit/SKILL.md) | HUMMBL | Apache-2.0 | Adversarial self-audit that stress-tests uniqueness and capability claims against the extern... |
| [`policy-draft`](skills/policy-draft/SKILL.md) | HUMMBL | Apache-2.0 | Draft internal policies -- AI acceptable use, data handling, incident response, access control |
| [`poly-agent`](skills/poly-agent/SKILL.md) | HUMMBL | Apache-2.0 | Manifest-driven N-agent dispatch (N≥5) — declare agents, topology, sync points, context budg... |
| [`polycube-lab`](skills/polycube-lab/SKILL.md) | HUMMBL | Apache-2.0 | "Compose, decompose, validate, and audit face-connected lattice polycubes, including labeled... |
| [`pong-loop`](skills/pong-loop/SKILL.md) | HUMMBL | Apache-2.0 | Two-paddle build loop. caveman-ponytail (minimal code, YAGNI) and caveman-bespoke (anticipat... |
| [`ponytail`](skills/ponytail/SKILL.md) | HUMMBL | MIT | Forces the laziest solution that actually works: simplest, shortest, most minimal. Channels ... |
| [`port-map`](skills/port-map/SKILL.md) | HUMMBL | Apache-2.0 | Map listening ports to services, detect conflicts, verify expected bindings |
| [`portfolio-optimization`](skills/portfolio-optimization/SKILL.md) | HUMMBL | Apache-2.0 | Use when a user asks to build, optimize, backtest, rebalance, or analyze a stock portfolio w... |
| [`portfolio-score`](skills/portfolio-score/SKILL.md) | HUMMBL | Apache-2.0 | Score all repos against Arbiter quality standards — identify which need work before showcasing |
| [`postgresql-optimization`](skills/postgresql-optimization/SKILL.md) | HUMMBL | Apache-2.0 | 'PostgreSQL-specific development assistant focusing on unique PostgreSQL features, advanced ... |
| [`postmortem`](skills/postmortem/SKILL.md) | HUMMBL | Apache-2.0 | Blameless post-incident review with timeline, root cause, contributing factors, and action i... |
| [`pptx`](skills/pptx/SKILL.md) | HUMMBL | Apache-2.0 | "Create, read, edit, extract, combine, or update PowerPoint presentations. Use whenever a .p... |
| [`pr-scope-check`](skills/pr-scope-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify a PR's body accurately enumerates the files actually changed. Catches body-undercount... |
| [`pr-summary`](skills/pr-summary/SKILL.md) | HUMMBL | Apache-2.0 | Generate PR title + body from branch diff and create the PR. |
| [`prd-write`](skills/prd-write/SKILL.md) | HUMMBL | Apache-2.0 | Write a Product Requirements Document from a brief. Structures problem, users, goals, scope,... |
| [`pre-mortem`](skills/pre-mortem/SKILL.md) | HUMMBL | Apache-2.0 | Identify fragile code and write realistic failure scenarios before they happen. |
| [`predictingthepast`](skills/predictingthepast/SKILL.md) | HUMMBL | Apache-2.0 | Ancient text restoration, attribution, dating, contextualization, and embedding via Aeneas (... |
| [`preprint-scan`](skills/preprint-scan/SKILL.md) | HUMMBL | Apache-2.0 | Audit sources before or after ingestion — flag preprints, check peer-review status, detect r... |
| [`press-release`](skills/press-release/SKILL.md) | HUMMBL | Apache-2.0 | Amazon-style working-backwards future press release. Write the headline 6 months from now, t... |
| [`pricing-model`](skills/pricing-model/SKILL.md) | HUMMBL | Apache-2.0 | Model pricing strategies (cost-plus, value-based, competitive) with competitor benchmarks |
| [`principal-engineer`](skills/principal-engineer/SKILL.md) | HUMMBL | Apache-2.0 | Principal Engineer persona for swarm health, orchestration resilience, and fleet momentum. M... |
| [`prisma-database-setup`](skills/prisma-database-setup/SKILL.md) | HUMMBL | MIT | Guides for configuring Prisma with different database providers (PostgreSQL, MySQL, SQLite, ... |
| [`privacy-audit`](skills/privacy-audit/SKILL.md) | HUMMBL | Apache-2.0 | State privacy law scan (CCPA, CTDPA, VCDPA, etc.) for data handling practices |
| [`privacy-policy`](skills/privacy-policy/SKILL.md) | HUMMBL | Apache-2.0 | Draft a Privacy Policy compliant with CCPA, GDPR (basic), and state privacy laws. Covers dat... |
| [`product-experience-review`](skills/product-experience-review/SKILL.md) | HUMMBL | Apache-2.0 | Combined UI/UX release-gate review for product surfaces. Use when deciding whether a feature... |
| [`prompt-lab`](skills/prompt-lab/SKILL.md) | HUMMBL | Apache-2.0 | Version, test, and compare prompts across models -- A/B testing for prompt engineering. |
| [`prompt-regression`](skills/prompt-regression/SKILL.md) | HUMMBL | Apache-2.0 | Detect when prompt or system prompt changes break expected outputs by running saved test cases |
| [`proof-check`](skills/proof-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify claims by contradiction or contrapositive -- stress-test assertions in code, docs, an... |
| [`proof-pack`](skills/proof-pack/SKILL.md) | HUMMBL | Apache-2.0 | Bundle resume, case study, demo recording, and evidence into a job application submission pack |
| [`proposal-internal`](skills/proposal-internal/SKILL.md) | HUMMBL | Apache-2.0 | Draft internal technical proposals with a falsifiable thesis, evidence-backed recommendation... |
| [`proposal-write`](skills/proposal-write/SKILL.md) | HUMMBL | Apache-2.0 | Generate client proposal from scope, timeline, rate, and deliverables. |
| [`protein-sequence-msa`](skills/protein-sequence-msa/SKILL.md) | HUMMBL | Apache-2.0 | Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need t... |
| [`protein-sequence-similarity-search`](skills/protein-sequence-similarity-search/SKILL.md) | HUMMBL | Apache-2.0 | Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehens... |
| [`pubchem-database`](skills/pubchem-database/SKILL.md) | HUMMBL | Apache-2.0 | Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searc... |
| [`pubmed-database`](skills/pubmed-database/SKILL.md) | HUMMBL | Apache-2.0 | Search PubMed for scientific literature, including published clinical trials. Fetch abstract... |
| [`purpleteam`](skills/purpleteam/SKILL.md) | HUMMBL | Apache-2.0 | Synthesis of /redteam + /blueteam in one pass. For each attack vector, surface the defense; ... |
| [`pymol`](skills/pymol/SKILL.md) | HUMMBL | Apache-2.0 | Visualize, analyze, and render protein and molecular structures using PyMOL. Use when the us... |
| [`pypi-publish`](skills/pypi-publish/SKILL.md) | HUMMBL | Apache-2.0 | Publish Python package to PyPI with version bump, changelog, and git tag. |
| [`python-upgrade`](skills/python-upgrade/SKILL.md) | HUMMBL | Apache-2.0 | Check codebase compatibility with target Python version |
| [`quad-agent`](skills/quad-agent/SKILL.md) | HUMMBL | Apache-2.0 | Four-agent workflow — full Research→Design→Implement→Validate pipeline or parallel investiga... |
| [`quickgo-database`](skills/quickgo-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this when you need ... |
| [`quinquepartite-watch`](skills/quinquepartite-watch/SKILL.md) | HUMMBL | Apache-2.0 | Continuous five-surface autonomous surveillance orchestrator governing Coordination Bus, Rem... |
| [`quiz`](skills/quiz/SKILL.md) | HUMMBL | Apache-2.0 | Interactive quiz from flashcards or topic area with scoring and review |
| [`radix`](skills/radix/SKILL.md) | HUMMBL | Apache-2.0 | Canonical Radix & Positional Numeral Notation Registry and Transcoding Engine. Map 43 known ... |
| [`rag-blueprint`](skills/rag-blueprint/SKILL.md) | HUMMBL | Apache-2.0 | "NVIDIA RAG Blueprint — deploy, configure, troubleshoot, and manage. Handles any RAG action:... |
| [`rag-chunk`](skills/rag-chunk/SKILL.md) | HUMMBL | Apache-2.0 | Optimize document chunking strategies (fixed/semantic/sentence/recursive) for RAG pipelines |
| [`rag-eval`](skills/rag-eval/SKILL.md) | HUMMBL | Apache-2.0 | Filesystem RAG benchmarks: corpus/, train.json, evaluate_rag.py (RAGAS quality). Not for pro... |
| [`rag-evaluate`](skills/rag-evaluate/SKILL.md) | HUMMBL | Apache-2.0 | Evaluate RAG pipeline quality with retrieval accuracy, faithfulness, answer relevance, and c... |
| [`rag-hybrid`](skills/rag-hybrid/SKILL.md) | HUMMBL | Apache-2.0 | Combine keyword (BM25) and semantic (vector) search in hybrid RAG pipelines with reciprocal ... |
| [`rag-perf`](skills/rag-perf/SKILL.md) | HUMMBL | Apache-2.0 | Performance benchmarking for a deployed NVIDIA RAG Blueprint server: profiling pass + aiperf... |
| [`rag-pipeline`](skills/rag-pipeline/SKILL.md) | HUMMBL | Apache-2.0 | Design and test RAG pipelines -- chunking strategy, embedding selection, retrieval tuning, a... |
| [`rag-rerank`](skills/rag-rerank/SKILL.md) | HUMMBL | Apache-2.0 | Rerank retrieved documents with cross-encoders or LLM-based reranking for improved precision |
| [`rate-limit-design`](skills/rate-limit-design/SKILL.md) | HUMMBL | Apache-2.0 | Design rate limiting strategy for APIs with algorithm selection and code generation |
| [`reactome-database`](skills/reactome-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the Reactome database (Analysis and Content Services). Use when the user asks about pa... |
| [`readability`](skills/readability/SKILL.md) | HUMMBL | Apache-2.0 | Score content readability using Flesch-Kincaid and Gunning Fog metrics |
| [`readme-gen`](skills/readme-gen/SKILL.md) | HUMMBL | Apache-2.0 | Generate or refresh README.md from code structure, imports, and conventions |
| [`reasoning-router`](skills/reasoning-router/SKILL.md) | HUMMBL | Apache-2.0 | Route reasoning tasks across free model providers (Cloudflare, Groq, Gemini, GitHub Models, ... |
| [`reasoning-trace-hummbl`](skills/reasoning-trace-hummbl/SKILL.md) | HUMMBL | Apache-2.0 | Produces and consumes the native HUMMBL ReasoningTrace JSON format (ReasoningStep → Reasonin... |
| [`red-team-mode`](skills/red-team-mode/SKILL.md) | HUMMBL | Apache-2.0 | Adversarial analysis — find how it breaks, not how it works. Every finding has severity and ... |
| [`redteam`](skills/redteam/SKILL.md) | HUMMBL | Apache-2.0 | Adversarial testing for agent systems — LLM agents (jailbreak/injection/escape/exfil) AND no... |
| [`reframe`](skills/reframe/SKILL.md) | HUMMBL | Apache-2.0 | Cognitive reframe for any problem statement or belief. Returns 5 reframes across different l... |
| [`regex-lab`](skills/regex-lab/SKILL.md) | HUMMBL | Apache-2.0 | Build, test, and explain regular expressions with sample matching, edge case generation, and... |
| [`regression-check`](skills/regression-check/SKILL.md) | HUMMBL | Apache-2.0 | Identify what could break from a code change by tracing callers, dependents, and downstream ... |
| [`release-announce`](skills/release-announce/SKILL.md) | HUMMBL | Apache-2.0 | Draft release announcement across channels -- GitHub release notes, blog post, social media,... |
| [`release-manager`](skills/release-manager/SKILL.md) | HUMMBL | Apache-2.0 | Plan and coordinate release promotion from merge-ready change to deployed, verified, and rec... |
| [`release-notes`](skills/release-notes/SKILL.md) | HUMMBL | Apache-2.0 | Release prep -- changelog, breaking changes, migration notes. |
| [`remediation-plan`](skills/remediation-plan/SKILL.md) | HUMMBL | Apache-2.0 | Generate prioritized remediation plan from gap analysis with effort estimates and milestones. |
| [`renewal-check`](skills/renewal-check/SKILL.md) | HUMMBL | Apache-2.0 | Flag engagements approaching end date and draft renewal or upsell proposal email |
| [`repo-init-secured`](skills/repo-init-secured/SKILL.md) | HUMMBL | Apache-2.0 | "Initialize repos with redteam-before-ship: propose scaffold, threat-model the environment, ... |
| [`repo-scaffold`](skills/repo-scaffold/SKILL.md) | HUMMBL | Apache-2.0 | Initialize new repo with your conventions and standard tooling |
| [`repo-sync`](skills/repo-sync/SKILL.md) | HUMMBL | Apache-2.0 | Check status across all $PROJECTS_DIR/ repos for dirty state, remote sync, and CI |
| [`report-card`](skills/report-card/SKILL.md) | HUMMBL | Apache-2.0 | Force a rigorous, evidence-backed self-assessment after completing a body of work. The agent... |
| [`reproducibility-check`](skills/reproducibility-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify research reproducibility - check code availability, data availability, environment pi... |
| [`research`](skills/research/SKILL.md) | HUMMBL | Apache-2.0 | Intelligence surge mode — sweep, ingest, synthesize, dispatch. For deep research sessions th... |
| [`research-digest`](skills/research-digest/SKILL.md) | HUMMBL | Apache-2.0 | Summarize recent research findings from Open Brain, autoresearch pipeline, and docs/research/. |
| [`research-ingest`](skills/research-ingest/SKILL.md) | HUMMBL | Apache-2.0 | Ingest research findings into the knowledge system — Cognitive Ledger, evidence docs, Open B... |
| [`research-pipeline`](skills/research-pipeline/SKILL.md) | HUMMBL | Apache-2.0 | Explicit 5-stage research orchestrator (Internal Sweep→External Sweep→Gate→Ingest→Dispatch) ... |
| [`retrospective`](skills/retrospective/SKILL.md) | HUMMBL | Apache-2.0 | Session or sprint retrospective -- extract learnings, failures, and patterns to compound kno... |
| [`retry-audit`](skills/retry-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit retry logic, backoff strategies, timeouts, and jitter across the codebase |
| [`revenue-forecast`](skills/revenue-forecast/SKILL.md) | HUMMBL | Apache-2.0 | Project revenue from CRM pipeline, conversion rates, and contract values |
| [`review-orchestrator`](skills/review-orchestrator/SKILL.md) | HUMMBL | Apache-2.0 | Govern a remediation or merge-readiness review through explicit stages, proof bundles, and r... |
| [`review-pr`](skills/review-pr/SKILL.md) | HUMMBL | Apache-2.0 | Structured PR review -- fetch diff, run mtsmu-review, check CI, post summary. |
| [`rfc-write`](skills/rfc-write/SKILL.md) | HUMMBL | Apache-2.0 | Write Request for Comments documents for technical proposals with problem statement, alterna... |
| [`rice-prioritize`](skills/rice-prioritize/SKILL.md) | HUMMBL | Apache-2.0 | RICE scoring (Reach, Impact, Confidence, Effort) for feature and task prioritization. |
| [`risk-register`](skills/risk-register/SKILL.md) | HUMMBL | Apache-2.0 | Maintain and score a risk register with likelihood, impact, mitigation status, and trending |
| [`role-discovery`](skills/role-discovery/SKILL.md) | HUMMBL | Apache-2.0 | Discover what ROLE the agent plays in relation to the humans it serves — tool, colleague, su... |
| [`rollback`](skills/rollback/SKILL.md) | HUMMBL | Apache-2.0 | CD recovery skill for reverting a bad release or deployment with health verification, rollba... |
| [`rollback-cd`](skills/rollback-cd/SKILL.md) | HUMMBL | Apache-2.0 | CD recovery skill for reverting a bad release or deployment with health verification, rollba... |
| [`root-cause`](skills/root-cause/SKILL.md) | HUMMBL | Apache-2.0 | Perform evidence-backed 5-why analysis for test, CI, service, code, workflow, or process fai... |
| [`routing-evolve`](skills/routing-evolve/SKILL.md) | HUMMBL | Apache-2.0 | Cross-reference skill-routing.md against telemetry — find dead triggers, missing triggers, o... |
| [`routing-gap`](skills/routing-gap/SKILL.md) | HUMMBL | Apache-2.0 | Find skills with no routing entries in skill-routing.md, and routing entries pointing to ski... |
| [`rsi-dashboard`](skills/rsi-dashboard/SKILL.md) | HUMMBL | Apache-2.0 | Recursive self-improvement metrics and system compounding signals. |
| [`rtk`](skills/rtk/SKILL.md) | HUMMBL | Apache-2.0 | CLI proxy that compresses bash command outputs before agent reads them. Single Rust binary, ... |
| [`rtvi-cv-customize-model`](skills/rtvi-cv-customize-model/SKILL.md) | HUMMBL | Apache-2.0 | How to swap the DeepStream CV detection model in the VSS Alerts Blueprint verification (2d_c... |
| [`rtvi-cv-scaffold-vss-service`](skills/rtvi-cv-scaffold-vss-service/SKILL.md) | HUMMBL | "NVIDIA Proprietary" | Scaffold a standalone RTVI CV microservice that plugs into VSS Search and Alerts profiles vi... |
| [`rtvi-vlm-customize-model`](skills/rtvi-vlm-customize-model/SKILL.md) | HUMMBL | Apache-2.0 | How to swap the VLM in the VSS Alerts Blueprint — covers RTVI-VLM microservice deployment me... |
| [`rtx-remix-modding`](skills/rtx-remix-modding/SKILL.md) | HUMMBL | Apache-2.0 | Mod or remaster a game with RTX Remix - open and edit projects, swap textures and models. Co... |
| [`rules-evolve`](skills/rules-evolve/SKILL.md) | HUMMBL | Apache-2.0 | Score .claude/rules/ files for relevance, overlap, and context budget cost — archive/compres... |
| [`runbook-test`](skills/runbook-test/SKILL.md) | HUMMBL | Apache-2.0 | Dry-run runbook steps to verify procedures still work — commands exist, paths valid, service... |
| [`runbook-write`](skills/runbook-write/SKILL.md) | HUMMBL | Apache-2.0 | Generate operational runbook from service architecture and incident history |
| [`runway`](skills/runway/SKILL.md) | HUMMBL | Apache-2.0 | Cash runway and cost forecasting from cost-governor data and API spend. |
| [`sandbox-sdk`](skills/sandbox-sdk/SKILL.md) | HUMMBL | Apache-2.0 | "Build Cloudflare Sandbox SDK code-execution apps, code interpreters, CI/CD sandboxes, inter... |
| [`sbom-generate`](skills/sbom-generate/SKILL.md) | HUMMBL | Apache-2.0 | Generate Software Bill of Materials in SPDX or CycloneDX format from project dependencies |
| [`scavenge`](skills/scavenge/SKILL.md) | HUMMBL | Apache-2.0 | "Read a retirement index from apex-nexus and execute scavenger-mode work items in dependency... |
| [`scenario-plan`](skills/scenario-plan/SKILL.md) | HUMMBL | Apache-2.0 | Model best/base/worst financial scenarios with configurable variables and sensitivity analysis |
| [`schema-diff`](skills/schema-diff/SKILL.md) | HUMMBL | Apache-2.0 | "Compare two API or data schema versions and classify changes as breaking or non-breaking. P... |
| [`schema-migrate`](skills/schema-migrate/SKILL.md) | HUMMBL | Apache-2.0 | Generate migration scripts when contract schemas change |
| [`scope-decompose`](skills/scope-decompose/SKILL.md) | HUMMBL | Apache-2.0 | Break an epic or feature into ordered user stories with acceptance criteria. |
| [`screen-reader-test`](skills/screen-reader-test/SKILL.md) | HUMMBL | Apache-2.0 | Test screen reader compatibility and announce accuracy. [Maps to P9.] |
| [`script-existence-check`](skills/script-existence-check/SKILL.md) | HUMMBL | Apache-2.0 | Scan all SKILL.md files for ~/bin/ script references and verify the binaries exist. Catches ... |
| [`script-flag-check`](skills/script-flag-check/SKILL.md) | HUMMBL | Apache-2.0 | Scan SKILL.md files for CLI flag references (--flag) and verify they exist in the referenced... |
| [`secret-scan`](skills/secret-scan/SKILL.md) | HUMMBL | Apache-2.0 | Scan for leaked secrets -- API keys, tokens, credentials. |
| [`security-scan`](skills/security-scan/SKILL.md) | HUMMBL | Apache-2.0 | On-demand Bandit + Semgrep security scan. |
| [`seed-scan`](skills/seed-scan/SKILL.md) | HUMMBL | Apache-2.0 | Python-harness scanner over the same canonical surfaces nexus scans (rules, candidates, arch... |
| [`seed-search`](skills/seed-search/SKILL.md) | HUMMBL | Apache-2.0 | Systematically discover testable seed candidates from playground sessions, bus pain points, ... |
| [`self-discovery`](skills/self-discovery/SKILL.md) | HUMMBL | Apache-2.0 | Teach any AI coding agent or sub-agent profile how to perform structured self-discovery: int... |
| [`self-review`](skills/self-review/SKILL.md) | HUMMBL | Apache-2.0 | Grade Codex's own session, plan, artifact, or workflow performance. Use when the user asks f... |
| [`send-discord`](skills/send-discord/SKILL.md) | HUMMBL | Apache-2.0 | "Send Discord webhook messages through hummbl_governance.gateway.dispatch with named webhook... |
| [`send-email`](skills/send-email/SKILL.md) | HUMMBL | Apache-2.0 | Send email through the Codex Gmail connector by default; legacy direct Gmail API helper rema... |
| [`send-signal`](skills/send-signal/SKILL.md) | HUMMBL | Apache-2.0 | "Send Signal messages through hummbl_governance.gateway.dispatch with circuit-breaker protec... |
| [`send-telegram`](skills/send-telegram/SKILL.md) | HUMMBL | Apache-2.0 | "RETIRED 2026-09-21 — Telegram is not needed. Do not invoke. Tombstone only." |
| [`seo-check`](skills/seo-check/SKILL.md) | HUMMBL | Apache-2.0 | Audit page or README for SEO/GEO/AEO signals including meta, headings, schema, llms.txt |
| [`service-agreement`](skills/service-agreement/SKILL.md) | HUMMBL | Apache-2.0 | Draft a Master Service Agreement (MSA) or standalone Service Agreement. Covers scope, paymen... |
| [`seshat`](skills/seshat/SKILL.md) | HUMMBL | Apache-2.0 | Cross-session sovereign mode — reads all state before acting, orchestration-only, receipts-f... |
| [`session-forensics-batch`](skills/session-forensics-batch/SKILL.md) | HUMMBL | Apache-2.0 | Summarize all agent sessions in a time window (default 48h) with message counts, tool calls,... |
| [`session-forensics-manifest`](skills/session-forensics-manifest/SKILL.md) | HUMMBL | Apache-2.0 | SUPERSEDED — merged into session-forensics skill v0.3.0. Use `session-forensics` with the --... |
| [`session-metrics`](skills/session-metrics/SKILL.md) | HUMMBL | Apache-2.0 | Track token usage, tool calls, agent dispatches, and rate limit hits per session |
| [`session-render`](skills/session-render/SKILL.md) | HUMMBL | Apache-2.0 | Render session research artifacts as a beautiful self-contained HTML dashboard and open in b... |
| [`session-replay`](skills/session-replay/SKILL.md) | HUMMBL | Apache-2.0 | Replay and summarize what happened in a previous session from git log, bus messages, and led... |
| [`ship`](skills/ship/SKILL.md) | HUMMBL | Apache-2.0 | Shipping surge mode — test, scan, PR, merge, tag. Zero manual steps between green tests and ... |
| [`ship-check`](skills/ship-check/SKILL.md) | HUMMBL | Apache-2.0 | Pre-ship checklist -- run before merging or deploying any feature. Chains pre-mortem, test-r... |
| [`signal`](skills/signal/SKILL.md) | HUMMBL | Apache-2.0 | Narrative meta-skill — composes format skills via audience + Gramsci arc + voice. Takes tria... |
| [`signing-in-to-aws`](skills/signing-in-to-aws/SKILL.md) | HUMMBL | Apache-2.0 | Gets AWS credentials for CLI/SDK access via `aws login`. Activates when a developer needs to... |
| [`silverteam`](skills/silverteam/SKILL.md) | HUMMBL | Apache-2.0 | Compliance and audit -- regulatory compliance, audit trail verification, control mapping (NI... |
| [`sim`](skills/sim/SKILL.md) | HUMMBL | Apache-2.0 | "Use Dune Sim for real-time wallet, token, NFT, DeFi, transaction, holder, or stablecoin loo... |
| [`simple-skill-sync`](skills/simple-skill-sync/SKILL.md) | HUMMBL | Apache-2.0 | Plan and safely run registered simple advisory skill adapters with deterministic parsing, me... |
| [`sitrep`](skills/sitrep/SKILL.md) | HUMMBL | Apache-2.0 | Generate a situational report from live system state. READ-ONLY — no writes, no fixes. Trigg... |
| [`sitrep-coordinator`](skills/sitrep-coordinator/SKILL.md) | HUMMBL | Apache-2.0 | Military-style Situation Report (SITREP) generation for multi-agent coordination. Creates st... |
| [`skill-archive`](skills/skill-archive/SKILL.md) | HUMMBL | Apache-2.0 | Move a dormant skill to cold storage. Only after 90d dormancy across ALL runtimes + no routi... |
| [`skill-audit`](skills/skill-audit/SKILL.md) | HUMMBL | Apache-2.0 | Security + epistemic rigor audit of SKILL.md files. Checks secrets, unsafe shell, privacy ga... |
| [`skill-card-generator`](skills/skill-card-generator/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | "Use only to generate or update a governance skill card for a specified existing agent skill... |
| [`skill-collision-detect`](skills/skill-collision-detect/SKILL.md) | HUMMBL | Apache-2.0 | Detect name/description/trigger collisions before a new skill is created. Prevents duplicate... |
| [`skill-create`](skills/skill-create/SKILL.md) | HUMMBL | Apache-2.0 | Guided skill creation -- generates a properly formatted SKILL.md with triggers, chains, and ... |
| [`skill-creator`](skills/skill-creator/SKILL.md) | HUMMBL | Apache-2.0 | "Create, edit, evaluate, benchmark, and optimize agent skills, including trigger description... |
| [`skill-demote`](skills/skill-demote/SKILL.md) | HUMMBL | Apache-2.0 | Demote a skill from a runtime lean set back to skills-full-only (on-demand). Removes the lea... |
| [`skill-dependency-map`](skills/skill-dependency-map/SKILL.md) | HUMMBL | Apache-2.0 | Map which skills chain to which -- the skill dependency graph. Reads SKILL.md Skill Chains s... |
| [`skill-deps`](skills/skill-deps/SKILL.md) | HUMMBL | Apache-2.0 | Check if scripts, references, and assets referenced in SKILL.md actually exist on disk. Catc... |
| [`skill-diff`](skills/skill-diff/SKILL.md) | HUMMBL | Apache-2.0 | Compare two skills side-by-side — frontmatter, body, chains, and referenced files. Use when ... |
| [`skill-evolve`](skills/skill-evolve/SKILL.md) | HUMMBL | Apache-2.0 | Score and rank installed skills using usage telemetry, epistemic rigor, and security posture... |
| [`skill-export`](skills/skill-export/SKILL.md) | HUMMBL | Apache-2.0 | Export skills for other agents -- translate to Codex AGENTS.md, OpenClaw SOUL.md, or portabl... |
| [`skill-merge`](skills/skill-merge/SKILL.md) | HUMMBL | Apache-2.0 | Merge two overlapping skills into one — combine frontmatter, body sections, chains, and bund... |
| [`skill-supersession-check`](skills/skill-supersession-check/SKILL.md) | HUMMBL | Apache-2.0 | 'Scan for skills marked status: superseded and verify their successors exist and no live ref... |
| [`skill-test`](skills/skill-test/SKILL.md) | HUMMBL | Apache-2.0 | Validate skills -- check for broken commands, stale paths, missing tools, format compliance. |
| [`skills-factory`](skills/skills-factory/SKILL.md) | HUMMBL | Apache-2.0 | "Orchestrate the fleet skill lifecycle factory: candidate discovery, HUAOMP+MTSMU assessment... |
| [`skills-fix`](skills/skills-fix/SKILL.md) | HUMMBL | Apache-2.0 | Auto-remediate skill format issues found by /skill-test (dry-run by default; --apply to exec... |
| [`sla-track`](skills/sla-track/SKILL.md) | HUMMBL | Apache-2.0 | Define and monitor SLAs/SLOs/SLIs with burn rate calculation, error budget tracking, and bre... |
| [`slack-gif-creator`](skills/slack-gif-creator/SKILL.md) | HUMMBL | Apache-2.0 | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints... |
| [`slo-define`](skills/slo-define/SKILL.md) | HUMMBL | Apache-2.0 | Define SLOs and SLIs from observed service behavior. Helps establish service-level objective... |
| [`smoke`](skills/smoke/SKILL.md) | HUMMBL | Apache-2.0 | Report availability of the legacy Morning Briefing smoke pipeline without executing it. |
| [`soc2-check`](skills/soc2-check/SKILL.md) | HUMMBL | Apache-2.0 | SOC 2 Type II readiness assessment against trust service criteria |
| [`social-post`](skills/social-post/SKILL.md) | HUMMBL | Apache-2.0 | Draft platform-specific social posts from content with character limits and conventions |
| [`sow-generate`](skills/sow-generate/SKILL.md) | HUMMBL | Apache-2.0 | Generate Statement of Work from proposal with milestones and payment schedule. |
| [`spectrum-wargame`](skills/spectrum-wargame/SKILL.md) | HUMMBL | Apache-2.0 | "Full-spectrum multi-color security wargame orchestrator. Dispatches 3+ color teams (Red, Bl... |
| [`speed-runner`](skills/speed-runner/SKILL.md) | HUMMBL | MIT | Speed-first coding mode. Ship the simplest thing that works. Optimize for time-to-working-co... |
| [`sprint-status`](skills/sprint-status/SKILL.md) | HUMMBL | Apache-2.0 | Sprint health -- focus area, effort, capacity, blocked issues. |
| [`sqlite-database-expert`](skills/sqlite-database-expert/SKILL.md) | HUMMBL | Apache-2.0 | Expert in SQLite embedded database development for Tauri/desktop applications with focus on ... |
| [`sqlite-inspect`](skills/sqlite-inspect/SKILL.md) | HUMMBL | Apache-2.0 | Inspect SQLite databases -- schema, row counts, recent writes, integrity check. |
| [`ssl-check`](skills/ssl-check/SKILL.md) | HUMMBL | Apache-2.0 | Check SSL certificate expiry dates, chain validity, and HSTS headers across domains |
| [`stakeholder-discovery`](skills/stakeholder-discovery/SKILL.md) | HUMMBL | Apache-2.0 | Discover all stakeholders in a decision, project, or system — who has authority, who is affe... |
| [`stakeholder-update`](skills/stakeholder-update/SKILL.md) | HUMMBL | Apache-2.0 | Draft a stakeholder update (investor, board, partner, customer, team). Audience-calibrated r... |
| [`stale-head-check`](skills/stale-head-check/SKILL.md) | HUMMBL | Apache-2.0 | Verify the PR head SHA you reviewed is still the PR head at post/merge time — catches review... |
| [`standup-digest`](skills/standup-digest/SKILL.md) | HUMMBL | Apache-2.0 | Aggregate standups from multiple agents and humans into a single team digest with highlights... |
| [`start-session`](skills/start-session/SKILL.md) | HUMMBL | Apache-2.0 | Disciplined session start. Run at the beginning of any session. Bookend partner to /end-sess... |
| [`stash-audit`](skills/stash-audit/SKILL.md) | HUMMBL | Apache-2.0 | Detect stashes across PROJECTS repos, classify each by contamination risk (stash branch != c... |
| [`stash-manager`](skills/stash-manager/SKILL.md) | HUMMBL | Apache-2.0 | Autonomous stash lifecycle management for agent fleets (detect, classify, extract, park, drop) |
| [`status-page`](skills/status-page/SKILL.md) | HUMMBL | Apache-2.0 | Generate a status page from health probes showing service status and incidents |
| [`stdlib-or-not`](skills/stdlib-or-not/SKILL.md) | HUMMBL | Apache-2.0 | Audit any codebase to classify imports as stdlib vs third-party, with try-wrapped detection ... |
| [`steelman-build`](skills/steelman-build/SKILL.md) | HUMMBL | Apache-2.0 | Build the strongest possible version of an opposing argument. Epistemic tool -- strengthens ... |
| [`story-bible-writer`](skills/story-bible-writer/SKILL.md) | HUMMBL | Apache-2.0 | Write a Higgsfield Global Film Festival story bible — logline, look lock, cast/locations (So... |
| [`story-write`](skills/story-write/SKILL.md) | HUMMBL | Apache-2.0 | Write user stories with acceptance criteria, edge cases, and test scenarios. |
| [`stream-inference`](skills/stream-inference/SKILL.md) | HUMMBL | Apache-2.0 | Stream token-by-token output from Cloudflare Workers AI models. Real-time SSE streaming for ... |
| [`string-database`](skills/string-database/SKILL.md) | HUMMBL | Apache-2.0 | Query the STRING database for protein-protein interactions (PPIs), functional enrichment, an... |
| [`structure-analyzer`](skills/structure-analyzer/SKILL.md) | HUMMBL | Apache-2.0 | "Classify a fleet governance structure against the 10 archetypes from composition-doctrine.m... |
| [`study-plan`](skills/study-plan/SKILL.md) | HUMMBL | Apache-2.0 | Generate structured study plan with spaced repetition schedule |
| [`succession-mode`](skills/succession-mode/SKILL.md) | HUMMBL | Apache-2.0 | Constitutional Tier 5 — what happens when the operator is no longer available. A will, not a... |
| [`supabase-postgres-best-practices`](skills/supabase-postgres-best-practices/SKILL.md) | HUMMBL | MIT | "Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this sk... |
| [`supply-chain-audit`](skills/supply-chain-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit software supply chain including lockfile integrity, typosquatting detection, provenanc... |
| [`surge`](skills/surge/SKILL.md) | HUMMBL | Apache-2.0 | Execution surge mode — act-first, full tool access, maximum throughput. Ship the simplest th... |
| [`survival-mode`](skills/survival-mode/SKILL.md) | HUMMBL | Apache-2.0 | Constitutional Tier 0 — operator existence is the precondition for everything. Always active... |
| [`swarm`](skills/swarm/SKILL.md) | HUMMBL | Apache-2.0 | Fan-out/fan-in orchestration across machines using claude -p over SSH. Dispatch parallel age... |
| [`swarm-collect`](skills/swarm-collect/SKILL.md) | HUMMBL | Apache-2.0 | Collect worktree artifacts from completed swarm agents — copy files, verify tests, batch com... |
| [`swarm-drip-deploy`](skills/swarm-drip-deploy/SKILL.md) | HUMMBL | Apache-2.0 | Formalized drip-deployment strategy for continuous fleet auditing with host-health throttlin... |
| [`swarm-manifest`](skills/swarm-manifest/SKILL.md) | HUMMBL | Apache-2.0 | Generate and validate swarm dispatch manifests — lane allocation, budget estimation, pre-fli... |
| [`swarm-research`](skills/swarm-research/SKILL.md) | HUMMBL | Apache-2.0 | Adaptive swarm research pattern (C+S+G notation). C canaries map territory, S swarm agents v... |
| [`swarm-subagent`](skills/swarm-subagent/SKILL.md) | HUMMBL | Apache-2.0 | Fan-out/fan-in orchestration using your runtime's sub-agent dispatch. Dispatch parallel sub-... |
| [`synthesis-mode`](skills/synthesis-mode/SKILL.md) | HUMMBL | Apache-2.0 | Compress exploration into action — every output is a decision, recommendation, or not-yet. |
| [`system-prompt`](skills/system-prompt/SKILL.md) | HUMMBL | Apache-2.0 | Design, version, and test system prompts for agents, apps, and MCP servers. |
| [`systematic-map`](skills/systematic-map/SKILL.md) | HUMMBL | Apache-2.0 | Systematic evidence mapping - breadth-first evidence inventory across a research question wi... |
| [`tag-release`](skills/tag-release/SKILL.md) | HUMMBL | Apache-2.0 | Create SemVer git tag with release notes and contract baseline validation. |
| [`talk-prep`](skills/talk-prep/SKILL.md) | HUMMBL | Apache-2.0 | Conference talk preparation -- abstract, outline, slide structure, speaker notes, timing |
| [`tao-analyze-changenet-rca`](skills/tao-analyze-changenet-rca/SKILL.md) | HUMMBL | Apache-2.0 | Performs deep Root Cause Analysis (RCA) on NVIDIA TAO Visual ChangeNet classification experi... |
| [`tao-analyze-detection-kpi`](skills/tao-analyze-detection-kpi/SKILL.md) | HUMMBL | Apache-2.0 | Run TAO Data Services KPI analysis for object detection, comparing inference annotations aga... |
| [`tao-analyze-gaps-od-map`](skills/tao-analyze-gaps-od-map/SKILL.md) | HUMMBL | Apache-2.0 | Run TAO Data Services object-detection gap analysis from ground-truth and inference annotati... |
| [`tao-analyze-gaps-visual-changenet`](skills/tao-analyze-gaps-visual-changenet/SKILL.md) | HUMMBL | Apache-2.0 | Performs gap analysis on NVIDIA TAO VCN Classify (Visual Component Net) experiments by invok... |
| [`tao-analyze-gaps-vlm-bcq`](skills/tao-analyze-gaps-vlm-bcq/SKILL.md) | HUMMBL | Apache-2.0 | Extract false-positive and false-negative gaps from VLM binary-classification-question (BCQ,... |
| [`tao-artifacts`](skills/tao-artifacts/SKILL.md) | HUMMBL | Apache-2.0 | The contract home for TAO's SDK-free execution pipeline — authoritative JSON Schemas for the... |
| [`tao-convert-dataset-format`](skills/tao-convert-dataset-format/SKILL.md) | HUMMBL | Apache-2.0 | Run `tao-daft convert` to convert NVIDIA TAO DAFT datasets between supported formats. Do not... |
| [`tao-data-io`](skills/tao-data-io/SKILL.md) | HUMMBL | Apache-2.0 | The data-mover for TAO jobs — decides the storage tier (A pre-positioned mount with zero fet... |
| [`tao-finetune-clip`](skills/tao-finetune-clip/SKILL.md) | HUMMBL | Apache-2.0 | CLIP vision-language model for image-text retrieval, zero-shot classification, embedding ext... |
| [`tao-finetune-cosmos-embed`](skills/tao-finetune-cosmos-embed/SKILL.md) | HUMMBL | Apache-2.0 | Cosmos-Embed1 video-text embedding for text-to-video retrieval, video-to-video search, seman... |
| [`tao-finetune-cosmos-reason`](skills/tao-finetune-cosmos-reason/SKILL.md) | HUMMBL | Apache-2.0 | Shared Cosmos3 frontend that explicitly routes Cosmos Framework and Cosmos-RL, validates run... |
| [`tao-finetune-huggingface-model`](skills/tao-finetune-huggingface-model/SKILL.md) | HUMMBL | Apache-2.0 | Fine-tune any HuggingFace CV / VLM / LLM model on local NVIDIA GPUs inside an NGC PyTorch co... |
| [`tao-finetune-nv-tesseract-ad-diffusion`](skills/tao-finetune-nv-tesseract-ad-diffusion/SKILL.md) | HUMMBL | Apache-2.0 | NV-Tesseract AD Diffusion — diffusion-based anomaly detection and fine-tuning for multivaria... |
| [`tao-finetune-nv-tesseract-forecasting`](skills/tao-finetune-nv-tesseract-forecasting/SKILL.md) | HUMMBL | Apache-2.0 | NV-Tesseract Forecasting — transformer-based multivariate time series forecasting with DARR ... |
| [`tao-finetune-video-clip`](skills/tao-finetune-video-clip/SKILL.md) | HUMMBL | Apache-2.0 | InternVideo2-CLIP L14 (TAO video_clip) for video-text retrieval, zero-shot classification, e... |
| [`tao-generate-image-embeddings`](skills/tao-generate-image-embeddings/SKILL.md) | HUMMBL | Apache-2.0 | Run TAO Data Services image embedding to turn a parquet of image filepaths into an embedding... |
| [`tao-generate-image-grounding`](skills/tao-generate-image-grounding/SKILL.md) | HUMMBL | Apache-2.0 | "Two-step image grounding pipeline: extracts referring expressions from (image, caption) pai... |
| [`tao-generate-referring-expressions`](skills/tao-generate-referring-expressions/SKILL.md) | HUMMBL | Apache-2.0 | "Four-step image referring-expression pipeline: turns images plus KITTI bounding-box labels ... |
| [`tao-generate-video-reasoning-annotations`](skills/tao-generate-video-reasoning-annotations/SKILL.md) | HUMMBL | Apache-2.0 | Multi-step video annotation pipeline that turns raw videos into Chain-of-Thought training da... |
| [`tao-launch-workflow`](skills/tao-launch-workflow/SKILL.md) | HUMMBL | Apache-2.0 | The mandatory pre-launch gate and four-verb execution contract for every TAO workflow or act... |
| [`tao-list-capabilities`](skills/tao-list-capabilities/SKILL.md) | HUMMBL | Apache-2.0 | Answer what the TAO Skill Bank plugin can do by generating the response from packaged applic... |
| [`tao-mine-aoi-images`](skills/tao-mine-aoi-images/SKILL.md) | HUMMBL | Apache-2.0 | Runs the DEFT embed-then-mine workflow for VCN AOI iterations — embeds the gap-analysis targ... |
| [`tao-mine-nearest-neighbors`](skills/tao-mine-nearest-neighbors/SKILL.md) | HUMMBL | Apache-2.0 | Run TAO Data Services TMM nearest-neighbor mining from embedding parquet files. Use when a w... |
| [`tao-mine-od-images`](skills/tao-mine-od-images/SKILL.md) | HUMMBL | Apache-2.0 | Run TAO Data Services TMM unique-neighbor matching mining from embedding parquet files for o... |
| [`tao-port-huggingface-model`](skills/tao-port-huggingface-model/SKILL.md) | HUMMBL | Apache-2.0 | Integrate a HuggingFace Computer Vision model into the NVIDIA TAO Toolkit ecosystem (tao-cor... |
| [`tao-route-visual-changenet-samples`](skills/tao-route-visual-changenet-samples/SKILL.md) | HUMMBL | Apache-2.0 | Routes the weakest VCN samples (output of `tao-analyze-gaps-visual-changenet`) into per-augm... |
| [`tao-run-automl`](skills/tao-run-automl/SKILL.md) | HUMMBL | Apache-2.0 | Run container-backed AutoML / hyperparameter optimization (HPO) for NVIDIA TAO networks usin... |
| [`tao-run-automl-deft-pipeline`](skills/tao-run-automl-deft-pipeline/SKILL.md) | HUMMBL | Apache-2.0 | Run the canonical NVIDIA AOI three-phase training pipeline — Phase 1 AutoML baseline (HPO), ... |
| [`tao-run-deft-aoi`](skills/tao-run-deft-aoi/SKILL.md) | HUMMBL | Apache-2.0 AND CC-BY-4.0 | Run the full DEFT AOI improvement loop for NVIDIA TAO VisualChangeNet / ChangeNet PCB inspec... |
| [`tao-run-deft-aoi-cosmos3`](skills/tao-run-deft-aoi-cosmos3/SKILL.md) | HUMMBL | Apache-2.0 AND CC-BY-4.0 | Run the disk-backed DEFT AOI improvement loop for NVIDIA Cosmos Reason 3 / Cosmos3 models, u... |
| [`tao-run-deft-cr-its-mining`](skills/tao-run-deft-cr-its-mining/SKILL.md) | HUMMBL | Apache-2.0 | Run the mining-based DEFT improvement workflow for ITS Cosmos-Reason binary video questions,... |
| [`tao-run-deft-object-detection`](skills/tao-run-deft-object-detection/SKILL.md) | HUMMBL | Apache-2.0 | Run the full DEFT smart-data-augmentation loop for NVIDIA TAO Grounding DINO object detectio... |
| [`tao-run-inference-service`](skills/tao-run-inference-service/SKILL.md) | HUMMBL | Apache-2.0 | Start, query, and stop a network-specific TAO inference microservice ({network_arch}-inferen... |
| [`tao-run-on-brev`](skills/tao-run-on-brev/SKILL.md) | HUMMBL | Apache-2.0 | Run a TAO training/evaluation/inference container on an NVIDIA Brev GPU instance. Instance p... |
| [`tao-run-on-docker`](skills/tao-run-on-docker/SKILL.md) | HUMMBL | Apache-2.0 | The Docker execution platform for TAO jobs — a local daemon or a remote GPU box via DOCKER_H... |
| [`tao-run-on-kubernetes`](skills/tao-run-on-kubernetes/SKILL.md) | HUMMBL | Apache-2.0 | Kubernetes execution platform — submits TAO container jobs as k8s Jobs with NVIDIA GPU sched... |
| [`tao-run-on-slurm`](skills/tao-run-on-slurm/SKILL.md) | HUMMBL | Apache-2.0 | Remote SLURM GPU cluster execution over SSH with sbatch/srun, Pyxis/Enroot containers, and L... |
| [`tao-run-on-virtualenv`](skills/tao-run-on-virtualenv/SKILL.md) | HUMMBL | Apache-2.0 | Run a Python training/eval script directly in an existing local virtualenv — no docker, no c... |
| [`tao-setup`](skills/tao-setup/SKILL.md) | HUMMBL | Apache-2.0 | One-time session setup and orchestration map for the TAO skill bank. Run this first when the... |
| [`tao-setup-nvidia-gpu-host`](skills/tao-setup-nvidia-gpu-host/SKILL.md) | HUMMBL | Apache-2.0 | Host setup for TAO GPU backends. Checks and, after user approval, installs minimum-compatibl... |
| [`tao-train-action-recognition`](skills/tao-train-action-recognition/SKILL.md) | HUMMBL | Apache-2.0 | Action recognition from video sequences. Supports RGB, optical flow, and joint (multi-stream... |
| [`tao-train-bevfusion`](skills/tao-train-bevfusion/SKILL.md) | HUMMBL | Apache-2.0 | BEVFusion for multi-sensor 3D object detection. Fuses LiDAR point clouds and camera images i... |
| [`tao-train-centerpose`](skills/tao-train-centerpose/SKILL.md) | HUMMBL | Apache-2.0 | CenterPose for keypoint / pose estimation. Detects object centers and regresses keypoint loc... |
| [`tao-train-codetr`](skills/tao-train-codetr/SKILL.md) | HUMMBL | Apache-2.0 | Co-DETR (CoDINO) for object detection. A DETR-family detector with collaborative hybrid |
| [`tao-train-deformable-detr`](skills/tao-train-deformable-detr/SKILL.md) | HUMMBL | Apache-2.0 | Deformable DETR for 2D object detection. Uses deformable attention for efficient multi-scale... |
| [`tao-train-depth-anything-v2`](skills/tao-train-depth-anything-v2/SKILL.md) | HUMMBL | Apache-2.0 | Monocular depth estimation using Metric Depth Anything v2 or Relative Depth Anything archite... |
| [`tao-train-dino`](skills/tao-train-dino/SKILL.md) | HUMMBL | Apache-2.0 | DINO (DETR with Improved DeNoising Anchor Boxes) for 2D object detection. Transformer-based ... |
| [`tao-train-dinov3`](skills/tao-train-dinov3/SKILL.md) | HUMMBL | Apache-2.0 | DINOv3 continual self-supervised pre-training. Domain-adapts public DINOv3 ViT backbones |
| [`tao-train-fast-foundation-stereo`](skills/tao-train-fast-foundation-stereo/SKILL.md) | HUMMBL | Apache-2.0 | Real-time stereo depth estimation using FastFoundationStereo (FFS), the distilled bp2 commer... |
| [`tao-train-foundation-stereo`](skills/tao-train-foundation-stereo/SKILL.md) | HUMMBL | Apache-2.0 | Stereo depth estimation using FoundationStereo. Predicts disparity maps from stereo image pa... |
| [`tao-train-grounding-dino`](skills/tao-train-grounding-dino/SKILL.md) | HUMMBL | Apache-2.0 | Grounding DINO for open-set object detection. Combines DINO-style detection with a BERT text... |
| [`tao-train-image-classification`](skills/tao-train-image-classification/SKILL.md) | HUMMBL | Apache-2.0 | PyTorch-based TAO image classification. Supports a wide range of backbones (FAN, EfficientNe... |
| [`tao-train-mask-auto-encoder`](skills/tao-train-mask-auto-encoder/SKILL.md) | HUMMBL | Apache-2.0 | Masked Auto-Encoder (MAE) for self-supervised pretraining and fine-tuning. Masks random patc... |
| [`tao-train-mask-auto-label`](skills/tao-train-mask-auto-label/SKILL.md) | HUMMBL | Apache-2.0 | MAL (Mask Auto-Label) for weakly-supervised segmentation. Produces segmentation masks from m... |
| [`tao-train-mask-grounding-dino`](skills/tao-train-mask-grounding-dino/SKILL.md) | HUMMBL | Apache-2.0 | Mask Grounding DINO for grounded instance segmentation. Extends Grounding DINO with a mask-p... |
| [`tao-train-mask2former`](skills/tao-train-mask2former/SKILL.md) | HUMMBL | Apache-2.0 | Mask2Former for universal image segmentation (panoptic, instance, and semantic). Transformer... |
| [`tao-train-metric-learning-recognition`](skills/tao-train-metric-learning-recognition/SKILL.md) | HUMMBL | Apache-2.0 | Metric-learning recognition (ml-recog) for fine-grained visual recognition. Learns embedding... |
| [`tao-train-nvdinov2`](skills/tao-train-nvdinov2/SKILL.md) | HUMMBL | Apache-2.0 | NVDINOv2 for self-supervised visual representation learning. Trains vision transformers via ... |
| [`tao-train-nvpanoptix3d`](skills/tao-train-nvpanoptix3d/SKILL.md) | HUMMBL | Apache-2.0 | NVPanoptix3D for panoptic 3D scene reconstruction from posed RGB images. Produces 3D panopti... |
| [`tao-train-ocdnet`](skills/tao-train-ocdnet/SKILL.md) | HUMMBL | Apache-2.0 | OCDNet for scene text detection. Detects arbitrary-oriented text regions in natural images u... |
| [`tao-train-ocrnet`](skills/tao-train-ocrnet/SKILL.md) | HUMMBL | Apache-2.0 | OCRNet for scene text recognition. Recognizes text content from cropped text-region images a... |
| [`tao-train-oneformer`](skills/tao-train-oneformer/SKILL.md) | HUMMBL | Apache-2.0 | OneFormer for universal image segmentation. Unifies panoptic, instance, and semantic segment... |
| [`tao-train-optical-inspection`](skills/tao-train-optical-inspection/SKILL.md) | HUMMBL | Apache-2.0 | Optical Inspection for defect detection using Siamese networks. Compares image pairs to dete... |
| [`tao-train-pointpillars`](skills/tao-train-pointpillars/SKILL.md) | HUMMBL | Apache-2.0 | PointPillars for 3D object detection from LiDAR point clouds. Encodes point clouds into a ps... |
| [`tao-train-pose-classification`](skills/tao-train-pose-classification/SKILL.md) | HUMMBL | Apache-2.0 | Pose classification using ST-GCN (Spatial Temporal Graph Convolutional Network). Classifies ... |
| [`tao-train-reid`](skills/tao-train-reid/SKILL.md) | HUMMBL | Apache-2.0 | Person re-identification (ReID). Learns discriminative embeddings to match the same person a... |
| [`tao-train-rtdetr`](skills/tao-train-rtdetr/SKILL.md) | HUMMBL | Apache-2.0 | RT-DETR (Real-Time DEtection TRansformer) for 2D object detection. Designed for real-time in... |
| [`tao-train-segformer`](skills/tao-train-segformer/SKILL.md) | HUMMBL | Apache-2.0 | SegFormer for semantic segmentation. Lightweight transformer-based architecture with hierarc... |
| [`tao-train-single-step`](skills/tao-train-single-step/SKILL.md) | HUMMBL | Apache-2.0 | Standard single-step train/eval/export workflow for any TAO model. Use when training a TAO m... |
| [`tao-train-sparse4d`](skills/tao-train-sparse4d/SKILL.md) | HUMMBL | Apache-2.0 | Sparse4D for multi-camera temporal 3D object detection and tracking. Uses sparse queries wit... |
| [`tao-train-visual-changenet`](skills/tao-train-visual-changenet/SKILL.md) | HUMMBL | Apache-2.0 | Visual ChangeNet for binary image classification and segmentation in AOI defect detection. U... |
| [`tao-validate-dataset-format`](skills/tao-validate-dataset-format/SKILL.md) | HUMMBL | Apache-2.0 | Run `tao-daft validate` to check NVIDIA TAO DAFT datasets for structure, schema, and cross-r... |
| [`tao-validate-recipe-transfer`](skills/tao-validate-recipe-transfer/SKILL.md) | HUMMBL | Apache-2.0 | Port a published computer vision paper's official code and training recipe onto a customer's... |
| [`tax-prep`](skills/tax-prep/SKILL.md) | HUMMBL | Apache-2.0 | Organize deductions, receipts, quarterly estimates for tax filing. Solo founder focus. |
| [`tdd`](skills/tdd/SKILL.md) | HUMMBL | Apache-2.0 | RED-GREEN-REFACTOR cycle enforcement for test-driven development. |
| [`tech-cyber-aggregator-research`](skills/tech-cyber-aggregator-research/SKILL.md) | HUMMBL | Apache-2.0 | Domain research skill for Tech & Cyber aggregator discovery. Catalogs canonical aggregators,... |
| [`tech-debt`](skills/tech-debt/SKILL.md) | HUMMBL | Apache-2.0 | Comprehensive multi-repo tech debt scanner, classifier, and reducer. Covers all 8 debt categ... |
| [`tempo`](skills/tempo/SKILL.md) | HUMMBL | Apache-2.0 | Switch operational tempo -- changes permission profile and interaction mode. |
| [`tensorrt-engine-baker`](skills/tensorrt-engine-baker/SKILL.md) | HUMMBL | Apache-2.0 | Headless ONNX-to-TensorRT engine compiler for in-game neural models. Compiles local AI model... |
| [`terms-of-service`](skills/terms-of-service/SKILL.md) | HUMMBL | Apache-2.0 | Draft Terms of Service (ToS) / Terms of Use for a SaaS product or website. Covers acceptable... |
| [`test-gen`](skills/test-gen/SKILL.md) | HUMMBL | Apache-2.0 | Generate test scaffolding from source code or specs. Creates test files, fixtures, and test ... |
| [`test-run`](skills/test-run/SKILL.md) | HUMMBL | Apache-2.0 | Run tests by target (unit, integration, e2e, security, or -k). |
| [`test-trends`](skills/test-trends/SKILL.md) | HUMMBL | Apache-2.0 | Track test count, pass rate, duration, and flake rate over time from CI and git history |
| [`testflight-prep`](skills/testflight-prep/SKILL.md) | HUMMBL | Apache-2.0 | Pre-submission checklist for TestFlight/iOS builds. |
| [`testimonial`](skills/testimonial/SKILL.md) | HUMMBL | Apache-2.0 | Collect, format, and organize client testimonials for marketing materials |
| [`thematic-analysis`](skills/thematic-analysis/SKILL.md) | HUMMBL | Apache-2.0 | Qualitative thematic analysis - identify, analyze, and report patterns (themes) in qualitati... |
| [`theme-factory`](skills/theme-factory/SKILL.md) | HUMMBL | Apache-2.0 | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings,... |
| [`thoth`](skills/thoth/SKILL.md) | HUMMBL | Apache-2.0 | Cross-session closing ritual — reads session artifacts, extracts patterns, distills wisdom i... |
| [`thread-write`](skills/thread-write/SKILL.md) | HUMMBL | Apache-2.0 | Write threaded content for X/Twitter or LinkedIn carousels with hook, body, CTA structure |
| [`threat-model`](skills/threat-model/SKILL.md) | HUMMBL | Apache-2.0 | Guided STRIDE threat modeling for a component. |
| [`tilegym-adding-cutile-kernel`](skills/tilegym-adding-cutile-kernel/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Add a new cuTile GPU kernel operator to TileGym. Covers dispatch registration in ops.py, cuT... |
| [`tilegym-converting-cutile-to-julia`](skills/tilegym-converting-cutile-to-julia/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Converts cuTile Python GPU kernels (@ct.kernel) to cuTile.jl Julia equivalents. Handles kern... |
| [`tilegym-converting-cutile-to-triton`](skills/tilegym-converting-cutile-to-triton/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Converts cuTile GPU kernels (@ct.kernel) to Triton (@triton.jit). Handles standard in-repo c... |
| [`tilegym-cutile-autotuning`](skills/tilegym-cutile-autotuning/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | "Use when adding, modifying, optimizing, or debugging CuTile autotuning code. Trigger signal... |
| [`tilegym-cutile-python`](skills/tilegym-cutile-python/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | "Expert cuTile programming assistant. Write high-performance GPU kernels using cuTile's tile... |
| [`tilegym-improve-cutile-kernel-perf`](skills/tilegym-improve-cutile-kernel-perf/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Iteratively optimize cuTile kernel performance through systematic profiling, bottleneck anal... |
| [`tilegym-monkey-patch-kernels-to-transformers`](skills/tilegym-monkey-patch-kernels-to-transformers/SKILL.md) | HUMMBL | CC-BY-4.0 AND Apache-2.0 | Integrate TileGym kernels into Hugging Face `transformers` models by replacing the library's... |
| [`time-track`](skills/time-track/SKILL.md) | HUMMBL | Apache-2.0 | Log and summarize billable time by project, client, and category |
| [`tm-counsel`](skills/tm-counsel/SKILL.md) | HUMMBL | Apache-2.0 | "Internal trademark strategy review for clearance artifacts or mark questions: section 2(d),... |
| [`token-estimate`](skills/token-estimate/SKILL.md) | HUMMBL | Apache-2.0 | Estimate token count and cost for prompts, documents, or conversations across models. |
| [`tournament`](skills/tournament/SKILL.md) | HUMMBL | Apache-2.0 | Governed multi-agent cooperative tournament runner. Dispatches competing agents in dialectic... |
| [`transformation-workflow`](skills/transformation-workflow/SKILL.md) | HUMMBL | Apache-2.0 | Practical application guide for HUMMBL's 6 transformations (Perspective, Inversion, Composit... |
| [`travel-itinerary`](skills/travel-itinerary/SKILL.md) | HUMMBL | Apache-2.0 | Build a complete trip itinerary with logistics, day-by-day schedule, ground transport, conta... |
| [`tree-synthesis`](skills/tree-synthesis/SKILL.md) | HUMMBL | Apache-2.0 | Centralized Asynchronous Isolated Delegation (CAID) 10:1 recursive fan-in tree synthesis |
| [`tri-agent`](skills/tri-agent/SKILL.md) | HUMMBL | Apache-2.0 | Three-agent workflow with selectable topology — extends dual-agent to include a third role (... |
| [`triage`](skills/triage/SKILL.md) | HUMMBL | Apache-2.0 | Adopt / Adapt / Avoid evaluation for any external candidate (project, library, tool, model, ... |
| [`trichotomy-route`](skills/trichotomy-route/SKILL.md) | HUMMBL | Apache-2.0 | Route an artifact to the correct tier (_internal/, _between/, _external/) based on authorshi... |
| [`trusting`](skills/trusting/SKILL.md) | HUMMBL | MIT | Trusting coding mode. Assume valid inputs from trusted callers. Let errors bubble to boundar... |
| [`truth-mode`](skills/truth-mode/SKILL.md) | HUMMBL | Apache-2.0 | Constitutional Tier 0 — epistemic honesty floor. No mode may override. Every claim has evide... |
| [`try-except-audit`](skills/try-except-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit exception handling for overly broad catches, swallowed errors, and missing context. |
| [`ts-test-run`](skills/ts-test-run/SKILL.md) | HUMMBL | Apache-2.0 | Run TypeScript/JavaScript tests via jest, vitest, or node --test. The TS/JS counterpart to t... |
| [`tuk`](skills/tuk/SKILL.md) | HUMMBL | MIT | Caveman character: TUK, the toolmaker. Curious, experimental, always fiddling with rocks and... |
| [`turnstile-spin`](skills/turnstile-spin/SKILL.md) | HUMMBL | Apache-2.0 | "Set up or fix Cloudflare Turnstile/CAPTCHA end to end: widget creation, siteverify Worker, ... |
| [`type-check`](skills/type-check/SKILL.md) | HUMMBL | Apache-2.0 | Run mypy or pyright type checking, report untyped functions, suggest type annotations for wo... |
| [`ucsc-conservation-and-tfbs`](skills/ucsc-conservation-and-tfbs/SKILL.md) | HUMMBL | Apache-2.0 | Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding ... |
| [`ui-audit`](skills/ui-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit UI code for quality — scores against the vibe-coded→engineered spectrum (60-point scale) |
| [`ui-design-system`](skills/ui-design-system/SKILL.md) | HUMMBL | Apache-2.0 | Define, audit, or extend UI design systems including tokens, components, states, spacing, ty... |
| [`ulla`](skills/ulla/SKILL.md) | HUMMBL | MIT | Cavewoman character: ULLA, the storyteller and elder. Long-winded, speaks in parables and re... |
| [`uncertainty-map`](skills/uncertainty-map/SKILL.md) | HUMMBL | Apache-2.0 | "Map a decision, project, incident, or strategy into knowns, unknowns, blind spots, assumpti... |
| [`unibind-database`](skills/unibind-database/SKILL.md) | HUMMBL | Apache-2.0 | Queries the UniBind database for experimentally validated transcription factor (TF) binding ... |
| [`uniprot-database`](skills/uniprot-database/SKILL.md) | HUMMBL | Apache-2.0 | Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and Un... |
| [`unit-economics`](skills/unit-economics/SKILL.md) | HUMMBL | Apache-2.0 | Calculate CAC, LTV, payback period, gross margins per product or service line |
| [`uptime-check`](skills/uptime-check/SKILL.md) | HUMMBL | Apache-2.0 | HTTP health check across multiple endpoints with latency measurement and status codes |
| [`usability-test`](skills/usability-test/SKILL.md) | HUMMBL | Apache-2.0 | Plan, run, or synthesize task-based usability tests for products, prototypes, flows, docs, A... |
| [`usage-monitor`](skills/usage-monitor/SKILL.md) | HUMMBL | Apache-2.0 | Track Cloudflare Neuron consumption against the 10K/day free-tier ceiling. Log inference cal... |
| [`user-discovery`](skills/user-discovery/SKILL.md) | HUMMBL | Apache-2.0 | Discover the end-users of the systems and products the agent builds or serves — who they are... |
| [`user-journey`](skills/user-journey/SKILL.md) | HUMMBL | Apache-2.0 | Map what users see, think, feel, and do at each stage of interacting with a product. Maps to... |
| [`uv`](skills/uv/SKILL.md) | HUMMBL | Apache-2.0 | Checks whether the uv Python package manager is installed and installs it if missing. Ensure... |
| [`ux-audit`](skills/ux-audit/SKILL.md) | HUMMBL | Apache-2.0 | Audit UX patterns for quality — navigation, flows, feedback, consistency, cognitive load, co... |
| [`value-prop`](skills/value-prop/SKILL.md) | HUMMBL | Apache-2.0 | Craft and test value propositions for different audience segments with messaging hierarchy a... |
| [`velocity-tune`](skills/velocity-tune/SKILL.md) | HUMMBL | Apache-2.0 | Measure and iteratively improve development velocity -- find bottlenecks, remove friction. M... |
| [`vendor-ai-review`](skills/vendor-ai-review/SKILL.md) | HUMMBL | Apache-2.0 | AI governance due diligence review for a vendor or third-party AI tool. Grades transparency,... |
| [`vendor-gen-eval`](skills/vendor-gen-eval/SKILL.md) | HUMMBL | Apache-2.0 | Full benchmarking, evaluation, and testing program for the vendor-neutral generation system ... |
| [`venv-manage`](skills/venv-manage/SKILL.md) | HUMMBL | Apache-2.0 | Create, verify, and troubleshoot Python virtual environments |
| [`verification-discipline`](skills/verification-discipline/SKILL.md) | HUMMBL | Apache-2.0 | 'Agent operating-discipline self-checks: verification vocabulary (spot-checked vs verified b... |
| [`video-analyze`](skills/video-analyze/SKILL.md) | HUMMBL | Apache-2.0 | Analyze video content from YouTube URLs, local files, or streams by combining audio transcri... |
| [`video-script`](skills/video-script/SKILL.md) | HUMMBL | Apache-2.0 | Script for explainer or tutorial video with sections, timing, and visual notes |
| [`visual-design-review`](skills/visual-design-review/SKILL.md) | HUMMBL | Apache-2.0 | Review visual design quality including hierarchy, composition, brand fit, polish, contrast, ... |
| [`vram-budget-sentinel`](skills/vram-budget-sentinel/SKILL.md) | HUMMBL | Apache-2.0 | 12 GB VRAM memory allocator and texture footprint auditor. Hooks into nvidia-smi and Vulkan/... |
| [`vss-ask-video`](skills/vss-ask-video/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill to ask the VSS agent's video_understanding tool a fresh visual question about... |
| [`vss-deploy-dense-captioning`](skills/vss-deploy-dense-captioning/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when deploying standalone RT-VLM dense captioning or calling its REST API (up... |
| [`vss-deploy-detection-tracking-2d`](skills/vss-deploy-detection-tracking-2d/SKILL.md) | HUMMBL | Apache-2.0 | "Use this skill when the user wants to deploy, run, debug, tear down, or call the REST API o... |
| [`vss-deploy-detection-tracking-3d`](skills/vss-deploy-detection-tracking-3d/SKILL.md) | HUMMBL | Apache-2.0 | Deploy and operate the RTVI-CV-3D microservice as MV3DT (`MODE=mv3dt`): per-camera DeepStrea... |
| [`vss-deploy-profile`](skills/vss-deploy-profile/SKILL.md) | HUMMBL | Apache-2.0 | Use to select, configure, deploy, verify, debug, or tear down a VSS profile (base, search, l... |
| [`vss-deploy-video-embedding`](skills/vss-deploy-video-embedding/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when deploying, operating, or integrating the VSS 3.2 GA RT-Embed Video Embed... |
| [`vss-generate-video-calibration`](skills/vss-generate-video-calibration/SKILL.md) | HUMMBL | Apache-2.0 | Use to run AutoMagicCalib on local MP4s, RTSP, or the bundled sample dataset, and to deploy ... |
| [`vss-generate-video-report`](skills/vss-generate-video-report/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when producing a VSS analysis report — Mode A per-clip VLM, Mode B incident-r... |
| [`vss-manage-alerts`](skills/vss-manage-alerts/SKILL.md) | HUMMBL | Apache-2.0 | Use for VSS alert workflows — real-time monitoring, Alert-Bridge subscriptions, Slack notifi... |
| [`vss-manage-video-io-storage`](skills/vss-manage-video-io-storage/SKILL.md) | HUMMBL | Apache-2.0 | Use to call the VIOS REST API (sensor list, timelines, clip extraction, snapshots, add/delet... |
| [`vss-query-analytics`](skills/vss-query-analytics/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill when reading video-analytics metrics, incidents, alerts, and sensor data via ... |
| [`vss-search-archive`](skills/vss-search-archive/SKILL.md) | HUMMBL | Apache-2.0 | Use this skill to run top-level VSS fusion search on archived video, or to ingest video file... |
| [`vss-setup-behavior-analytics`](skills/vss-setup-behavior-analytics/SKILL.md) | HUMMBL | Apache-2.0 | Use to deploy the vss-behavior-analytics service standalone (entrypoint, config-source, opti... |
| [`vss-setup-video-analytics-api`](skills/vss-setup-video-analytics-api/SKILL.md) | HUMMBL | Apache-2.0 | Use to deploy the vss-video-analytics-api REST service standalone (config-source, data-log b... |
| [`vss-summarize-video`](skills/vss-summarize-video/SKILL.md) | HUMMBL | Apache-2.0 | Use to summarize a recorded video via the LVS summarization microservice (HITL-gated) with a... |
| [`wargame`](skills/wargame/SKILL.md) | HUMMBL | Apache-2.0 | "Run a full red/blue/purple security exercise with scoring, posture grade, and residual-risk... |
| [`warm-intro`](skills/warm-intro/SKILL.md) | HUMMBL | Apache-2.0 | Draft warm introduction emails with mutual context, reason for connecting, and clear ask |
| [`warp-compile-time-optimizer`](skills/warp-compile-time-optimizer/SKILL.md) | HUMMBL | Apache-2.0 | Use when compile time or startup time is the problem in code that uses Warp: a request to im... |
| [`warp-debug-gradients`](skills/warp-debug-gradients/SKILL.md) | HUMMBL | Apache-2.0 | Use to diagnose and fix incorrect gradients in differentiable Warp programs. Anything traine... |
| [`warp-eval`](skills/warp-eval/SKILL.md) | HUMMBL | Apache-2.0 | Evaluate whether an existing hot path is a credible NVIDIA Warp candidate. Use for irregular... |
| [`watch-session`](skills/watch-session/SKILL.md) | HUMMBL | Apache-2.0 | Monitor a parallel agent session's work across bus, git, and filesystem surfaces. |
| [`web-artifacts-builder`](skills/web-artifacts-builder/SKILL.md) | HUMMBL | Apache-2.0 | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern... |
| [`web-perf`](skills/web-perf/SKILL.md) | HUMMBL | Apache-2.0 | "Audit or optimize web performance with Chrome DevTools MCP: Core Web Vitals, Lighthouse/pag... |
| [`web-research`](skills/web-research/SKILL.md) | HUMMBL | Apache-2.0 | Structured web research -- search, fetch, evaluate sources, synthesize findings. |
| [`webapp-testing`](skills/webapp-testing/SKILL.md) | HUMMBL | Apache-2.0 | Toolkit for interacting with and testing local web applications using Playwright. Supports v... |
| [`webhook-manage`](skills/webhook-manage/SKILL.md) | HUMMBL | Apache-2.0 | Create, test, and monitor webhook integrations with retry logic, payload inspection, and del... |
| [`weekly-digest`](skills/weekly-digest/SKILL.md) | HUMMBL | Apache-2.0 | Weekly operational digest covering CRM pipeline, email activity, calendar, and content metrics. |
| [`weekly-plan`](skills/weekly-plan/SKILL.md) | HUMMBL | Apache-2.0 | Forward-looking week allocation. Sets THE ONE THING per day, maps sprint goals to days, writ... |
| [`weekly-review`](skills/weekly-review/SKILL.md) | HUMMBL | Apache-2.0 | Weekly planning and review -- what shipped, what's next, what to deprioritize. |
| [`whiteteam`](skills/whiteteam/SKILL.md) | HUMMBL | Apache-2.0 | Exercise referee -- orchestrate, control, and drive exercise outcomes. Neutral adjudicator f... |
| [`win-loss`](skills/win-loss/SKILL.md) | HUMMBL | Apache-2.0 | Analyze won and lost deals for patterns, competitor displacement, and improvement opportunities |
| [`workers-ai`](skills/workers-ai/SKILL.md) | HUMMBL | Apache-2.0 | Deploy and manage Cloudflare Workers AI models — text generation, embeddings, image classifi... |
| [`workers-analytics-engine`](skills/workers-analytics-engine/SKILL.md) | HUMMBL | Apache-2.0 | Configure Cloudflare Analytics Engine — time-series data ingestion, SQL queries via Workers ... |
| [`workers-best-practices`](skills/workers-best-practices/SKILL.md) | HUMMBL | Apache-2.0 | "Write or review Cloudflare Workers code, wrangler config, bindings, streaming, global state... |
| [`workers-d1`](skills/workers-d1/SKILL.md) | HUMMBL | Apache-2.0 | Manage Cloudflare D1 SQLite databases — schema, migrations, queries, and bindings from Workers |
| [`workers-kv`](skills/workers-kv/SKILL.md) | HUMMBL | Apache-2.0 | Manage Cloudflare KV namespaces — key-value storage with TTL, listing, and bulk operations f... |
| [`workers-queue`](skills/workers-queue/SKILL.md) | HUMMBL | Apache-2.0 | Manage Cloudflare Queues — producer/consumer patterns, dead letter queues, and batch process... |
| [`workers-r2`](skills/workers-r2/SKILL.md) | HUMMBL | Apache-2.0 | Manage Cloudflare R2 object storage — buckets, objects, lifecycle policies, and S3-compatibl... |
| [`workflow-lint`](skills/workflow-lint/SKILL.md) | HUMMBL | Apache-2.0 | Lint CI/CD workflows for anti-patterns, security issues, deprecated actions, and efficiency ... |
| [`workflow-skill-creator`](skills/workflow-skill-creator/SKILL.md) | HUMMBL | Apache-2.0 | Distills a completed user workflow or interaction into a reusable agent skill. Use when the ... |
| [`worktree`](skills/worktree/SKILL.md) | HUMMBL | Apache-2.0 | Manage git worktrees for parallel development -- create, list, clean up. |
| [`worst-case`](skills/worst-case/SKILL.md) | HUMMBL | Apache-2.0 | Find conditions that maximize failure -- inverse optimization for stress testing. Maps to IN16. |
| [`wrangler`](skills/wrangler/SKILL.md) | HUMMBL | Apache-2.0 | "Use Wrangler CLI for Cloudflare Workers dev/deploy and managing KV, R2, D1, Vectorize, Hype... |
| [`xlsx`](skills/xlsx/SKILL.md) | HUMMBL | Apache-2.0 | "Create, read, edit, clean, format, chart, or convert spreadsheet deliverables (.xlsx, .xlsm... |
| [`yara`](skills/yara/SKILL.md) | HUMMBL | MIT | Cavewoman character: YARA, the healer. Gentle, firm, plant-wise, body-aware. The tribe's med... |
| [`yellowteam`](skills/yellowteam/SKILL.md) | HUMMBL | Apache-2.0 | Builder security -- secure coding, architecture, development, DevOps. Build security into sy... |
| [`yoda`](skills/yoda/SKILL.md) | HUMMBL | MIT | Mentor character: YODA, the Jedi Master. Ancient, patient, speaks in inverted syntax and aph... |
| [`yoda-mode`](skills/yoda-mode/SKILL.md) | HUMMBL | Apache-2.0 | Yoda voice adapter for HUMMBL communication profiles. Equivalent to --voice=yoda with defaul... |

## Upstream Licensing & Attribution

This repository provides a unified catalog of agent skills released under permissive open-source licenses:

- **HUMMBL Original Skills (1,267 skills)**: Licensed under [Apache-2.0](LICENSE) © 2026 HUMMBL, LLC.
- **NVIDIA Corporation Tooling & SDK Guides (15 skills)**: Authored by NVIDIA teams (CUDA-Q, Holoscan, Nemotron) under CC-BY-4.0 / Apache-2.0 © NVIDIA Corporation.
- **Community & Ecosystem Harnesses**: Retain original author and license metadata in their respective `SKILL.md` frontmatter.

See [ATTRIBUTION.md](ATTRIBUTION.md) for individual upstream copyright statements.
