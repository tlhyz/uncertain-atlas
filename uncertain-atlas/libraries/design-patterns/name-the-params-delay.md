# 模式：把 ConsensusParams H→H+1 生效三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**例**：[本高回了 ConsensusParams ≠ 已经在本高生效](../../tracks/implementation/worked-example-params-delay-vs-set.md)。

## 三个名字

1. **本高回了不是已经在本高生效：** 看见本高 Finalize 回了 ConsensusParams 不是本高提议已经按新参数。
2. **H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票：** 看见参数走 H→H+1 不是新人已经在 H+1 计票。
3. **参数更新写了 H+1 不是已经是扩展启用高度那种切换：** 看见立刻生效不是已经只改填的那一项。

## 为什么要分开叫

官方把 H 回了就对 H+1 立刻生效、集合更新只在 H+2 生效、扩展启用高度的 H / H+1 Prepare 切换写成三件事。把它们叫成一个「看见本高回了就已经在本高生效」，会把换人延迟、空/没回/只填一项和扩展启用高度一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「本高回了 ConsensusParams 就已经在本高生效」，先数清问的是本高回了不是已经在本高生效、H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票，还是参数更新写了 H+1 不是已经是扩展启用高度那种切换，再决定要不要同一次发布。
