# HUMMBL Universal Agent Skills (v1.0.0)

A curated, open-source library of **1283 universal AI agent skills**, workflows, evaluation harnesses, and cognitive tools.

Built for **Cursor**, **Claude Code**, **Antigravity CLI**, **OpenCode**, and **Codex**.

## Quick Install

### Install for Claude Code (~/.claude/skills)
```bash
git clone https://github.com/hummbl/agent-skills.git ~/.claude/skills/hummbl
```

### Install for Cursor (.cursor/skills)
```bash
git clone https://github.com/hummbl/agent-skills.git .cursor/skills/hummbl
```

## Featured Skills

| Skill | Description |
|:---|:---|
| [`index`](skills/_index/SKILL.md) | Skill index -- generated catalog of every local skill under ~/.agents/skills so agents can |
| [`a11y-audit`](skills/a11y-audit/SKILL.md) | Web accessibility audit against WCAG 2.1 AA standards |
| [`a11y-fix`](skills/a11y-fix/SKILL.md) | Generate specific fixes for accessibility audit findings with code patches |
| [`aar`](skills/aar/SKILL.md) | Generate an After Action Report with Base120 references and receipts. |
| [`aar-followthrough`](skills/aar-followthrough/SKILL.md) | Run AFTER [aar] completes to elaborate and plan every §7 recommendation into an owned, ver |
| [`ab-test-analyzer`](skills/ab-test-analyzer/SKILL.md) | Analyze A/B test results for statistical significance, effect size, and practical importan |
| [`absence-audit`](skills/absence-audit/SKILL.md) | Find what's MISSING from a system -- unhandled cases, missing tests, absent monitoring, si |
| [`accelerated-computing-cudf`](skills/accelerated-computing-cudf/SKILL.md) | Official NVIDIA-authored guidance for NVIDIA cuDF GPU DataFrames, pandas acceleration, das |
| [`adapter-status`](skills/adapter-status/SKILL.md) | Check which service adapters are wired and operational. |
| [`admission-gate`](skills/admission-gate/SKILL.md) | Redaction gate for publishing fleet artifacts to external remotes. Hard-fails on local pat |
| [`adr-review`](skills/adr-review/SKILL.md) | Review Architecture Decision Records for staleness, superseded decisions, missing outcomes |
| [`agent`](skills/agent/SKILL.md) | Initialize any agent by name -- looks up the dispatch table and runs the right primitive ( |
| [`agent-audit`](skills/agent-audit/SKILL.md) | Audit a specific agent's bus activity, commit history, trust score, and guardrail complian |
| [`agent-browser`](skills/agent-browser/SKILL.md) | Browser automation CLI for AI agents. Use when the user needs to interact with websites, i |
| [`agent-compare`](skills/agent-compare/SKILL.md) | Side-by-side comparison of agent outputs on identical tasks — quality, speed, cost, accura |
| [`agent-cost-track`](skills/agent-cost-track/SKILL.md) | Track per-agent token usage and API costs with budget alerts and cost attribution |
| [`agent-design`](skills/agent-design/SKILL.md) | Design agentic workflows -- tool selection, loop structure, guardrails, memory, terminatio |
| [`agent-grade`](skills/agent-grade/SKILL.md) | Grade an agent's work on a 100-point rubric that scores verified, authorized state change  |
| [`agent-guardrail`](skills/agent-guardrail/SKILL.md) | Configure and test agent guardrails for input/output validation, tool-use constraints, and |
| [`agent-memory`](skills/agent-memory/SKILL.md) | Design agent memory systems with short-term, long-term, episodic, and semantic memory and  |
| [`agent-metrics`](skills/agent-metrics/SKILL.md) | Aggregate agent performance metrics from bus, git, and CI history |
| [`agent-roster`](skills/agent-roster/SKILL.md) | Live probe of all known agents and models -- registry, bus activity, process status, model |
| [`agent-trace`](skills/agent-trace/SKILL.md) | Trace and debug agentic workflows by logging tool calls, decision points, and state transi |
| [`agent-usage-report`](skills/agent-usage-report/SKILL.md) | Report named-agent usage telemetry, citation counts, first/last use, and backfill coverage |
| [`agents-sdk`](skills/agents-sdk/SKILL.md) | Build Cloudflare Workers agents with Agents SDK: stateful agents, WebSockets, MCP servers, |
| [`ai-cost-optimize`](skills/ai-cost-optimize/SKILL.md) | Reduce AI API costs through caching, batching, model downsizing, prompt compression, and r |
| [`ai-policy-review`](skills/ai-policy-review/SKILL.md) | Review and grade an existing internal AI use policy against NIST AI RMF, ISO 42001, and EU |
| [`ai-regulation`](skills/ai-regulation/SKILL.md) | Track AI-specific regulations -- EU AI Act, US executive orders, state bills, sector-speci |
| [`ai-risk-assessment`](skills/ai-risk-assessment/SKILL.md) | Full AI system risk assessment aligned to NIST AI RMF. Maps risks across GOVERN/MAP/MEASUR |
| [`ai-safety-check`](skills/ai-safety-check/SKILL.md) | Validate AI outputs for safety, bias, and robustness with comprehensive testing. [Maps to  |
| [`aiq-deploy`](skills/aiq-deploy/SKILL.md) | \| |
| [`aiq-research`](skills/aiq-research/SKILL.md) | \| |
| [`alert-digest`](skills/alert-digest/SKILL.md) | Summarize and deduplicate recent alerts, identify fatigue patterns |
| [`alert-noise-reduce`](skills/alert-noise-reduce/SKILL.md) | Deduplicate and correlate alerts to reduce noise. Groups similar alerts by signature, supp |
| [`alert-rule`](skills/alert-rule/SKILL.md) | Create and manage alert rules for health probes, cost thresholds, and CI failures |
| [`alert-triage`](skills/alert-triage/SKILL.md) | >- |
| [`algorithmic-art`](skills/algorithmic-art/SKILL.md) | Create original, self-contained, and verified p5.js generative art from an algorithmic phi |
| [`alignment-check`](skills/alignment-check/SKILL.md) | Verify agent outputs align with stated goals — detect goal drift, reward hacking, specific |
| [`alphafold-database-fetch-and-analyze`](skills/alphafold-database-fetch-and-analyze/SKILL.md) | > |
| [`alphagenome-single-variant-analysis`](skills/alphagenome-single-variant-analysis/SKILL.md) | > |
| [`amazon-bedrock`](skills/amazon-bedrock/SKILL.md) | >- |
| [`amberteam`](skills/amberteam/SKILL.md) | Supply chain security -- security of dependencies, third-party libraries, build pipelines, |
| [`amc-run-rtsp-calibration`](skills/amc-run-rtsp-calibration/SKILL.md) | Calibrate a new dataset from live RTSP camera streams via the AutoMagicCalib REST API. Use |
| [`amc-run-sample-calibration`](skills/amc-run-sample-calibration/SKILL.md) | Run end-to-end calibration on the shipped sample dataset (sdg_08_2_sample_data_010926.zip) |
| [`amc-run-video-calibration`](skills/amc-run-video-calibration/SKILL.md) | Calibrates pre-recorded `cam_*.mp4` datasets through the AutoMagicCalib REST API. Use for  |
| [`amc-setup-calibration-stack`](skills/amc-setup-calibration-stack/SKILL.md) | Launch AutoMagicCalib microservice and web UI from NGC release images via Docker Compose.  |
| [`anthropic-watch`](skills/anthropic-watch/SKILL.md) | Track bleeding-edge Anthropic announcements -- model releases, API changes, Claude Code up |
| [`apex`](skills/apex/SKILL.md) | Recon-first assessment mode — think before acting, produce a plan, delegate execution to t |
| [`api-design`](skills/api-design/SKILL.md) | Design REST/HTTP APIs with consistent patterns -- endpoints, errors, pagination, auth. |
| [`api-docs`](skills/api-docs/SKILL.md) | Generate API documentation from FastAPI/Flask endpoints or Python function signatures |
| [`api-test`](skills/api-test/SKILL.md) | Generate and run HTTP API tests against live or mocked endpoints |
| [`apply-review`](skills/apply-review/SKILL.md) | Review application materials (resume, cover letter, LinkedIn copy, portfolio one-pager, ou |
| [`arcana-peer-review`](skills/arcana-peer-review/SKILL.md) | Simulate independent non-author review by dispatching ARCANA-archetype subagents, each app |
| [`arcana-review`](skills/arcana-review/SKILL.md) | Multi-agent peer review using diverse epistemological lenses. Dispatches N subagents (suba |
| [`arcana-to-pitch`](skills/arcana-to-pitch/SKILL.md) | Transform ARCANA multi-lens synthesis outputs into HUMMBL pitch materials. Converts philos |
| [`arch-diagram`](skills/arch-diagram/SKILL.md) | Generate interactive architecture diagrams as self-contained HTML/SVG files. |
| [`aria-label-audit`](skills/aria-label-audit/SKILL.md) | Audit ARIA labels and accessibility attributes for correctness and completeness. [Maps to  |
| [`artifact-compiler-benchmark`](skills/artifact-compiler-benchmark/SKILL.md) | Run multi-dimensional latency, memory, and scaling benchmarks for the Compatibility-Aware  |
| [`ask-the-stack`](skills/ask-the-stack/SKILL.md) | Query the full knowledge stack (CLP + bibliography + bus + evidence docs) for research-gro |
| [`assessment-report`](skills/assessment-report/SKILL.md) | Generate governance assessment report from checklist results and scores. |
| [`assumption-audit`](skills/assumption-audit/SKILL.md) | Surface hidden assumptions in code, architecture, or decisions — list what must be true fo |
| [`async-update`](skills/async-update/SKILL.md) | Quick 3-sentence async update for any stakeholder. Where things stand, what's next, what t |
| [`audit-prep`](skills/audit-prep/SKILL.md) | Prepare for external audit -- evidence checklist, gap identification, document organizatio |
| [`auth-audit`](skills/auth-audit/SKILL.md) | Audit authentication and authorization patterns including token handling, session manageme |
| [`auto-ship`](skills/auto-ship/SKILL.md) | Alias for the lfg skill (compound-engineering plugin). Full autonomous shipping pipeline:  |
| [`autofix`](skills/autofix/SKILL.md) | Safely review and apply CodeRabbit PR review-thread feedback from GitHub with per-change a |
| [`automation-roi`](skills/automation-roi/SKILL.md) | Calculate ROI for automating a manual workflow -- time saved, break-even, payback period. |
| [`autoresearch-mode`](skills/autoresearch-mode/SKILL.md) | Governed, receipt-producing autonomous research mode with scheduled cadence and operator-f |
| [`autoresearch-tui`](skills/autoresearch-tui/SKILL.md) | Real-time observability TUI for the autoresearch overnight GPU training loop. One file, st |
| [`autotile-rule-compiler`](skills/autotile-rule-compiler/SKILL.md) | Generates 2D auto-tiling rulesets from minimal input. Supports 2x2 corner-based, 3x3 minim |
| [`aws-ai-ml`](skills/aws-ai-ml/SKILL.md) | >- |
| [`aws-auth`](skills/aws-auth/SKILL.md) | >- |
| [`aws-billing-and-cost-management`](skills/aws-billing-and-cost-management/SKILL.md) | >- |
| [`aws-blocks`](skills/aws-blocks/SKILL.md) | >- |
| [`aws-cdk`](skills/aws-cdk/SKILL.md) | >- |
| [`aws-cloudformation`](skills/aws-cloudformation/SKILL.md) | >- |
| [`aws-compute`](skills/aws-compute/SKILL.md) | >- |
| [`aws-containers`](skills/aws-containers/SKILL.md) | >- |
| [`aws-database`](skills/aws-database/SKILL.md) | >- |
| [`aws-deployment`](skills/aws-deployment/SKILL.md) | >- |
| [`aws-iam`](skills/aws-iam/SKILL.md) | >- |
| [`aws-messaging-and-streaming`](skills/aws-messaging-and-streaming/SKILL.md) | >- |
| [`aws-networking`](skills/aws-networking/SKILL.md) | >- |
| [`aws-observability`](skills/aws-observability/SKILL.md) | >- |
| [`aws-sdk-js-v3-usage`](skills/aws-sdk-js-v3-usage/SKILL.md) | >- |
| [`aws-sdk-python-usage`](skills/aws-sdk-python-usage/SKILL.md) | >- |
| [`aws-sdk-swift-usage`](skills/aws-sdk-swift-usage/SKILL.md) | >- |
| [`aws-security`](skills/aws-security/SKILL.md) | >- |
| [`aws-serverless`](skills/aws-serverless/SKILL.md) | >- |
| [`aws-storage`](skills/aws-storage/SKILL.md) | >- |
| [`base120`](skills/base120/SKILL.md) | Look up and apply HUMMBL Base120 mental models via MCP server. |
| [`base120-compose`](skills/base120-compose/SKILL.md) | The Synthesist. Composition transformation of Base120 (CO1-CO20). Build the whole the part |
| [`base120-decompose`](skills/base120-decompose/SKILL.md) | The Anatomist. Decomposition transformation of Base120 (DE1-DE20). Break wholes until each |
| [`base120-infrastructure`](skills/base120-infrastructure/SKILL.md) | Infrastructure for adding --base120 cognitive structuring to skill scripts at fleet scale. |
| [`base120-invert`](skills/base120-invert/SKILL.md) | The Contrarian. Inversion transformation of Base120 (IN1-IN20). Negate assumptions, find t |
| [`base120-perspect`](skills/base120-perspect/SKILL.md) | The Framer. Perspective transformation of Base120 (P1-P20). Name what is before anyone tou |
| [`base120-recurse`](skills/base120-recurse/SKILL.md) | The Iterator. Recursion transformation of Base120 (RE1-RE20). Apply patterns across scales |
| [`base120-systema`](skills/base120-systema/SKILL.md) | The Steward. Systems transformation of Base120 (SY1-SY20). Hold the whole — find the lever |
| [`base120-verify`](skills/base120-verify/SKILL.md) | Grade Base120 alignment reports as draft or receipt using artifact evidence fields — rejec |
| [`basen`](skills/basen/SKILL.md) | BaseN-tier multi-variant operator catalog. Lookup / search / apply / recommend across regi |
| [`bg-agent`](skills/bg-agent/SKILL.md) | Manage background subagents with tier-routed models, stripped tool contexts, lifecycle pru |
| [`bibliometric`](skills/bibliometric/SKILL.md) | Bibliometric analysis - publication counts, h-index, citation impact, co-authorship networ |
| [`bio-energy-physical-aggregator-research`](skills/bio-energy-physical-aggregator-research/SKILL.md) | > |
| [`biocognitive-assessment`](skills/biocognitive-assessment/SKILL.md) | Administer and score the HUMMBL Biocognitive OS Assessment — an 18-question diagnostic ins |
| [`bki-cite-audit`](skills/bki-cite-audit/SKILL.md) | Audit the BKI corpus bibliography — verify each citation exists, check claim-source match, |
| [`bki-evidence-flywheel`](skills/bki-evidence-flywheel/SKILL.md) | Search for new empirical evidence supporting BKI propositions (belonging, cognitive scienc |
| [`bki-reframe`](skills/bki-reframe/SKILL.md) | Capture and classify somatic-linguistic belonging reframes ("have to" vs "get to"). Names  |
| [`bki-session-export`](skills/bki-session-export/SKILL.md) | Package BKI session insights (new questions, corrections, theory updates) as a structured  |
| [`blocker-scanner`](skills/blocker-scanner/SKILL.md) | Scan local fleet surfaces for P0-P3 blockers — git, bus, rules, skills, tests, security, g |
| [`blog-draft`](skills/blog-draft/SKILL.md) | Draft technical blog post with outline, code samples, SEO metadata, and CTA |
| [`blueteam`](skills/blueteam/SKILL.md) | Defensive analysis — for a given asset, system, change, or red-team report, identify exist |
| [`board-meeting-orchestrator`](skills/board-meeting-orchestrator/SKILL.md) | > |
| [`bokka`](skills/bokka/SKILL.md) | > |
| [`brainstorm`](skills/brainstorm/SKILL.md) | Design-first exploration -- no code until the user approves a design. |
| [`branch-strategy`](skills/branch-strategy/SKILL.md) | Visualize branch topology, find stale/diverged branches, suggest cleanup. |
| [`brand`](skills/brand/SKILL.md) | DEPRECATED: Use brand-guidelines instead. This skill is retired as of 2026-08-19 and kept  |
| [`brand-admission`](skills/brand-admission/SKILL.md) | Brand-specific admission gate overlay that adds palette-token, visual-asset, and brand-gui |
| [`brand-factory`](skills/brand-factory/SKILL.md) | Generate novel brand name candidates from etymological roots, verify domain availability v |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | Applies HUMMBL's official design system tokens (two-tone green system with Grove and Verde |
| [`brew-audit`](skills/brew-audit/SKILL.md) | Audit Homebrew packages for outdated, unused, and security issues |
| [`briefing-history`](skills/briefing-history/SKILL.md) | List, search, compare, and show past morning briefings. |
| [`budget-plan`](skills/budget-plan/SKILL.md) | Monthly/quarterly budget allocation with variance tracking against actuals |
| [`build`](skills/build/SKILL.md) | Implementation surge mode — TDD-first, coverage-verified, deslop-checked. For feature buil |
| [`bulk-edit`](skills/bulk-edit/SKILL.md) | Apply the same edit across many files safely -- find, preview, apply, verify. |
| [`burn-rate-track`](skills/burn-rate-track/SKILL.md) | Track monthly burn rate with trend analysis. Monitors spend velocity, forecasts runway, an |
| [`bus`](skills/bus/SKILL.md) | Read or post to the coordination bus (append-only TSV message log). |
| [`bus-analytics`](skills/bus-analytics/SKILL.md) | Analyze coordination bus message patterns, frequency, and agent activity. |
| [`bus-audit`](skills/bus-audit/SKILL.md) | Parse the fleet bus TSV and produce a Rumsfeldian epistemological map -- known knowns, kno |
| [`bus-forensics`](skills/bus-forensics/SKILL.md) | >- |
| [`business-review`](skills/business-review/SKILL.md) | Review an external business using source-traceable evidence, explicit uncertainty, commerc |
| [`canary-deploy`](skills/canary-deploy/SKILL.md) | Gradual rollout verification -- deploy to subset, compare metrics, promote or rollback |
| [`canvas-design`](skills/canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. You should |
| [`cap-table`](skills/cap-table/SKILL.md) | Build or update an equity cap table. Founders, investors, option pool. Shows ownership %,  |
| [`case-study`](skills/case-study/SKILL.md) | Generate a structured case study from project data with metrics and outcomes |
| [`cashflow-project`](skills/cashflow-project/SKILL.md) | Project cash flow scenarios (base/bull/bear). Models inflows, outflows, and runway under m |
| [`catalog-write`](skills/catalog-write/SKILL.md) | Orchestrate catalog-style research writeups — individual pieces first, index last, git-tra |
| [`caveman-bespoke`](skills/caveman-bespoke/SKILL.md) | > |
| [`caveman-mode`](skills/caveman-mode/SKILL.md) | > |
| [`caveman-ponytail`](skills/caveman-ponytail/SKILL.md) | > |
| [`cd-monitor`](skills/cd-monitor/SKILL.md) | Monitor deployment, rollout, promotion, and post-release health status. Use when the user  |
| [`cert-tracker`](skills/cert-tracker/SKILL.md) | Track certification progress with deadlines, study hours, and requirements |
| [`chain-evolve`](skills/chain-evolve/SKILL.md) | Validate skill-chains.md against actual usage sequences — find emergent chains, dead chain |
| [`chain-validate`](skills/chain-validate/SKILL.md) | Verify every skill referenced in Skill Chains sections actually exists in the registry. Ca |
| [`changelog`](skills/changelog/SKILL.md) | Generate changelog between two refs using conventional commits. |
| [`changelog-digest`](skills/changelog-digest/SKILL.md) | Generate a human-readable digest of changes for non-technical stakeholders. |
| [`changelog-post`](skills/changelog-post/SKILL.md) | Turn a git changelog into a polished "What's New" blog post or social announcement |
| [`changelog-rss`](skills/changelog-rss/SKILL.md) | Publish changelog as RSS/Atom feed for external subscribers |
| [`changelog-subscribe`](skills/changelog-subscribe/SKILL.md) | Watch upstream dependencies for breaking changes and security advisories |
| [`chaos-test`](skills/chaos-test/SKILL.md) | Run controlled chaos tests to verify circuit breakers and kill switch behavior |
| [`chart`](skills/chart/SKILL.md) | Generate ASCII or SVG charts from data (bar, line, scatter, histogram, pie) |
| [`chatgpt-handoff`](skills/chatgpt-handoff/SKILL.md) | Ingest a ChatGPT response, route to downstream skills based on category tag, confirm scope |
| [`chembl-database`](skills/chembl-database/SKILL.md) | > |
| [`cherry-pick-safe`](skills/cherry-pick-safe/SKILL.md) | Cherry-pick commits with conflict detection, test verification, and bus notification. |
| [`churn-analysis`](skills/churn-analysis/SKILL.md) | Analyze client churn signals including engagement drops, support spikes, and renewal risk  |
| [`ci-monitor`](skills/ci-monitor/SKILL.md) | Monitor GitHub Actions -- list runs, check status, view logs, retry failed jobs. |
| [`ci-wait`](skills/ci-wait/SKILL.md) | Watch a CI run until completion and report pass/fail. |
| [`circuit-status`](skills/circuit-status/SKILL.md) | Show circuit breaker state per adapter. |
| [`citation-network`](skills/citation-network/SKILL.md) | Analyze citation networks - build directed graphs of citations, identify influential works |
| [`claim-verify`](skills/claim-verify/SKILL.md) | Extract all factual claims from text, verify against web sources, produce verdict table wi |
| [`claims-review`](skills/claims-review/SKILL.md) | Structured peer review of a claim set from an artifact or tool. Dual-mode (artifact claims |
| [`claude-api`](skills/claude-api/SKILL.md) | Build, debug, migrate, or optimize Claude API / Anthropic SDK apps, including prompt cachi |
| [`cli-design`](skills/cli-design/SKILL.md) | Design CLI interfaces with consistent flags, help text, and subcommands |
| [`cli-harness`](skills/cli-harness/SKILL.md) | > |
| [`client-report`](skills/client-report/SKILL.md) | Generate periodic client progress report from time logs, deliverables, and milestones |
| [`clinical-trials-database`](skills/clinical-trials-database/SKILL.md) | > |
| [`clinvar-database`](skills/clinvar-database/SKILL.md) | > |
| [`cloud-estate-manager`](skills/cloud-estate-manager/SKILL.md) | Inventory, reconcile, and record provenance for the HUMMBL cloud-estate against the closed |
| [`cloudflare`](skills/cloudflare/SKILL.md) | Build or debug Cloudflare platform work across Workers, Pages, KV, D1, R2, Workers AI, Vec |
| [`cloudflare-email-service`](skills/cloudflare-email-service/SKILL.md) | Build or debug Cloudflare Email Sending/Routing in Workers or apps, including bindings, RE |
| [`code-review`](skills/code-review/SKILL.md) | AI-powered code review using CodeRabbit. Default code-review skill. Trigger for any explic |
| [`codebase-tour`](skills/codebase-tour/SKILL.md) | Generate a guided tour of a codebase with entry points, key modules, data flow, and start- |
| [`codegen-eval`](skills/codegen-eval/SKILL.md) | > |
| [`coding-scheme`](skills/coding-scheme/SKILL.md) | Develop and apply qualitative coding schemes - deductive, inductive, or abductive coding w |
| [`coffee-chat`](skills/coffee-chat/SKILL.md) | Informal networking call prep. Who is this person, what to learn (not pitch), 3 questions, |
| [`cognitive-load`](skills/cognitive-load/SKILL.md) | Estimate cognitive load of UI elements using task complexity, information density, and Hic |
| [`color-contrast`](skills/color-contrast/SKILL.md) | Check and suggest color contrast ratios for WCAG compliance. [Maps to P9.] |
| [`color-team-engine`](skills/color-team-engine/SKILL.md) | Full-spectrum color team registry and dispatcher for security wargames. Reads color-regist |
| [`commerce-travel-culture-aggregator-research`](skills/commerce-travel-culture-aggregator-research/SKILL.md) | > |
| [`commit`](skills/commit/SKILL.md) | Stage and commit changes with Conventional Commits format and co-author attribution. |
| [`competitive-intel`](skills/competitive-intel/SKILL.md) | Research and compare competitors, alternatives, and market positioning. |
| [`complexity-score`](skills/complexity-score/SKILL.md) | Cyclomatic and cognitive complexity scoring per function with hotspot ranking and simplifi |
| [`compliance-calendar`](skills/compliance-calendar/SKILL.md) | Generate and track compliance deadlines, audit windows, certification expirations |
| [`concept-map`](skills/concept-map/SKILL.md) | Generate concept maps from code or docs — dependency graphs as Mermaid or ASCII diagrams |
| [`config-drift`](skills/config-drift/SKILL.md) | Detect configuration drift across machines in the mesh |
| [`config-matrix`](skills/config-matrix/SKILL.md) | Systematically test configuration combinations -- env vars, feature flags, provider settin |
| [`conflict-resolve`](skills/conflict-resolve/SKILL.md) | Guided merge conflict resolution with context from both sides and semantic understanding. |
| [`container-scan`](skills/container-scan/SKILL.md) | Scan container images for vulnerabilities, bloat, unnecessary packages, and hardening issu |
| [`content-calendar`](skills/content-calendar/SKILL.md) | Plan and track content across channels (blog, social, newsletter) with publish dates |
| [`content-design`](skills/content-design/SKILL.md) | Design product microcopy, labels, onboarding text, empty states, error messages, help text |
| [`content-review`](skills/content-review/SKILL.md) | Review outbound content (blog posts, one-pagers, social, docs) for accuracy, tone, brand,  |
| [`context-budget`](skills/context-budget/SKILL.md) | Monitor and optimize context window usage -- suggest compaction, trim bloat, manage token  |
| [`context-evolve`](skills/context-evolve/SKILL.md) | Measure token cost of every auto-injected file — rank by cost-per-relevance, suggest compr |
| [`context-export`](skills/context-export/SKILL.md) | Export live machine context as a pasteable block for claude.ai conversations |
| [`contract-drift`](skills/contract-drift/SKILL.md) | Detect drift in structured contracts from SKILL.md frontmatter against a frozen baseline;  |
| [`contract-negotiate`](skills/contract-negotiate/SKILL.md) | Review contract/SOW terms, flag risky clauses, and suggest alternatives |
| [`contract-review`](skills/contract-review/SKILL.md) | Review and validate contract schemas for breaking changes and compatibility. |
| [`contract-test`](skills/contract-test/SKILL.md) | Verify service responses against contract schemas in contracts/ directory |
| [`contractor-agreement`](skills/contractor-agreement/SKILL.md) | Draft an Independent Contractor Agreement (ICA). Covers scope, rate, IP assignment, confid |
| [`contributor-guide`](skills/contributor-guide/SKILL.md) | Generate CONTRIBUTING.md with dev setup, PR process, code style, and testing requirements  |
| [`control-catalog`](skills/control-catalog/SKILL.md) | Manage a catalog of governance controls mapped to multiple frameworks (NIST, ISO, SOC 2). |

## License

Apache-2.0 © HUMMBL, LLC
