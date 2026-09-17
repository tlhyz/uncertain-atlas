# 例：看见没定义 lane_priorities is not already prioritized interchangeable / not already CheckTx Priority interchangeable / not already settled interchangeable

**层次**：实现 / 没定义 lane_priorities not already prioritized / not already CheckTx Priority / not already settled 正式三事（367 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「没定义 lane_priorities not already prioritized / not already CheckTx Priority / not already settled 正式三事（367 余量）/ not 824 lane-notpriority interchangeable / not 367 lane-vs-priority bundled interchangeable」，不是 Info 车道 bundled（367），也不是 CheckTx 的 Priority 就已经是共识顺序（317），也不是 Info Usage 可选车道就已经是 367 bundled（497/666），也不是 CheckTxState 就已经是 ExecuteTxState（312）。不要另写怎样写 Info 车道。

## 官方三件事

1. **看见应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道 / 看见没填表 / 这份表 is not already 已经排了优先 interchangeable / 317 priority interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 824 lane-notpriority interchangeable / 825 lane-notselected interchangeable / 367 lane item 2 空对空 interchangeable，也不是已经没定义 lane_priorities not already prioritized / not already CheckTx Priority / not already settled 正式三事 bundled（367 item 1 余量） interchangeable / 367 lane item 1 interchangeable。**  
   官方写：应用不必定义 `lane_priorities`。这时 CometBFT 把所有交易分到一条道。看见没填表，不是已经排了优先 interchangeable——本页从 367 item 1 侧钉 not already prioritized 单句。367 lane vs priority bundled unbundling 在本页 item 1 启动。

2. **看见没填表 / 看见并成一条道 / 这份表 is not already 已经是 CheckTxResponse.Priority interchangeable / 317 priority interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 824 lane-notpriority interchangeable / 367 lane item 3 优先级 0 interchangeable / 826 lane-notinblock interchangeable，也不是已经 Info Usage 可选车道就已经是 367 bundled interchangeable / 497 infousage / 666 infousage-notlaneoptional interchangeable，也不是已经 CheckTxState 就已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把并成一条道和已经是 CheckTx Priority 分开——367 bundled 第一件事常与 317 / 497 / 312 混成「看见没填表就已经排了优先或已经是 CheckTx Priority interchangeable」，本页钉 not already CheckTx Priority 单句。

3. **看见没填表 / 看见 Info 回了 / 这份表 is not already 已经交差 interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 824 lane-notpriority interchangeable / 825 lane-notselected interchangeable。**  
   官方把 Info 回了和已经交差分开。看见 Info 回了，不是已经交差 interchangeable。367 lane vs priority bundled unbundling 在本页 item 1 启动。

怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **没定义 lane_priorities not already prioritized ≠ 317 interchangeable：** 官方把可以不设道和已经排了优先分开。
- **看见并成一条道 not already CheckTx Priority ≠ 已经是 CheckTx Priority interchangeable：** 官方把并成一条道和已经是 CheckTx Priority 分开。
- **看见 Info 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Info 回了和已经交差分开；367 lane vs priority bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没定义 lane_priorities | 不是已经排了优先（317） | 不是空表对空默认（825/367 item 2） |
| 看见并成一条道 | 不是已经是 CheckTx Priority | 不是 Info Usage 可选车道（497/666） |
| 看见 Info 回了 | 不是已经交差 | 不是 CheckTxState（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没定义 lane_priorities not already prioritized / not already CheckTx Priority / not already settled 正式三事（367 余量），必须分开是不是已经排了优先 interchangeable / 317、是不是已经是 CheckTx Priority、是不是已经交差。可以跳过「看见没填表就已经排了优先」。不要另写怎样写 Info 车道。367 lane vs priority bundled unbundling 在本页 item 1 启动；续 [`worked-example-lane-notselected-vs-bundled.md`](worked-example-lane-notselected-vs-bundled.md)（不变量 825 item 2）。

## 本页不抄

- 怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id。
- Info 车道 bundled。那是不变量 367。
- 空表对空默认。那是不变量 367 item 2 余量 / 825。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
- Info Usage 可选车道就已经是 367 bundled。那是不变量 497 / 666。
