# 例：看见 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 is not already only liveness interchangeable / not already block invalid interchangeable / not already nondet interchangeable

**层次**：实现 / Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness / not already block invalid / not already nondet 正式三事（348 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness / not already block invalid / not already nondet 正式三事（348 余量）/ not 870 req6-notliveness interchangeable / not 348 req6-coherence-vs-accept bundled interchangeable」，不是 Extend–Verify 一致性 bundled（348），也不是 Verify 必须只依赖扩展、这块和上一份状态（341），也不是验签拒收整张预提交就已经是块非法（34）。不要另写怎样写 Extend 或 Verify。

## 官方三件事

1. **看见 Extend 或 Verify（或两边）里有确定 bug / 看见带无效扩展的 Precommit 会被丢掉 这份确定 is not already 已经只是活性问题 interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 870 req6-notliveness interchangeable / 869 req6-notany interchangeable / 348 req6 item 1 必须 Accept interchangeable，也不是已经 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness / not already block invalid / not already nondet 正式三事 bundled（348 item 2 余量） interchangeable / 348 req6 item 2 interchangeable。**  
   官方写：反过来，若 `ExtendVote` 或 `VerifyVoteExtension`（或两边）里有确定 bug，带无效扩展的 Precommit 会被丢掉。看见有确定 bug，不是已经只伤活性 interchangeable——本页从 348 item 2 侧钉 not already only liveness 单句。348 req6 vs accept bundled unbundling 在本页 item 2 续。

2. **看见带无效扩展的 Precommit 会被丢掉 / 看见算丢掉 / 这份确定 is not already 已经是块非法 interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 870 req6-notliveness interchangeable / 348 req6 item 3 活性 interchangeable / 871 req6-notsafety interchangeable，也不是已经验签拒收整张预提交就已经是块非法 interchangeable / 34 voteext interchangeable。**  
   官方把 Precommit 被丢掉和已经是块非法分开——348 bundled 第二件事常与 34 / 341 混成「看见丢掉就已经只是活性或已经是块非法 interchangeable」，本页钉 not already block invalid 单句。

3. **看见带无效扩展的 Precommit 会被丢掉 / 看见有确定 bug / 这份确定 is not already 已经是 Verify 非确定 bug interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 870 req6-notliveness interchangeable / 869 req6-notany interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态 interchangeable / 341 verifydet interchangeable。**  
   官方把确定 bug 和已经是 341 那种 Accept/Reject 不再确定分开。看见算丢掉，不是已经是非确定 bug interchangeable。348 req6 vs accept bundled unbundling 在本页 item 2 续。

怎样写 Extend / Verify、怎样测、怎样写空扩展是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness ≠ 已经只是活性问题 interchangeable：** 官方把确定 bug 丢掉 Precommit 和只伤活性分开。
- **看见 Precommit 被丢掉 not already block invalid ≠ 已经是块非法 interchangeable：** 官方把丢掉和已经是块非法分开。
- **看见有确定 bug not already nondet ≠ 已经是非确定 bug interchangeable：** 官方把确定 bug 和已经是非确定 bug 分开；348 req6 vs accept bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 | 不是已经只是活性问题 | 不是 Verify 必须只依赖扩展、这块和上一份状态（341） |
| 看见 Precommit 被丢掉 | 不是已经是块非法 | 不是验签拒收整张预提交就已经是块非法（34） |
| 看见有确定 bug | 不是已经是非确定 bug | 不是必须 Accept 就已经任意扩展都会过（869） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness / not already block invalid / not already nondet 正式三事（348 余量），必须分开是不是已经只是活性问题、是不是已经是块非法、是不是已经是非确定 bug。可以跳过「看见丢掉就已经只是活性问题」。不要另写怎样写 Extend 或 Verify。348 req6 vs accept bundled unbundling 在本页 item 2 续；续 [`worked-example-req6-notsafety-vs-bundled.md`](worked-example-req6-notsafety-vs-bundled.md)（不变量 871 item 3）。

## 本页不抄

- 怎样写 Extend / Verify、怎样测、怎样写空扩展。
- Extend–Verify 一致性 bundled。那是不变量 348。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348 item 1 余量 / 869。
- Verify 必须只依赖扩展、这块和上一份状态。那是不变量 341。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
