# 模式：把写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事（343 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**例**：[写成 0 not already enabled ≠ bundled（343）](../../tracks/implementation/worked-example-pbtsheight-notzero-vs-bundled.md)。

## 三个名字

1. **写成 0 不是 already enabled：** 看见写成 0 / 大于 0 才是启用高度 / `PbtsEnableHeight`，不是已经启用 PBTS interchangeable / 已经 enabled interchangeable / 已经启用交差 interchangeable，不是 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable。

2. **填了 Precision 不是 already precision-pbts：** 看见填了 Precision / MessageDelay / 同步参数在，不是已经填了 Precision 就是 PBTS interchangeable / 已经 precision-pbts interchangeable / 已经同步参数交差 interchangeable，不是 761 precision-notmsgdelay interchangeable / 762 precision-notpbts interchangeable。

3. **字段在 不是 already switched：** 看见字段在 / 配置里有 PbtsEnableHeight / FeatureParams 里有这一栏，不是已经切算法 interchangeable / 已经 switched interchangeable / 已经切到 PBTS 交差 interchangeable，不是 40 block-time interchangeable / 783 pbtsheight-notbfttime interchangeable。

官方把 0 表示关掉、同步参数、字段在配置里写成三个名字。把它们叫成一个「看见写成 0 就已经启用 interchangeable / 就已经填了 Precision 就是 PBTS interchangeable / 就已经切到 PBTS interchangeable」，会把 not already enabled、not already precision-pbts、not already switched 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事（343 余量），先数清问的是写成 0 是不是 already enabled / 343 / pbtsheight-sold-as-enabled，是不是填了 Precision 是不是 already precision-pbts，还是字段在 是不是 already switched，再决定要不要同一次发布。343 pbtsheight vs params bundled unbundling 在本页 item 1 启动。
