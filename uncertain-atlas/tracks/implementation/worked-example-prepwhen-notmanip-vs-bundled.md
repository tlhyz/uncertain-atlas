# 例：看见应用可以改列表不是已经 Prepare 改列表 bundled；看见MAY 先整块执行出候选不是已经候选已经是 ExecuteTxState；看见应用可以改列表不是已经 +2/3 之后才进来的扩展

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareWhen manip not already Prepare-list / not already ExecuteTxState / not already late-ext 正式三事（505 余量）/ not 1312 prepwhen-notmanip interchangeable / not 505 preparewhen-collect-vs-bundled bundled interchangeable」，不是 preparewhen collect vs bundled bundled（505），也不是已经 Prepare 改列表（355），也不是已经 候选已经是 ExecuteTxState（311）。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。

## 官方三件事

1. **看见应用可以改列表 / 看见应用可以改列表 这份对象 is not already 已经 Prepare 改列表 bundled interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1312 prepwhen-notmanip interchangeable / 1310 prepwhen-notprio interchangeable，也不是已经 PrepareWhen manip not already Prepare-list / not already ExecuteTxState / not already late-ext 正式三事 bundled（505 item 3 余量） interchangeable / 505 prepwhen item 3 interchangeable。**  
   官方把应用可以改列表和已经 Prepare 改列表 bundled写成两件。看见应用可以改列表，不是已经 Prepare 改列表 bundled。

2. **看见MAY 先整块执行出候选 / 看见应用可以改列表 / 这份对象 is not already 已经候选已经是 ExecuteTxState interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1312 prepwhen-notmanip interchangeable / 1311 prepwhen-notsync interchangeable，也不是已经 Prepare 改列表 interchangeable / 355 Prepare 改列表 interchangeable。**  
   官方把MAY 先整块执行出候选和已经候选已经是 ExecuteTxState写成两件。看见MAY 先整块执行出候选，不是已经候选已经是 ExecuteTxState。

3. **看见应用可以改列表 / 看见MAY 先整块执行出候选 / 这份对象 is not already 已经 +2/3 之后才进来的扩展 interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1312 prepwhen-notmanip interchangeable / 1310 prepwhen-notprio interchangeable，也不是已经 候选已经是 ExecuteTxState interchangeable / 311 候选已经是 ExecuteTxState interchangeable。**  
   官方把应用可以改列表和已经 +2/3 之后才进来的扩展写成两件。看见应用可以改列表，不是已经 +2/3 之后才进来的扩展。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。

## 官方为什么这样拆

- **can manipulate transactions 不是 Prepare 改列表 bundled interchangeable：官方把 When 侧 manipulate 能力单句和改列表后果 bundled 分开。**
- **看见 MAY 先整块执行出候选 不是已经候选已经是 ExecuteTxState：那是不变量 311。**
- **看见可以改列表 不是已经 +2/3 之后才进来的扩展：那是不变量 352。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Prepare 改列表 bundled | 不是已经 Prepare 改列表 bundled | 不是已经Prepare 改列表（355） |
| 已经候选已经是 ExecuteTxState | 不是已经候选已经是 ExecuteTxState | 不是已经候选已经是 ExecuteTxState（311） |
| 已经 +2/3 之后才进来的扩展 | 不是已经 +2/3 之后才进来的扩展 | 不是已经1310 prepwhen-notprio |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareWhen manip not already Prepare-list / not already ExecuteTxState / not already late-ext 正式三事（505 余量），必须分开是不是已经 Prepare 改列表 bundled、是不是已经候选已经是 ExecuteTxState、是不是已经 +2/3 之后才进来的扩展。可以跳过「看见自己是提议者就已经 raw proposal bundled interchangeable、已经能在返回后再改裁决、已经 Prepare 改列表 bundled interchangeable」。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。505 PrepareProposal When collect bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做从池子收交易、怎样造头、怎样改 Prepare 列表、怎样缓存候选。
- 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。
