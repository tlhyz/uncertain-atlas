# 反模式：把 Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事（404 余量） 写成已经 已经对上 AppHash / 已经是按键查 / 已经交差

**层次**：实现 / Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事（404 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-fhash-notalign-vs-bundled.md`](../tracks/implementation/worked-example-fhash-notalign-vs-bundled.md)。

把 Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事（404 余量） 写成已经 已经对上 AppHash / 已经是按键查 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 锚 正式三事（404 余量），必须分开 not already apphash-aligned、not already keyed-lookup、not already settled 三件事，不要和 404 / 325 / 431 / 1100 / 1102 糊成一句。

也不是：

- [fhash-notheader-sold-as-bundled](fhash-notheader-sold-as-bundled.md) 是空或硬编码仍未印进本头单句边界（1100 item 1），不是本页 Query 锚仍未对上 AppHash 边界。
- ProofOp.type 就已经是按键查是不变量 325，不是本页有锚仍未是按键查边界。
