# Public HUMMBL implementation sources

Checked 2026-10-01 against [OSS revision 5f915a3][oss-snapshot]. These links
pin the inspected source. For subsequent changes, use the repository's
[current package inventory][current-inventory].

## Languages and contracts

| Language | Source | Scope at the inspected revision |
| --- | --- | --- |
| Python | [Base120][base120] | Reasoning operator SDK and canonical registry |
| Python | [Governance][governance] | Runtime governance primitives |
| Python | [Typed tuples][tuples] | Tuple schemas, envelopes and references |
| TypeScript | [Tuple reference][typescript] | Tuple records and serialization |
| Rust | [Tuple reference][rust] | Tuple records and serialization |
| Lean 4 | [Formalization tree][lean] | Formalization source; outside Python CI |
| Node.js | [Base120 MCP canary][node] | Technical canary; public launch held |

The Rust and TypeScript references are inside the Python tuple package's
`reference_impl/` directory. The package's primary-language badge does not
describe all of its source implementations. Check the respective manifests
for runtime dependencies and use each implementation's contract documentation.

The Node canary's [product manifest][node-product] records
`public_launch: false` and admission blockers. This map supplies a source
link and does not supply an npm installation or launch instruction.

The [official Base120 skill][skill] in this repository includes its own
versioned offline SDK snapshot. Its [distribution record][distribution]
pins copied source; it is maintained independently from the OSS tree's SDK
version. Use that whole skill directory for offline operator lookup.

## Service adapter source

| Service | Source | Requirements or scope recorded by the package |
| --- | --- | --- |
| Discord | [Local MCP adapter][discord] | Bot API and bot-token configuration |
| Signal | [Local MCP adapter][signal] | Consult package setup requirements |
| 1Password | [CLI MCP adapter][onepassword] | 1Password CLI integration |
| Vapi | [Voice MCP adapter][voice] | Voice API and credential configuration |
| Proton | [Local MCP adapter][proton] | Mail Bridge; Drive/Calendar limits |

These entries are an inspected selection of public source. Use the package
READMEs for configuration and supported behavior. Package publication,
provider access and live runtime qualification require their own evidence;
this directory map does not establish those outcomes.

## Verification receipt

The non-truncated Git tree and package READMEs were read at the full OSS
revision `5f915a301fef483b72e7353ccb0833ca3dd2d6a3`. Rust and TypeScript
reference source headers were inspected. The Node product manifest supplied
the release-hold status. No provider credentials, calls, runtime launches,
package publication or implementation test execution were used for this map.

Sources are already public in `hummbl-io/oss`. Repository visibility and
reference links were checked through GitHub's API on the date above.

[oss-snapshot]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3
[current-inventory]: https://github.com/hummbl-io/oss/blob/main/README.md#packages
[base120]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/base120
[governance]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-governance
[tuples]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-tuples
[typescript]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-tuples/reference_impl/typescript
[rust]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-tuples/reference_impl/rust
[lean]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/lean/hummbl-formalization
[node]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/node/mcp-base120
[node-product]: https://github.com/hummbl-io/oss/blob/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/node/mcp-base120/product.json
[skill]: ../skills/base120/SKILL.md
[distribution]: ../skills/base120/distribution.json
[discord]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-mcp-discord
[signal]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-mcp-signal
[onepassword]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-mcp-onepassword
[voice]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-mcp-voice
[proton]: https://github.com/hummbl-io/oss/tree/5f915a301fef483b72e7353ccb0833ca3dd2d6a3/packages/python/hummbl-mcp-proton
