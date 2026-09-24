# 例：看见没定义 lane_priorities 不是已经排了优先；看见空表对空默认不是已经选型；看见优先级 0 留给不设道不是已经进了块

**层次**：实现 / Info 车道。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「没定义 lane_priorities 不是已经排了优先 / 空表对空默认不是已经选型 / 优先级 0 留给不设道不是已经进了块」，不是 CheckTx 的 Priority 就已经是共识顺序，也不是提案收了就已经从池里删掉。不要另写怎样写 Info 车道。367 lane-vs-priority bundled unbundling 启动（848）；精读 [`worked-example-lane-notpriority-vs-bundled.md`](worked-example-lane-notpriority-vs-bundled.md)（不变量 848 item 1）。

## 官方三件事

规范把应用可以不定义车道、空表必须对空默认、优先级 0 留给不设道写成三件独立的实现事，不是「看见 Info 回了车道就已经排了优先、已经选型、已经进了块」一件事：

1. **看见应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道 / 看见没填表 不是已经排了优先，也不是已经交差。**  
   官方写：应用不必定义 `lane_priorities`。这时 CometBFT 把所有交易分到一条道。看见没填表，不是已经排了优先。看见并成一条道，不是已经是 `CheckTxResponse.Priority`。看见 Info 回了，不是已经交差。
2. **看见 `lane_priorities` 空当且仅当 `default_lane` 空、默认道必须是表里的一个标识 / 看见对上了 不是已经选型，也不是已经交差。**  
   官方写：`lane_priorities` 空，当且仅当 `default_lane` 空。`default_lane` 必须是 `lane_priorities` 里定义过的一个标识。看见空对空，不是已经选型。看见默认道在表里，不是已经排了优先。看见对上了，不是已经进了块。
3. **看见最低优先级是 1、0 留给应用不设道（`ResponseCheckTx` 里空 `lane_id`） / 看见写了 0 不是已经进了块，也不是已经从池里删掉。**  
   官方写：一条道最低优先级是 `1`。`0` 留给应用不设道的情况，对应 `ResponseCheckTx` 里空的 `lane_id`。看见写了 0，不是已经进了块。看见空 `lane_id`，不是已经从池里删掉。看见有优先级，不是已经是共识顺序。

怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id` 是规范里的做法，本页不抄。CheckTx 的 Priority 就已经是共识顺序是不变量 317，本页不抄。

## 官方为什么这样拆

- **没定义 lane_priorities ≠ 已经排了优先：** 官方把可以不设道和已经排了优先分开。
- **空表对空默认 ≠ 已经选型：** 官方把空对空和已经选定算法分开。
- **优先级 0 留给不设道 ≠ 已经进了块：** 官方把预留 0 和已经进共识分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没定义 lane_priorities | 不是已经排了优先 | 不是 CheckTx 的 Priority 就已经是共识顺序（317） |
| 空表对空默认 | 不是已经选型 | 不是 CheckTxState 就已经是 ExecuteTxState（312） |
| 优先级 0 留给不设道 | 不是已经进了块 | 不是提案收了就已经从池里删掉（301） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Info 回了车道就已经排了优先、已经选型、已经进了块」，必须分开没定义 lane_priorities 是不是已经排了优先、空表对空默认是不是已经选型、优先级 0 留给不设道是不是已经进了块。可以跳过「看见 Info 回了车道就已经排了优先」。不要另写怎样写 Info 车道。367 lane-vs-priority bundled unbundling 启动（848）。

## 本页不抄

- 怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id`。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
- CheckTxState 就已经是 ExecuteTxState。那是不变量 312。
- 提案收了就已经从池里删掉。那是不变量 301。
