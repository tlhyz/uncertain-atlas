# 模式：把 FinalizeBlockResponse consensus_param_updates H→H+1 not effective at H / not validator_updates H+2 / not app-requirements delay 正式三事（471 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[H→H+1 ≠ bundled（471）](../../tracks/implementation/worked-example-fincparam-nothatH-vs-bundled.md)。

## 三个名字

1. **H apply to H+1 不是已经在块 H 生效：** 看见用于 H+1，不是已经在块 H 验这块 interchangeable / 710 fincparam-nothatH interchangeable。
2. **看见能指 H+1 不是 validator_updates H+2 才计票：** 看见 H→H+1，不是已经 459 interchangeable。
3. **看见 Usage 这句 不是 app requirements 生效延迟：** 看见 H→H+1 单句，不是已经 333 interchangeable。

官方把 FinalizeBlockResponse consensus_param_updates 三条核心句拆成三个名字。把它们叫成一个「看见回了 consensus_param_updates 就已经在块 H 生效」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事（471 余量），先数清问的是 H→H+1 是不是已经在块 H 生效、是不是集合 H+2 才计票 / 459、还是看见 Usage 是不是 app requirements 延迟 / 333，再决定要不要同一次发布。471 fincparam vs heffective bundled unbundling 在本页 item 1 启动。
