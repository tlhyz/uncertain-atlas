# 反模式：把 ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事（416 余量） 写成已经 已经填了 TimeoutPropose / 已经离开关键路径 / 已经会调 Process

**层次**：实现 / ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事（416 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应**：[`../tracks/implementation/worked-example-ptime-notcfg-vs-bundled.md`](../tracks/implementation/worked-example-ptime-notcfg-vs-bundled.md)。

把 ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事（416 余量） 写成已经 已经填了 TimeoutPropose / 已经离开关键路径 / 已经会调 Process，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposeTimeout 正式三事（416 余量），必须分开 not already timeout-propose、not already left-critical、not already will-call 三件事，不要和 416 / 327 / 354 / 1095 / 1096 糊成一句。

也不是：

- [ionce-notchg-sold-as-bundled](ionce-notchg-sold-as-bundled.md) 是 InitChain Validators-as-update 仍未改了集合边界（412/1093），不是本页 ProposeTimeout 仍未填了 TimeoutPropose 边界。
- 立刻整块执行就已经离开关键路径是不变量 327，不是本页进了这一轮仍未离开关键路径边界。
