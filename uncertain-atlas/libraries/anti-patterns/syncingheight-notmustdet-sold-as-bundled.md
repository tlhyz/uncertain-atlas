# 反模式：把 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事（382 余量）说成已经必须确定 / 已经交差 / 已经是结果列表同一顺序

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了事件 not already mustdet ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notmustdet-vs-bundled.md)。

## 卖法

把回了事件 / Finalize 回包 events 标成非确定 / events 的 Deterministic 列是 No 写成已经必须确定 interchangeable / 已经 mustdet interchangeable / 已经必须像状态那样只依赖上一份状态和决定块交差 interchangeable / 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable；把标成非确定 / Deterministic 是 No / 事件不必像状态那样确定 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把能按类型键值索引 / 有 events 类型键值 / 能按账户建索引 写成已经是结果列表同一顺序 interchangeable / 已经 ordered interchangeable / 已经是共识顺序交差 interchangeable，或已经和 382 syncingheight bundled / syncingheight-sold-as-history interchangeable / 895 syncingheight-notmustdet interchangeable。

## 为什么错

官方把回了事件、不是已经交差、不是已经是结果列表同一顺序写成三件独立的实现事。把它们卖成 already mustdet interchangeable / already settled interchangeable / already ordered interchangeable，会把 not already mustdet、not already settled、not already ordered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事（382 余量），必须分开 not already mustdet、not already settled、not already ordered 三件事，不要和 382 / 342 / 316 / 323 糊成一句。

## 和相邻反模式

- [syncingheight-sold-as-history](syncingheight-sold-as-history.md) 是 syncingheight bundled 全段，不是本页回了事件 item 3 单句边界。
- [syncingheight-nothistory-sold-as-bundled](syncingheight-nothistory-sold-as-bundled.md) 是填了目标 item 1 单句边界，不是本页 not already mustdet 边界。
- [syncingheight-notempty-sold-as-bundled](syncingheight-notempty-sold-as-bundled.md) 是空着 item 2 单句边界，不是本页 not already settled 边界。
- [finalizedet-sold-as-prepare](finalizedet-sold-as-prepare.md) 是 Finalize 算出的状态就必须只依赖上一份状态和决定块（342），不是本页 not already mustdet 单句。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表就已经同一顺序（316），不是本页 not already ordered 边界。
