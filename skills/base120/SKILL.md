---
name: base120
description: Look up and apply HUMMBL Base120 mental models via MCP server.
version: 0.1.0
execution-mode: advisory
category: fleet-ops
status: candidate
---
# Base120 Mental Model Alignment

Look up, search, and apply HUMMBL Base120 mental models. Uses the HUMMBL MCP server (enhanced) for model data when available, with a built-in reference fallback.

## Usage

```bash
[base120] P1                        # Look up a specific model by code
[base120] "root cause"              # Search models by keyword
[base120] apply "We keep adding features but velocity is dropping"
[base120] recommend "How should we prioritize the Q2 roadmap?"
[base120] transformations           # List all 6 transformations
```

## Task

$ARGUMENTS

## The Base120 Framework

120 mental models organized into 6 transformations, 20 models each:

| Code | Transformation | Focus |
|------|---------------|-------|
| **P** (1-20) | Perspective | Frame and name what is. Anchor or shift point of view. |
| **IN** (1-20) | Inversion | Reverse assumptions. Examine opposites, edges, negations. |
| **CO** (1-20) | Composition | Combine parts into wholes. Build complexity from simplicity. |
| **DE** (1-20) | Decomposition | Break wholes into parts. Simplify by separation. |
| **RE** (1-20) | Recursion | Apply patterns across scales. Self-reference and iteration. |
| **SY** (1-20) | Systems | Understand how parts interact, create emergent behavior, and shape dynamics. |

## Execution

### Mode: Lookup (code like P1, IN7, CO3)
1. Try the HUMMBL MCP server first: call `get_model` with the code
2. If MCP unavailable, use the built-in quick reference below
3. Return: code, name, definition, priority, transformation context

### Mode: Search (keyword or phrase)
1. Try MCP: call `search_models` with the query
2. If MCP unavailable, search the quick reference
3. Return: matching models ranked by relevance

### Mode: Apply (prefixed with "apply")
Analyze a situation through Base120 lenses:
1. Parse the problem description
2. Try MCP: call `recommend_models` with the problem
3. If MCP unavailable, manually identify 3-5 relevant models
4. For each model, explain:
   - **Why it applies**: How this model illuminates the situation
   - **What it reveals**: The insight or reframe it provides
   - **Action**: A concrete next step derived from the model
5. Format as an alignment report

### Mode: Recommend (prefixed with "recommend")
1. Try MCP: call `recommend_models` with the question
2. Return 3-5 models with priority weighting
3. Explain the recommendation chain

### Mode: Transformations
List all 6 transformations with descriptions and example models.

## MCP Server

The HUMMBL enhanced MCP server provides 10 tools:

| Tool | Purpose |
|------|---------|
| `get_model` | Get specific model by code (P1, IN1, etc.) |
| `list_all_models` | List all 120 models with optional filter |
| `search_models` | Search by keyword |
| `get_transformation` | Get transformation details (P, IN, CO, DE, RE, SY) |
| `search_problem_patterns` | Find patterns by keyword/synonym |
| `recommend_models` | Recommendations for a given problem |
| `get_related_models` | Model relationship graph |
| `semantic_search` | Deep semantic search across all models |
| `get_workflow` | Get structured workflow by ID |
| `match_workflow` | Match a problem to the best workflow |

**Server location**: `$HOME/hummbl-mcp-enhanced/enhanced-server.js`

To check if MCP is available, attempt the tool call. If it fails, fall back to the built-in reference.

## Quick Reference (Top Models by Priority)

### Priority 1 (use frequently)
- **P1** First Principles Framing -- Reduce to foundational truths
- **P2** Stakeholder Mapping -- Identify all interested parties
- **P4** Lens Shifting -- Adopt different interpretive frameworks
- **IN1** Subtractive Thinking -- Improve by removing, not adding
- **IN2** Premortem Analysis -- Assume failure, work backward
- **CO1** Synergy Principle -- Whole greater than sum of parts
- **CO2** Chunking -- Break large wholes into manageable, processable units
- **DE1** Root Cause Analysis (5 Whys) -- Trace symptoms to underlying causes
- **RE1** Recursive Improvement (Kaizen) -- Apply iterative, incremental improvement at every scale
- **SY1** Leverage Points -- Find where small interventions produce large systemic change

### Priority 2 (use regularly)
- **P3** Identity Stack -- Multiple nested identities
- **P7** Perspective Switching -- Rotate viewpoints
- **P10** Context Windowing -- Define scope boundaries
- **P15** Assumption Surfacing -- Make beliefs explicit
- **IN3** Problem Reversal -- Solve the inverse
- **IN7** Boundary Testing -- Find system limits
- **IN9** Backward Induction -- Start from end state
- **IN10** Red Teaming -- Adversarial review
- **CO3** Functional Composition -- Chain functions so each output feeds the next input
- **CO6** Gestalt Integration -- Perceive and leverage whole patterns rather than isolated components
- **DE2** Factorization -- Separate multiplicative components to understand relative contribution of each factor
- **RE2** Feedback Loops -- Find reinforcing/balancing feedback loops in a system

## Alignment Report Format

When applying models to a situation:

```
Base120 Alignment | <situation summary>
═══════════════════════════════════════

Problem: <1-2 sentence description>

Models Applied:
  1. <CODE> <Name> (Priority <N>)
     Why: <why this model applies>
     Reveals: <the insight>
     Action: <concrete next step>

  2. <CODE> <Name> (Priority <N>)
     ...

Transformation Pattern: <which transformations dominate and why>
Primary Recommendation: <the single most important action>
```

## Integration with Other Skills

- **/aar**: AAR sections reference Base120 codes (e.g., "DE1: Root Cause Analysis (5 Whys)")
- **/apex + [nexus]**: Apex/Nexus can invoke Base120 alignment for strategic decisions and canonical-surface checks
- **/brand**: Base120 is core HUMMBL IP -- always present it with brand voice

## Constraints

- Do NOT invent model codes or definitions -- use only the official 120
- Do NOT force-fit models -- if none apply well, say so
- Priority ratings (1-5) indicate frequency of use, not importance
- When citing Base120 in other outputs (AARs, reports), use format: `<CODE>: <Name>`
- The MCP server is the source of truth; the quick reference here is a fallback subset
- When the MCP server is unreachable, tag all Base120 references as `[UNVERIFIED - MCP unavailable]` rather than guessing model names, definitions, or transformation labels from memory
- NEVER approximate or paraphrase Base120 definitions — use exact text from the MCP server or say "unable to verify"
- SY = **Systems** (NOT Synthesis). This is a known hallucination pattern. Always verify transformation names against the MCP server.
