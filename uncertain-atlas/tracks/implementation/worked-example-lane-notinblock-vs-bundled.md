# 例：看见优先级 0 留给不设道 is not already in-block interchangeable / not already deleted from pool interchangeable / not already consensus order interchangeable

**层次**：实现 / 优先级 0 留给不设道 not already in-block / not already deleted from pool / not already consensus order 正式三事（367 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「优先级 0 留给不设道 not already in-block / not already deleted from pool / not already consensus order 正式三事（367 余量）/ not 826 lane-notinblock interchangeable / not 367 lane-vs-priority bundled interchangeable」，不是 Info 车道 bundled（367），也不是提案收了就已经从池里删掉（301），也不是 CheckTx 的 Priority 就已经是共识顺序（317），也不是 Info Usage 优先级 0 就已经是 367 bundled（498/664），也不是 CheckTx 空 lane_id 就已经是默认道（482/704）。不要另写怎样写 Info 车道。

## 官方三件事

1. **看见最低优先级是 1、0 留给应用不设道（`ResponseCheckTx` 里空 `lane_id`） / 看见写了 0 / 这份预留 is not already 已经进了块 interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 826 lane-notinblock interchangeable / 824 lane-notpriority interchangeable / 367 lane item 1 没填表 interchangeable，也不是已经优先级 0 留给不设道 not already in-block / not already deleted from pool / not already consensus order 正式三事 bundled（367 item 3 余量） interchangeable / 367 lane item 3 interchangeable。**  
   官方写：一条道最低优先级是 `1`。`0` 留给应用不设道的情况，对应 `ResponseCheckTx` 里空的 `lane_id`。看见写了 0，不是已经进了块 interchangeable——本页从 367 item 3 侧钉 not already in-block 单句。367 lane vs priority bundled unbundling 在本页 item 3 完成。

2. **看见写了 0 / 看见空 lane_id / 这份预留 is not already 已经从池里删掉 interchangeable / 301 deleted interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 826 lane-notinblock interchangeable / 367 lane item 2 空对空 interchangeable / 825 lane-notselected interchangeable，也不是已经 Info Usage 优先级 0 就已经是 367 bundled interchangeable / 498 infousage / 664 infousage-notpriorityzero interchangeable，也不是已经 CheckTx 空 lane_id 就已经是默认道 interchangeable / 482 chktxlane / 704 chktxlane-notempty interchangeable。**  
   官方把空 lane_id 和已经从池里删掉分开——367 bundled 第三件事常与 301 / 498 / 482 混成「看见写了 0 就已经进了块或已经从池里删掉 interchangeable」，本页钉 not already deleted from pool 单句。

3. **看见写了 0 / 看见有优先级 / 这份预留 is not already 已经是共识顺序 interchangeable，也不是已经 Info 车道 bundled（367） interchangeable / 826 lane-notinblock interchangeable / 824 lane-notpriority interchangeable，也不是已经 CheckTx 的 Priority 就已经是共识顺序 interchangeable / 317 priority interchangeable。**  
   官方把有优先级和已经是共识顺序分开。看见有优先级，不是已经是共识顺序 interchangeable。367 lane vs priority bundled unbundling 在本页 item 3 完成。

怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **优先级 0 留给不设道 not already in-block ≠ 已经进了块 interchangeable：** 官方把预留 0 和已经进共识分开。
- **看见空 lane_id not already deleted ≠ 301 interchangeable：** 官方把空 lane_id 和已经从池里删掉分开。
- **看见有优先级 not already consensus order ≠ 317 interchangeable：** 官方把有优先级和已经是共识顺序分开；367 lane vs priority bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 优先级 0 留给不设道 | 不是已经进了块 | 不是没定义 lane_priorities（824/367 item 1） |
| 看见空 lane_id | 不是已经从池里删掉（301） | 不是 Info Usage 优先级 0（498/664） |
| 看见有优先级 | 不是已经是共识顺序（317） | 不是 CheckTx 空 lane_id（482/704） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级 0 留给不设道 not already in-block / not already deleted from pool / not already consensus order 正式三事（367 余量），必须分开是不是已经进了块、是不是已经从池里删掉 interchangeable / 301、是不是已经是共识顺序 interchangeable / 317。可以跳过「看见写了 0 就已经进了块」。不要另写怎样写 Info 车道。367 lane vs priority bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id。
- Info 车道 bundled。那是不变量 367。
- 没定义 lane_priorities。那是不变量 367 item 1 余量 / 824。
- 提案收了就已经从池里删掉。那是不变量 301。
- Info Usage 优先级 0 就已经是 367 bundled。那是不变量 498 / 664。
