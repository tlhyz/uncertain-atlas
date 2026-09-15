# 例：看见 ProcessProposalResponse.status 是 REJECT 时共识假设收到的提案不合法不是已经当成块非法；看见验证者会 prevote nil 不是已经 VerifyVoteExtension REJECT 拒整张票；看见 REJECT 共识假设不是已经不能整块执行候选

**层次**：实现 / ProcessProposal REJECT 共识假设正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「REJECT 时共识假设收到的提案不合法不是已经当成块非法 / 验证者会 prevote nil 不是已经 VerifyVoteExtension REJECT 拒整张票 / REJECT 共识假设不是已经不能整块执行候选」，不是 Process 回包栏 bundled 三事，也不是 ProposalStatus 枚举语义，也不是四门 REJECT = prevote nil 那种已经结算。不要另写怎样挑 ACCEPT/REJECT。

## 官方三件事

规范把 REJECT 时共识假设收到的提案不合法、验证者 prevote nil、REJECT 与整块执行候选分开写成三件独立的实现事，不是「看见 Process 回了 REJECT 就已经当成块非法、已经 prevote nil  interchangeable、已经不能整块执行候选」一件事：

1. **看见 `ProcessProposalResponse.status` 是 `REJECT` 时共识假设收到的提案不合法 / 看见共识 assumes the proposal received is not valid 不是已经当成块非法，也不是已经永久标成非法块。**  
   官方写：If `ProcessProposalResponse.status` is `REJECT`, consensus assumes the proposal received is not valid。看见假设不合法，不是已经验签拒收整张 Precommit 就已经是块非法那种已经当成块非法。看见共识 assumes not valid，不是已经应用状态里永久拉黑这块。看见 REJECT，不是已经 ProposalStatus 枚举语义（376）就已经是同一句 interchangeable。
2. **看见验证者会 prevote nil / 看见 When 里 `REJECT`: _p_ prevotes `nil` 不是已经 VerifyVoteExtension REJECT 拒整张票，也不是已经四门 REJECT = prevote nil 那种已经结算。**  
   官方 When 写：If _p_ is a validator and the returned value is `REJECT`: _p_ prevotes `nil`。看见会 prevote nil，不是已经 VerifyVoteExtensionResponse.status 是 REJECT 那种拒掉整张 Precommit。看见验证者 prevote nil，不是已经 Process 回包栏 bundled（430）里 status 必须只依赖请求和上一份状态就已经是同一句 interchangeable。看见 REJECT 后 prevote nil，不是已经 async Process 之后还能 Reject（354）。
3. **看见 REJECT 共识假设不是已经不能整块执行候选，也不是已经 Process MAY 整块执行就意味着已经交差。**  
   官方 Usage 也写：The Application MAY fully execute the block (immediate execution)。However, any resulting state changes must be kept as _candidate state_。看见回了 REJECT，不是已经不能 MAY 像 Finalize 那样整块执行出候选。看见 assumes not valid，不是已经 Process 跑过就意味着已经改了已提交状态（452）。看见共识假设不合法，不是已经 Finalize + Commit 那种已经交差。

怎样挑 ACCEPT/REJECT、怎样整块执行候选、怎样写 Process 回包栏是规范里的做法，本页不抄。Process 回包栏 bundled 三事（430）是 status 必须只依赖请求和上一份状态 / SHOULD Accept 那套另一切片，ProposalStatus 枚举语义（376）是 UNKNOWN/ACCEPT/REJECT 那套另一切片，四门 REJECT = prevote nil 不是免费过滤（33）是四门已经结算那套另一切片，本页不抄。

## 官方为什么这样拆

- **REJECT → consensus assumes not valid ≠ 已经当成块非法：** 官方把共识假设不合法和块非法、永久拉黑分开。
- **REJECT → prevote nil ≠ 已经 VerifyVoteExtension REJECT：** 官方把 Process prevote nil 和 Verify 拒整张票分开。
- **REJECT 共识假设 ≠ 已经不能整块执行候选：** 官方把 assumes not valid 和 MAY fully execute / candidate state 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT → consensus assumes not valid | 不是已经当成块非法 | 不是 VerifyVoteExtension REJECT 拒整张票（433） |
| REJECT → prevote nil | 不是已经 Verify 拒整张票 | 不是 Process 回包栏 bundled 三事（430） |
| REJECT 共识假设 | 不是已经不能整块执行候选 | 不是 Process MAY 整块执行就已经交差（452） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 回了 REJECT 就已经当成块非法、已经 prevote nil interchangeable、已经不能整块执行候选」，必须分开 REJECT 时共识假设收到的提案不合法是不是已经当成块非法、验证者 prevote nil 是不是已经 VerifyVoteExtension REJECT、REJECT 共识假设是不是已经不能整块执行候选。可以跳过「看见 Process 回了 REJECT 就已经当成块非法」。不要另写怎样挑 ACCEPT/REJECT。

## 本页不抄

- 怎样挑 ACCEPT/REJECT、怎样整块执行候选、怎样写 Process 回包栏。
- Process 回包栏 bundled 三事。那是不变量 430。
- ProposalStatus 枚举语义。那是不变量 376。
- Process REJECT = prevote nil 不是免费过滤。那是不变量 33。
