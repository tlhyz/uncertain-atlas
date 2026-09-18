# 例：看见REJECT 时共识 assumes not valid 不是已经不能 Reject不是已经 Process SHOULD Accept bundled；看见REJECT assumes not valid不是已经 ProcessProposalResponse.status bundled；看见REJECT 时共识 assumes not valid 不是已经不能 Reject不是已经 Process REJECT consensus assume bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcAcceptDef REJECT-path not already can't-Reject / not already 430-bundled / not already 455-assume 正式三事（532 余量）/ not 1341 pacdef-notrej interchangeable / not 532 procaccept-default-vs-bundled bundled interchangeable」，不是 procaccept default vs bundled bundled（532），也不是已经 Process 回包栏（430），也不是已经 Process REJECT assume（455）。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方三件事

1. **看见REJECT 时共识 assumes not valid 不是已经不能 Reject / 看见REJECT 时共识 assumes not valid 不是已经不能 Reject 这份对象 is not already 已经 Process SHOULD Accept bundled interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1341 pacdef-notrej interchangeable / 1340 pacdef-notcant interchangeable，也不是已经 ProcAcceptDef REJECT-path not already can't-Reject / not already 430-bundled / not already 455-assume 正式三事 bundled（532 item 2 余量） interchangeable / 532 pacdef item 2 interchangeable。**  
   官方把REJECT 时共识 assumes not valid 不是已经不能 Reject和已经 Process SHOULD Accept bundled写成两件。看见REJECT 时共识 assumes not valid 不是已经不能 Reject，不是已经 Process SHOULD Accept bundled。

2. **看见REJECT assumes not valid / 看见REJECT 时共识 assumes not valid 不是已经不能 Reject / 这份对象 is not already 已经 ProcessProposalResponse.status bundled interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1341 pacdef-notrej interchangeable / 1342 pacdef-not340 interchangeable，也不是已经 Process 回包栏 interchangeable / 430 Process 回包栏 interchangeable。**  
   官方把REJECT assumes not valid和已经 ProcessProposalResponse.status bundled写成两件。看见REJECT assumes not valid，不是已经 ProcessProposalResponse.status bundled。

3. **看见REJECT 时共识 assumes not valid 不是已经不能 Reject / 看见REJECT assumes not valid / 这份对象 is not already 已经 Process REJECT consensus assume bundled interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1341 pacdef-notrej interchangeable / 1340 pacdef-notcant interchangeable，也不是已经 Process REJECT assume interchangeable / 455 Process REJECT assume interchangeable。**  
   官方把REJECT 时共识 assumes not valid 不是已经不能 Reject和已经 Process REJECT consensus assume bundled写成两件。看见REJECT 时共识 assumes not valid 不是已经不能 Reject，不是已经 Process REJECT consensus assume bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方为什么这样拆

- **REJECT assumes not valid 不是 can't Reject interchangeable：官方把 REJECT 路径存在和已经不能 Reject 分开。**
- **看见 consensus assumes not valid 不是已经 Process REJECT consensus assume：455 钉 assumes not valid / prevote nil bundled，本页钉 Usage 侧 REJECT 路径存在。**
- **看见 not can't Reject 不是已经 Process REJECT = prevote nil 不是免费过滤：33 钉 prevote nil 路径，本页钉 Usage SHOULD Accept 默认策略边界。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Process SHOULD Accept bundled | 不是已经 Process SHOULD Accept bundled | 不是已经Process 回包栏（430） |
| 已经 ProcessProposalResponse.status bundled | 不是已经 ProcessProposalResponse.status bundled | 不是已经Process REJECT assume（455） |
| 已经 Process REJECT consensus assume bundled | 不是已经 Process REJECT consensus assume bundled | 不是已经1340 pacdef-notcant |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcAcceptDef REJECT-path not already can't-Reject / not already 430-bundled / not already 455-assume 正式三事（532 余量），必须分开是不是已经 Process SHOULD Accept bundled、是不是已经 ProcessProposalResponse.status bundled、是不是已经 Process REJECT consensus assume bundled。可以跳过「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。532 ProcessProposal Usage SHOULD Accept default bundled unbundling 在本页 item 2 续；续 [`worked-example-pacdef-not340-vs-bundled.md`](worked-example-pacdef-not340-vs-bundled.md)（不变量 1342 item 3）。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。
