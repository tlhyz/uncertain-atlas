# 模式：把 PbtsEnableHeight 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**例**：[写成 0 不是已经启用 PBTS ≠ 已经填了 Precision 就是 PBTS](../../tracks/implementation/worked-example-pbts-height-vs-params.md)。

## 三个名字

1. **写成 0 不是已经启用 PBTS 不是已经填了 Precision 就是 PBTS：** 看见字段在不是已经切算法。
2. **H 之前仍用 BFT Time 不是已经切到 PBTS：** 看见到了 H 不是已经是 MTP。
3. **启用之后不能关不是已经是扩展启用高度那种切换：** 看见必须比当前高不是已经能改回 0。

## 为什么要分开叫

官方把 0 表示关掉、到了 H 才换钟、启用之后不能关写成三件事。把它们叫成一个「看见填了同步参数就已经启用」，会把 Precision / MessageDelay、块时间点名和扩展启用高度一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了同步参数就已经启用」，先数清问的是写成 0 不是已经启用 PBTS 不是已经填了 Precision 就是 PBTS、H 之前仍用 BFT Time 不是已经切到 PBTS，还是启用之后不能关不是已经是扩展启用高度那种切换，再决定要不要同一次发布。
