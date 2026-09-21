# 反模式：看见填了 Precision 就当成已经是 MessageDelay / 看见填了两个就当成已经启用 PBTS / 看见用于 PBTS 就当成已经是永恒常数

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**例**：[填了 Precision ≠ 已经是 MessageDelay](../../tracks/implementation/worked-example-precision-vs-msgdelay.md)。

## 塌法

1. 看见填了 `SynchronyParams.Precision` / 看见提议者钟偏有界，就当成已经是 `MessageDelay`，或当成已经 timely。
2. 看见填了两个 / 看见这两个参数用于 PBTS，就当成已经启用 PBTS，或当成已经不能关。
3. 看见用于 PBTS / 看见能出合法提案，就当成已经是永恒常数，或当成已经是 BFT Time 中位数。

## 为什么会出事

官方写：Precision 限制钟偏，MessageDelay 限制提案消息还能走多久。两把尺都由 PBTS 使用。填了两个不是已经到了 PbtsEnableHeight。用于 PBTS 不是已经抄成产品常数，也不是已经是中位数。

## 和相邻反模式

- [precision-notpbts-sold-as-bundled](precision-notpbts-sold-as-bundled.md) 是填了两个不是已经启用 PBTS item 2 单句边界，不是本页 Precision bundled 全段。
- [precision-notmsgdelay-sold-as-bundled](precision-notmsgdelay-sold-as-bundled.md) 是填了 Precision 不是已经是 MessageDelay item 1 单句边界，不是本页 Precision bundled 全段。
- [pbts-sold-as-mtp](pbts-sold-as-mtp.md) 是提议者时间被写成 MTP / 中位数 / 墙上现在，不是本页这种两把尺互替。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H ≠ 已经 Prepare 带了扩展，不是本页这种同步参数。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径，不是本页。
