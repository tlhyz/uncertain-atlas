# 反模式：把没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事（367 余量）说成已经排了优先 / 已经是 CheckTx Priority / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[没填表 not already prioritized ≠ bundled（367）](../../tracks/implementation/worked-example-lane-notpriority-vs-bundled.md)。

## 卖法

把没填表 / 应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道 / 没定义 写成已经排了优先 interchangeable / 已经 prioritized interchangeable / 已经排了优先交差 interchangeable / 367 lane bundled interchangeable / lane-sold-as-priority interchangeable；把并成一条道 / 这时引擎把交易都放进一条道 / 没定义就并道 写成已经是 `CheckTxResponse.Priority` interchangeable / 已经 checktx-priority interchangeable / 已经是 CheckTx Priority 交差 interchangeable；把 Info 回了 / Info 回了车道 / 回了车道字段 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 367 lane bundled / lane-sold-as-priority interchangeable / 848 lane-notpriority interchangeable。

## 为什么错

官方把没填表、不是已经是 CheckTx Priority、不是已经交差写成三件独立的实现事。把它们卖成 already prioritized interchangeable / already checktx-priority interchangeable / already settled interchangeable，会把 not already prioritized、not already checktx-priority、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事（367 余量），必须分开 not already prioritized、not already checktx-priority、not already settled 三件事，不要和 367 / 317 / 849 / 850 糊成一句。

## 和相邻反模式

- [lane-sold-as-priority](lane-sold-as-priority.md) 是 lane bundled 全段，不是本页没填表 item 1 单句边界。
- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTx 的 Priority 就已经是共识顺序（317），不是本页 not already checktx-priority 边界。
- [infousage-notlaneoptional-sold-as-bundled](infousage-notlaneoptional-sold-as-bundled.md) 是 optional lane_priorities vs Info lane bundled（666），不是本页 not already settled 单句。
