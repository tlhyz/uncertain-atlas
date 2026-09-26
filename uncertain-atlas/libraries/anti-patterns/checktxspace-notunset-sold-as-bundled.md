# 反模式：把 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 余量）说成已经不设道 / 已经排了优先 / 已经进了块

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了道 not already unset ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notunset-vs-bundled.md)。

## 卖法

把填了道 / CheckTx 的 lane_id 必须在 Info 回包车道范围内 / 填了 lane_id 写成已经不设道 interchangeable / 已经 unset interchangeable / 已经不设道交差 interchangeable / 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable；把在范围内 / 落在 Info 车道范围内 / 道在范围内 写成已经排了优先 interchangeable / 已经 priority interchangeable / 已经排了优先交差 interchangeable；把能指道 / 能指 lane_id / 有车道指派 写成已经进了块 interchangeable / 已经 included interchangeable / 已经进了块交差 interchangeable，或已经和 381 checktxspace bundled / checktxspace-sold-as-code interchangeable / 892 checktxspace-notunset interchangeable。

## 为什么错

官方把填了道、不是已经排了优先、不是已经进了块写成三件独立的实现事。把它们卖成 already unset interchangeable / already priority interchangeable / already included interchangeable，会把 not already unset、not already priority、not already included 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 余量），必须分开 not already unset、not already priority、not already included 三件事，不要和 381 / 367 / 890 / 891 糊成一句。

## 和相邻反模式

- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 checktxspace bundled 全段，不是本页填了道 item 3 单句边界。
- [checktxspace-notcode-sold-as-bundled](checktxspace-notcode-sold-as-bundled.md) 是写了空间 not already code（381 item 1），不是本页 not already unset 边界。
- [checktxspace-notsettled-sold-as-bundled](checktxspace-notsettled-sold-as-bundled.md) 是回了事件 not already settled（381 item 2），不是本页 not already unset 单句。
- [lane-sold-as-priority](lane-sold-as-priority.md) 是没定义 lane_priorities 就已经排了优先（367），不是本页 not already priority 边界。
