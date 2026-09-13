# 例：看见应用 SHOULD 总是设 ProcessProposalResponse.status 为 ACCEPT 不是已经 honest proposal 必须 Accept；看见除非真的知道 REJECT 的活性代价不是已经 REJECT 是免费过滤；看见写了默认 Accept 不是已经是 Requirement 3 已经测过

**层次**：实现 / ProcessProposal SHOULD Accept 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「应用 SHOULD 总是设 ACCEPT 不是已经 honest proposal 必须 Accept / 除非真的知道 REJECT 的活性代价不是已经 REJECT 是免费过滤 / 写了默认 Accept 不是已经是 Requirement 3 已经测过」，不是 Process 回包栏 bundled 三事，也不是 Process 必须只依赖请求和上一份状态那种 SHOULD Accept 通则，也不是 Process REJECT 共识假设。不要另写怎样写默认 Accept 策略。

## 官方三件事

规范把应用 SHOULD 总是设 ACCEPT、除非真的知道 REJECT 的活性代价、SHOULD Accept 默认策略写成三件独立的实现事，不是「看见写了默认 Accept 就已经 honest proposal 必须 Accept、已经 REJECT 是免费过滤、已经 Requirement 3 已经测过」一件事：

1. **看见应用 SHOULD 总是设 `ProcessProposalResponse.status` 为 `ACCEPT` / 看见 SHOULD always set to ACCEPT 不是已经 honest proposal 必须 Accept，也不是已经是 Requirement 3 已经测过。**  
   官方写：Moreover, application implementers SHOULD always set `ProcessProposalResponse.status` to `ACCEPT`。看见 SHOULD 总是 Accept，不是已经正确提议者的准备提案必须被正确接收者 Accept 那种 honest proposal 必须 Accept。看见写了默认 Accept，不是已经 Requirement 3 是大量测试和自动验证的目标那种已经测过。看见 SHOULD，不是已经 MUST Accept 任何块。
2. **看见除非他们 _really_ know what the potential liveness implications of returning `REJECT` are / 看见除非真的知道 REJECT 的活性代价 不是已经 REJECT 是免费过滤，也不是已经 Process REJECT = prevote nil 那种已经结算。**  
   官方写：unless they _really_ know what the potential liveness implications of returning `REJECT` are。看见除非真的知道活性代价，不是已经 Process REJECT 是 prevote nil 不是免费过滤（33）就已经是同一句 interchangeable。看见知道 liveness implications，不是已经 REJECT 时共识假设不合法（455）就已经是不能 Reject。看见可以 Reject，不是已经 REJECT 没有代价。
3. **看见 SHOULD Accept 默认策略不是已经不能 Reject，也不是已经 Process 必须只依赖请求和上一份状态那种 SHOULD Accept 通则 interchangeable。**  
   官方 Usage 也写：If `ProcessProposalResponse.status` is `REJECT`, consensus assumes the proposal received is not valid。看见 SHOULD Accept，不是已经不能回 REJECT。看见默认 Accept，不是已经 Process 非确定 bug 没有现成解法那种 SHOULD Accept 通则（340）就已经是同一句 interchangeable。看见 SHOULD，不是已经 status 必须只依赖请求和上一份状态（430 bundled）就已经是 MUST Accept。

怎样写默认 Accept 策略、怎样评估 REJECT 活性代价、怎样写 Process 回包栏是规范里的做法，本页不抄。Process 回包栏 bundled 三事（430）是 REJECT 共识假设 / status 必须只依赖 / SHOULD Accept 那套另一切片，Process 必须只依赖请求和上一份状态（340）是 Req 4–5 / 非确定 bug 那套另一切片，Process REJECT 共识假设（455）是 assumes not valid / prevote nil 那套另一切片，本页不抄。

## 官方为什么这样拆

- **SHOULD 总是设 ACCEPT ≠ 已经 honest proposal 必须 Accept：** 官方把 SHOULD 建议和 Requirement 3 必须 Accept 分开。
- **除非真的知道 REJECT 的活性代价 ≠ 已经 REJECT 是免费过滤：** 官方把 liveness implications 和 Process REJECT = prevote nil 不是免费过滤分开。
- **SHOULD Accept 默认策略 ≠ 已经 Requirement 3 已经测过：** 官方把 Usage SHOULD 和 Req 3 测试目标分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| SHOULD 总是设 ACCEPT | 不是已经 honest proposal 必须 Accept | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |
| 除非真的知道 REJECT 的活性代价 | 不是已经 REJECT 是免费过滤 | 不是 Process REJECT = prevote nil 不是免费过滤（33） |
| SHOULD Accept 默认策略 | 不是已经 Requirement 3 已经测过 | 不是 Process 回包栏 bundled 三事（430） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见写了默认 Accept 就已经 honest proposal 必须 Accept、已经 REJECT 是免费过滤、已经 Requirement 3 已经测过」，必须分开应用 SHOULD 总是设 ACCEPT 是不是已经 honest proposal 必须 Accept、除非真的知道 REJECT 的活性代价是不是已经 REJECT 是免费过滤、SHOULD Accept 默认策略是不是已经 Requirement 3 已经测过。可以跳过「看见写了默认 Accept 就已经 honest proposal 必须 Accept」。不要另写怎样写默认 Accept 策略。

## 本页不抄

- 怎样写默认 Accept 策略、怎样评估 REJECT 活性代价、怎样写 Process 回包栏。
- Process 回包栏 bundled 三事。那是不变量 430。
- Process 必须只依赖请求和上一份状态 / SHOULD Accept 通则。那是不变量 340。
- Process REJECT 共识假设。那是不变量 455。
