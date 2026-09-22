# 模式：把 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**例**：[H 之前仍用 BFT Time not already switched-to-pbts ≠ bundled（343）](../../tracks/implementation/worked-example-pbtsheight-notbfttime-vs-bundled.md)。

## 三个名字

1. **H 之前仍用 BFT Time 不是 already switched-to-pbts：** 看见 H 之前或写成 0 仍用 BFT Time / 到了 H 才用 PBTS / 旧钟还在，不是已经切到 PBTS interchangeable / 已经 switched-to-pbts interchangeable / 已经切到 PBTS 交差 interchangeable，不是 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable。

2. **到了 H 不是 already mtp：** 看见到了 H / 写了用于 PBTS / 配置高度到了，不是已经是 MTP interchangeable / 已经 mtp interchangeable / 已经中位数时间交差 interchangeable，不是 pbts-sold-as-mtp interchangeable / 40 block-time interchangeable。

3. **能出合法提案 不是 already clock-changed：** 看见还能出合法提案 / 仍能出合法提案 / 提案时间戳合法，不是已经换完钟 interchangeable / 已经 clock-changed interchangeable / 已经换钟交差 interchangeable，不是 782 pbtsheight-notzero interchangeable / 784 pbtsheight-notveheight interchangeable。

官方把旧钟还在、到了启用高度、还能提案写成三个名字。把它们叫成一个「看见 H 之前仍用 BFT Time 就已经切到 PBTS interchangeable / 就已经是 MTP interchangeable / 就已经换完钟 interchangeable」，会把 not already switched-to-pbts、not already mtp、not already clock-changed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 余量），先数清问的是 H 之前仍用 BFT Time 是不是 already switched-to-pbts / 343 / pbtsheight-sold-as-enabled，是不是到了 H 是不是 already mtp，还是能出合法提案 是不是 already clock-changed，再决定要不要同一次发布。343 pbtsheight vs params bundled unbundling 在本页 item 2 续。
