# 例：看见验证者会 prevote nil / When 里 `REJECT`: _p_ prevotes `nil` / Process REJECT prevote nil is not Verify REJECT whole vote 不是已经 Process REJECT consensus assume bundled interchangeable / 已经 Verify REJECT whole vote interchangeable / 已经 Process 回包栏 bundled interchangeable

**层次**：实现 / ProcessProposal REJECT prevote nil not Verify whole vote 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process REJECT prevote nil not Verify whole vote 不是 Process REJECT consensus assume bundled interchangeable / 不是已经 Verify REJECT whole vote interchangeable / 不是已经 Process 回包栏 bundled interchangeable」，不是 Process REJECT consensus assume bundled（455），也不是 VerifyVoteExtensionResponse.status REJECT bundled（433），也不是 Process REJECT = prevote nil 不是免费过滤（33）。不要另写怎样挑 ACCEPT/REJECT。

## 官方三件事

规范把 ProcessProposal When 里 REJECT 后验证者 prevote nil 写成三件独立的实现事，不是「看见 Process 回了 REJECT 就已经 Verify REJECT whole vote interchangeable、已经 Process 回包栏 bundled interchangeable、已经 REJECT 是免费过滤 interchangeable」一件事：

1. **看见验证者会 prevote nil / 看见 When 里 If _p_ is a validator and the returned value is `REJECT`: _p_ prevotes `nil` / 看见 Process REJECT prevote nil is not Verify REJECT whole vote 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 Verify REJECT whole vote interchangeable / 已经 consensus rejects whole vote interchangeable，也不是已经 VerifyVoteExtensionResponse.status is REJECT bundled（433） interchangeable / 已经 consensus rejects whole vote interchangeable / 已经验签拒收整张 Precommit interchangeable，也不是已经 VerifyStatus REJECT bundled（539 余量） interchangeable / 已经 rejects whole vote interchangeable / 已经 Process prevote nil interchangeable，也不是已经 ProcessProposalResponse.status valid/invalid bundled（533 余量） interchangeable / 已经 block invalid interchangeable / 已经 assumes not valid interchangeable，也不是已经 Process REJECT consensus assume not block invalid bundled（540 余量） interchangeable / 已经当成块非法 interchangeable。**  
   官方 When 写：If _p_ is a validator and the returned value is `REJECT`: _p_ prevotes `nil`。看见会 prevote nil，不是已经 VerifyVoteExtensionResponse.status 是 REJECT 那种拒掉整张 Precommit——455 bundled 常被写成「回了 REJECT 就已经 Verify REJECT whole vote」，本页钉 Process prevote nil not Verify whole vote 单句。看见 prevote nil，不是已经 Verify 433 REJECT whole vote interchangeable——433 钉 Verify Response status REJECT 拒整张票，本页钉 Process When prevote nil 单句。看见 _p_ prevotes nil，不是已经 VerifyStatus REJECT（539 余量） interchangeable——539 钉 VerifyStatus REJECT rejects whole vote，本页钉 Process When prevote nil 边界。
2. **看见 Process REJECT prevote nil is not Process 回包栏 bundled interchangeable / 看见验证者 prevote nil 不是已经 Process 回包栏 bundled（430） interchangeable / 已经 status 必须只依赖 interchangeable / 已经 MUST Accept interchangeable 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 assumes not valid interchangeable / 已经 block invalid interchangeable，也不是已经 ProcessProposalResponse.status valid/invalid bundled（533 余量） interchangeable / 已经 status valid/invalid interchangeable / 已经 assumes not valid not block invalid interchangeable，也不是已经 ProcessProposalResponse.status must exclusively depend bundled（534 余量） interchangeable / 已经和对任意块同一裁决 interchangeable，也不是已经 Process REJECT consensus assume not block invalid bundled（540 余量） interchangeable / 已经当成块非法 interchangeable / 已经 permanently blacklisted interchangeable，也不是已经 ProposalStatus REJECT bundled（376） interchangeable / 已经会发 Prevote nil interchangeable。**  
   官方把 Process When prevote nil 和 Process 回包栏 bundled 三事分开——455 bundled 常与 430 混成「回了 REJECT 就已经 status 必须只依赖 interchangeable」，本页钉 prevote nil not Process resp bundled 单句。看见 prevote nil，不是已经 Process 回包栏 bundled（430） interchangeable——430 钉 Response status 依赖 / SHOULD Accept，本页钉 When prevote nil 单句。看见 When 后效，不是已经 status valid/invalid（533 余量） interchangeable——533 钉 Response status 语义，本页钉 When prevote nil 边界。
