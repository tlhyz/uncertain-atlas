# 例：看见空表对空默认 is not already selected interchangeable / not already prioritized interchangeable / not already in-block interchangeable

**层次**：实现 / 空表对空默认 not already selected / not already prioritized / not already in-block 正式三事（367 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「空表对空默认 not already selected / not already prioritized / not already in-block 正式三事（367 余量）/ not 825 lane-notselected interchangeable / not 367 lane-vs-priority bundled interchangeable」，不是 Info 车道 bundled（367），也不是 Info Usage 空对空就已经是 367 bundled（497/667），也不是 default_lane 在表里就已经选型（498/663），也不是 CheckTxState 就已经是 ExecuteTxState（312）。不要另写怎样写 Info 车道。

## 官方三件事

1. **看见 `lane_priorities` 空当且仅当 `default_lane` 空、默认道必须是表里的一个标识 / 看见对上了 / 这份空对空 is not already 已经选型 interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 825 lane-notselected interchangeable / 824 lane-notpriority interchangeable / 367 lane item 1 没填表 interchangeable，也不是已经空表对空默认 not already selected / not already prioritized / not already in-block 正式三事 bundled（367 item 2 余量） interchangeable / 367 lane item 2 interchangeable。**  
   官方写：`lane_priorities` 空，当且仅当 `default_lane` 空。`default_lane` 必须是 `lane_priorities` 里定义过的一个标识。看见空对空，不是已经选型 interchangeable——本页从 367 item 2 侧钉 not already selected 单句。367 lane vs priority bundled unbundling 在本页 item 2 续。

2. **看见对上了 / 看见默认道在表里 / 这份空对空 is not already 已经排了优先 interchangeable / 317 priority interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 825 lane-notselected interchangeable / 367 lane item 3 优先级 0 interchangeable / 826 lane-notinblock interchangeable，也不是已经 Info Usage 空对空就已经是 367 bundled interchangeable / 497 infousage / 667 infousage-notemptyiff interchangeable，也不是已经 default_lane 在表里就已经选型 interchangeable / 498 infousage / 663 infousage-notintable interchangeable。**  
   官方把默认道在表里和已经排了优先分开——367 bundled 第二件事常与 317 / 497 / 498 混成「看见对上了就已经选型或已经排了优先 interchangeable」，本页钉 not already prioritized 单句。

3. **看见对上了 / 看见空对空 / 这份空对空 is not already 已经进了块 interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 825 lane-notselected interchangeable / 824 lane-notpriority interchangeable，也不是已经 CheckTxState 就已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把空对空和已经进了块分开。看见空对空，不是已经进了块 interchangeable。367 lane vs priority bundled unbundling 在本页 item 2 续。

怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **空表对空默认 not already selected ≠ 已经选型 interchangeable：** 官方把空对空和已经选定算法分开。
- **看见默认道在表里 not already prioritized ≠ 已经排了优先 interchangeable：** 官方把默认道在表里和已经排了优先分开。
- **看见空对空 not already in-block ≠ 已经进了块 interchangeable：** 官方把空对空和已经进了块分开；367 lane vs priority bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空表对空默认 | 不是已经选型 | 不是没定义 lane_priorities（824/367 item 1） |
| 看见默认道在表里 | 不是已经排了优先 | 不是 Info Usage 空对空（497/667） |
| 看见空对空 | 不是已经进了块 | 不是 default_lane 在表里（498/663） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空表对空默认 not already selected / not already prioritized / not already in-block 正式三事（367 余量），必须分开是不是已经选型、是不是已经排了优先、是不是已经进了块。可以跳过「看见对上了就已经选型」。不要另写怎样写 Info 车道。367 lane vs priority bundled unbundling 在本页 item 2 续；续 [`worked-example-lane-notinblock-vs-bundled.md`](worked-example-lane-notinblock-vs-bundled.md)（不变量 826 item 3）。

## 本页不抄

- 怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id。
- Info 车道 bundled。那是不变量 367。
- 没定义 lane_priorities。那是不变量 367 item 1 余量 / 824。
- Info Usage 空对空就已经是 367 bundled。那是不变量 497 / 667。
- default_lane 在表里就已经选型。那是不变量 498 / 663。
