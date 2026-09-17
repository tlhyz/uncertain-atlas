# 模式：把 FinalizeBlockResponse consensus_param_updates may be empty keep current not params cleared / not InitChain empty params / not empty-update bundled 正式三事（471 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[may ≠ bundled（471）](../../tracks/implementation/worked-example-fincparam-notcleared-vs-bundled.md)。

## 三个名字

1. **may be empty keep current 不是已经清掉参数：** 看见 keep current values，不是已经清掉 interchangeable / 712 fincparam-notcleared interchangeable。
2. **看见空着 不是 InitChain 空参数：** 看见 empty，不是已经没有参数 interchangeable。
3. **看见 Usage 这句 不是空更新 bundled：** 看见 may be empty 单句，不是已经 458 / 319 interchangeable。

官方把 FinalizeBlockResponse consensus_param_updates 三条核心句拆成三个名字。把它们叫成一个「看见回了 consensus_param_updates 就已经在块 H 生效」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates may be empty 正式三事（471 余量），先数清问的是 empty 是不是已经清掉参数、是不是 InitChain 空参数、还是看见 Usage 是不是空更新 bundled / 458 / 319，再决定要不要同一次发布。471 fincparam vs heffective bundled unbundling 在本页 item 3 完成。
