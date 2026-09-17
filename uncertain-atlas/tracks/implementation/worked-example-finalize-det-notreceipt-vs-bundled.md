# 例：看见 Finalize 算出的结果必须只依赖上一份状态和决定块 is not already Code/Data in header interchangeable / not already same list order interchangeable / not already settled interchangeable

**层次**：实现 / Finalize 算出的结果必须只依赖上一份状态和决定块 not already Code/Data in header / not already same list order / not already settled 正式三事（342 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 算出的结果必须只依赖上一份状态和决定块 not already Code/Data in header / not already same list order / not already settled 正式三事（342 余量）/ not 888 finalize-det-notreceipt interchangeable / not 342 finalize-det-vs-prepare bundled interchangeable」，不是 FinalizeBlock 确定性 bundled（342），也不是结果列表已经同一顺序（316），也不是造出 *s_h* 就已经落盘。不要另写怎样写 FinalizeBlock。

## 官方三件事

1. **看见 Finalize 算出的结果必须只依赖上一份状态和决定块 / 看见 *T_h* 必须确定 这份结果 is not already 已经是 Code/Data 印进本头 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 888 finalize-det-notreceipt interchangeable / 887 finalize-det-notprep interchangeable / 342 finalize-det item 1 状态 interchangeable，也不是已经 Finalize 算出的结果必须只依赖上一份状态和决定块 not already Code/Data in header / not already same list order / not already settled 正式三事 bundled（342 item 2 余量） interchangeable / 342 finalize-det item 2 interchangeable。**  
   官方写：同一次 `FinalizeBlock` 另外造出交易结果集合 *T_{p,h}*。Requirement 12：*T_{p,h}* 的内容只依赖 *s_{p,h-1}* 和 *v_{p,h}*。看见结果必须确定，不是已经印进本头 interchangeable——本页从 342 item 2 侧钉 not already Code/Data in header 单句。342 finalize-det vs prepare bundled unbundling 在本页 item 2 续。

2. **看见只依赖这两份 / 看见造出了 *T* / 这份结果 is not already 已经是回执顺序对上 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 888 finalize-det-notreceipt interchangeable / 342 finalize-det item 3 复制 interchangeable / 889 finalize-det-notprocess interchangeable，也不是已经结果列表已经同一顺序 interchangeable / 316 same-order interchangeable。**  
   官方把只依赖这两份和已经是回执顺序对上分开——342 bundled 第二件事常与 316 混成「看见结果必须确定就已经印进本头或已经顺序对上 interchangeable」，本页钉 not already same list order 单句。

3. **看见造出了 *T* / 看见结果必须确定 / 这份结果 is not already 已经交差 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 888 finalize-det-notreceipt interchangeable / 887 finalize-det-notprep interchangeable，也不是已经造出 *s_h* 就已经落盘 interchangeable。**  
   官方把造出了 *T* 和已经落盘 / 已经交差分开。看见造出了 *T*，不是已经落盘 interchangeable。342 finalize-det vs prepare bundled unbundling 在本页 item 2 续。

怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize 算出的结果必须只依赖上一份状态和决定块 not already Code/Data in header ≠ 已经是 Code/Data 印进本头 interchangeable：** 官方把结果集合的确定性和回执字段怎么进头分开。
- **看见只依赖这两份 not already same list order ≠ 已经是回执顺序对上 interchangeable：** 官方把结果确定性和列表同一顺序分开。
- **看见造出了 *T* not already settled ≠ 已经交差 interchangeable：** 官方把造出了 *T* 和已经交差分开；342 finalize-det vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 算出的结果必须只依赖上一份状态和决定块 | 不是已经是 Code/Data 印进本头 | 不是结果列表已经同一顺序（316） |
| 看见只依赖这两份 | 不是已经是回执顺序对上 | 不是 Prepare 没有确定性要求（338） |
| 看见造出了 *T* | 不是已经交差 | 不是状态必须确定就已经可以像 Prepare 那样（887） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的结果必须只依赖上一份状态和决定块 not already Code/Data in header / not already same list order / not already settled 正式三事（342 余量），必须分开是不是已经是 Code/Data 印进本头、是不是已经是回执顺序对上、是不是已经交差。可以跳过「看见结果必须确定就已经印进本头」。不要把造出 *T* 当已经落盘。不要另写怎样写 FinalizeBlock。342 finalize-det vs prepare bundled unbundling 在本页 item 2 续；续 [`worked-example-finalize-det-notprocess-vs-bundled.md`](worked-example-finalize-det-notprocess-vs-bundled.md)（不变量 889 item 3）。

## 本页不抄

- 怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量。
- FinalizeBlock 确定性 bundled。那是不变量 342。
- Finalize 算出的状态必须只依赖上一份状态和决定块。那是不变量 342 item 1 余量 / 887。
- 结果列表已经同一顺序。那是不变量 316。
- Prepare 没有确定性要求。那是不变量 338。
