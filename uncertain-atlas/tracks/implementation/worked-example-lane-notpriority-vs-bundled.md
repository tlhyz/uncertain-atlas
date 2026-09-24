# 例：看见没填表 / 看见并成一条道 / 看见 Info 回了 is not already already prioritized interchangeable / already checktx-priority interchangeable / already settled interchangeable

**层次**：实现 / 没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事（367 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事（367 余量）/ not 848 lane-notpriority interchangeable / not 367 lane bundled interchangeable」，不是 lane bundled（367），也不是空表对空默认不是已经选型（849 item 2 余量）或优先级 0 留给不设道不是已经进了块（850 item 3 余量）。不要另写怎样写 Info 车道。

## 官方三件事

规范把 Methods 里应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道 和「已经是没填表就已经排了优先 interchangeable / 已经是并成一条道就已经是 CheckTx Priority interchangeable / 已经是 Info 回了就已经交差 interchangeable / 已经是 lane bundled interchangeable」分开写成三件独立的实现事，不是「看见没填表就已经排了优先 interchangeable / 就已经是 CheckTx Priority interchangeable / 就已经交差 interchangeable」一件事：

1. **看见没填表 / 看见应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道 / 看见没定义 is not already 已经排了优先 interchangeable / 已经 prioritized interchangeable / 已经排了优先交差 interchangeable / 367 lane bundled interchangeable / 317 checktx-priority interchangeable / lane-sold-as-priority interchangeable，也不是已经 lane bundled（367） interchangeable / 848 lane-notpriority interchangeable / 367 lane item 1 interchangeable，也不是已经没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事 bundled（367 item 1 余量） interchangeable / 367 lane item 1 interchangeable，也不是已经空表对空就已经选型（849） interchangeable / 850 lane-notinblock interchangeable / 301 proposed interchangeable，也不是已经 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable。**  
   官方写：应用不必定义 `lane_priorities`。这时 CometBFT 把所有交易分到一条道。看见没填表，不是已经排了优先。看见没填表，不是已经 prioritized interchangeable——367 钉 bundled 三事，本页从 item 1 侧钉 not already prioritized 单句。看见应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道，不是已经 lane bundled（367） interchangeable——367 钉 bundled，本页钉 item 1 第一件事。看见没填表，不是已经空表对空就已经选型（849） interchangeable——849 另钉 item 2。看见没填表，不是已经写了 0 就已经进了块（850） interchangeable——850 另钉 item 3。367 lane-vs-priority bundled unbundling 在本页 item 1 启动。

2. **看见并成一条道 / 看见这时引擎把交易都放进一条道 / 看见没定义就并道 is not already 已经是 `CheckTxResponse.Priority` interchangeable / 已经 checktx-priority interchangeable / 已经是 CheckTx Priority 交差 interchangeable / 367 lane bundled interchangeable / 317 checktx-priority interchangeable，也不是已经 lane bundled（367） interchangeable / 848 lane-notpriority interchangeable / 367 lane item 2 空对空 interchangeable / 367 lane item 3 留 0 interchangeable，也不是已经没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事 bundled（367 item 1 余量） interchangeable / 367 lane item 1 interchangeable，也不是已经排了优先（本页第一件事） interchangeable。**  
   官方写：看见并成一条道，不是已经是 `CheckTxResponse.Priority`。看见这时引擎把交易都放进一条道，不是已经 checktx-priority interchangeable——本页钉 not already checktx-priority 单句。看见没定义就并道，不是已经排了优先（本页第一件事） interchangeable——三件事分开钉。367 lane-vs-priority bundled unbundling 在本页 item 1 启动。

3. **看见 Info 回了 / 看见 Info 回了车道 / 看见回了车道字段 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 367 lane bundled interchangeable / 33 fourgates interchangeable，也不是已经 lane bundled（367） interchangeable / 848 lane-notpriority interchangeable / 367 lane item 2 / 367 lane item 3，也不是已经没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事 bundled（367 item 1 余量） interchangeable / 367 lane item 1 interchangeable，也不是已经排了优先（本页第一件事） interchangeable / 已经是 CheckTx Priority（本页第二件事） interchangeable。**  
   官方写：看见 Info 回了，不是已经交差。看见 Info 回了车道，不是已经 settled interchangeable——本页钉 not already settled 单句。看见回了车道字段，不是已经是 CheckTx Priority（本页第二件事） interchangeable——三件事分开钉。367 lane-vs-priority bundled unbundling 在本页 item 1 启动。

怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id` 是规范里的做法，本页不抄。lane bundled（367）、空表对空默认不是已经选型（367 item 2 余量 / 849）、优先级 0 留给不设道不是已经进了块（367 item 3 余量 / 850）、CheckTx 的 Priority 就已经是共识顺序（317）、CheckTxState 就已经是 ExecuteTxState（312）、提案收了就已经从池里删掉（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **没填表 not already prioritized ≠ 367 / 317 interchangeable：** 官方把可以不设道和已经排了优先分开。
- **并成一条道 not already checktx-priority ≠ 已经是 CheckTx Priority interchangeable：** 官方把并成一条道和已经是 CheckTx Priority 分开。
- **Info 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Info 回了和已经交差分开；367 lane-vs-priority bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没填表 | 不是 already prioritized | 不是 CheckTx 的 Priority 就已经是共识顺序 alone（317） |
| 并成一条道 | 不是 already checktx-priority | 不是空表对空 already algo alone（849） |
| Info 回了 | 不是 already settled | 不是写了 0 already in-block alone（850） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事（367 余量），必须分开没填表 是不是 already prioritized interchangeable / 367 lane bundled interchangeable / lane-sold-as-priority interchangeable、并成一条道 是不是 already checktx-priority interchangeable、Info 回了 是不是 already settled interchangeable。可以跳过「看见没填表就已经排了优先 interchangeable / 就已经是 CheckTx Priority interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Info 车道。367 lane-vs-priority bundled unbundling 在本页 item 1 启动；完成 [`worked-example-lane-notalgo-vs-bundled.md`](worked-example-lane-notalgo-vs-bundled.md)（不变量 849 item 2）；完成 [`worked-example-lane-notinblock-vs-bundled.md`](worked-example-lane-notinblock-vs-bundled.md)（不变量 850 item 3）。

## 本页不抄

- 怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id`。
- lane bundled。那是不变量 367。
- 空表对空默认不是已经选型。那是不变量 367 item 2 余量 / 849。
- 优先级 0 留给不设道不是已经进了块。那是不变量 367 item 3 余量 / 850。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
- CheckTxState 就已经是 ExecuteTxState。那是不变量 312。
- 提案收了就已经从池里删掉。那是不变量 301。
