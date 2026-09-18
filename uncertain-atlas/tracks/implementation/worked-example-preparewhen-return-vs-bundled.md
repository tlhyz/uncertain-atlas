# 例：看见 includes transaction list in return parameters / returns from the call 不是已经 raw proposal bundled interchangeable / 已经 Process 紧跟 Prepare interchangeable；看见 uses the (possibly) modified block as proposal 不是已经 validValue 跳过 Prepare interchangeable / 已经 ProcessProposalRequest 八栏齐 interchangeable

**层次**：实现 / PrepareProposal When return / use-as-proposal 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「includes tx list in return / returns from call / uses modified block as proposal 不是 raw proposal bundled interchangeable / 不是 Process 紧跟 Prepare bundled interchangeable / 不是 validValue 跳过 Prepare interchangeable」，不是 When collect / synchronous / manipulate（505），也不是 Prepare Usage raw proposal（503）。不要另写怎样填回包、怎样广播提案、怎样写 Usage 规则。

## 官方三件事

规范把 PrepareProposal When 里交回列表 / 从调用返回 / 用改过的块当提案写成三件独立的实现事，不是「看见应用改了列表就已经 raw proposal bundled interchangeable、已经 Process 紧跟 Prepare interchangeable、已经 validValue 跳过 Prepare interchangeable」一件事：

1. **看见 The Application includes the transaction list (whether modified or not) in the return parameters (see the rules in section _Usage_) / 看见应用把交易列表（改没改都算）放进回包参数、并遵守 Usage 规则 不是已经 preliminary raw proposal bundled（503） interchangeable / 已经能改这套就交差 interchangeable，也不是已经 can manipulate transactions bundled（505） interchangeable / 已经 Prepare 改列表 consequences bundled（355） interchangeable，也不是已经 PrepareProposalResponse.txs 是可能改过的列表 Response栏（427） interchangeable / 已经保证是这一次 Prepare interchangeable。**  
   官方 When step 4 写：The Application includes the transaction list (whether modified or not) in the return parameters (see the rules in section _Usage_)。看见 whether modified or not，不是已经 Usage raw proposal / can modify this set（503） interchangeable——503 钉 Usage 侧 raw proposal 单句，本页钉 When 侧 includes in return 单句。看见 see the rules in section Usage，不是已经 MUST remove if > max_tx_bytes（503 第三件事） interchangeable——503 钉 MUST remove 义务，本页钉 When 侧 includes + Usage 交叉引用。看见 includes in return parameters，不是已经 can manipulate transactions（505 第三件事） interchangeable——505 钉 When 侧 manipulate 能力，本页钉 When 侧 return 单句。
2. **看见 and returns from the call / 看见从 PrepareProposal 调用返回 不是已经 Process 通常紧跟 Prepare、`ProcessProposalRequest.txs` equals `PrepareProposalResponse.txs` bundled（351） interchangeable / 已经不用再 Process interchangeable，也不是已经 The call is synchronous blocks until returns（505） interchangeable / 已经能在返回后再改 PrepareProposalResponse interchangeable，也不是已经 ProcessProposal 含执行所需全部信息（453） interchangeable / 已经跑过 Process interchangeable。**  
   官方 When step 4 续：and returns from the call。看见 returns from the call，不是已经 Process 也会在提议者那边叫（351） interchangeable——351 钉 Process Usage 侧提议者 Process / 通常对得上，本页钉 When 侧 returns 单句。看见从调用返回，不是已经 synchronous Prepare call（505） interchangeable——505 钉 blocks until returns，本页钉 When 侧 returns 完成调用。看见返回了，不是已经 ProcessProposal Contains all information needed to fully execute（453） interchangeable——453 钉 Process 八栏，本页钉 When 侧 returns 单句。
