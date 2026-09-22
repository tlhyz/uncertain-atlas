# 反模式：看见写成 0 就当成已经启用 PBTS / 看见填了 Precision 就当成已经是 PBTS / 看见 H 之前仍用 BFT Time 就当成已经切到 PBTS / 看见启用之后不能关就当成已经是扩展启用高度那种切换

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**例**：[写成 0 不是已经启用 PBTS ≠ 已经填了 Precision 就是 PBTS](../../tracks/implementation/worked-example-pbts-height-vs-params.md)。

## 塌法

1. 看见写成 0 / 看见大于 0 才是启用高度，就当成已经启用 PBTS，或当成已经填了 Precision 就是 PBTS。
2. 看见 H 之前或写成 0 仍用 BFT Time / 看见到了 H 才用 PBTS，就当成已经切到 PBTS，或当成已经是 MTP。
3. 看见启用之后不能关 / 看见不能写成当前高度或更矮，就当成已经是扩展启用高度那种切换，或当成已经能关。

## 为什么会出事

官方写：0 表示 PBTS 关掉；大于 0 才是启用高度。到了这一高才用 PBTS 出时间戳、验时间戳；之前或写成 0 仍用 BFT Time。一旦启用就不能关，也不能写成当前高度或更矮。

## 和相邻反模式

- [pbtsheight-notzero-sold-as-bundled](pbtsheight-notzero-sold-as-bundled.md) 是写成 0 not already enabled / not already precision-pbts / not already switched 正式三事（343 item 1），不是本页 bundled 全段 alone。
- [pbtsheight-notbfttime-sold-as-bundled](pbtsheight-notbfttime-sold-as-bundled.md) 是 H 之前仍用 BFT Time not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 item 2），不是本页 bundled 全段 alone。
- [pbtsheight-notveheight-sold-as-bundled](pbtsheight-notveheight-sold-as-bundled.md) 是启用之后不能关 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 item 3），不是本页 bundled 全段 alone。
- [precision-sold-as-msgdelay](precision-sold-as-msgdelay.md) 是 Precision 不是已经是 MessageDelay，不是本页这种写成 0 不是已经启用。
- [pbts-sold-as-mtp](pbts-sold-as-mtp.md) 是块时间必须点名算法，不是本页这种 H 之前仍用 BFT Time 不是已经切到 PBTS。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展，不是本页这种启用之后不能关不是已经是那种切换。
