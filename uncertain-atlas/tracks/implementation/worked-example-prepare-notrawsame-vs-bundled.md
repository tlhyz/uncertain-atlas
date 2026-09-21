# 例：看见两边 raw 提案一样 / 看见同一高度同一轮 / 看见诚实准备 is not already already same-prepared interchangeable / already must-same-u interchangeable / already same-list interchangeable

**层次**：实现 / 两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事（338 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事（338 余量）/ not 768 prepare-notrawsame interchangeable / not 338 preparenondet bundled interchangeable」，不是 Prepare nondet bundled（338），也不是 PrepareProposal 没有确定性要求不是已经必须确定（767 item 1 余量）或 ExtendVote 没有确定性要求不是已经是同一份扩展（769 item 3 余量）。不要另写怎样写 Prepare 或怎样写 ExtendVote。

## 官方三件事

规范把 Requirements 里两边 raw 提案一样、*v_p = v_q* 和「已经是 raw 一样就已经是同一份 prepared interchangeable / 已经是同一高度同一轮就必须同一份 interchangeable / 已经是诚实准备就已经同一份列表 interchangeable / 已经是 preparenondet bundled interchangeable」分开写成三件独立的实现事，不是「看见两边 raw 一样就已经是同一份提案 interchangeable / 就已经必须同一份 interchangeable / 就已经同一份列表 interchangeable」一件事：

1. **看见两边 raw 提案一样 / 看见 *v_p = v_q* / 看见同一份 raw is not already 已经是同一份 prepared 提案 interchangeable / 已经 same-prepared interchangeable / 已经同一份 prepared 交差 interchangeable / 338 preparenondet bundled interchangeable / 327 preparetimeout interchangeable / preparenondet-sold-as-deterministic interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 768 prepare-notrawsame interchangeable / 338 preparenondet item 2 interchangeable，也不是已经两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事 bundled（338 item 2 余量） interchangeable / 338 preparenondet item 2 interchangeable，也不是已经 PrepareProposal 没有确定性要求不是已经必须确定（767） interchangeable / 769 extend-notsameext interchangeable / 33 four gates interchangeable，也不是已经立刻整块执行已经离开关键路径（327） interchangeable。**  
   官方写：*v_p = v_q* **并不蕴涵** *u_p = u_q*。两个正确进程拿到同一份 raw，各自 Prepare 可以回不同的 prepared。看见 raw 一样，不是已经 same-prepared interchangeable——338 钉 bundled 三事，本页从 item 2 侧钉 not already same-prepared 单句。看见 *v_p = v_q*，不是已经 Prepare nondet bundled（338） interchangeable——338 钉 bundled，本页钉 item 2 第一件事。看见同一份 raw，不是已经立刻整块执行已经离开关键路径（327） interchangeable——327 另钉。338 preparenondet vs process bundled unbundling 在本页 item 2 续。

2. **看见同一高度、同一轮 / 看见同一高度同一轮 / 看见同一轮次 is not already 已经必须同一份 interchangeable / 已经 must-same-u interchangeable / 已经必须同一份交差 interchangeable / 338 preparenondet bundled interchangeable / 33 four gates interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 768 prepare-notrawsame interchangeable / 338 preparenondet item 1 必须确定 interchangeable / 338 preparenondet item 3 ExtendVote interchangeable，也不是已经两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事 bundled（338 item 2 余量） interchangeable / 338 preparenondet item 2 interchangeable，也不是已经是同一份 prepared（本页第一件事） interchangeable。**  
   官方写：看见同一高度、同一轮，不是已经同一份列表，也不是已经必须同一份。看见同一高度同一轮，不是已经 must-same-u interchangeable——本页钉 not already must-same-u 单句。看见同一轮次，不是已经是同一份 prepared（本页第一件事） interchangeable——三件事分开钉。338 preparenondet vs process bundled unbundling 在本页 item 2 续。

3. **看见诚实准备 / 看见诚实 Prepare / 看见正确进程各自 Prepare is not already 已经同一份列表 interchangeable / 已经 same-list interchangeable / 已经同一份列表交差 interchangeable / 338 preparenondet bundled interchangeable / 347 req3-coherence interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 768 prepare-notrawsame interchangeable / 338 preparenondet item 1 / 338 preparenondet item 3，也不是已经两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事 bundled（338 item 2 余量） interchangeable / 338 preparenondet item 2 interchangeable，也不是已经是同一份 prepared（本页第一件事） interchangeable / 已经必须同一份（本页第二件事） interchangeable。**  
   官方写：看见诚实准备，不是已经和「诚实 Process 必须 Accept」同一句。看见诚实 Prepare，不是已经 same-list interchangeable——本页钉 not already same-list 单句。看见正确进程各自 Prepare，不是已经必须同一份（本页第二件事） interchangeable——三件事分开钉。338 preparenondet vs process bundled unbundling 在本页 item 2 续。

怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑那些「其它值或操作」是规范里的做法，本页不抄。Prepare nondet bundled（338）、PrepareProposal 没有确定性要求不是已经必须确定（338 item 1 余量 / 767）、ExtendVote 没有确定性要求不是已经是同一份扩展（338 item 3 余量 / 769）、四门已经结算（33）、立刻整块执行已经离开关键路径（327）、验签拒收整张预提交（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **两边 raw 一样 not already same-prepared ≠ 338 / 327 interchangeable：** 官方把同一份 raw 和同一份 prepared 分开。
- **同一高度同一轮 not already must-same-u ≠ 已经必须同一份 interchangeable：** 官方把同一高度同一轮和已经必须同一份分开。
- **诚实准备 not already same-list ≠ 已经同一份列表 interchangeable：** 官方把诚实准备和已经同一份列表、诚实 Process 必须 Accept 分开；338 preparenondet vs process bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边 raw 一样 | 不是 already same-prepared | 不是立刻整块执行已经离开关键路径 alone（327） |
| 同一高度同一轮 | 不是 already must-same-u | 不是 Prepare 没有确定性要求就已经必须确定 alone（767） |
| 诚实准备 | 不是 already same-list | 不是 ExtendVote 没有确定性要求就已经是同一份扩展 alone（769） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事（338 余量），必须分开两边 raw 一样 是不是 already same-prepared interchangeable / 338 preparenondet bundled interchangeable / preparenondet-sold-as-deterministic interchangeable、同一高度同一轮 是不是 already must-same-u interchangeable、诚实准备 是不是 already same-list interchangeable。可以跳过「看见两边 raw 一样就已经是同一份提案 interchangeable / 就已经必须同一份 interchangeable / 就已经同一份列表 interchangeable」。不要把「其它值或操作」当不确定常数。不要另写怎样写 Prepare 或怎样写 ExtendVote。338 preparenondet vs process bundled unbundling 在本页 item 2 续（767 + 768）；续 [`worked-example-extend-notsameext-vs-bundled.md`](worked-example-extend-notsameext-vs-bundled.md)（不变量 769 item 3）。

## 本页不抄

- 怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑其它值或操作。
- Prepare nondet bundled。那是不变量 338。
- PrepareProposal 没有确定性要求不是已经必须确定。那是不变量 338 item 1 余量 / 767。
- ExtendVote 没有确定性要求不是已经是同一份扩展。那是不变量 338 item 3 余量 / 769。
- 四门已经结算。那是不变量 33。
- 立刻整块执行已经离开关键路径。那是不变量 327。
- 验签拒收整张预提交。那是不变量 34。
