# 模式：把 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事（382 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[回了事件 not already mustdet ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notmustdet-vs-bundled.md)。

## 三个名字

1. **回了事件 不是 already mustdet：** 看见回了事件 / Finalize 回包 events 标成非确定 / events 的 Deterministic 列是 No，不是已经必须确定 interchangeable / 已经 mustdet interchangeable / 已经必须像状态那样只依赖上一份状态和决定块交差 interchangeable，不是 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable。

2. **标成非确定 不是 already settled：** 看见标成非确定 / Deterministic 是 No / 事件不必像状态那样确定，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 316 txresults interchangeable / 894 syncingheight-notempty interchangeable。

3. **能按类型键值索引 不是 already ordered：** 看见能按类型键值索引 / 有 events 类型键值 / 能按账户建索引，不是已经是结果列表同一顺序 interchangeable / 已经 ordered interchangeable / 已经是共识顺序交差 interchangeable，不是 316 txresults interchangeable / 382 syncingheight item 1 interchangeable。

官方把回了事件、不是已经交差、不是已经是结果列表同一顺序写成三个名字。把它们叫成一个「看见回了事件就已经必须确定 interchangeable / 就已经交差 interchangeable / 就已经是结果列表同一顺序 interchangeable」，会把 not already mustdet、not already settled、not already ordered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事（382 余量），先数清问的是回了事件 是不是 already mustdet / 382 / syncingheight-sold-as-history，是不是标成非确定 是不是 already settled，还是能按类型键值索引 是不是 already ordered，再决定要不要同一次发布。382 syncingheight-vs-history bundled unbundling 在本页 item 3 完成。
