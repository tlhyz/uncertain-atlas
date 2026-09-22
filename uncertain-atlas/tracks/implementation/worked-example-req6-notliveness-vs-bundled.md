# 例：看见 Extend 或 Verify 里有确定 bug / 看见带无效扩展的 Precommit 会被丢掉 / 看见有确定 bug is not already already only-liveness interchangeable / already block-invalid interchangeable / already nondet interchangeable

**层次**：实现 / Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事（348 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事（348 余量）/ not 798 req6-notliveness interchangeable / not 348 req6coherence bundled interchangeable」，不是 Extend–Verify 一致性 bundled（348），也不是正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept（797 item 1 余量）或会面对和 Req 5 同一类活性问题不是已经丢了安全性（799 item 3 余量）。不要另写怎样写 Extend 或 Verify。

## 官方三件事

规范把 Requirements 里 Extend 或 Verify（或两边）里有确定 bug、带无效扩展的 Precommit 会被丢掉 和「已经是有确定 bug 就已经只是活性问题 interchangeable / 已经是 Precommit 被丢掉就已经是块非法 interchangeable / 已经是有确定 bug 就已经是 Verify 非确定 bug interchangeable / 已经是 req6coherence bundled interchangeable」分开写成三件独立的实现事，不是「看见丢掉就已经只是活性问题 interchangeable / 就已经是块非法 interchangeable / 就已经是非确定 bug interchangeable」一件事：

1. **看见 Extend 或 Verify（或两边）里有确定 bug / 看见带无效扩展的 Precommit 会被丢掉 / 看见有确定 bug is not already 已经只是活性问题 interchangeable / 已经 only-liveness interchangeable / 已经只伤活性交差 interchangeable / 348 req6coherence bundled interchangeable / 341 verifydet interchangeable / req6coherence-sold-as-accept interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 798 req6-notliveness interchangeable / 348 req6 item 2 interchangeable，也不是已经 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事 bundled（348 item 2 余量） interchangeable / 348 req6 item 2 interchangeable，也不是已经正确进程交出的扩展必须 Accept（797） interchangeable / 799 req6-notsafety interchangeable / 34 voteext interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态（341） interchangeable。**  
   官方写：反过来，若 `ExtendVote` 或 `VerifyVoteExtension`（或两边）里有**确定** bug，带无效扩展的 Precommit 会被丢掉。看见有确定 bug，不是已经只伤活性。看见带无效扩展的 Precommit 会被丢掉，不是已经 only-liveness interchangeable——348 钉 bundled 三事，本页从 item 2 侧钉 not already only-liveness 单句。看见 Extend 或 Verify（或两边）里有确定 bug，不是已经 Extend–Verify 一致性 bundled（348） interchangeable——348 钉 bundled，本页钉 item 2 第一件事。看见有确定 bug，不是已经正确进程交出的扩展必须 Accept（797） interchangeable——797 另钉 item 1。348 req6 vs accept bundled unbundling 在本页 item 2 续。

2. **看见 Precommit 被丢掉 / 看见带无效扩展的 Precommit 会被丢掉 / 看见算丢掉 is not already 已经是块非法 interchangeable / 已经 block-invalid interchangeable / 已经块非法交差 interchangeable / 348 req6coherence bundled interchangeable / 34 vote-extension-sold-as-block interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 798 req6-notliveness interchangeable / 348 req6 item 1 必须 Accept interchangeable / 348 req6 item 3 活性 interchangeable，也不是已经 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事 bundled（348 item 2 余量） interchangeable / 348 req6 item 2 interchangeable，也不是已经只是活性问题（本页第一件事） interchangeable。**  
   官方写：看见 Precommit 被丢掉，不是已经是块非法。看见带无效扩展的 Precommit 会被丢掉，不是已经 block-invalid interchangeable——本页钉 not already block-invalid 单句。看见算丢掉，不是已经只是活性问题（本页第一件事） interchangeable——三件事分开钉。348 req6 vs accept bundled unbundling 在本页 item 2 续。

3. **看见有确定 bug / 看见算丢掉 / 看见确定 bug 让 Precommit 被丢掉 is not already 已经是 Verify 非确定 bug interchangeable / 已经 nondet interchangeable / 已经非确定交差 interchangeable / 348 req6coherence bundled interchangeable / 341 verifydet-sold-as-extend interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 798 req6-notliveness interchangeable / 348 req6 item 1 / 348 req6 item 3，也不是已经 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事 bundled（348 item 2 余量） interchangeable / 348 req6 item 2 interchangeable，也不是已经只是活性问题（本页第一件事） interchangeable / 已经是块非法（本页第二件事） interchangeable。**  
   官方写：看见有确定 bug，不是已经是 341 那种 Accept/Reject 不再确定。看见算丢掉，不是已经 nondet interchangeable——本页钉 not already nondet 单句。看见确定 bug 让 Precommit 被丢掉，不是已经是块非法（本页第二件事） interchangeable——三件事分开钉。348 req6 vs accept bundled unbundling 在本页 item 2 续。

怎样写 Extend / Verify、怎样测、怎样写空扩展是规范里的做法，本页不抄。Extend–Verify 一致性 bundled（348）、正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept（348 item 1 余量 / 797）、会面对和 Req 5 同一类活性问题不是已经丢了安全性（348 item 3 余量 / 799）、Verify 必须只依赖扩展、这块和上一份状态（341）、验签拒收整张预提交就已经是块非法（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only-liveness ≠ 348 / 341 interchangeable：** 官方把确定 bug 丢掉 Precommit 和只伤活性分开。
- **Precommit 被丢掉 not already block-invalid ≠ 已经是块非法 interchangeable：** 官方把丢掉和已经是块非法分开。
- **有确定 bug not already nondet ≠ 已经是非确定 bug interchangeable：** 官方把确定 bug 和已经是非确定 bug 分开；348 req6 vs accept bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 | 不是 already only-liveness | 不是 Verify 必须只依赖扩展、这块和上一份状态 alone（341） |
| Precommit 被丢掉 | 不是 already block-invalid | 不是验签拒收整张预提交就已经是块非法 alone（34） |
| 有确定 bug | 不是 already nondet | 不是必须 Accept 就已经任意扩展都会过 alone（797） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事（348 余量），必须分开 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 是不是 already only-liveness interchangeable / 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable、Precommit 被丢掉 是不是 already block-invalid interchangeable、有确定 bug 是不是 already nondet interchangeable。可以跳过「看见丢掉就已经只是活性问题 interchangeable / 就已经是块非法 interchangeable / 就已经是非确定 bug interchangeable」。不要另写怎样写 Extend 或 Verify。348 req6 vs accept bundled unbundling 在本页 item 2 续（797 + 798）；续 [`worked-example-req6-notsafety-vs-bundled.md`](worked-example-req6-notsafety-vs-bundled.md)（不变量 799 item 3）；完成见 799。

## 本页不抄

- 怎样写 Extend / Verify、怎样测、怎样写空扩展。
- Extend–Verify 一致性 bundled。那是不变量 348。
- 正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept。那是不变量 348 item 1 余量 / 797。
- 会面对和 Req 5 同一类活性问题不是已经丢了安全性。那是不变量 348 item 3 余量 / 799。
- Verify 必须只依赖扩展、这块和上一份状态。那是不变量 341。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
