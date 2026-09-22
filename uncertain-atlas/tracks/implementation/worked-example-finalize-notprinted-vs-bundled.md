# 例：看见 Finalize 算出的结果必须只依赖上一份状态和决定块 / 看见 *T_h* 必须确定 / 看见造出了 *T* is not already already printed interchangeable / already same-order interchangeable / already persisted interchangeable

**层次**：实现 / Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事（342 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事（342 余量）/ not 780 finalize-notprinted interchangeable / not 342 finalizedet bundled interchangeable」，不是 FinalizeBlock 确定性 bundled（342），也不是 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值（779 item 1 余量）或两边状态机复制不是已经是 Process 对任意块同一裁决（781 item 3 余量）。不要另写怎样写 FinalizeBlock。

## 官方三件事

规范把 Requirements 里 Finalize 算出的结果集合 *T_h*、必须只依赖上一份状态和决定块 和「已经是结果必须确定就已经印进本头 interchangeable / 已经是只依赖这两份就已经是回执顺序对上 interchangeable / 已经是造出了 *T* 就已经落盘 interchangeable / 已经是 finalizedet bundled interchangeable」分开写成三件独立的实现事，不是「看见结果必须确定就已经印进本头 interchangeable / 就已经是回执顺序对上 interchangeable / 就已经落盘 interchangeable」一件事：

1. **看见 Finalize 算出的结果必须只依赖上一份状态和决定块 / 看见 *T_h* 必须确定 / 看见造出交易结果集合 is not already 已经是 Code/Data 印进本头 interchangeable / 已经 printed interchangeable / 已经印进本头交差 interchangeable / 342 finalizedet bundled interchangeable / 316 exectxresult interchangeable / finalizedet-sold-as-prepare interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 780 finalize-notprinted interchangeable / 342 finalizedet item 2 interchangeable，也不是已经 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事 bundled（342 item 2 余量） interchangeable / 342 finalizedet item 2 interchangeable，也不是已经 Finalize 算出的状态不是已经可以像 Prepare 那样（779） interchangeable / 781 finalize-notprocesssame interchangeable / 335 finalizepersist interchangeable，也不是已经结果列表已经同一顺序（316） interchangeable。**  
   官方写：同一次 `FinalizeBlock` **另外**造出交易结果集合 *T_{p,h}*。Requirement 12：*T_{p,h}* 的内容 **只**依赖 *s_{p,h-1}* 和 *v_{p,h}*。看见结果必须确定，不是已经印进本头。看见 *T_h* 必须确定，不是已经 printed interchangeable——342 钉 bundled 三事，本页从 item 2 侧钉 not already printed 单句。看见造出交易结果集合，不是已经 FinalizeBlock 确定性 bundled（342） interchangeable——342 钉 bundled，本页钉 item 2 第一件事。看见结果必须确定，不是已经结果列表已经同一顺序（316） interchangeable——316 另钉。342 finalizedet vs prepare bundled unbundling 在本页 item 2 续。

2. **看见只依赖这两份 / 看见只依赖 *s_{h-1}* 和 *v* / 看见结果内容只依赖这两份 is not already 已经是回执顺序对上 interchangeable / 已经 same-order interchangeable / 已经顺序对上交差 interchangeable / 342 finalizedet bundled interchangeable / 316 exectxresult interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 780 finalize-notprinted interchangeable / 342 finalizedet item 1 像 Prepare interchangeable / 342 finalizedet item 3 状态机复制 interchangeable，也不是已经 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事 bundled（342 item 2 余量） interchangeable / 342 finalizedet item 2 interchangeable，也不是已经印进本头（本页第一件事） interchangeable。**  
   官方写：看见只依赖这两份，不是已经是回执顺序对上。看见只依赖 *s_{h-1}* 和 *v*，不是已经 same-order interchangeable——本页钉 not already same-order 单句。看见结果内容只依赖这两份，不是已经印进本头（本页第一件事） interchangeable——三件事分开钉。342 finalizedet vs prepare bundled unbundling 在本页 item 2 续。

3. **看见造出了 *T* / 看见造出了交易结果集合 / 看见 *T_{p,h}* 回来了 is not already 已经落盘 interchangeable / 已经 persisted interchangeable / 已经落盘交差 interchangeable / 342 finalizedet bundled interchangeable / 335 finalizepersist interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 780 finalize-notprinted interchangeable / 342 finalizedet item 1 / 342 finalizedet item 3，也不是已经 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事 bundled（342 item 2 余量） interchangeable / 342 finalizedet item 2 interchangeable，也不是已经印进本头（本页第一件事） interchangeable / 已经是回执顺序对上（本页第二件事） interchangeable。**  
   官方写：看见造出了 *T*，不是已经落盘。看见造出了交易结果集合，不是已经 persisted interchangeable——本页钉 not already persisted 单句。看见 *T_{p,h}* 回来了，不是已经是回执顺序对上（本页第二件事） interchangeable——三件事分开钉。342 finalizedet vs prepare bundled unbundling 在本页 item 2 续。

怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。FinalizeBlock 确定性 bundled（342）、Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值（342 item 1 余量 / 779）、两边状态机复制不是已经是 Process 对任意块同一裁决（342 item 3 余量 / 781）、Prepare 没有确定性要求（338）、结果列表已经同一顺序（316）、Finalize 改了状态不是已经落盘（335）是另外那套，本页不抄。

## 官方为什么这样拆

- **结果必须确定 not already printed ≠ 342 / 316 interchangeable：** 官方把结果集合的确定性和 Code/Data 印进本头分开。
- **只依赖这两份 not already same-order ≠ 已经是回执顺序对上 interchangeable：** 官方把只依赖上一份状态 / 决定块和回执顺序对上分开。
- **造出了 *T* not already persisted ≠ 已经落盘 interchangeable：** 官方把造出结果集合和已经落盘分开；342 finalizedet vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 结果必须确定 | 不是 already printed | 不是结果列表已经同一顺序 alone（316） |
| 只依赖这两份 | 不是 already same-order | 不是必须确定就已经可以像 Prepare 那样 alone（779） |
| 造出了 *T* | 不是 already persisted | 不是状态机复制就已经是 Process 同判 alone（781） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事（342 余量），必须分开结果必须确定 是不是 already printed interchangeable / 342 finalizedet bundled interchangeable / finalizedet-sold-as-prepare interchangeable、只依赖这两份 是不是 already same-order interchangeable、造出了 *T* 是不是 already persisted interchangeable。可以跳过「看见结果必须确定就已经印进本头 interchangeable / 就已经是回执顺序对上 interchangeable / 就已经落盘 interchangeable」。不要把造出 *T* 当已经落盘。不要另写怎样写 FinalizeBlock。342 finalizedet vs prepare bundled unbundling 在本页 item 2 续（779 + 780）；续 [`worked-example-finalize-notprocesssame-vs-bundled.md`](worked-example-finalize-notprocesssame-vs-bundled.md)（不变量 781 item 3）已写；完成见 781。

## 本页不抄

- 怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量。
- FinalizeBlock 确定性 bundled。那是不变量 342。
- Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值。那是不变量 342 item 1 余量 / 779。
- 两边状态机复制不是已经是 Process 对任意块同一裁决。那是不变量 342 item 3 余量 / 781。
- Prepare 没有确定性要求。那是不变量 338。
- 结果列表已经同一顺序。那是不变量 316。
- Finalize 改了状态不是已经落盘。那是不变量 335。
