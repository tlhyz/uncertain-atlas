# 模式：把快照装回三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**例**：[Offer 收下 ≠ 已经装完](../../tracks/implementation/worked-example-snapshot-restore-vs-offer.md)。

## 三个名字

1. **Offer 收下不是已经装完：** 看见选了这份不是已经有了全部块。
2. **一块 chunk 收下不是已经齐：** 看见回了再拉不是已经交差。
3. **拉失败换一份不是已经能接着装：** 看见换了一份不是已经能接着上次。

## 为什么要分开叫

官方把收下 Offer 再按顺序装、应用回再拉或拒快照、拉失败换一份要应用自己决定能不能重开写成三件事。把它们叫成一个「看见 Offer 收下就已经装完」，会把轻验 AppHash、启动对齐和崩溃三步一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「快照已经收下」，先数清问的是 Offer 收下不是已经装完、一块 chunk 收下不是已经齐，还是拉失败换一份不是已经能接着装，再决定要不要同一次发布。
