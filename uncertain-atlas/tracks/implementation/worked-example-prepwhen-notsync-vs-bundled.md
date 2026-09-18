# 例：看见PrepareProposal 调用是同步的不是已经能在返回之后再改裁决；看见引擎会等到应用返回不是已经离开关键路径；看见PrepareProposal 调用是同步的不是已经 Process 调用是同步的

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareWhen sync not already can-change-after-return / not already left-critical-path / not already Process-sync 正式三事（505 余量）/ not 1311 prepwhen-notsync interchangeable / not 505 preparewhen-collect-vs-bundled bundled interchangeable」，不是 preparewhen collect vs bundled bundled（505），也不是已经 Process 同步（354），也不是已经 离开关键路径（327）。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。

## 官方三件事

1. **看见PrepareProposal 调用是同步的 / 看见PrepareProposal 调用是同步的 这份对象 is not already 已经能在返回之后再改裁决 interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1311 prepwhen-notsync interchangeable / 1310 prepwhen-notprio interchangeable，也不是已经 PrepareWhen sync not already can-change-after-return / not already left-critical-path / not already Process-sync 正式三事 bundled（505 item 2 余量） interchangeable / 505 prepwhen item 2 interchangeable。**  
   官方把PrepareProposal 调用是同步的和已经能在返回之后再改裁决写成两件。看见PrepareProposal 调用是同步的，不是已经能在返回之后再改裁决。

2. **看见引擎会等到应用返回 / 看见PrepareProposal 调用是同步的 / 这份对象 is not already 已经离开关键路径 interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1311 prepwhen-notsync interchangeable / 1312 prepwhen-notmanip interchangeable，也不是已经 Process 同步 interchangeable / 354 Process 同步 interchangeable。**  
   官方把引擎会等到应用返回和已经离开关键路径写成两件。看见引擎会等到应用返回，不是已经离开关键路径。

3. **看见PrepareProposal 调用是同步的 / 看见引擎会等到应用返回 / 这份对象 is not already 已经 Process 调用是同步的 interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1311 prepwhen-notsync interchangeable / 1310 prepwhen-notprio interchangeable，也不是已经 离开关键路径 interchangeable / 327 离开关键路径 interchangeable。**  
   官方把PrepareProposal 调用是同步的和已经 Process 调用是同步的写成两件。看见PrepareProposal 调用是同步的，不是已经 Process 调用是同步的。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。

## 官方为什么这样拆

- **synchronous Prepare call 不是能在返回后再改裁决 interchangeable：官方把 Prepare When 同步单句和 Process 同步 / 离开关键路径分开。**
- **看见引擎会等到应用返回 不是已经离开关键路径：327 钉 immediate execution 快路径，本页钉 When 侧 synchronous。**
- **看见同步调用 不是已经 Process 调用是同步的：那是不变量 354。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经能在返回之后再改裁决 | 不是已经能在返回之后再改裁决 | 不是已经Process 同步（354） |
| 已经离开关键路径 | 不是已经离开关键路径 | 不是已经离开关键路径（327） |
| 已经 Process 调用是同步的 | 不是已经 Process 调用是同步的 | 不是已经1310 prepwhen-notprio |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareWhen sync not already can-change-after-return / not already left-critical-path / not already Process-sync 正式三事（505 余量），必须分开是不是已经能在返回之后再改裁决、是不是已经离开关键路径、是不是已经 Process 调用是同步的。可以跳过「看见自己是提议者就已经 raw proposal bundled interchangeable、已经能在返回后再改裁决、已经 Prepare 改列表 bundled interchangeable」。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。505 PrepareProposal When collect bundled unbundling 在本页 item 2 续；续 [`worked-example-prepwhen-notmanip-vs-bundled.md`](worked-example-prepwhen-notmanip-vs-bundled.md)（不变量 1312 item 3）。

## 本页不抄

- 怎样做从池子收交易、怎样造头、怎样改 Prepare 列表、怎样缓存候选。
- 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。
