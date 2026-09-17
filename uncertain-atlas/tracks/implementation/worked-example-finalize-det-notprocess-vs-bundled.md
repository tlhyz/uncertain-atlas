# 例：看见两边状态机复制 is not already Process same verdict interchangeable / not already Prepare may be nondet interchangeable / not already settled interchangeable

**层次**：实现 / 两边状态机复制 not already Process same verdict / not already Prepare may be nondet / not already settled 正式三事（342 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边状态机复制 not already Process same verdict / not already Prepare may be nondet / not already settled 正式三事（342 余量）/ not 889 finalize-det-notprocess interchangeable / not 342 finalize-det-vs-prepare bundled interchangeable」，不是 FinalizeBlock 确定性 bundled（342），也不是 Process 必须只依赖请求和上一份状态（340），也不是 Prepare 没有确定性要求（338）。不要另写怎样写 FinalizeBlock。

## 官方三件事

1. **看见两边状态机复制 / 看见应用状态一起演化 这份复制 is not already 已经是 Process 对任意块同一裁决 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 889 finalize-det-notprocess interchangeable / 887 finalize-det-notprep interchangeable / 342 finalize-det item 1 状态 interchangeable，也不是已经两边状态机复制 not already Process same verdict / not already Prepare may be nondet / not already settled 正式三事 bundled（342 item 3 余量） interchangeable / 342 finalize-det item 3 interchangeable。**  
   官方写：Requirement 11 和 12 再加上共识的 Agreement，保证状态机复制：各正确进程上的应用状态一起演化。看见状态机复制，不是已经是 Process 对任意块同一 Accept/Reject interchangeable——本页从 342 item 3 侧钉 not already Process same verdict 单句。342 finalize-det vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见两边状态一起走 / 看见 Agreement / 这份复制 is not already 已经是 Prepare 可以不确定 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 889 finalize-det-notprocess interchangeable / 342 finalize-det item 2 T_h interchangeable / 888 finalize-det-notreceipt interchangeable，也不是已经 Process 必须只依赖请求和上一份状态 interchangeable / 340 processdet interchangeable。**  
   官方把两边状态一起走和已经是 Prepare 可以不确定分开——342 bundled 第三件事常与 340 / 338 混成「看见状态机复制就已经是 Process 同判或已经是 Prepare 可以不确定 interchangeable」，本页钉 not already Prepare may be nondet 单句。

3. **看见 Agreement / 看见状态机复制 / 这份复制 is not already 已经交差 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 889 finalize-det-notprocess interchangeable / 887 finalize-det-notprep interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把 Agreement 和已经交差分开。看见 Agreement，不是已经交差 interchangeable。342 finalize-det vs prepare bundled unbundling 在本页 item 3 完成。

怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **两边状态机复制 not already Process same verdict ≠ 已经是 Process 对任意块同一裁决 interchangeable：** 官方把状态一起演化和提案裁决同判分开。
- **看见两边状态一起走 not already Prepare may be nondet ≠ 已经是 Prepare 可以不确定 interchangeable：** 官方把状态机复制和 Prepare 可以不确定分开。
- **看见 Agreement not already settled ≠ 已经交差 interchangeable：** 官方把 Agreement 和已经交差分开；342 finalize-det vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边状态机复制 | 不是已经是 Process 对任意块同一裁决 | 不是 Process 必须只依赖请求和上一份状态（340） |
| 看见两边状态一起走 | 不是已经是 Prepare 可以不确定 | 不是 Prepare 没有确定性要求（338） |
| 看见 Agreement | 不是已经交差 | 不是状态必须确定就已经可以像 Prepare 那样（887） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边状态机复制 not already Process same verdict / not already Prepare may be nondet / not already settled 正式三事（342 余量），必须分开是不是已经是 Process 对任意块同一裁决、是不是已经是 Prepare 可以不确定、是不是已经交差。可以跳过「看见状态机复制就已经是 Process 同判」。不要另写怎样写 FinalizeBlock。342 finalize-det vs prepare bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量。
- FinalizeBlock 确定性 bundled。那是不变量 342。
- Finalize 算出的状态必须只依赖上一份状态和决定块。那是不变量 342 item 1 余量 / 887。
- Process 必须只依赖请求和上一份状态。那是不变量 340。
- Prepare 没有确定性要求。那是不变量 338。
