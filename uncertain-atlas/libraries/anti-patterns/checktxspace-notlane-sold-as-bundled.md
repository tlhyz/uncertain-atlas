# 反模式：把 CheckTx lane_id not already no-lane / not already prioritized / not already in-block 正式三事（381 余量） 说成已经不设道 / 已经排了优先 / 已经进了块

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notlane-vs-bundled.md)。

## 卖法

把 CheckTx 回包这句写成已经已经不设道 / 已经排了优先 / 已经进了块 interchangeable，或已经和 381 checktxspace-vs-code bundled / checktxspace-notlane-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx 回包 codespace / events / lane_id 三条核心句写成三件独立的实现事。把它们卖成已经不设道 / 已经排了优先 / 已经进了块，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx lane_id 正式三事（381 余量），必须分开 not already no-lane、not already prioritized、not already in-block 三件事，不要和 381 / 367 / 482 / 785 / 786 糊成一句。

## 和相邻反模式

- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 CheckTx 回包 bundled（381），不是本页 item 3 单句边界。
- [checktxspace-notsettled-sold-as-bundled](checktxspace-notsettled-sold-as-bundled.md) 是 events 单句边界（786 item 2），不是本页 lane_id 边界。
