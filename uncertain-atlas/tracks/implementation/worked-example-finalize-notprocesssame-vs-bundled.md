# 例：看见两边状态机复制 / 看见应用状态一起演化 / 看见 Agreement is not already already process-same interchangeable / already prepare-nondet interchangeable / already settled interchangeable

**层次**：实现 / 两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事（342 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事（342 余量）/ not 781 finalize-notprocesssame interchangeable / not 342 finalizedet bundled interchangeable」，不是 FinalizeBlock 确定性 bundled（342），也不是 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值（779 item 1 余量）或 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头（780 item 2 余量）。不要另写怎样写 FinalizeBlock。

## 官方三件事

规范把 Requirements 11 和 12 再加上共识 Agreement 保证的状态机复制 和「已经是两边状态一起走就已经是 Process 对任意块同一 Accept/Reject interchangeable / 已经是应用状态一起演化就已经是 Prepare 可以不确定 interchangeable / 已经是 Agreement 就已经交差 interchangeable / 已经是 finalizedet bundled interchangeable」分开写成三件独立的实现事，不是「看见状态机复制就已经是 Process 同判 interchangeable / 就已经是 Prepare nondet interchangeable / 就已经交差 interchangeable」一件事：

1. **看见两边状态机复制 / 看见应用状态一起演化 / 看见各正确进程上的应用状态一起演化 is not already 已经是 Process 对任意块同一 Accept/Reject interchangeable / 已经 process-same interchangeable / 已经 Process 同判交差 interchangeable / 342 finalizedet bundled interchangeable / 340 processdet interchangeable / finalizedet-sold-as-prepare interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 781 finalize-notprocesssame interchangeable / 342 finalizedet item 3 interchangeable，也不是已经两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事 bundled（342 item 3 余量） interchangeable / 342 finalizedet item 3 interchangeable，也不是已经 Finalize 算出的状态不是已经可以像 Prepare 那样（779） interchangeable / 780 finalize-notprinted interchangeable / 33 four gates interchangeable，也不是已经 Process 必须只依赖请求和上一份状态（340） interchangeable。**  
   官方写：Requirement 11 和 12 再加上共识的 Agreement，保证**状态机复制**：各正确进程上的应用状态一起演化。看见状态机复制，不是已经是 Process 对任意块同一 Accept/Reject。看见应用状态一起演化，不是已经 process-same interchangeable——342 钉 bundled 三事，本页从 item 3 侧钉 not already process-same 单句。看见各正确进程上的应用状态一起演化，不是已经 FinalizeBlock 确定性 bundled（342） interchangeable——342 钉 bundled，本页钉 item 3 第一件事。看见状态机复制，不是已经 Process 必须只依赖请求和上一份状态（340） interchangeable——340 另钉。342 finalizedet vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见两边状态一起走 / 看见状态一起演化 / 看见不是只靠 Process 同判 is not already 已经是 Prepare 可以不确定 interchangeable / 已经 prepare-nondet interchangeable / 已经和 Prepare / ExtendVote 同一把尺交差 interchangeable / 342 finalizedet bundled interchangeable / 338 preparenondet interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 781 finalize-notprocesssame interchangeable / 342 finalizedet item 1 像 Prepare interchangeable / 342 finalizedet item 2 结果集合 interchangeable，也不是已经两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事 bundled（342 item 3 余量） interchangeable / 342 finalizedet item 3 interchangeable，也不是已经 Process 同判（本页第一件事） interchangeable。**  
   官方写：看见两边状态一起走，不是已经是 Prepare 可以不确定。看见状态一起演化，不是已经 prepare-nondet interchangeable——本页钉 not already prepare-nondet 单句。看见不是只靠 Process 同判，不是已经 Process 同判（本页第一件事） interchangeable——三件事分开钉。342 finalizedet vs prepare bundled unbundling 在本页 item 3 完成。

3. **看见 Agreement / 看见共识 Agreement / 看见已经造出 *s_h* 和 *T_h* is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差同一句 interchangeable / 342 finalizedet bundled interchangeable / 335 finalizepersist interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 781 finalize-notprocesssame interchangeable / 342 finalizedet item 1 / 342 finalizedet item 2，也不是已经两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事 bundled（342 item 3 余量） interchangeable / 342 finalizedet item 3 interchangeable，也不是已经 Process 同判（本页第一件事） interchangeable / 已经是 Prepare nondet（本页第二件事） interchangeable。**  
   官方写：看见 Agreement，不是已经交差。看见共识 Agreement，不是已经 settled interchangeable——本页钉 not already settled 单句。看见已经造出 *s_h* 和 *T_h*，不是已经是 Prepare nondet（本页第二件事） interchangeable——三件事分开钉。不要把造出 *s_h* 当已经落盘。342 finalizedet vs prepare bundled unbundling 在本页 item 3 完成。

怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。FinalizeBlock 确定性 bundled（342）、Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值（342 item 1 余量 / 779）、Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头（342 item 2 余量 / 780）、Prepare 没有确定性要求（338）、ProcessProposal 确定性（340）、四门已经结算（33）、Finalize 改了状态不是已经落盘（335）是另外那套，本页不抄。

## 官方为什么这样拆

- **状态机复制 not already process-same ≠ 342 / 340 interchangeable：** 官方把状态一起演化和 Process 对任意块同一裁决分开。
- **状态一起演化 not already prepare-nondet ≠ 已经是 Prepare 可以不确定 interchangeable：** 官方把 Finalize 确定性后果和 Prepare 可以不确定分开。
- **Agreement not already settled ≠ 已经交差 interchangeable：** 官方把 Agreement 和已经交差分开；342 finalizedet vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 状态机复制 | 不是 already process-same | 不是 Process 必须只依赖请求和上一份状态 alone（340） |
| 状态一起演化 | 不是 already prepare-nondet | 不是 Prepare 没有确定性要求 alone（338） |
| Agreement | 不是 already settled | 不是 Finalize 改了状态不是已经落盘 alone（335） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事（342 余量），必须分开状态机复制 是不是 already process-same interchangeable / 342 finalizedet bundled interchangeable / finalizedet-sold-as-prepare interchangeable、状态一起演化 是不是 already prepare-nondet interchangeable、Agreement 是不是 already settled interchangeable。可以跳过「看见状态机复制就已经是 Process 同判 interchangeable / 就已经是 Prepare nondet interchangeable / 就已经交差 interchangeable」。不要把造出 *s_h* 当已经落盘。不要另写怎样写 FinalizeBlock。342 finalizedet vs prepare bundled unbundling 在本页 item 3 完成（779 + 780 + 781）。

## 本页不抄

- 怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量。
- FinalizeBlock 确定性 bundled。那是不变量 342。
- Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值。那是不变量 342 item 1 余量 / 779。
- Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头。那是不变量 342 item 2 余量 / 780。
- Prepare 没有确定性要求。那是不变量 338。
- ProcessProposal 确定性。那是不变量 340。
- 四门已经结算。那是不变量 33。
- Finalize 改了状态不是已经落盘。那是不变量 335。
