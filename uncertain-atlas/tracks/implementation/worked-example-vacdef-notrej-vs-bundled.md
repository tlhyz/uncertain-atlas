# 例：看见REJECT 时共识拒整张票不是已经不能 Reject不是已经 Verify SHOULD Accept bundled；看见REJECT rejects whole vote不是已经 VerifyVoteExtensionResponse.status bundled；看见REJECT 时共识拒整张票不是已经不能 Reject不是已经 Verify When REJECT discard bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage SHOULD Accept default strategy 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyAcceptDef REJECT-path not already can't-Reject / not already 433-bundled / not already 517-discard 正式三事（529 余量）/ not 1338 vacdef-notrej interchangeable / not 529 verifyaccept-default-vs-bundled bundled interchangeable」，不是 verifyaccept default vs bundled bundled（529），也不是已经 Verify 回包栏（433），也不是已经 When REJECT discard（517）。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方三件事

1. **看见REJECT 时共识拒整张票不是已经不能 Reject / 看见REJECT 时共识拒整张票不是已经不能 Reject 这份对象 is not already 已经 Verify SHOULD Accept bundled interchangeable，也不是已经 verifyaccept default vs bundled bundled（529） interchangeable / 1338 vacdef-notrej interchangeable / 1337 vacdef-notcant interchangeable，也不是已经 VerifyAcceptDef REJECT-path not already can't-Reject / not already 433-bundled / not already 517-discard 正式三事 bundled（529 item 2 余量） interchangeable / 529 vacdef item 2 interchangeable。**  
   官方把REJECT 时共识拒整张票不是已经不能 Reject和已经 Verify SHOULD Accept bundled写成两件。看见REJECT 时共识拒整张票不是已经不能 Reject，不是已经 Verify SHOULD Accept bundled。

2. **看见REJECT rejects whole vote / 看见REJECT 时共识拒整张票不是已经不能 Reject / 这份对象 is not already 已经 VerifyVoteExtensionResponse.status bundled interchangeable，也不是已经 verifyaccept default vs bundled bundled（529） interchangeable / 1338 vacdef-notrej interchangeable / 1339 vacdef-not341 interchangeable，也不是已经 Verify 回包栏 interchangeable / 433 Verify 回包栏 interchangeable。**  
   官方把REJECT rejects whole vote和已经 VerifyVoteExtensionResponse.status bundled写成两件。看见REJECT rejects whole vote，不是已经 VerifyVoteExtensionResponse.status bundled。

3. **看见REJECT 时共识拒整张票不是已经不能 Reject / 看见REJECT rejects whole vote / 这份对象 is not already 已经 Verify When REJECT discard bundled interchangeable，也不是已经 verifyaccept default vs bundled bundled（529） interchangeable / 1338 vacdef-notrej interchangeable / 1337 vacdef-notcant interchangeable，也不是已经 When REJECT discard interchangeable / 517 When REJECT discard interchangeable。**  
   官方把REJECT 时共识拒整张票不是已经不能 Reject和已经 Verify When REJECT discard bundled写成两件。看见REJECT 时共识拒整张票不是已经不能 Reject，不是已经 Verify When REJECT discard bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。

## 官方为什么这样拆

- **REJECT rejects whole vote 不是 can't Reject interchangeable：官方把 REJECT 路径存在和已经不能 Reject 分开。**
- **看见 consensus rejects whole vote 不是已经 Verify When REJECT discard：517 钉 When step 4 REJECT discard，本页钉 Usage 侧 REJECT 路径存在。**
- **看见 not can't Reject 不是已经验签拒收整张 Precommit：34 钉整张 Precommit 非法，本页钉 Usage SHOULD Accept 默认策略边界。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify SHOULD Accept bundled | 不是已经 Verify SHOULD Accept bundled | 不是已经Verify 回包栏（433） |
| 已经 VerifyVoteExtensionResponse.status bundled | 不是已经 VerifyVoteExtensionResponse.status bundled | 不是已经When REJECT discard（517） |
| 已经 Verify When REJECT discard bundled | 不是已经 Verify When REJECT discard bundled | 不是已经1337 vacdef-notcant |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyAcceptDef REJECT-path not already can't-Reject / not already 433-bundled / not already 517-discard 正式三事（529 余量），必须分开是不是已经 Verify SHOULD Accept bundled、是不是已经 VerifyVoteExtensionResponse.status bundled、是不是已经 Verify When REJECT discard bundled。可以跳过「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」。不要另写 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。529 VerifyVoteExtension Usage SHOULD Accept default bundled unbundling 在本页 item 2 续；续 [`worked-example-vacdef-not341-vs-bundled.md`](worked-example-vacdef-not341-vs-bundled.md)（不变量 1339 item 3）。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价。
