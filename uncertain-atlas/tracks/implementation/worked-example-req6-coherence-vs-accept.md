# 例：看见正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept；看见 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题；看见会面对和 Req 5 同一类活性问题不是已经丢了安全性

**层次**：实现 / Extend–Verify 一致性。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept / Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 / 会面对和 Req 5 同一类活性问题不是已经丢了安全性」，不是验签拒收整张预提交就已经是块非法，也不是 Verify 必须只依赖扩展、这块和上一份状态。不要另写怎样写 Extend 或 Verify。

## 官方三件事

规范把 Extend 和 Verify 的一致性写成三件独立的实现事，不是「看见必须 Accept 就已经任意扩展都会过、已经只是活性、已经丢了安全性」一件事：

1. **看见正确进程交出的扩展、正确接收者 Verify 必须 Accept / 看见正确进程之间永远过 不是已经是任意扩展都会 Accept，也不是已经是 Verify 默认 Accept。**  
   官方写：任意两个不同的正确进程 *p*、*q*，若 *q* 在高度 *h* 收到 *p* 交出的扩展 *e<sup>r</sup><sub>p</sub>*，*q* 的应用必须在 `VerifyVoteExtensionResponse` 里回 Accept。看见正确进程交出来的必须过，不是任意扩展已经都会过。看见必须 Accept，不是已经写了默认 Accept。看见正确进程之间过，不是拜占庭扩展已经也会过。
2. **看见 Extend 或 Verify（或两边）里有确定 bug / 看见带无效扩展的 Precommit 会被丢掉 不是已经只是活性问题，也不是已经是块非法，也不是已经是 Verify 非确定 bug。**  
   官方写：反过来，若 `ExtendVote` 或 `VerifyVoteExtension`（或两边）里有**确定** bug，带无效扩展的 Precommit 会被丢掉。看见有确定 bug，不是已经只伤活性。看见 Precommit 被丢掉，不是已经是块非法。看见算丢掉，不是已经是 341 那种 Accept/Reject 不再确定。
3. **看见会面对和 Requirement 5 同一类活性问题 / 看见和 Process 确定性那条同一路 不是已经丢了安全性，也不是已经是 347 那种提案一致性。**  
   官方写：这时会面对和 Requirement 5 写过的同一类活性问题。看见会伤活性，不是已经丢了安全性。看见和 Req 5 同一路，不是已经是正确提议者的准备提案必须被正确接收者 Accept。看见扩展这条，不是已经是提案那条。

怎样写 Extend / Verify、怎样测、怎样写空扩展是规范里的做法，本页不抄。验签拒收整张预提交是不变量 34，本页不抄。

## 官方为什么这样拆

- **正确进程交出的扩展必须被正确接收者 Verify Accept ≠ 已经是任意扩展都会 Accept：** 官方把正确进程之间必须过和任意扩展都会过分开。
- **Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 ≠ 已经只是活性问题：** 官方把确定 bug 丢掉 Precommit 和只伤活性、块非法、非确定 bug 分开。
- **会面对和 Req 5 同一类活性问题 ≠ 已经丢了安全性：** 官方把扩展这条活性问题和已经丢了安全性、提案一致性分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 正确进程交出的扩展必须被正确接收者 Verify Accept | 不是已经是任意扩展都会 Accept | 不是验签拒收整张预提交就已经是块非法（34） |
| Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 | 不是已经只是活性问题 | 不是 Verify 必须只依赖扩展、这块和上一份状态（341） |
| 会面对和 Req 5 同一类活性问题 | 不是已经丢了安全性 | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须 Accept 就已经任意扩展都会过、已经只是活性、已经丢了安全性」，必须分开正确进程交出的扩展必须被正确接收者 Verify Accept 是不是已经是任意扩展都会 Accept、Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉是不是已经只是活性问题、会面对和 Req 5 同一类活性问题是不是已经丢了安全性。可以跳过「看见必须 Accept 就已经交差」。不要另写怎样写 Extend 或 Verify。348 req6 vs accept bundled unbundling 完成（869 item 1 / 870 item 2 / 871 item 3）；精读 [`worked-example-req6-notany-vs-bundled.md`](worked-example-req6-notany-vs-bundled.md)（不变量 869 item 1）。

## 本页不抄

- 怎样写 Extend / Verify、怎样测、怎样写空扩展。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- Verify 必须只依赖扩展、这块和上一份状态。那是不变量 341。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
