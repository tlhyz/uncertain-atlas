# 例：看见用可能改过的块当这一轮提案不是已经 validValue 非 nil 跳过 Prepare；看见possibly modified block不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs；看见用可能改过的块当这一轮提案不是已经 ProcessProposal 八栏齐

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareWhenRet use-as-proposal not already validValue-skip / not already txs-equal / not already eight-cols 正式三事（506 余量）/ not 1315 whenret-notuse interchangeable / not 506 preparewhen-return-vs-bundled bundled interchangeable」，不是 preparewhen return vs bundled bundled（506），也不是已经 validValue 跳过（356），也不是已经 Process txs 对得上（351）。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。

## 官方三件事

1. **看见用可能改过的块当这一轮提案 / 看见用可能改过的块当这一轮提案 这份对象 is not already 已经 validValue 非 nil 跳过 Prepare interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1315 whenret-notuse interchangeable / 1313 whenret-notlist interchangeable，也不是已经 PrepareWhenRet use-as-proposal not already validValue-skip / not already txs-equal / not already eight-cols 正式三事 bundled（506 item 3 余量） interchangeable / 506 whenret item 3 interchangeable。**  
   官方把用可能改过的块当这一轮提案和已经 validValue 非 nil 跳过 Prepare写成两件。看见用可能改过的块当这一轮提案，不是已经 validValue 非 nil 跳过 Prepare。

2. **看见possibly modified block / 看见用可能改过的块当这一轮提案 / 这份对象 is not already 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1315 whenret-notuse interchangeable / 1314 whenret-notret interchangeable，也不是已经 validValue 跳过 interchangeable / 356 validValue 跳过 interchangeable。**  
   官方把possibly modified block和已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs写成两件。看见possibly modified block，不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs。

3. **看见用可能改过的块当这一轮提案 / 看见possibly modified block / 这份对象 is not already 已经 ProcessProposal 八栏齐 interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1315 whenret-notuse interchangeable / 1313 whenret-notlist interchangeable，也不是已经 Process txs 对得上 interchangeable / 351 Process txs 对得上 interchangeable。**  
   官方把用可能改过的块当这一轮提案和已经 ProcessProposal 八栏齐写成两件。看见用可能改过的块当这一轮提案，不是已经 ProcessProposal 八栏齐。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。

## 官方为什么这样拆

- **uses modified block as proposal 不是 validValue 跳过 Prepare interchangeable：官方把 When 侧 uses as proposal 单句和 validValue 跳过分开。**
- **看见 possibly modified block 不是已经 Process txs 对得上：351 钉 Usage 侧通常对得上，本页钉 When 侧 uses as proposal。**
- **看见当这一轮提案 不是已经 Process 八栏齐：那是不变量 453。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 validValue 非 nil 跳过 Prepare | 不是已经 validValue 非 nil 跳过 Prepare | 不是已经validValue 跳过（356） |
| 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs | 不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs | 不是已经Process txs 对得上（351） |
| 已经 ProcessProposal 八栏齐 | 不是已经 ProcessProposal 八栏齐 | 不是已经1313 whenret-notlist |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareWhenRet use-as-proposal not already validValue-skip / not already txs-equal / not already eight-cols 正式三事（506 余量），必须分开是不是已经 validValue 非 nil 跳过 Prepare、是不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs、是不是已经 ProcessProposal 八栏齐。可以跳过「看见应用改了列表就已经 raw proposal bundled interchangeable、已经 Process 紧跟 Prepare interchangeable、已经 validValue 跳过 Prepare interchangeable」。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。506 PrepareProposal When return bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做填回包、怎样广播提案、怎样遵守 Usage MUST remove。
- 怎样填回包、怎样广播提案、怎样写 Usage 规则。
