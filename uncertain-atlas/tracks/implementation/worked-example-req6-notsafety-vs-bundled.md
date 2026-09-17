# 例：看见会面对和 Req 5 同一类活性问题 is not already lost safety interchangeable / not already Req 3 proposal coherence interchangeable / not already settled interchangeable

**层次**：实现 / 会面对和 Req 5 同一类活性问题 not already lost safety / not already Req 3 proposal coherence / not already settled 正式三事（348 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「会面对和 Req 5 同一类活性问题 not already lost safety / not already Req 3 proposal coherence / not already settled 正式三事（348 余量）/ not 871 req6-notsafety interchangeable / not 348 req6-coherence-vs-accept bundled interchangeable」，不是 Extend–Verify 一致性 bundled（348），也不是正确提议者的准备提案必须被正确接收者 Accept（347），也不是验签拒收整张预提交就已经是块非法（34）。不要另写怎样写 Extend 或 Verify。

## 官方三件事

1. **看见会面对和 Requirement 5 同一类活性问题 / 看见会伤活性 这份活性 is not already 已经丢了安全性 interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 871 req6-notsafety interchangeable / 869 req6-notany interchangeable / 348 req6 item 1 必须 Accept interchangeable，也不是已经会面对和 Req 5 同一类活性问题 not already lost safety / not already Req 3 proposal coherence / not already settled 正式三事 bundled（348 item 3 余量） interchangeable / 348 req6 item 3 interchangeable。**  
   官方写：这时会面对和 Requirement 5 写过的同一类活性问题。看见会伤活性，不是已经丢了安全性 interchangeable——本页从 348 item 3 侧钉 not already lost safety 单句。348 req6 vs accept bundled unbundling 在本页 item 3 完成。

2. **看见会伤活性 / 看见和 Req 5 同一路 / 这份活性 is not already 已经是正确提议者的准备提案必须被正确接收者 Accept interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 871 req6-notsafety interchangeable / 348 req6 item 2 确定 bug interchangeable / 870 req6-notliveness interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept interchangeable / 347 req3 interchangeable。**  
   官方把和 Req 5 同一路和已经是 347 那种提案一致性分开——348 bundled 第三件事常与 347 混成「看见会伤活性就已经丢了安全性或已经是提案一致性 interchangeable」，本页钉 not already Req 3 proposal coherence 单句。

3. **看见会伤活性 / 看见扩展这条 / 这份活性 is not already 已经交差 interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 871 req6-notsafety interchangeable / 869 req6-notany interchangeable，也不是已经验签拒收整张预提交就已经是块非法 interchangeable / 34 voteext interchangeable。**  
   官方把扩展这条和已经是提案那条 / 已经交差分开。看见扩展这条，不是已经交差 interchangeable。348 req6 vs accept bundled unbundling 在本页 item 3 完成。

怎样写 Extend / Verify、怎样测、怎样写空扩展是规范里的做法，本页不抄。

## 官方为什么这样拆

- **会面对和 Req 5 同一类活性问题 not already lost safety ≠ 已经丢了安全性 interchangeable：** 官方把扩展这条活性问题和已经丢了安全性分开。
- **看见和 Req 5 同一路 not already Req 3 proposal coherence ≠ 已经是提案一致性 interchangeable：** 官方把和 Req 5 同一路和已经是提案一致性分开。
- **看见扩展这条 not already settled ≠ 已经交差 interchangeable：** 官方把扩展这条和已经交差分开；348 req6 vs accept bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 会面对和 Req 5 同一类活性问题 | 不是已经丢了安全性 | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |
| 看见和 Req 5 同一路 | 不是已经是提案一致性 | 不是验签拒收整张预提交就已经是块非法（34） |
| 看见扩展这条 | 不是已经交差 | 不是必须 Accept 就已经任意扩展都会过（869） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看会面对和 Req 5 同一类活性问题 not already lost safety / not already Req 3 proposal coherence / not already settled 正式三事（348 余量），必须分开是不是已经丢了安全性、是不是已经是提案一致性、是不是已经交差。可以跳过「看见会伤活性就已经丢了安全性」。不要另写怎样写 Extend 或 Verify。348 req6 vs accept bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Extend / Verify、怎样测、怎样写空扩展。
- Extend–Verify 一致性 bundled。那是不变量 348。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348 item 1 余量 / 869。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
