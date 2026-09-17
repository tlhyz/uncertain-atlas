# 例：看见 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经验过扩展；看见 VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票不是已经当成块非法；看见 VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票不是已经会发 Prevote nil

**层次**：实现 / VerifyStatus。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经验过扩展 / VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票不是已经当成块非法 / VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票不是已经会发 Prevote nil」，不是 ProposalStatus 那种 ACCEPT 会发 Prevote，也不是 VerifyVoteExtensionResponse.status 必须只依赖请求和上一份状态那种对任意扩展同一裁决。不要另写怎样写 VerifyStatus。

## 官方三件事

规范把 VerifyStatus 的 UNKNOWN 一律是错、ACCEPT 会收下这张票、REJECT 会拒掉整张票写成三件独立的实现事，不是「看见回了 VerifyStatus 就已经验过扩展、已经当成块非法、已经会发 Prevote nil」一件事：

1. **看见 VerifyStatus 的 `UNKNOWN` 一律是错、引擎当应用坏了会崩 / 看见回了 `UNKNOWN` 不是已经验过扩展，也不是已经扩展启用。**  
   官方写：`VerifyStatus` 用在 `VerifyVoteExtension` 回包。若 `Status` 是 `UNKNOWN`，应用出了问题。CometBFT 会当应用坏了，然后崩。看见回了 `UNKNOWN`，不是已经验过扩展。看见崩了，不是已经扩展启用。看见有枚举，不是已经选型。
2. **看见 VerifyStatus 的 `ACCEPT` 表示应用认为扩展合法、共识会收下这张票 / 看见回了 `ACCEPT` 不是已经当成块非法，也不是已经正确进程交出的扩展必须 Accept。**  
   官方写：若 `Status` 是 `ACCEPT`，共识算法会收下这张票，当成合法。Usage 也写：*p* 会把收到的票和对应扩展留在内部结构。看见回了 `ACCEPT`，不是已经验签拒收整张 Precommit 就已经是块非法那种已经当成块非法。看见会收下这张票，不是已经是 Requirement 6 必须 Accept 那种已经必须 Accept。看见合法，不是已经块合法。
3. **看见 VerifyStatus 的 `REJECT` 表示应用认为扩展非法、共识会拒掉整张票 / 看见回了 `REJECT` 不是已经会发 Prevote nil，也不是已经当成块非法。**  
   官方写：若 `Status` 是 `REJECT`，共识算法会拒掉整张票，当成非法。Usage 也写：*p* 会把这张 Precommit 当非法丢掉。看见回了 `REJECT`，不是已经 ProposalStatus 那种 REJECT 会发 Prevote nil。看见拒掉整张票，不是已经 ProcessProposalResponse.status 那种 REJECT 会让验证者 prevote nil。看见非法，不是已经当成块非法。

怎样写 `VerifyStatus`、怎样挑枚举、怎样拒整张 Precommit 是规范里的做法，本页不抄。ProposalStatus 那种 ACCEPT 会发 Prevote 是不变量 376，本页不抄。

## 官方为什么这样拆

- **VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩 ≠ 已经验过扩展：** 官方把回 UNKNOWN 会崩和已经验过扩展分开。
- **VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票 ≠ 已经当成块非法：** 官方把收下这张票和块非法分开。
- **VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票 ≠ 已经会发 Prevote nil：** 官方把拒整张 Precommit 和 Process 的 Prevote nil 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩 | 不是已经验过扩展 | 不是 UNKNOWN 一律是错就已经是四门已经结算（376） |
| VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票 | 不是已经当成块非法 | 不是 ACCEPT 表示应用认为提案合法、共识会发 Prevote（376） |
| VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票 | 不是已经会发 Prevote nil | 不是 REJECT 表示应用认为提案非法、共识会发 Prevote nil（376） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 VerifyStatus 就已经验过扩展、已经当成块非法、已经会发 Prevote nil」，必须分开 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩是不是已经验过扩展、VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票是不是已经当成块非法、VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票是不是已经会发 Prevote nil。可以跳过「看见回了 VerifyStatus 就已经验过扩展」。不要另写怎样写 VerifyStatus。

## 本页不抄

- 怎样写 `VerifyStatus`、怎样挑枚举、怎样拒整张 Precommit。
- ProposalStatus 那种 ACCEPT 会发 Prevote。那是不变量 376。
- VerifyVoteExtensionResponse.status 必须只依赖请求和上一份状态。那是不变量 433。
- 验签拒收整张 Precommit 就已经是块非法。那是不变量 34。
