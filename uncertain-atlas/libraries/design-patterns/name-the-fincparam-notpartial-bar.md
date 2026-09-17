# 模式：把 FinalizeBlockResponse consensus_param_updates gas/size/Deterministic Yes not only one field / not finrespend bundled / not next_block_delay nondet means whole gate 正式三事（471 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[gas/size/Deterministic ≠ bundled（471）](../../tracks/implementation/worked-example-fincparam-notpartial-vs-bundled.md)。

## 三个名字

1. **gas/size/Deterministic Yes 不是只填一项：** 看见能改 gas/size，不是已经 319 interchangeable / 711 fincparam-notpartial interchangeable。
2. **看见 Deterministic = Yes 不是回包末栏 bundled：** 看见 consensus_param_updates 栏，不是已经 432 interchangeable。
3. **看见 Usage 这句 不是 next_block_delay 非确定代表整门非确定：** 看见 Deterministic = Yes，不是已经 469 interchangeable。

官方把 FinalizeBlockResponse consensus_param_updates 三条核心句拆成三个名字。把它们叫成一个「看见回了 consensus_param_updates 就已经在块 H 生效」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates gas/size 正式三事（471 余量），先数清问的是 gas/size 是不是只填一项 / 319、是不是回包末栏 bundled / 432、还是看见 Usage 是不是 next_block_delay 非确定代表整门非确定 / 469，再决定要不要同一次发布。471 fincparam vs heffective bundled unbundling 在本页 item 2 续。