3. **看见 Process REJECT prevote nil is not async Process can still Reject / 看见 REJECT 后 prevote nil 不是已经 async Process 之后还能 Reject 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 async Process 之后还能 Reject interchangeable / 已经 REJECT 是免费过滤 interchangeable，也不是已经 Process REJECT = prevote nil 不是免费过滤 bundled（33） interchangeable / 已经 REJECT 是免费过滤 interchangeable / 已经当成块非法 interchangeable / 已经四门 REJECT = prevote nil 那种已经结算 interchangeable，也不是已经 ProcessProposal Usage unless really know liveness implications bundled（531 余量） interchangeable / 已经 REJECT 没有代价 interchangeable，也不是已经 Process REJECT consensus assume not block invalid bundled（540 余量） interchangeable / 已经 assumes not valid interchangeable，也不是已经 Process REJECT consensus assume can't execute bundled（542 余量） interchangeable / 已经不能整块执行候选 interchangeable。**  
   官方 When 把 REJECT 后 prevote nil 和 async Process 之后还能 Reject 分开——455 bundled 常与 354 混成「prevote nil 就已经 async 之后还能 Reject」，本页钉 prevote nil not async can still Reject 单句。看见 prevote nil，不是已经 Process REJECT = prevote nil 不是免费过滤（33） interchangeable——33 钉四门 REJECT 不是免费过滤，本页钉 When prevote nil 单句。看见 When 后效，不是已经 unless really know liveness（531 余量） interchangeable——531 钉 REJECT 有活性代价，本页钉 When prevote nil 边界。

怎样挑 ACCEPT/REJECT、怎样写 Process 回包栏 是规范里的做法，本页不抄。Process REJECT consensus assume bundled（455）、Verify REJECT whole vote（433/539）、Process REJECT = prevote nil 不是免费过滤（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **Process prevote nil not Verify whole vote ≠ Process REJECT consensus assume bundled interchangeable：** 官方把 Process When prevote nil 和 Verify 拒整张 Precommit 分开。
- **prevote nil not Process resp bundled ≠ status must exclusively depend interchangeable：** 官方把 When prevote nil 和 Process 回包栏 bundled 分开。
- **prevote nil not async can still Reject ≠ REJECT free filter interchangeable：** 官方把 When prevote nil 和 async Process 之后还能 Reject / 四门 REJECT 不是免费过滤 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process REJECT prevote nil | 不是 Verify REJECT whole vote | 不是 VerifyVoteExtensionResponse.status REJECT（433） |
| prevote nil | 不是 Process resp bundled | 不是 Process 回包栏 bundled（430） |
| REJECT after prevote nil | 不是 async can still Reject | 不是 Process REJECT = prevote nil 不是免费过滤（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT prevote nil not Verify whole vote 正式三事，必须分开 Process prevote nil 是不是 Verify REJECT whole vote interchangeable / 433 whole vote interchangeable / 539 VerifyStatus REJECT interchangeable、prevote nil 是不是 Process resp bundled interchangeable / 430 status must exclusively depend interchangeable、REJECT after prevote nil 是不是 async can still Reject interchangeable / 33 free filter interchangeable。可以跳过「看见 Process 回了 REJECT 就已经 Verify REJECT whole vote interchangeable」。不要另写怎样挑 ACCEPT/REJECT。

## 本页不抄

- 怎样做挑 ACCEPT/REJECT、怎样写 Process 回包栏。
- REJECT → consensus assumes not valid ≠ block invalid。那是不变量 540（455 item 1 余量）。
- REJECT 共识假设 ≠ 已经不能整块执行候选。那是不变量 542（455 item 3 余量）。
- ProcessProposal Response status valid/invalid 正式三事 bundled。那是不变量 533。
