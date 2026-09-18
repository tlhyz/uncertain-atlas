# 模式：点名 prepwhen-notprio 杠

**层次**：实现 / PrepareWhen collect not already raw-proposal / not already full-pool / not already validValue-skip 正式三事（505 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应**：[`../tracks/implementation/worked-example-prepwhen-notprio-vs-bundled.md`](../tracks/implementation/worked-example-prepwhen-notprio-vs-bundled.md)。

- **从池子按优先级收未决交易 不是已经 preliminary raw proposal bundled：看见从池子按优先级收未决交易，不是已经 preliminary raw proposal bundled interchangeable / 1310 prepwhen-notprio interchangeable。**
- **造头再调 Prepare 不是已经整池可见：看见造头再调 Prepare，不是已经整池可见 interchangeable / 1310 prepwhen-notprio interchangeable。**
- **从池子按优先级收未决交易 不是已经 validValue 非 nil 跳过 Prepare：看见从池子按优先级收未决交易，不是已经 validValue 非 nil 跳过 Prepare interchangeable / 1310 prepwhen-notprio interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事（505 余量），必须分开 not already raw-proposal、not already can-change-after-return、not already Prepare-list 三件事。
