# 例：看见写了 0 / 看见空 lane_id / 看见有优先级 is not already already in-block interchangeable / already removed interchangeable / already consensus-order interchangeable

**层次**：实现 / 优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事（367 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事（367 余量）/ not 850 lane-notinblock interchangeable / not 367 lane bundled interchangeable」，不是 lane bundled（367），也不是没定义 lane_priorities 不是已经排了优先（848 item 1 余量）或空表对空默认不是已经选型（849 item 2 余量）。不要另写怎样写 Info 车道。

## 官方三件事

规范把 Methods 里一条道最低优先级是 `1`、`0` 留给应用不设道（`ResponseCheckTx` 里空 `lane_id`） 和「已经是写了 0 就已经进了块 interchangeable / 已经是空 lane_id 就已经从池里删掉 interchangeable / 已经是有优先级就已经是共识顺序 interchangeable / 已经是 lane bundled interchangeable」分开写成三件独立的实现事，不是「看见写了 0 就已经进了块 interchangeable / 就已经从池里删掉 interchangeable / 就已经是共识顺序 interchangeable」一件事：

1. **看见写了 0 / 看见最低优先级是 1、0 留给应用不设道 / 看见预留 0 is not already 已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable / 367 lane bundled interchangeable / 301 proposed interchangeable / lane-sold-as-priority interchangeable，也不是已经 lane bundled（367） interchangeable / 850 lane-notinblock interchangeable / 367 lane item 3 interchangeable，也不是已经优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事 bundled（367 item 3 余量） interchangeable / 367 lane item 3 interchangeable，也不是已经没填表就已经排了优先（848） interchangeable / 849 lane-notalgo interchangeable / 317 checktx-priority interchangeable，也不是已经提案收了就已经从池里删掉（301） interchangeable。**  
   官方写：一条道最低优先级是 `1`。`0` 留给应用不设道的情况。看见写了 0，不是已经进了块。看见写了 0，不是已经 in-block interchangeable——367 钉 bundled 三事，本页从 item 3 侧钉 not already in-block 单句。看见最低优先级是 1、0 留给应用不设道，不是已经 lane bundled（367） interchangeable——367 钉 bundled，本页钉 item 3 第一件事。看见写了 0，不是已经没填表就已经排了优先（848） interchangeable——848 另钉 item 1。看见写了 0，不是已经空对空就已经选型（849） interchangeable——849 另钉 item 2。367 lane-vs-priority bundled unbundling 在本页 item 3 完成。

2. **看见空 `lane_id` / 看见对应 `ResponseCheckTx` 里空的 `lane_id` / 看见不设道空 id is not already 已经从池里删掉 interchangeable / 已经 removed interchangeable / 已经从池里删掉交差 interchangeable / 367 lane bundled interchangeable / 301 proposed interchangeable，也不是已经 lane bundled（367） interchangeable / 850 lane-notinblock interchangeable / 367 lane item 1 没填表 interchangeable / 367 lane item 2 空对空 interchangeable，也不是已经优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事 bundled（367 item 3 余量） interchangeable / 367 lane item 3 interchangeable，也不是已经进了块（本页第一件事） interchangeable。**  
   官方写：看见空 `lane_id`，不是已经从池里删掉。看见对应 `ResponseCheckTx` 里空的 `lane_id`，不是已经 removed interchangeable——本页钉 not already removed 单句。看见不设道空 id，不是已经进了块（本页第一件事） interchangeable——三件事分开钉。367 lane-vs-priority bundled unbundling 在本页 item 3 完成。

3. **看见有优先级 / 看见最低是 1、有道就有优先级 / 看见写了优先级 is not already 已经是共识顺序 interchangeable / 已经 consensus-order interchangeable / 已经是共识顺序交差 interchangeable / 367 lane bundled interchangeable / 317 checktx-priority interchangeable，也不是已经 lane bundled（367） interchangeable / 850 lane-notinblock interchangeable / 367 lane item 1 / 367 lane item 2，也不是已经优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事 bundled（367 item 3 余量） interchangeable / 367 lane item 3 interchangeable，也不是已经进了块（本页第一件事） interchangeable / 已经从池里删掉（本页第二件事） interchangeable。**  
   官方写：看见有优先级，不是已经是共识顺序。看见最低是 1、有道就有优先级，不是已经 consensus-order interchangeable——本页钉 not already consensus-order 单句。看见写了优先级，不是已经从池里删掉（本页第二件事） interchangeable——三件事分开钉。367 lane-vs-priority bundled unbundling 在本页 item 3 完成。

怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id` 是规范里的做法，本页不抄。lane bundled（367）、没定义 lane_priorities 不是已经排了优先（367 item 1 余量 / 848）、空表对空默认不是已经选型（367 item 2 余量 / 849）、CheckTx 的 Priority 就已经是共识顺序（317）、CheckTxState 就已经是 ExecuteTxState（312）、提案收了就已经从池里删掉（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **写了 0 not already in-block ≠ 367 / 301 interchangeable：** 官方把预留 0 和已经进了块分开。
- **空 lane_id not already removed ≠ 已经从池里删掉 interchangeable：** 官方把空 lane_id 和已经从池里删掉分开。
- **有优先级 not already consensus-order ≠ 已经是共识顺序 interchangeable：** 官方把有优先级和已经是共识顺序分开；367 lane-vs-priority bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写了 0 | 不是 already in-block | 不是提案收了就已经从池里删掉 alone（301） |
| 空 lane_id | 不是 already removed | 不是没填表 already prioritized alone（848） |
| 有优先级 | 不是 already consensus-order | 不是空对空 already algo alone（849） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事（367 余量），必须分开写了 0 是不是 already in-block interchangeable / 367 lane bundled interchangeable / lane-sold-as-priority interchangeable、空 lane_id 是不是 already removed interchangeable、有优先级 是不是 already consensus-order interchangeable。可以跳过「看见写了 0 就已经进了块 interchangeable / 就已经从池里删掉 interchangeable / 就已经是共识顺序 interchangeable」。不要另写怎样写 Info 车道。367 lane-vs-priority bundled unbundling 在本页 item 3 完成（848 + 849 + 850）。

## 本页不抄

- 怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id`。
- lane bundled。那是不变量 367。
- 没定义 lane_priorities 不是已经排了优先。那是不变量 367 item 1 余量 / 848。
- 空表对空默认不是已经选型。那是不变量 367 item 2 余量 / 849。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
- CheckTxState 就已经是 ExecuteTxState。那是不变量 312。
- 提案收了就已经从池里删掉。那是不变量 301。
