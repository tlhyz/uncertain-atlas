# 例：看见把交易列表放进回包参数不是已经 preliminary raw proposal bundled；看见改没改都算不是已经 can manipulate transactions bundled；看见把交易列表放进回包参数不是已经 PrepareProposalResponse.txs 是可能改过的列表

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareWhenRet return-list not already raw-proposal / not already manipulate / not already Response-txs 正式三事（506 余量）/ not 1313 whenret-notlist interchangeable / not 506 preparewhen-return-vs-bundled bundled interchangeable」，不是 preparewhen return vs bundled bundled（506），也不是已经 Prepare Usage raw proposal（503），也不是已经 When manipulate（505）。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。

## 官方三件事

1. **看见把交易列表放进回包参数 / 看见把交易列表放进回包参数 这份对象 is not already 已经 preliminary raw proposal bundled interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1313 whenret-notlist interchangeable / 1314 whenret-notret interchangeable，也不是已经 PrepareWhenRet return-list not already raw-proposal / not already manipulate / not already Response-txs 正式三事 bundled（506 item 1 余量） interchangeable / 506 whenret item 1 interchangeable。**  
   官方把把交易列表放进回包参数和已经 preliminary raw proposal bundled写成两件。看见把交易列表放进回包参数，不是已经 preliminary raw proposal bundled。

2. **看见改没改都算 / 看见把交易列表放进回包参数 / 这份对象 is not already 已经 can manipulate transactions bundled interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1313 whenret-notlist interchangeable / 1315 whenret-notuse interchangeable，也不是已经 Prepare Usage raw proposal interchangeable / 503 Prepare Usage raw proposal interchangeable。**  
   官方把改没改都算和已经 can manipulate transactions bundled写成两件。看见改没改都算，不是已经 can manipulate transactions bundled。

3. **看见把交易列表放进回包参数 / 看见改没改都算 / 这份对象 is not already 已经 PrepareProposalResponse.txs 是可能改过的列表 interchangeable，也不是已经 preparewhen return vs bundled bundled（506） interchangeable / 1313 whenret-notlist interchangeable / 1314 whenret-notret interchangeable，也不是已经 When manipulate interchangeable / 505 When manipulate interchangeable。**  
   官方把把交易列表放进回包参数和已经 PrepareProposalResponse.txs 是可能改过的列表写成两件。看见把交易列表放进回包参数，不是已经 PrepareProposalResponse.txs 是可能改过的列表。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。

## 官方为什么这样拆

- **includes tx list in return 不是 raw proposal bundled interchangeable：官方把 When 侧 includes in return 单句和 Usage raw proposal bundled 分开。**
- **看见改没改都算 不是已经 can manipulate transactions：505 钉 When 侧能力，本页钉 When 侧 return 单句。**
- **看见放进回包 不是已经 Response 栏 txs：427 钉 Response 栏，本页钉 When step 4 includes。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 preliminary raw proposal bundled | 不是已经 preliminary raw proposal bundled | 不是已经Prepare Usage raw proposal（503） |
| 已经 can manipulate transactions bundled | 不是已经 can manipulate transactions bundled | 不是已经When manipulate（505） |
| 已经 PrepareProposalResponse.txs 是可能改过的列表 | 不是已经 PrepareProposalResponse.txs 是可能改过的列表 | 不是已经1314 whenret-notret |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareWhenRet return-list not already raw-proposal / not already manipulate / not already Response-txs 正式三事（506 余量），必须分开是不是已经 preliminary raw proposal bundled、是不是已经 can manipulate transactions bundled、是不是已经 PrepareProposalResponse.txs 是可能改过的列表。可以跳过「看见应用改了列表就已经 raw proposal bundled interchangeable、已经 Process 紧跟 Prepare interchangeable、已经 validValue 跳过 Prepare interchangeable」。不要另写 怎样填回包、怎样广播提案、怎样写 Usage 规则。506 PrepareProposal When return bundled unbundling 在本页 item 1 启动；续 [`worked-example-whenret-notret-vs-bundled.md`](worked-example-whenret-notret-vs-bundled.md)（不变量 1314 item 2）。

## 本页不抄

- 怎样做填回包、怎样广播提案、怎样遵守 Usage MUST remove。
- 怎样填回包、怎样广播提案、怎样写 Usage 规则。
