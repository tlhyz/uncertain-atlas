# 例：看见 unless they really know liveness implications of REJECT / not free filter reject whole precommit / can Reject is not no cost 不是已经 Verify SHOULD Accept bundled interchangeable / 已经拒整张 Precommit 是免费过滤 interchangeable / 已经 Verify REJECT = 块非法 interchangeable

**层次**：实现 / VerifyVoteExtension Usage unless really know liveness implications 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage unless really know liveness implications 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「unless really know liveness implications / not free filter / can Reject not no cost 不是 Verify SHOULD Accept bundled interchangeable / 不是已经拒整张 Precommit 是免费过滤 interchangeable / 不是已经 Verify REJECT = 块非法 interchangeable」，不是 VerifyVoteExtension SHOULD Accept bundled（457），也不是 SHOULD always set ACCEPT（527），也不是 SHOULD Accept default strategy is not can't Reject（529 余量）。不要另写怎样评估 REJECT 活性代价。

## 官方三件事

规范把 VerifyVoteExtension Usage 里 unless they really know liveness implications of REJECT 写成三件独立的实现事，不是「看见除非真的知道活性代价 就已经拒整张 Precommit 是免费过滤 interchangeable、已经 Verify REJECT = 块非法 interchangeable、已经 REJECT 没有代价 interchangeable」一件事：

1. **看见 unless they _really_ know what the potential liveness implications of returning `REJECT` are / 看见除非真的知道 REJECT 的活性代价 不是已经 Verify SHOULD Accept bundled（457） interchangeable / 已经拒整张 Precommit 是免费过滤 interchangeable / 已经 Verify REJECT = 块非法 interchangeable，也不是已经 SHOULD always set ACCEPT bundled（457 第一件事 / 527） interchangeable / 已经 correct process must Accept interchangeable，也不是已经验签拒收整张 Precommit bundled（34） interchangeable / 已经当成块非法 interchangeable，也不是已经 SHOULD Accept 默认策略 bundled（457 第三件事 / 529 余量） interchangeable / 已经不能 Reject interchangeable。**  
   官方 VerifyVoteExtension Usage 写：unless they _really_ know what the potential liveness implications of returning REJECT are。看见 unless really know liveness implications，不是已经 Verify SHOULD Accept bundled（457） interchangeable——457 钉 bundled 三事，本页钉 unless really know 单句。看见除非真的知道活性代价，不是已经 SHOULD always set ACCEPT（527） interchangeable——527 钉 SHOULD always Accept，本页钉 unless 条件单句。看见 potential liveness implications，不是已经验签拒收整张 Precommit（34） interchangeable——34 钉验签拒收整张 Precommit 是块非法，本页钉 liveness implications 单句。
2. **看见 knowing liveness implications is not free filter reject whole precommit / 看见知道活性代价不是已经拒整张 Precommit 是免费过滤 不是已经 Verify SHOULD Accept bundled（457） interchangeable / 已经拒整张 Precommit 是免费过滤 interchangeable，也不是已经验签拒收整张 Precommit bundled（34） interchangeable / 已经当成块非法 interchangeable / 已经 Verify REJECT = 块非法 interchangeable，也不是已经 VerifyVoteExtensionResponse.status is REJECT bundled（433） interchangeable / 已经 consensus rejects whole vote interchangeable / 已经不能 Reject interchangeable，也不是已经 Verify When step 3 REJECT discard bundled（517） interchangeable / 已经丢掉 Precommit interchangeable。**  
   官方 VerifyVoteExtension Usage 把 liveness implications 和免费过滤分开——457 bundled 常被写成「验扩展失败 = 块非法 = 免费过滤」，本页钉 not free filter 单句。看见不是免费过滤，不是已经验签拒收整张 Precommit（34） interchangeable——34 钉整张 Precommit 非法，本页钉 REJECT 有 liveness 代价不是免费过滤。看见 knowing implications，不是已经 Verify 回包栏（433） interchangeable——433 钉 REJECT 时共识拒整张票 bundled，本页钉 Usage unless 条件单句。
3. **看见 can Reject is not no cost / REJECT has liveness implications / 看见可以 Reject 不是已经 REJECT 没有代价 不是已经 Verify SHOULD Accept bundled（457） interchangeable / 已经 REJECT 没有代价 interchangeable / 已经不能 Reject interchangeable，也不是已经 VerifyVoteExtensionResponse.status is REJECT bundled（433） interchangeable / 已经 consensus rejects whole vote interchangeable / 已经 SHOULD Accept 默认策略 bundled（529 余量） interchangeable，也不是已经 Verify 非确定 bug 会伤活性 bundled（341） interchangeable / 已经 SHOULD Accept 通则 interchangeable / 已经丢了安全性 interchangeable，也不是已经 Verify When step 3 REJECT discard bundled（517） interchangeable / 已经 REJECT 丢掉 Precommit interchangeable。**  
   官方 VerifyVoteExtension Usage 把 can Reject 和 no cost 分开——433 bundled 常被写成「REJECT 拒整张票 = 已经不能 Reject」，本页钉 can Reject not no cost 单句。看见可以 Reject，不是已经不能 Reject（529 余量） interchangeable——529 钉 SHOULD Accept 默认策略不是 can't Reject，本页钉 REJECT 有 liveness 代价。看见 not no cost，不是已经 Verify 非确定伤活性（341） interchangeable——341 钉非确定 bug 伤活性 SHOULD Accept 通则，本页钉 Usage unless really know 单句。

怎样做评估 REJECT 活性代价、怎样写 Verify 回包栏 是规范里的做法，本页不抄。VerifyVoteExtension SHOULD Accept bundled（457）、SHOULD always set ACCEPT（527）、SHOULD Accept default strategy（529 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **unless really know liveness implications ≠ 已经拒整张 Precommit 是免费过滤 interchangeable：** 官方把 liveness implications 条件和免费过滤分开。
- **not free filter ≠ 已经 Verify REJECT = 块非法 interchangeable：** 官方把 REJECT 有代价和验签拒收整张 Precommit 就已经是块非法分开。
- **can Reject not no cost ≠ 已经不能 Reject interchangeable：** 官方把 can Reject 有 liveness 代价和 433 REJECT 拒整张票 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| unless really know liveness implications | 不是 free filter | 不是 SHOULD always set ACCEPT（527） |
| not free filter reject whole precommit | 不是 block invalid (34) | 不是 Verify REJECT = block invalid |
| can Reject not no cost | 不是 can't Reject | 不是 SHOULD Accept default strategy（529） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage unless really know liveness implications 正式三事，必须分开 unless really know 是不是已经拒整张 Precommit 是免费过滤 interchangeable / 已经 Verify REJECT = 块非法 interchangeable、not free filter 是不是验签拒收整张 Precommit interchangeable / 已经当成块非法 interchangeable、can Reject not no cost 是不是已经不能 Reject interchangeable / 已经 REJECT 没有代价 interchangeable。可以跳过「看见除非真的知道活性代价 就已经拒整张 Precommit 是免费过滤 interchangeable」。不要另写怎样评估 REJECT 活性代价。

## 本页不抄

- 怎样做评估 REJECT 活性代价、怎样写 Verify 回包栏。
- SHOULD always set VerifyVoteExtensionResponse.status to ACCEPT。那是不变量 527（457 item 1）。
- SHOULD Accept default strategy is not can't Reject。那是不变量 529（457 item 3 余量）。
- Verify 回包栏 bundled 三事。那是不变量 433。
