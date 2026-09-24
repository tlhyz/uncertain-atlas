# 例：看见空对空 / 看见默认道在表里 / 看见对上了 is not already already algo interchangeable / already prioritized interchangeable / already in-block interchangeable

**层次**：实现 / 空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事（367 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事（367 余量）/ not 849 lane-notalgo interchangeable / not 367 lane bundled interchangeable」，不是 lane bundled（367），也不是没定义 lane_priorities 不是已经排了优先（848 item 1 余量）或优先级 0 留给不设道不是已经进了块（850 item 3 余量）。不要另写怎样写 Info 车道。

## 官方三件事

规范把 Methods 里 `lane_priorities` 空当且仅当 `default_lane` 空、默认道必须是表里的一个标识 和「已经是空对空就已经选型 interchangeable / 已经是默认道在表里就已经排了优先 interchangeable / 已经是对上了就已经进了块 interchangeable / 已经是 lane bundled interchangeable」分开写成三件独立的实现事，不是「看见空对空就已经选型 interchangeable / 就已经排了优先 interchangeable / 就已经进了块 interchangeable」一件事：

1. **看见空对空 / 看见 `lane_priorities` 空当且仅当 `default_lane` 空 / 看见空表对空默认 is not already 已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable / 367 lane bundled interchangeable / 312 checktxstate interchangeable / lane-sold-as-priority interchangeable，也不是已经 lane bundled（367） interchangeable / 849 lane-notalgo interchangeable / 367 lane item 2 interchangeable，也不是已经空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事 bundled（367 item 2 余量） interchangeable / 367 lane item 2 interchangeable，也不是已经没填表就已经排了优先（848） interchangeable / 850 lane-notinblock interchangeable / 317 checktx-priority interchangeable，也不是已经 CheckTxState 就已经是 ExecuteTxState（312） interchangeable。**  
   官方写：`lane_priorities` 空，当且仅当 `default_lane` 空。看见空对空，不是已经选型。看见空对空，不是已经 algo interchangeable——367 钉 bundled 三事，本页从 item 2 侧钉 not already algo 单句。看见 `lane_priorities` 空当且仅当 `default_lane` 空，不是已经 lane bundled（367） interchangeable——367 钉 bundled，本页钉 item 2 第一件事。看见空对空，不是已经没填表就已经排了优先（848） interchangeable——848 另钉 item 1。看见空对空，不是已经写了 0 就已经进了块（850） interchangeable——850 另钉 item 3。367 lane-vs-priority bundled unbundling 在本页 item 2 续。

2. **看见默认道在表里 / 看见 `default_lane` 必须是 `lane_priorities` 里定义过的一个标识 / 看见默认道是表里标识 is not already 已经排了优先 interchangeable / 已经 prioritized interchangeable / 已经排了优先交差 interchangeable / 367 lane bundled interchangeable / 317 checktx-priority interchangeable，也不是已经 lane bundled（367） interchangeable / 849 lane-notalgo interchangeable / 367 lane item 1 没填表 interchangeable / 367 lane item 3 留 0 interchangeable，也不是已经空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事 bundled（367 item 2 余量） interchangeable / 367 lane item 2 interchangeable，也不是已经选型（本页第一件事） interchangeable。**  
   官方写：看见默认道在表里，不是已经排了优先。看见 `default_lane` 必须是表里定义过的一个标识，不是已经 prioritized interchangeable——本页钉 not already prioritized 单句。看见默认道是表里标识，不是已经选型（本页第一件事） interchangeable——三件事分开钉。367 lane-vs-priority bundled unbundling 在本页 item 2 续。

3. **看见对上了 / 看见空对空且默认道在表里 / 看见约束对上 is not already 已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable / 367 lane bundled interchangeable / 301 proposed interchangeable，也不是已经 lane bundled（367） interchangeable / 849 lane-notalgo interchangeable / 367 lane item 1 / 367 lane item 3，也不是已经空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事 bundled（367 item 2 余量） interchangeable / 367 lane item 2 interchangeable，也不是已经选型（本页第一件事） interchangeable / 已经排了优先（本页第二件事） interchangeable。**  
   官方写：看见对上了，不是已经进了块。看见空对空且默认道在表里，不是已经 in-block interchangeable——本页钉 not already in-block 单句。看见约束对上，不是已经排了优先（本页第二件事） interchangeable——三件事分开钉。367 lane-vs-priority bundled unbundling 在本页 item 2 续。

怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id` 是规范里的做法，本页不抄。lane bundled（367）、没定义 lane_priorities 不是已经排了优先（367 item 1 余量 / 848）、优先级 0 留给不设道不是已经进了块（367 item 3 余量 / 850）、CheckTx 的 Priority 就已经是共识顺序（317）、CheckTxState 就已经是 ExecuteTxState（312）、提案收了就已经从池里删掉（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **空对空 not already algo ≠ 367 / 312 interchangeable：** 官方把空对空和已经选型分开。
- **默认道在表里 not already prioritized ≠ 已经排了优先 interchangeable：** 官方把默认道在表里和已经排了优先分开。
- **对上了 not already in-block ≠ 已经进了块 interchangeable：** 官方把对上了和已经进了块分开；367 lane-vs-priority bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空对空 | 不是 already algo | 不是 CheckTxState 就已经是 ExecuteTxState alone（312） |
| 默认道在表里 | 不是 already prioritized | 不是没填表 already prioritized alone（848） |
| 对上了 | 不是 already in-block | 不是写了 0 already in-block alone（850） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事（367 余量），必须分开空对空 是不是 already algo interchangeable / 367 lane bundled interchangeable / lane-sold-as-priority interchangeable、默认道在表里 是不是 already prioritized interchangeable、对上了 是不是 already in-block interchangeable。可以跳过「看见空对空就已经选型 interchangeable / 就已经排了优先 interchangeable / 就已经进了块 interchangeable」。不要另写怎样写 Info 车道。367 lane-vs-priority bundled unbundling 在本页 item 2 续。

## 本页不抄

- 怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id`。
- lane bundled。那是不变量 367。
- 没定义 lane_priorities 不是已经排了优先。那是不变量 367 item 1 余量 / 848。
- 优先级 0 留给不设道不是已经进了块。那是不变量 367 item 3 余量 / 850。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
- CheckTxState 就已经是 ExecuteTxState。那是不变量 312。
- 提案收了就已经从池里删掉。那是不变量 301。
