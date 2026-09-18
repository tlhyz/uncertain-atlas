# 例：看见从 PrepareProposal 调用返回不是已经 Process 通常紧跟 Prepare bundled；看见返回了不是已经 The call is synchronous；看见从 PrepareProposal 调用返回不是已经 ProcessProposal 含执行所需全部信息

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareWhenRet returns not already Process-follows-Prepare / not already sync-blocks / not already Process-all-info 正式三事（506 余量）/ not 1314 whenret-notret interchangeable / not 506 preparewhen-return-vs-bundled bundled interchangeable」，不是 preparewhen return vs bundled bundled（506），也不是已经 Process 紧跟 Prepare（351），也不是已经 Process 八栏（453）。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。

## 官方三件事

1. **看见从 PrepareProposal 调用返回 / 看见从 PrepareProposal 调用返回 这份对象 is not already 已经 Process 通常紧跟 Prepare bundled interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1314 whenret-notret interchangeable / 1313 whenret-notlist interchangeable，也不是已经 PrepareWhenRet returns not already Process-follows-Prepare / not already sync-blocks / not already Process-all-info 正式三事 bundled（506 item 2 余量） interchangeable / 506 whenret item 2 interchangeable。**  
   官方把从 PrepareProposal 调用返回和已经 Process 通常紧跟 Prepare bundled写成两件。看见从 PrepareProposal 调用返回，不是已经 Process 通常紧跟 Prepare bundled。

2. **看见返回了 / 看见从 PrepareProposal 调用返回 / 这份对象 is not already 已经 The call is synchronous interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1314 whenret-notret interchangeable / 1315 whenret-notuse interchangeable，也不是已经 Process 紧跟 Prepare interchangeable / 351 Process 紧跟 Prepare interchangeable。**  
   官方把返回了和已经 The call is synchronous写成两件。看见返回了，不是已经 The call is synchronous。

3. **看见从 PrepareProposal 调用返回 / 看见返回了 / 这份对象 is not already 已经 ProcessProposal 含执行所需全部信息 interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1314 whenret-notret interchangeable / 1313 whenret-notlist interchangeable，也不是已经 Process 八栏 interchangeable / 453 Process 八栏 interchangeable。**  
   官方把从 PrepareProposal 调用返回和已经 ProcessProposal 含执行所需全部信息写成两件。看见从 PrepareProposal 调用返回，不是已经 ProcessProposal 含执行所需全部信息。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。

## 官方为什么这样拆

- **returns from the call 不是 Process 紧跟 Prepare interchangeable：官方把 When 侧 returns 单句和 Process Usage 通常对得上分开。**
- **看见返回了 不是已经 synchronous Prepare call：505 钉 blocks until returns，本页钉 When 侧 returns 完成调用。**
- **看见从调用返回 不是已经 ProcessProposal 含执行所需全部信息：那是不变量 453。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Process 通常紧跟 Prepare bundled | 不是已经 Process 通常紧跟 Prepare bundled | 不是已经Process 紧跟 Prepare（351） |
| 已经 The call is synchronous | 不是已经 The call is synchronous | 不是已经Process 八栏（453） |
| 已经 ProcessProposal 含执行所需全部信息 | 不是已经 ProcessProposal 含执行所需全部信息 | 不是已经1313 whenret-notlist |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareWhenRet returns not already Process-follows-Prepare / not already sync-blocks / not already Process-all-info 正式三事（506 余量），必须分开是不是已经 Process 通常紧跟 Prepare bundled、是不是已经 The call is synchronous、是不是已经 ProcessProposal 含执行所需全部信息。可以跳过「看见应用改了列表就已经 raw proposal bundled interchangeable、已经 Process 紧跟 Prepare interchangeable、已经 validValue 跳过 Prepare interchangeable」。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。506 PrepareProposal When return bundled unbundling 在本页 item 2 续；续 [`worked-example-whenret-notuse-vs-bundled.md`](worked-example-whenret-notuse-vs-bundled.md)（不变量 1315 item 3）。

## 本页不抄

- 怎样做填回包、怎样广播提案、怎样遵守 Usage MUST remove。
- 怎样填回包、怎样广播提案、怎样写 Usage 规则。
