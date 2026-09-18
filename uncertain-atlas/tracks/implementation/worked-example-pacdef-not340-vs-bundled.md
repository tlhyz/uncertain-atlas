# 例：看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则不是已经 Process SHOULD Accept bundled；看见default Accept is not 340 general rule不是已经 Process 340 SHOULD Accept 通则；看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则不是已经 SHOULD always set ACCEPT bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcAcceptDef default not already 456-bundled / not already 340-general / not already 530-always 正式三事（532 余量）/ not 1342 pacdef-not340 interchangeable / not 532 procaccept-default-vs-bundled bundled interchangeable」，不是 procaccept default vs bundled bundled（532），也不是已经 Process det SHOULD Accept 通则（340），也不是已经 unless liveness（531）。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方三件事

1. **看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则 / 看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则 这份对象 is not already 已经 Process SHOULD Accept bundled interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1342 pacdef-not340 interchangeable / 1340 pacdef-notcant interchangeable，也不是已经 ProcAcceptDef default not already 456-bundled / not already 340-general / not already 530-always 正式三事 bundled（532 item 3 余量） interchangeable / 532 pacdef item 3 interchangeable。**  
   官方把默认 Accept 不是已经 Process 340 SHOULD Accept 通则和已经 Process SHOULD Accept bundled写成两件。看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则，不是已经 Process SHOULD Accept bundled。

2. **看见default Accept is not 340 general rule / 看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则 / 这份对象 is not already 已经 Process 340 SHOULD Accept 通则 interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1342 pacdef-not340 interchangeable / 1341 pacdef-notrej interchangeable，也不是已经 Process det SHOULD Accept 通则 interchangeable / 340 Process det SHOULD Accept 通则 interchangeable。**  
   官方把default Accept is not 340 general rule和已经 Process 340 SHOULD Accept 通则写成两件。看见default Accept is not 340 general rule，不是已经 Process 340 SHOULD Accept 通则。

3. **看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则 / 看见default Accept is not 340 general rule / 这份对象 is not already 已经 SHOULD always set ACCEPT bundled interchangeable，也不是已经 procaccept default vs bundled bundled（532） interchangeable / 1342 pacdef-not340 interchangeable / 1340 pacdef-notcant interchangeable，也不是已经 unless liveness interchangeable / 531 unless liveness interchangeable。**  
   官方把默认 Accept 不是已经 Process 340 SHOULD Accept 通则和已经 SHOULD always set ACCEPT bundled写成两件。看见默认 Accept 不是已经 Process 340 SHOULD Accept 通则，不是已经 SHOULD always set ACCEPT bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方为什么这样拆

- **default Accept 不是 Process det SHOULD Accept general rule interchangeable：官方把 Usage default strategy 和 340 通则分开。**
- **看见 default Accept 不是已经 Process 340 SHOULD Accept 通则：340 钉 determinism / liveness，本页钉 Usage default strategy 不是 340 通则。**
- **看见 SHOULD Accept 默认策略 不是已经 Process SHOULD Accept bundled：456 bundled 三事常被写成默认策略 = 340 通则 = 430 MUST Accept，本页钉 default strategy 单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Process SHOULD Accept bundled | 不是已经 Process SHOULD Accept bundled | 不是已经Process det SHOULD Accept 通则（340） |
| 已经 Process 340 SHOULD Accept 通则 | 不是已经 Process 340 SHOULD Accept 通则 | 不是已经unless liveness（531） |
| 已经 SHOULD always set ACCEPT bundled | 不是已经 SHOULD always set ACCEPT bundled | 不是已经1340 pacdef-notcant |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcAcceptDef default not already 456-bundled / not already 340-general / not already 530-always 正式三事（532 余量），必须分开是不是已经 Process SHOULD Accept bundled、是不是已经 Process 340 SHOULD Accept 通则、是不是已经 SHOULD always set ACCEPT bundled。可以跳过「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。532 ProcessProposal Usage SHOULD Accept default bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。
