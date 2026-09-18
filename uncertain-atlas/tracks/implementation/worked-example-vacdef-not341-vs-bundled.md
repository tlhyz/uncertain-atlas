# 例：看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则不是已经 Verify SHOULD Accept bundled；看见default Accept is not 341 general rule不是已经 Verify 341 SHOULD Accept 通则；看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则不是已经 SHOULD always set ACCEPT bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage SHOULD Accept default strategy 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyAcceptDef default not already 457-bundled / not already 341-general / not already 527-always 正式三事（529 余量）/ not 1339 vacdef-not341 interchangeable / not 529 verifyaccept-default-vs-bundled bundled interchangeable」，不是 verifyaccept default vs bundled bundled（529），也不是已经 Verify det SHOULD Accept 通则（341），也不是已经 unless liveness（528）。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方三件事

1. **看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则 / 看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则 这份对象 is not already 已经 Verify SHOULD Accept bundled interchangeable，也不是已经 verifyaccept default vs bundled bundled（529） interchangeable / 1339 vacdef-not341 interchangeable / 1337 vacdef-notcant interchangeable，也不是已经 VerifyAcceptDef default not already 457-bundled / not already 341-general / not already 527-always 正式三事 bundled（529 item 3 余量） interchangeable / 529 vacdef item 3 interchangeable。**  
   官方把默认 Accept 不是已经 Verify 341 SHOULD Accept 通则和已经 Verify SHOULD Accept bundled写成两件。看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则，不是已经 Verify SHOULD Accept bundled。

2. **看见default Accept is not 341 general rule / 看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则 / 这份对象 is not already 已经 Verify 341 SHOULD Accept 通则 interchangeable，也不是已经 verifyaccept default vs bundled bundled（529） interchangeable / 1339 vacdef-not341 interchangeable / 1338 vacdef-notrej interchangeable，也不是已经 Verify det SHOULD Accept 通则 interchangeable / 341 Verify det SHOULD Accept 通则 interchangeable。**  
   官方把default Accept is not 341 general rule和已经 Verify 341 SHOULD Accept 通则写成两件。看见default Accept is not 341 general rule，不是已经 Verify 341 SHOULD Accept 通则。

3. **看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则 / 看见default Accept is not 341 general rule / 这份对象 is not already 已经 SHOULD always set ACCEPT bundled interchangeable，也不是已经 verifyaccept default vs bundled bundled（529） interchangeable / 1339 vacdef-not341 interchangeable / 1337 vacdef-notcant interchangeable，也不是已经 unless liveness interchangeable / 528 unless liveness interchangeable。**  
   官方把默认 Accept 不是已经 Verify 341 SHOULD Accept 通则和已经 SHOULD always set ACCEPT bundled写成两件。看见默认 Accept 不是已经 Verify 341 SHOULD Accept 通则，不是已经 SHOULD always set ACCEPT bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方为什么这样拆

- **default Accept 不是 Verify det SHOULD Accept general rule interchangeable：官方把 Usage default strategy 和 341 通则分开。**
- **看见 default Accept 不是已经 Verify 341 SHOULD Accept 通则：341 钉 determinism / liveness，本页钉 Usage default strategy 不是 341 通则。**
- **看见 SHOULD Accept 默认策略 不是已经 Verify SHOULD Accept bundled：457 bundled 三事常被写成默认策略 = 341 通则 = 433 MUST Accept，本页钉 default strategy 单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify SHOULD Accept bundled | 不是已经 Verify SHOULD Accept bundled | 不是已经Verify det SHOULD Accept 通则（341） |
| 已经 Verify 341 SHOULD Accept 通则 | 不是已经 Verify 341 SHOULD Accept 通则 | 不是已经unless liveness（528） |
| 已经 SHOULD always set ACCEPT bundled | 不是已经 SHOULD always set ACCEPT bundled | 不是已经1337 vacdef-notcant |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyAcceptDef default not already 457-bundled / not already 341-general / not already 527-always 正式三事（529 余量），必须分开是不是已经 Verify SHOULD Accept bundled、是不是已经 Verify 341 SHOULD Accept 通则、是不是已经 SHOULD always set ACCEPT bundled。可以跳过「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。529 VerifyVoteExtension Usage SHOULD Accept default bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。