3. **看见 _p_ uses the (possibly) modified block as _p_'s proposal in round _r_, height _h_ / 看见提议者用（可能改过的）块当这一轮这一高的提案 不是已经 validValue 非 nil 跳过 Prepare（356） interchangeable / 已经直接用它当提案 interchangeable，也不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs bundled（351） interchangeable / 已经保证是这一次 Prepare interchangeable，也不是已经 ProcessProposal 含执行所需全部信息（453） interchangeable / 已经只有 PrepareProposalResponse.txs interchangeable，也不是已经 ProposalStatus ACCEPT 就 prevote（376） interchangeable / 已经交差 interchangeable。**  
   官方 When step 5 写：_p_ uses the (possibly) modified block as _p_'s proposal in round _r_, height _h_。看见 uses as proposal，不是已经 validValue 非 nil 直接当提案（356） interchangeable——356 钉 validValue 跳过，本页钉 When 侧 uses modified block 单句。看见 possibly modified block，不是已经 ProcessProposalRequest 八栏齐（453） interchangeable——453 钉 Process 含执行所需全部信息，本页钉 When 侧 uses block as proposal 单句。看见 in round _r_, height _h_，不是已经 Process 通常 txs 对得上（351） interchangeable——351 钉 Usage 侧通常对得上 / 失败不保证，本页钉 When 侧 uses as proposal 单句。

怎样做填回包、怎样广播提案、怎样遵守 Usage MUST remove 是规范里的做法，本页不抄。When collect / synchronous / manipulate（505）、Prepare Usage raw proposal（503）、Prepare 改列表 consequences（355）是另外那套，本页不抄。

## 官方为什么这样拆

- **includes tx list in return ≠ raw proposal bundled interchangeable：** 官方把 When 侧 includes in return 单句和 Usage raw proposal bundled 分开。
- **returns from call ≠ Process 紧跟 Prepare bundled interchangeable：** 官方把 When 侧 returns 单句和 Process Usage 提议者 Process / 通常对得上 bundled 分开。
- **uses modified block as proposal ≠ validValue 跳过 Prepare interchangeable：** 官方把 When 侧 uses as proposal 单句和 validValue 跳过 / Process 八栏 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| includes tx list in return (whether modified or not) | 不是 raw proposal bundled（503） | 不是 can manipulate bundled（505） |
| returns from PrepareProposal call | 不是 Process 紧跟 Prepare bundled（351） | 不是 blocks until returns（505） |
| uses possibly modified block as proposal | 不是 validValue 跳过 Prepare（356） | 不是 Process 八栏齐（453） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事，必须分开 includes tx list in return 是不是 raw proposal bundled interchangeable、returns from call 是不是 Process 紧跟 Prepare bundled interchangeable、uses modified block as proposal 是不是 validValue 跳过 Prepare interchangeable / 已经 Process 八栏齐 interchangeable。可以跳过「看见应用改了列表就已经 raw proposal bundled interchangeable、已经 Process 紧跟 Prepare interchangeable、已经 validValue 跳过 Prepare interchangeable」。506 PrepareProposal When return bundled unbundling 完成（1313 item 1 / 1314 item 2 / 1315 item 3）；精读 [`worked-example-whenret-notlist-vs-bundled.md`](worked-example-whenret-notlist-vs-bundled.md)（不变量 1313 item 1）、[`worked-example-whenret-notret-vs-bundled.md`](worked-example-whenret-notret-vs-bundled.md)（不变量 1314 item 2）、[`worked-example-whenret-notuse-vs-bundled.md`](worked-example-whenret-notuse-vs-bundled.md)（不变量 1315 item 3）。不要另写怎样填回包、怎样广播提案。

## 本页不抄

- 怎样做填回包、怎样广播提案、怎样遵守 Usage MUST remove。
- When collect / synchronous / manipulate。那是不变量 505。
- Prepare Usage raw proposal / MUST remove。那是不变量 503。
- Process 也会在提议者那边叫 / 通常 txs 对得上。那是不变量 351。
- validValue 跳过 Prepare。那是不变量 356。
