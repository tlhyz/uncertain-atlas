# 反模式：把 prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事（416 余量） 写成已经 已经会调 Process / 已经还能再 Reject / 已经交差

**层次**：实现 / prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事（416 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应**：[`../tracks/implementation/worked-example-ptime-notcall-vs-bundled.md`](../tracks/implementation/worked-example-ptime-notcall-vs-bundled.md)。

把 prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事（416 余量） 写成已经 已经会调 Process / 已经还能再 Reject / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 prevote-or-nil 正式三事（416 余量），必须分开 not already will-call、not already still-reject、not already settled 三件事，不要和 416 / 354 / 351 / 1094 / 1095 糊成一句。

也不是：

- [ptime-notproc-sold-as-bundled](ptime-notproc-sold-as-bundled.md) 是先验块头仍未跑过 Process 单句边界（1095 item 2），不是本页看 prevote 仍未会调 Process 边界。
- Process 调用是同步的就已经能稍后改裁决是不变量 354，不是本页还没调仍未能再 Reject 边界。
