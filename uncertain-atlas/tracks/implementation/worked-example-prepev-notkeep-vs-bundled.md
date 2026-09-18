# 例：看见MUST 留到块决定之后不是已经 Process 时就交出去不是已经 Process 时就交出去；看见MUST keep until decided is not already handed at Process不是已经 REJECT 丢掉可以不算；看见MUST 留到块决定之后不是已经 Process 时就交出去不是已经因为 Prepare 过了就交差

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepEv MUST keep until decided not already handed at Process / not already discarded-on-REJECT / not already settled 正式三事（448 余量）/ not 1369 prepev-notkeep interchangeable / not 448 prepevents-vs-finalize bundled interchangeable」，不是 prepevents vs finalize bundled（448），也不是已经 Prepare 产出事件就已经交给引擎（357），也不是已经 FinalizeBlockResponse.events 栏（431）。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。

## 官方三件事

1. **看见MUST 留到块决定之后不是已经 Process 时就交出去 / 看见MUST 留到块决定之后不是已经 Process 时就交出去 这份对象 is not already 已经 Process 时就交出去 interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1369 prepev-notkeep interchangeable / 1368 prepev-notret interchangeable，也不是已经 PrepEv MUST keep until decided not already handed at Process / not already discarded-on-REJECT / not already settled 正式三事 bundled（448 item 2 余量） interchangeable / 448 prepev item 2 interchangeable。**  
   官方把MUST 留到块决定之后不是已经 Process 时就交出去和已经 Process 时就交出去写成两件。看见MUST 留到块决定之后不是已经 Process 时就交出去，不是已经 Process 时就交出去。

2. **看见MUST keep until decided is not already handed at Process / 看见MUST 留到块决定之后不是已经 Process 时就交出去 / 这份对象 is not already 已经 REJECT 丢掉可以不算 interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1369 prepev-notkeep interchangeable / 1370 prepev-notfin interchangeable，也不是已经 Prepare 产出事件就已经交给引擎 interchangeable / 357 Prepare 产出事件就已经交给引擎 interchangeable。**  
   官方把MUST keep until decided is not already handed at Process和已经 REJECT 丢掉可以不算写成两件。看见MUST keep until decided is not already handed at Process，不是已经 REJECT 丢掉可以不算。

3. **看见MUST 留到块决定之后不是已经 Process 时就交出去 / 看见MUST keep until decided is not already handed at Process / 这份对象 is not already 已经因为 Prepare 过了就交差 interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1369 prepev-notkeep interchangeable / 1368 prepev-notret interchangeable，也不是已经 FinalizeBlockResponse.events 栏 interchangeable / 431 FinalizeBlockResponse.events 栏 interchangeable。**  
   官方把MUST 留到块决定之后不是已经 Process 时就交出去和已经因为 Prepare 过了就交差写成两件。看见MUST 留到块决定之后不是已经 Process 时就交出去，不是已经因为 Prepare 过了就交差。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。

## 官方为什么这样拆

- **MUST 留到决定 不是已经 Process 时就交出去 interchangeable：官方把保留到决定和 Process 索引分开。**
- **看见块还没决定 不是已经因为 Prepare 过了就交差。**
- **看见另一块被决定 不是已经 Prepare 时那份可以不管。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Process 时就交出去 | 不是已经 Process 时就交出去 | 不是已经Prepare 产出事件就已经交给引擎（357） |
| 已经 REJECT 丢掉可以不算 | 不是已经 REJECT 丢掉可以不算 | 不是已经FinalizeBlockResponse.events 栏（431） |
| 已经因为 Prepare 过了就交差 | 不是已经因为 Prepare 过了就交差 | 不是已经1368 prepev-notret |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepEv MUST keep until decided not already handed at Process / not already discarded-on-REJECT / not already settled 正式三事（448 余量），必须分开是不是已经 Process 时就交出去、是不是已经 REJECT 丢掉可以不算、是不是已经因为 Prepare 过了就交差。可以跳过「看见 Prepare 里产出了事件就已经交给引擎」。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。448 Prepare events retention until Finalize bundled unbundling 在本页 item 2 续；续 [`worked-example-prepev-notfin-vs-bundled.md`](worked-example-prepev-notfin-vs-bundled.md)（不变量 1370 item 3）。

## 本页不抄

- 怎样攒 Prepare 事件、怎样等块决定、怎样在 Finalize 交回。
- 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。
