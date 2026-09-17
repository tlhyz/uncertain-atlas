# 例：看见正确进程交出的扩展必须被正确接收者 Verify Accept is not already any extension Accepts interchangeable / not already default Accept interchangeable / not already settled interchangeable

**层次**：实现 / 正确进程交出的扩展必须被正确接收者 Verify Accept not already any extension Accepts / not already default Accept / not already settled 正式三事（348 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「正确进程交出的扩展必须被正确接收者 Verify Accept not already any extension Accepts / not already default Accept / not already settled 正式三事（348 余量）/ not 869 req6-notany interchangeable / not 348 req6-coherence-vs-accept bundled interchangeable」，不是 Extend–Verify 一致性 bundled（348），也不是验签拒收整张预提交就已经是块非法（34），也不是 Req 9 无副作用（349/868）。不要另写怎样写 Extend 或 Verify。

## 官方三件事

1. **看见正确进程交出的扩展、正确接收者 Verify 必须 Accept / 看见正确进程之间永远过 这份必须 is not already 已经是任意扩展都会 Accept interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 869 req6-notany interchangeable / 870 req6-notliveness interchangeable / 348 req6 item 2 确定 bug interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept not already any extension Accepts / not already default Accept / not already settled 正式三事 bundled（348 item 1 余量） interchangeable / 348 req6 item 1 interchangeable。**  
   官方写：任意两个不同的正确进程 *p*、*q*，若 *q* 在高度 *h* 收到 *p* 交出的扩展，*q* 的应用必须在 `VerifyVoteExtensionResponse` 里回 Accept。看见正确进程交出来的必须过，不是任意扩展已经都会过 interchangeable——本页从 348 item 1 侧钉 not already any extension Accepts 单句。348 req6 vs accept bundled unbundling 在本页 item 1 启动。

2. **看见正确进程之间永远过 / 看见必须 Accept / 这份必须 is not already 已经写了默认 Accept interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 869 req6-notany interchangeable / 348 req6 item 3 活性 interchangeable / 871 req6-notsafety interchangeable，也不是已经验签拒收整张预提交就已经是块非法 interchangeable / 34 voteext interchangeable。**  
   官方把必须 Accept 和已经写了默认 Accept 分开——348 bundled 第一件事常与 34 混成「看见必须 Accept 就已经任意扩展都会过或已经是默认 Accept interchangeable」，本页钉 not already default Accept 单句。

3. **看见正确进程之间永远过 / 看见正确进程交出来的必须过 / 这份必须 is not already 已经交差 interchangeable，也不是已经 Extend–Verify 一致性 bundled（348） interchangeable / 869 req6-notany interchangeable / 870 req6-notliveness interchangeable，也不是已经 Req 9 无副作用 interchangeable / 349 req9 / 868 req9-notext interchangeable。**  
   官方把正确进程之间过和拜占庭扩展已经也会过 / 已经交差分开。看见正确进程之间过，不是拜占庭扩展已经也会过 interchangeable。348 req6 vs accept bundled unbundling 在本页 item 1 启动。

怎样写 Extend / Verify、怎样测、怎样写空扩展是规范里的做法，本页不抄。

## 官方为什么这样拆

- **正确进程交出的扩展必须被正确接收者 Verify Accept not already any extension Accepts ≠ 已经是任意扩展都会 Accept interchangeable：** 官方把正确进程之间必须过和任意扩展都会过分开。
- **看见必须 Accept not already default Accept ≠ 已经写了默认 Accept interchangeable：** 官方把必须 Accept 和已经写了默认 Accept 分开。
- **看见正确进程之间过 not already settled ≠ 已经交差 interchangeable：** 官方把正确进程之间过和已经交差分开；348 req6 vs accept bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 正确进程交出的扩展必须被正确接收者 Verify Accept | 不是已经是任意扩展都会 Accept | 不是验签拒收整张预提交就已经是块非法（34） |
| 看见必须 Accept | 不是已经写了默认 Accept | 不是 Req 9 无副作用（349/868） |
| 看见正确进程之间过 | 不是已经交差 | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确进程交出的扩展必须被正确接收者 Verify Accept not already any extension Accepts / not already default Accept / not already settled 正式三事（348 余量），必须分开是不是已经是任意扩展都会 Accept、是不是已经写了默认 Accept、是不是已经交差。可以跳过「看见必须 Accept 就已经交差」。不要另写怎样写 Extend 或 Verify。348 req6 vs accept bundled unbundling 在本页 item 1 启动；续 [`worked-example-req6-notliveness-vs-bundled.md`](worked-example-req6-notliveness-vs-bundled.md)（不变量 870 item 2）。

## 本页不抄

- 怎样写 Extend / Verify、怎样测、怎样写空扩展。
- Extend–Verify 一致性 bundled。那是不变量 348。
- Extend 或 Verify 里有确定 bug。那是不变量 348 item 2 余量 / 870。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- Req 9 无副作用。那是不变量 349 / 868。
