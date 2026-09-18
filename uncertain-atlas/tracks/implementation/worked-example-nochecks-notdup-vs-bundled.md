# 例：看见引擎不再做额外有效性检查不是已经验过重复；看见不再查重复交易不是已经有应用级重放保护；看见引擎不再做额外有效性检查不是已经内存池去重就已经保证不重放

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareNochecks nocheck not already checked-dup / not already app-replay / not already pool-dedup 正式三事（504 余量）/ not 1307 nochecks-notdup interchangeable / not 504 prepareusage-nochecks-vs-bundled bundled interchangeable」，不是 prepareusage nochecks vs bundled bundled（504），也不是已经 Prepare 回包校验（357），也不是已经 内存池去重（313）。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。

## 官方三件事

1. **看见引擎不再做额外有效性检查 / 看见引擎不再做额外有效性检查 这份对象 is not already 已经验过重复 interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1307 nochecks-notdup interchangeable / 1308 nochecks-notcrash interchangeable，也不是已经 PrepareNochecks nocheck not already checked-dup / not already app-replay / not already pool-dedup 正式三事 bundled（504 item 1 余量） interchangeable / 504 nochecks item 1 interchangeable。**  
   官方把引擎不再做额外有效性检查和已经验过重复写成两件。看见引擎不再做额外有效性检查，不是已经验过重复。

2. **看见不再查重复交易 / 看见引擎不再做额外有效性检查 / 这份对象 is not already 已经有应用级重放保护 interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1307 nochecks-notdup interchangeable / 1309 nochecks-notdet interchangeable，也不是已经 Prepare 回包校验 interchangeable / 357 Prepare 回包校验 interchangeable。**  
   官方把不再查重复交易和已经有应用级重放保护写成两件。看见不再查重复交易，不是已经有应用级重放保护。

3. **看见引擎不再做额外有效性检查 / 看见不再查重复交易 / 这份对象 is not already 已经内存池去重就已经保证不重放 interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1307 nochecks-notdup interchangeable / 1308 nochecks-notcrash interchangeable，也不是已经 内存池去重 interchangeable / 313 内存池去重 interchangeable。**  
   官方把引擎不再做额外有效性检查和已经内存池去重就已经保证不重放写成两件。看见引擎不再做额外有效性检查，不是已经内存池去重就已经保证不重放。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。

## 官方为什么这样拆

- **no additional validity checks 不是已经验过重复 interchangeable：官方把 Methods Usage no checks 单句和 Prepare 回包校验 bundled、内存池去重分开。**
- **看见不再查重复 不是已经有应用级重放保护：官方写引擎不再做额外有效性检查，不是应用已经有重放保护。**
- **看见不再做额外检查 不是已经内存池去重就已经保证不重放：那是不变量 313。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经验过重复 | 不是已经验过重复 | 不是已经Prepare 回包校验（357） |
| 已经有应用级重放保护 | 不是已经有应用级重放保护 | 不是已经内存池去重（313） |
| 已经内存池去重就已经保证不重放 | 不是已经内存池去重就已经保证不重放 | 不是已经1308 nochecks-notcrash |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareNochecks nocheck not already checked-dup / not already app-replay / not already pool-dedup 正式三事（504 余量），必须分开是不是已经验过重复、是不是已经有应用级重放保护、是不是已经内存池去重就已经保证不重放。可以跳过「看见回了 Prepare 回包就已经验过重复、已经是 Process REJECT、已经必须确定 interchangeable」。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。504 PrepareProposal Usage nochecks bundled unbundling 在本页 item 1 启动；续 [`worked-example-nochecks-notcrash-vs-bundled.md`](worked-example-nochecks-notcrash-vs-bundled.md)（不变量 1308 item 2）。

## 本页不抄

- 怎样做再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。
- 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。
