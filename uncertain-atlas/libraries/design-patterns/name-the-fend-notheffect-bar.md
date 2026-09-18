# 模式：点名 fend-notheffect 杠

**层次**：实现 / FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事（432 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-fend-notheffect-vs-bundled.md`](../tracks/implementation/worked-example-fend-notheffect-vs-bundled.md)。

- **consensus_param_updates 不是已经在块 H 生效：** 看见回了 consensus_param_updates，不是已经在块 H 生效 interchangeable / 1073 fend-notheffect interchangeable。
- **看见能指 H+1 不是已经在 H+1 换人：** 看见能指 H+1，不是已经在 H+1 换人 interchangeable。
- **看见有 ConsensusParams 不是已经只改这一项：** 看见有 ConsensusParams，不是已经只改这一项 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 consensus_param_updates 正式三事（432 余量），先数清问的是是不是已经在块 H 生效、是不是已经在 H+1 换人、还是看见有 ConsensusParams 是不是已经只改这一项，再决定要不要同一次发布。432 finrespend vs params bundled unbundling 在本页 item 1 启动。
