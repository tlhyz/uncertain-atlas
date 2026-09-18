# 例：看见 VerifyVoteExtensionResponse.status SHOULD Accept is not already honest-must interchangeable / not already req6-tested interchangeable / not already verified interchangeable

**层次**：实现 / VerifyVoteExtensionResponse.status SHOULD Accept not already honest-must / not already req6-tested / not already verified 正式三事（433 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionResponse.status SHOULD Accept not already honest-must / not already req6-tested / not already verified 正式三事（433 余量）/ not 1078 vresp-nothonest interchangeable / not 433 verifyresp-vs-status bundled interchangeable」，不是 Verify 回包栏 bundled（433），也不是正确进程交出的扩展必须被正确接收者 Verify Accept（348），也不是 Requirement 6 是大量测试和自动验证的目标那种已经测过。不要另写怎样写 Verify 回包栏。

## 官方三件事

1. **看见应用 SHOULD 总是设 ACCEPT，除非真的知道 REJECT 的活性代价 / 看见写了默认 Accept 这份栏 is not already 已经正确进程交出的扩展必须 Accept interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1078 vresp-nothonest interchangeable / 1076 vresp-notinvalid interchangeable / 433 verifyresp item 1 status interchangeable，也不是已经 VerifyVoteExtensionResponse.status SHOULD Accept not already honest-must / not already req6-tested / not already verified 正式三事 bundled（433 item 3 余量） interchangeable / 433 verifyresp item 3 interchangeable。**  
   官方写：应用实现者 SHOULD always set VerifyVoteExtensionResponse.status to ACCEPT，除非他们 really know what the potential liveness implications of returning REJECT are。看见 SHOULD 总是 Accept，不是已经正确进程交出的扩展必须 Accept interchangeable——本页从 433 item 3 侧钉 not already honest-must 单句。433 verifyresp vs status bundled unbundling 在本页 item 3 完成。

2. **看见除非真的知道活性代价 / 看见写了默认 Accept / 这份栏 is not already 已经是 Req 6 已经测过 interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1078 vresp-nothonest interchangeable / 433 verifyresp item 2 exclusive interchangeable / 1077 vresp-notext interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept interchangeable / 348 req6 interchangeable。**  
   官方把除非真的知道活性代价和已经是 Req 6 已经测过分开。看见除非真的知道活性代价，不是已经是 Req 6 已经测过 interchangeable。本页钉 not already req6-tested 单句。

3. **看见写了默认 Accept / 看见 SHOULD 总是 Accept / 这份栏 is not already 已经 Verify 默认 Accept 那种已经验过扩展 interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1078 vresp-nothonest interchangeable / 1076 vresp-notinvalid interchangeable，也不是已经 Requirement 6 是大量测试和自动验证的目标那种已经测过 interchangeable。**  
   官方把写了默认 Accept 和已经 Verify 默认 Accept 那种已经验过扩展分开。看见写了默认 Accept，不是已经 Verify 默认 Accept 那种已经验过扩展 interchangeable。433 verifyresp vs status bundled unbundling 在本页 item 3 完成。

怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionResponse.status SHOULD Accept not already honest-must ≠ 已经正确进程交出的扩展必须 Accept interchangeable：** 官方把 SHOULD Accept 和 Requirement 6 必须 Accept 分开。
- **看见除非真的知道活性代价 not already req6-tested ≠ 已经是 Req 6 已经测过 interchangeable：** 官方把除非真的知道活性代价和已经是 Req 6 已经测过分开。
- **看见写了默认 Accept not already verified ≠ 已经 Verify 默认 Accept 那种已经验过扩展 interchangeable：** 官方把写了默认 Accept 和已经 Verify 默认 Accept 那种已经验过扩展分开；433 verifyresp vs status bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价 | 不是已经正确进程交出的扩展必须 Accept | 不是正确进程交出的扩展必须被正确接收者 Verify Accept（348） |
| 看见除非真的知道活性代价 | 不是已经是 Req 6 已经测过 | 不是 Requirement 6 已经测过 |
| 看见写了默认 Accept | 不是已经 Verify 默认 Accept 那种已经验过扩展 | 不是 status 就已经当成块非法（1076） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionResponse.status SHOULD Accept not already honest-must / not already req6-tested / not already verified 正式三事（433 余量），必须分开是不是已经正确进程交出的扩展必须 Accept、是不是已经是 Req 6 已经测过、是不是已经 Verify 默认 Accept 那种已经验过扩展。可以跳过「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法」。不要另写怎样写 Verify 回包栏。433 verifyresp vs status bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit。
- Verify 回包栏 bundled。那是不变量 433。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- Verify 默认 Accept 那种已经验过扩展。那是相邻 Verify When 页，不是本页。
