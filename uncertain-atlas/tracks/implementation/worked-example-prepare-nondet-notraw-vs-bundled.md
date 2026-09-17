# 例：看见两边 raw 一样 is not already same prepared interchangeable / not already must be same interchangeable / not already settled interchangeable

**层次**：实现 / 两边 raw 一样 not already same prepared / not already must be same / not already settled 正式三事（338 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边 raw 一样 not already same prepared / not already must be same / not already settled 正式三事（338 余量）/ not 897 prepare-nondet-notraw interchangeable / not 338 prepare-nondet-vs-process bundled interchangeable」，不是 Prepare/ExtendVote 确定性 bundled（338），也不是立刻整块执行已经离开关键路径（327），也不是 Req 3 诚实对诚实必须 Accept（347/872）。不要另写怎样写 Prepare 或怎样写 ExtendVote。

## 官方三件事

1. **看见两边 raw 提案一样 / 看见 *v_p = v_q* 这份 raw is not already 已经是同一份 prepared 提案 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 897 prepare-nondet-notraw interchangeable / 896 prepare-nondet-notmust interchangeable / 338 prepare-nondet item 1 没有要求 interchangeable，也不是已经两边 raw 一样 not already same prepared / not already must be same / not already settled 正式三事 bundled（338 item 2 余量） interchangeable / 338 prepare-nondet item 2 interchangeable。**  
   官方写：*v_p = v_q* 并不蕴涵 *u_p = u_q*。两个正确进程拿到同一份 raw，各自 Prepare 可以回不同的 prepared。看见 raw 一样，不是已经同一份提案 interchangeable——本页从 338 item 2 侧钉 not already same prepared 单句。338 prepare-nondet vs process bundled unbundling 在本页 item 2 续。

2. **看见同一高度、同一轮 / 看见诚实准备 / 这份 raw is not already 已经必须同一份 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 897 prepare-nondet-notraw interchangeable / 338 prepare-nondet item 3 Extend interchangeable / 898 prepare-nondet-notext interchangeable，也不是已经立刻整块执行已经离开关键路径 interchangeable / 327 leave-path interchangeable。**  
   官方把同一高度、同一轮和已经必须同一份列表分开——338 bundled 第二件事常与 347 混成「看见 raw 一样就已经同一份或已经是诚实 Process 必须 Accept interchangeable」，本页钉 not already must be same 单句。

3. **看见诚实准备 / 看见 raw 一样 / 这份 raw is not already 已经交差 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 897 prepare-nondet-notraw interchangeable / 896 prepare-nondet-notmust interchangeable，也不是已经诚实 Process 必须 Accept interchangeable / 347 / 872 req3-notany interchangeable。**  
   官方把诚实准备和已经和「诚实 Process 必须 Accept」同一句 / 已经交差分开。看见诚实准备，不是已经和诚实 Process 必须 Accept 同一句 interchangeable。338 prepare-nondet vs process bundled unbundling 在本页 item 2 续。

怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑那些「其它值或操作」是规范里的做法，本页不抄。

## 官方为什么这样拆

- **两边 raw 一样 not already same prepared ≠ 已经是同一份提案 interchangeable：** 官方把同一份 raw 和同一份 prepared 分开。
- **看见同一高度、同一轮 not already must be same ≠ 已经必须同一份 interchangeable：** 官方把同一高度同一轮和已经必须同一份列表分开。
- **看见诚实准备 not already settled ≠ 已经交差 interchangeable：** 官方把诚实准备和已经交差分开；338 prepare-nondet vs process bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边 raw 一样 | 不是已经是同一份提案 | 不是立刻整块执行已经离开关键路径（327） |
| 看见同一高度、同一轮 | 不是已经必须同一份 | 不是 Req 3 必须 Accept（347/872） |
| 看见诚实准备 | 不是已经交差 | 不是 Prepare 没有确定性要求就已经必须确定（896） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边 raw 一样 not already same prepared / not already must be same / not already settled 正式三事（338 余量），必须分开是不是已经是同一份提案、是不是已经必须同一份、是不是已经交差。可以跳过「看见 raw 一样就已经同一份提案」。不要另写怎样写 Prepare 或怎样写 ExtendVote。338 prepare-nondet vs process bundled unbundling 在本页 item 2 续；续 [`worked-example-prepare-nondet-notext-vs-bundled.md`](worked-example-prepare-nondet-notext-vs-bundled.md)（不变量 898 item 3）。

## 本页不抄

- 怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑其它值或操作。
- Prepare/ExtendVote 确定性 bundled。那是不变量 338。
- Prepare 没有确定性要求。那是不变量 338 item 1 余量 / 896。
- 立刻整块执行已经离开关键路径。那是不变量 327。
- Req 3 必须 Accept。那是不变量 347 / 872。
