# 反模式：把 proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事（417 余量） 写成已经 已经不用再 Process / 已经保证是这一次 / 已经交差

**层次**：实现 / proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事（417 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-htmt-notskip-vs-bundled.md`](../tracks/implementation/worked-example-htmt-notskip-vs-bundled.md)。

把 proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事（417 余量） 写成已经 已经不用再 Process / 已经保证是这一次 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare-first 正式三事（417 余量），必须分开 not already skip-process、not already same-round、not already settled 三件事，不要和 417 / 351 / 416 / 1098 / 1099 糊成一句。

也不是：

- [ptime-notcall-sold-as-bundled](ptime-notcall-sold-as-bundled.md) 是 prevote-or-nil 仍未会调 Process 边界（416/1096），不是本页提议者先走 Prepare 仍未不用再 Process 边界。
- Process 也会在提议者那边叫就已经不用再 Process 是不变量 351，不是本页自己是提议者仍未保证是这一次边界。
