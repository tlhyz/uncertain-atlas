# 反模式：把 CheckTx 回包 events not already settled / not already not-in-block / not already consensus order 正式三事（381 余量） 说成已经交差 / 已经没进块 / 已经是共识顺序

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notsettled-vs-bundled.md)。

## 卖法

把 CheckTx 回包这句写成已经已经交差 / 已经没进块 / 已经是共识顺序 interchangeable，或已经和 381 checktxspace-vs-code bundled / checktxspace-notsettled-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx 回包 codespace / events / lane_id 三条核心句写成三件独立的实现事。把它们卖成已经交差 / 已经没进块 / 已经是共识顺序，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 events 正式三事（381 余量），必须分开 not already settled、not already not-in-block、not already consensus order 三件事，不要和 381 / 316 / 382 / 784 / 785 / 787 糊成一句。

## 和相邻反模式

- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 CheckTx 回包 bundled（381），不是本页 item 2 单句边界。
- [syncingheight-notdet-sold-as-bundled](syncingheight-notdet-sold-as-bundled.md) 是 Finalize 回包 events 就已经必须确定（382/784），不是本页 CheckTx events 边界。
