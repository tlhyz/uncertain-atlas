# 例：看见会面对和 Req 5 同一类活性问题 / 看见和 Process 确定性那条同一路 / 看见会伤活性 is not already already lost-safety interchangeable / already req3-same interchangeable / already proposal-path interchangeable

**层次**：实现 / 会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事（348 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事（348 余量）/ not 799 req6-notsafety interchangeable / not 348 req6coherence bundled interchangeable」，不是 Extend–Verify 一致性 bundled（348），也不是正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept（797 item 1 余量）或 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题（798 item 2 余量）。不要另写怎样写 Extend 或 Verify。

## 官方三件事

规范把 Requirements 里会面对和 Requirement 5 同一类活性问题、和 Process 确定性那条同一路 和「已经是会伤活性就已经丢了安全性 interchangeable / 已经是和 Req 5 同一路就已经是 347 提案一致性 interchangeable / 已经是扩展这条就已经是提案那条 interchangeable / 已经是 req6coherence bundled interchangeable」分开写成三件独立的实现事，不是「看见会伤活性就已经丢了安全性 interchangeable / 就已经是提案一致性 interchangeable / 就已经是提案那条 interchangeable」一件事：

1. **看见会面对和 Requirement 5 同一类活性问题 / 看见会伤活性 / 看见和 Process 确定性那条同一路 is not already 已经丢了安全性 interchangeable / 已经 lost-safety interchangeable / 已经丢安全性交差 interchangeable / 348 req6coherence bundled interchangeable / 340 processdet interchangeable / req6coherence-sold-as-accept interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 799 req6-notsafety interchangeable / 348 req6 item 3 interchangeable，也不是已经会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事 bundled（348 item 3 余量） interchangeable / 348 req6 item 3 interchangeable，也不是已经正确进程交出的扩展必须 Accept（797） interchangeable / 798 req6-notliveness interchangeable / 341 verifydet interchangeable，也不是已经 Process 非确定 bug 没有现成解法（340 / 775） interchangeable。**  
   官方写：这时会面对和 Requirement 5 写过的同一类活性问题。看见会伤活性，不是已经丢了安全性。看见会面对和 Req 5 同一类活性问题，不是已经 lost-safety interchangeable——348 钉 bundled 三事，本页从 item 3 侧钉 not already lost-safety 单句。看见会面对和 Requirement 5 同一类活性问题，不是已经 Extend–Verify 一致性 bundled（348） interchangeable——348 钉 bundled，本页钉 item 3 第一件事。看见会伤活性，不是已经 Process 非确定 bug 没有现成解法（340 / 775） interchangeable——340 / 775 另钉 Process 侧。348 req6 vs accept bundled unbundling 在本页 item 3 完成。

2. **看见和 Req 5 同一路 / 看见和 Process 确定性那条同一路 / 看见同一类活性问题 is not already 已经是 347 那种提案一致性 interchangeable / 已经 req3-same interchangeable / 已经提案一致性交差 interchangeable / 348 req6coherence bundled interchangeable / 347 req3coherence interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 799 req6-notsafety interchangeable / 348 req6 item 1 必须 Accept interchangeable / 348 req6 item 2 确定 bug interchangeable，也不是已经会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事 bundled（348 item 3 余量） interchangeable / 348 req6 item 3 interchangeable，也不是已经丢了安全性（本页第一件事） interchangeable。**  
   官方写：看见和 Req 5 同一路，不是已经是正确提议者的准备提案必须被正确接收者 Accept。看见和 Process 确定性那条同一路，不是已经 req3-same interchangeable——本页钉 not already req3-same 单句。看见同一类活性问题，不是已经丢了安全性（本页第一件事） interchangeable——三件事分开钉。348 req6 vs accept bundled unbundling 在本页 item 3 完成。

3. **看见扩展这条 / 看见 Extend–Verify 这条活性 / 看见 Req 6 这条 is not already 已经是提案那条 interchangeable / 已经 proposal-path interchangeable / 已经提案路径交差 interchangeable / 348 req6coherence bundled interchangeable / 347 req3coherence-sold-as-accept interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 799 req6-notsafety interchangeable / 348 req6 item 1 / 348 req6 item 2，也不是已经会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事 bundled（348 item 3 余量） interchangeable / 348 req6 item 3 interchangeable，也不是已经丢了安全性（本页第一件事） interchangeable / 已经是 347 提案一致性（本页第二件事） interchangeable。**  
   官方写：看见扩展这条，不是已经是提案那条。看见 Extend–Verify 这条活性，不是已经 proposal-path interchangeable——本页钉 not already proposal-path 单句。看见 Req 6 这条，不是已经是 347 提案一致性（本页第二件事） interchangeable——三件事分开钉。348 req6 vs accept bundled unbundling 在本页 item 3 完成。

怎样写 Extend / Verify、怎样测、怎样写空扩展是规范里的做法，本页不抄。Extend–Verify 一致性 bundled（348）、正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept（348 item 1 余量 / 797）、Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题（348 item 2 余量 / 798）、Process 非确定 bug 没有现成解法（340）、正确提议者的准备提案必须被正确接收者 Accept（347）、Req 9 无副作用（349）是另外那套，本页不抄。

## 官方为什么这样拆

- **会面对和 Req 5 同一类活性问题 not already lost-safety ≠ 348 / 340 interchangeable：** 官方把扩展这条活性问题和已经丢了安全性分开。
- **和 Req 5 同一路 not already req3-same ≠ 已经是 347 提案一致性 interchangeable：** 官方把同一类活性问题和已经是提案一致性分开。
- **扩展这条 not already proposal-path ≠ 已经是提案那条 interchangeable：** 官方把扩展这条和提案那条分开；348 req6 vs accept bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 会面对和 Req 5 同一类活性问题 | 不是 already lost-safety | 不是 Process 非确定 bug 没有现成解法 alone（340 / 775） |
| 和 Req 5 同一路 | 不是 already req3-same | 不是正确提议者的准备提案必须被正确接收者 Accept alone（347） |
| 扩展这条 | 不是 already proposal-path | 不是确定 bug 丢掉 Precommit alone（798） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事（348 余量），必须分开会面对和 Req 5 同一类活性问题 是不是 already lost-safety interchangeable / 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable、和 Req 5 同一路 是不是 already req3-same interchangeable、扩展这条 是不是 already proposal-path interchangeable。可以跳过「看见会伤活性就已经丢了安全性 interchangeable / 就已经是提案一致性 interchangeable / 就已经是提案那条 interchangeable」。不要另写怎样写 Extend 或 Verify。348 req6 vs accept bundled unbundling 在本页 item 3 完成（797 + 798 + 799）。

## 本页不抄

- 怎样写 Extend / Verify、怎样测、怎样写空扩展。
- Extend–Verify 一致性 bundled。那是不变量 348。
- 正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept。那是不变量 348 item 1 余量 / 797。
- Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题。那是不变量 348 item 2 余量 / 798。
- Process 非确定 bug 没有现成解法。那是不变量 340。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Req 9 无副作用。那是不变量 349。
