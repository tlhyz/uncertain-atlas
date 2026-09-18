# 例：看见SHOULD Accept 默认策略不是已经不能 Reject不是已经 Process SHOULD Accept bundled；看见SHOULD Accept default strategy不是已经不能 Reject；看见SHOULD Accept 默认策略不是已经不能 Reject不是已经 MUST Accept

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcAcceptDef default not already 456-bundled / not already can't-Reject / not already MUST-Accept 正式三事（532 余量）/ not 1340 pacdef-notcant interchangeable / not 532 procaccept-default-vs-bundled bundled interchangeable」，不是 procaccept default vs bundled bundled（532），也不是已经 Process SHOULD Accept bundled（456），也不是已经 SHOULD always set ACCEPT（530）。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方三件事

1. **看见SHOULD Accept 默认策略不是已经不能 Reject / 看见SHOULD Accept 默认策略不是已经不能 Reject 这份对象 is not already 已经 Process SHOULD Accept bundled interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1340 pacdef-notcant interchangeable / 1341 pacdef-notrej interchangeable，也不是已经 ProcAcceptDef default not already 456-bundled / not already can't-Reject / not already MUST-Accept 正式三事 bundled（532 item 1 余量） interchangeable / 532 pacdef item 1 interchangeable。**  
   官方把SHOULD Accept 默认策略不是已经不能 Reject和已经 Process SHOULD Accept bundled写成两件。看见SHOULD Accept 默认策略不是已经不能 Reject，不是已经 Process SHOULD Accept bundled。

2. **看见SHOULD Accept default strategy / 看见SHOULD Accept 默认策略不是已经不能 Reject / 这份对象 is not already 已经不能 Reject interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1340 pacdef-notcant interchangeable / 1342 pacdef-not340 interchangeable，也不是已经 Process SHOULD Accept bundled interchangeable / 456 Process SHOULD Accept bundled interchangeable。**  
   官方把SHOULD Accept default strategy和已经不能 Reject写成两件。看见SHOULD Accept default strategy，不是已经不能 Reject。

3. **看见SHOULD Accept 默认策略不是已经不能 Reject / 看见SHOULD Accept default strategy / 这份对象 is not already 已经 MUST Accept interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1340 pacdef-notcant interchangeable / 1341 pacdef-notrej interchangeable，也不是已经 SHOULD always set ACCEPT interchangeable / 530 SHOULD always set ACCEPT interchangeable。**  
   官方把SHOULD Accept 默认策略不是已经不能 Reject和已经 MUST Accept写成两件。看见SHOULD Accept 默认策略不是已经不能 Reject，不是已经 MUST Accept。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方为什么这样拆

- **SHOULD Accept default strategy 不是已经不能 Reject interchangeable：官方把 SHOULD 默认 Accept 和 can't Reject 分开。**
- **看见 SHOULD Accept 默认策略 不是已经 SHOULD always set ACCEPT：530 钉 SHOULD always set，本页钉 default strategy 不是 can't Reject。**
- **看见 can still Reject 不是已经 unless really know liveness：531 钉 unless 条件，本页钉 default strategy 边界。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Process SHOULD Accept bundled | 不是已经 Process SHOULD Accept bundled | 不是已经Process SHOULD Accept bundled（456） |
| 已经不能 Reject | 不是已经不能 Reject | 不是已经SHOULD always set ACCEPT（530） |
| 已经 MUST Accept | 不是已经 MUST Accept | 不是已经1341 pacdef-notrej |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcAcceptDef default not already 456-bundled / not already can't-Reject / not already MUST-Accept 正式三事（532 余量），必须分开是不是已经 Process SHOULD Accept bundled、是不是已经不能 Reject、是不是已经 MUST Accept。可以跳过「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。532 ProcessProposal Usage SHOULD Accept default bundled unbundling 在本页 item 1 启动；续 [`worked-example-pacdef-notrej-vs-bundled.md`](worked-example-pacdef-notrej-vs-bundled.md)（不变量 1341 item 2）。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。
