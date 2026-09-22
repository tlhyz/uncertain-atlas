# 例：看见正确进程交出的扩展必须被正确接收者 Verify Accept / 看见正确进程之间永远过 / 看见必须 Accept is not already already any-extension interchangeable / already default-accept interchangeable / already settled interchangeable

**层次**：实现 / 正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事（348 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事（348 余量）/ not 797 req6-notany interchangeable / not 348 req6coherence bundled interchangeable」，不是 Extend–Verify 一致性 bundled（348），也不是 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题（798 item 2 余量）或会面对和 Req 5 同一类活性问题不是已经丢了安全性（799 item 3 余量）。不要另写怎样写 Extend 或 Verify。

## 官方三件事

规范把 Requirements 里正确进程交出的扩展、正确接收者 Verify 必须 Accept 和「已经是正确进程之间过就已经任意扩展都会 Accept interchangeable / 已经是必须 Accept 就已经写了默认 Accept interchangeable / 已经是正确进程之间过就已经交差 interchangeable / 已经是 req6coherence bundled interchangeable」分开写成三件独立的实现事，不是「看见必须 Accept 就已经任意扩展都会过 interchangeable / 就已经写了默认 Accept interchangeable / 就已经交差 interchangeable」一件事：

1. **看见正确进程交出的扩展、正确接收者 Verify 必须 Accept / 看见正确进程之间永远过 / 看见正确进程交出来的必须过 is not already 已经是任意扩展都会 Accept interchangeable / 已经 any-extension interchangeable / 已经任意扩展过交差 interchangeable / 348 req6coherence bundled interchangeable / 34 voteext interchangeable / req6coherence-sold-as-accept interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 797 req6-notany interchangeable / 348 req6 item 1 interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事 bundled（348 item 1 余量） interchangeable / 348 req6 item 1 interchangeable，也不是已经 Extend 或 Verify 里有确定 bug（798） interchangeable / 799 req6-notsafety interchangeable / 347 req3coherence interchangeable，也不是已经验签拒收整张预提交就已经是块非法（34） interchangeable。**  
   官方写：任意两个不同的正确进程 *p*、*q*，若 *q* 在高度 *h* 收到 *p* 交出的扩展 *e<sup>r</sup><sub>p</sub>*，*q* 的应用必须在 `VerifyVoteExtensionResponse` 里回 Accept。看见正确进程交出来的必须过，不是任意扩展已经都会过。看见正确进程之间永远过，不是已经 any-extension interchangeable——348 钉 bundled 三事，本页从 item 1 侧钉 not already any-extension 单句。看见正确进程交出的扩展、正确接收者 Verify 必须 Accept，不是已经 Extend–Verify 一致性 bundled（348） interchangeable——348 钉 bundled，本页钉 item 1 第一件事。看见正确进程之间永远过，不是已经验签拒收整张预提交就已经是块非法（34） interchangeable——34 另钉。348 req6 vs accept bundled unbundling 在本页 item 1 启动。

2. **看见必须 Accept / 看见正确接收者 Verify 必须回 Accept / 看见正确进程之间永远过 is not already 已经写了默认 Accept interchangeable / 已经 default-accept interchangeable / 已经默认 Accept 交差 interchangeable / 348 req6coherence bundled interchangeable / 34 voteext interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 797 req6-notany interchangeable / 348 req6 item 2 确定 bug interchangeable / 348 req6 item 3 活性 interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事 bundled（348 item 1 余量） interchangeable / 348 req6 item 1 interchangeable，也不是已经是任意扩展都会 Accept（本页第一件事） interchangeable。**  
   官方写：看见必须 Accept，不是已经写了默认 Accept。看见正确接收者 Verify 必须回 Accept，不是已经 default-accept interchangeable——本页钉 not already default-accept 单句。看见正确进程之间永远过，不是已经是任意扩展都会 Accept（本页第一件事） interchangeable——三件事分开钉。348 req6 vs accept bundled unbundling 在本页 item 1 启动。

3. **看见正确进程之间过 / 看见正确进程交出来的必须过 / 看见正确接收者必须 Accept is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经 Accept 交差 interchangeable / 348 req6coherence bundled interchangeable / 347 req3coherence interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 797 req6-notany interchangeable / 348 req6 item 2 / 348 req6 item 3，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事 bundled（348 item 1 余量） interchangeable / 348 req6 item 1 interchangeable，也不是已经是任意扩展都会 Accept（本页第一件事） interchangeable / 已经写了默认 Accept（本页第二件事） interchangeable。**  
   官方写：看见正确进程之间过，不是拜占庭扩展已经也会过，也不是已经交差。看见正确进程交出来的必须过，不是已经 settled interchangeable——本页钉 not already settled 单句。看见正确接收者必须 Accept，不是已经写了默认 Accept（本页第二件事） interchangeable——三件事分开钉。348 req6 vs accept bundled unbundling 在本页 item 1 启动。

怎样写 Extend / Verify、怎样测、怎样写空扩展是规范里的做法，本页不抄。Extend–Verify 一致性 bundled（348）、Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题（348 item 2 余量 / 798）、会面对和 Req 5 同一类活性问题不是已经丢了安全性（348 item 3 余量 / 799）、验签拒收整张预提交就已经是块非法（34）、正确提议者的准备提案必须被正确接收者 Accept（347）、Req 9 无副作用（349）是另外那套，本页不抄。

## 官方为什么这样拆

- **正确进程交出的扩展必须被正确接收者 Verify Accept not already any-extension ≠ 348 / 34 interchangeable：** 官方把正确进程之间必须过和任意扩展都会过分开。
- **必须 Accept not already default-accept ≠ 已经写了默认 Accept interchangeable：** 官方把必须 Accept 和已经写了默认 Accept 分开。
- **正确进程之间过 not already settled ≠ 已经交差 interchangeable：** 官方把正确进程之间过和已经交差分开；348 req6 vs accept bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 正确进程交出的扩展必须被正确接收者 Verify Accept | 不是 already any-extension | 不是验签拒收整张预提交就已经是块非法 alone（34） |
| 必须 Accept | 不是 already default-accept | 不是 Req 9 无副作用 alone（349） |
| 正确进程之间过 | 不是 already settled | 不是正确提议者的准备提案必须被正确接收者 Accept alone（347） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事（348 余量），必须分开正确进程交出的扩展必须被正确接收者 Verify Accept 是不是 already any-extension interchangeable / 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable、必须 Accept 是不是 already default-accept interchangeable、正确进程之间过 是不是 already settled interchangeable。可以跳过「看见必须 Accept 就已经任意扩展都会过 interchangeable / 就已经写了默认 Accept interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Extend 或 Verify。348 req6 vs accept bundled unbundling 在本页 item 1 启动；续 [`worked-example-req6-notliveness-vs-bundled.md`](worked-example-req6-notliveness-vs-bundled.md)（不变量 798 item 2）；完成见 799。

## 本页不抄

- 怎样写 Extend / Verify、怎样测、怎样写空扩展。
- Extend–Verify 一致性 bundled。那是不变量 348。
- Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题。那是不变量 348 item 2 余量 / 798。
- 会面对和 Req 5 同一类活性问题不是已经丢了安全性。那是不变量 348 item 3 余量 / 799。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Req 9 无副作用。那是不变量 349。
