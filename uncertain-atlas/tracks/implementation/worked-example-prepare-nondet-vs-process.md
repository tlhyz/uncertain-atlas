# 例：看见 Prepare 没有确定性要求不是已经必须确定；看见两边 raw 一样不是已经是同一份提案；看见 ExtendVote 没有确定性要求不是已经是同一份扩展

**层次**：实现 / PrepareProposal 与 ExtendVote 的确定性。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Prepare 没有确定性要求不是已经必须确定 / 两边 raw 一样不是已经是同一份提案 / ExtendVote 没有确定性要求不是已经是同一份扩展」，不是四门已经结算，也不是立刻整块执行已经离开关键路径。不要另写怎样写 Prepare 或怎样写 ExtendVote。 338 preparenondet vs process bundled unbundling 续（767 + 768）；精读 [`worked-example-prepare-notmustdet-vs-bundled.md`](worked-example-prepare-notmustdet-vs-bundled.md)；[`worked-example-prepare-notrawsame-vs-bundled.md`](worked-example-prepare-notrawsame-vs-bundled.md)（不变量 768 item 2）。

## 官方三件事

规范把 Prepare 和 ExtendVote 的确定性写成三件独立的实现事，不是「看见可以不确定就已经必须确定、已经是同一份提案、已经是同一份扩展」一件事：

1. **看见 `PrepareProposal` 没有确定性要求 / 看见可以依赖其它值或操作 不是已经必须确定，也不是已经和 Process / Finalize 同一把尺。**  
   官方写：`PrepareProposal` 和 `ExtendVote` **都没有**与确定性相关的要求。`PrepareProposal` 不被要求确定。准备好的提案 *u_p* 可以依赖 raw 提案 *v_p* 和已提交状态 *s_{p,h-1}*，也可以依赖其它值或操作。看见没有这道要求，不是已经必须确定。看见可以依赖其它值，不是已经和 `ProcessProposal` / `FinalizeBlock` 同一把尺。看见 Prepare 回了，不是已经交差。
2. **看见两边 raw 提案一样 / 看见 *v_p = v_q* 不是已经是同一份 prepared 提案，也不是已经必须同一份。**  
   官方写：*v_p = v_q* **并不蕴涵** *u_p = u_q*。两个正确进程拿到同一份 raw，各自 Prepare 可以回不同的 prepared。看见 raw 一样，不是已经同一份提案。看见同一高度、同一轮，不是已经同一份列表。看见诚实准备，不是已经和「诚实 Process 必须 Accept」同一句。
3. **看见 `ExtendVote` 没有确定性要求 / 看见同一块 不是已经是同一份扩展，也不是已经必须同一份。**  
   官方写：`ExtendVote` 也可以不确定。扩展 *e^r_p* 可以依赖这块 *w^r_p* 和 *s_{p,h-1}*，也可以依赖其它值或操作。*w^r_p = w^r_q* **并不蕴涵** *e^r_p = e^r_q*。看见没有确定性要求，不是已经必须确定。看见同一块，不是已经同一份扩展。看见能签扩展，不是已经和 `VerifyVoteExtension` 必须确定同一把尺。

怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑那些「其它值或操作」是规范里的做法，本页不抄。四门已经结算是不变量 33，本页不抄。

## 官方为什么这样拆

- **Prepare 没有确定性要求 ≠ 已经必须确定：** 官方把 Prepare 没有这道要求和 Process / Finalize 必须确定分开。
- **两边 raw 一样 ≠ 已经是同一份提案：** 官方把同一份 raw 和同一份 prepared 分开。
- **ExtendVote 没有确定性要求 ≠ 已经是同一份扩展：** 官方把同一块和同一份扩展分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 没有确定性要求 | 不是已经必须确定 | 不是四门已经结算（33） |
| 两边 raw 一样 | 不是已经是同一份提案 | 不是立刻整块执行已经离开关键路径（327） |
| ExtendVote 没有确定性要求 | 不是已经是同一份扩展 | 不是验签拒收整张预提交（34） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见可以不确定就已经必须确定、已经是同一份提案、已经是同一份扩展」，必须分开 Prepare 没有确定性要求是不是已经必须确定、两边 raw 一样是不是已经是同一份提案、ExtendVote 没有确定性要求是不是已经是同一份扩展。可以跳过「看见可以不确定就必须确定」。不要把「其它值或操作」当不确定常数。不要另写怎样写 Prepare 或怎样写 ExtendVote。 338 preparenondet vs process bundled unbundling 续（767 + 768 item 2）。

## 本页不抄

- 怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑其它值或操作。
- 四门已经结算。那是不变量 33。
- 立刻整块执行已经离开关键路径。那是不变量 327。
- 验签拒收整张预提交。那是不变量 34。
