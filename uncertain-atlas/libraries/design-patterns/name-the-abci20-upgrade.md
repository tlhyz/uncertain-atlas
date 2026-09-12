# 模式：把 ABCI 2.0 协调升级三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**例**：[必须协调升级 ≠ 已经只改 VoteExtensionsEnableHeight](../../tracks/implementation/worked-example-abci20-upgrade-vs-height.md)。

## 三个名字

1. **必须协调升级不是已经只改 VoteExtensionsEnableHeight：** 看见字段在不是已经切完。
2. **h_e 必须高于当前不是已经能写成当前高度：** 看见升级过了不是已经能写成这一高。
3. **引擎按当前高度决定存什么要什么不是已经按创世配好了：** 看见创世写了启用高度不是已经按那一高在存。

## 为什么要分开叫

官方把换二进制的协调升级、升级之后才能写高于当前的启用高度、引擎按当前高度决定存什么要什么写成三件事。把它们叫成一个「看见填了启用高度就已经切完」，会把 H / H+1 Prepare 切换、治理 panic 和 PBTS 启用高度一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了启用高度就已经切完」，先数清问的是必须协调升级不是已经只改 VoteExtensionsEnableHeight、h_e 必须高于当前不是已经能写成当前高度，还是引擎按当前高度决定存什么要什么不是已经按创世配好了，再决定要不要同一次发布。
