# 例：看见 PrepareProposal 没有确定性要求 / 看见可以依赖其它值或操作 / 看见 Prepare 回了 is not already already must-deterministic interchangeable / already same-as-process interchangeable / already settled interchangeable

**层次**：实现 / PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事（338 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事（338 余量）/ not 767 prepare-notmustdet interchangeable / not 338 preparenondet bundled interchangeable」，不是 Prepare nondet bundled（338），也不是两边 raw 一样不是已经是同一份提案（768 item 2 余量）或 ExtendVote 没有确定性要求不是已经是同一份扩展（769 item 3 余量）。不要另写怎样写 Prepare 或怎样写 ExtendVote。

## 官方三件事

规范把 Requirements 里 `PrepareProposal` 没有确定性要求、可以依赖其它值或操作 和「已经是没有确定性要求就必须确定 interchangeable / 已经是可以依赖其它值就已经和 Process / Finalize 同一把尺 interchangeable / 已经是 Prepare 回了就已经交差 interchangeable / 已经是 preparenondet bundled interchangeable」分开写成三件独立的实现事，不是「看见没有确定性要求就已经必须确定 interchangeable / 就已经和 Process 同一把尺 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 PrepareProposal 没有确定性要求 / 看见 Prepare 不被要求确定 / 看见没有这道要求 is not already 已经必须确定 interchangeable / 已经 must-deterministic interchangeable / 已经必须确定交差 interchangeable / 338 preparenondet bundled interchangeable / 33 four gates interchangeable / preparenondet-sold-as-deterministic interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 767 prepare-notmustdet interchangeable / 338 preparenondet item 1 interchangeable，也不是已经 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事 bundled（338 item 1 余量） interchangeable / 338 preparenondet item 1 interchangeable，也不是已经两边 raw 一样不是已经是同一份提案（768） interchangeable / 769 extend-notsameext interchangeable / 327 preparetimeout interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`PrepareProposal` 和 `ExtendVote` **都没有**与确定性相关的要求。`PrepareProposal` 不被要求确定。看见没有这道要求，不是已经 must-deterministic interchangeable——338 钉 bundled 三事，本页从 item 1 侧钉 not already must-deterministic 单句。看见 Prepare 不被要求确定，不是已经 Prepare nondet bundled（338） interchangeable——338 钉 bundled，本页钉 item 1 第一件事。看见没有这道要求，不是已经四门已经结算（33） interchangeable——33 另钉。338 preparenondet vs process bundled unbundling 在本页 item 1 启动。

2. **看见可以依赖其它值或操作 / 看见准备好的提案可以依赖其它值 / 看见可以不止 raw 和已提交状态 is not already 已经和 Process / Finalize 同一把尺 interchangeable / 已经 same-as-process interchangeable / 已经同一把尺交差 interchangeable / 338 preparenondet bundled interchangeable / 340 process-det interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 767 prepare-notmustdet interchangeable / 338 preparenondet item 2 raw 一样 interchangeable / 338 preparenondet item 3 ExtendVote interchangeable，也不是已经 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事 bundled（338 item 1 余量） interchangeable / 338 preparenondet item 1 interchangeable，也不是已经必须确定（本页第一件事） interchangeable。**  
   官方写：准备好的提案 *u_p* 可以依赖 raw 提案 *v_p* 和已提交状态 *s_{p,h-1}*，也可以依赖其它值或操作。看见可以依赖其它值，不是已经和 `ProcessProposal` / `FinalizeBlock` 同一把尺。看见可以依赖其它值或操作，不是已经 same-as-process interchangeable——本页钉 not already same-as-process 单句。看见可以不止 raw 和已提交状态，不是已经必须确定（本页第一件事） interchangeable——三件事分开钉。338 preparenondet vs process bundled unbundling 在本页 item 1 启动。

3. **看见 Prepare 回了 / 看见 PrepareProposal 回了 / 看见准备好的提案回来了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差同一句 interchangeable / 338 preparenondet bundled interchangeable / 33 four gates interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 767 prepare-notmustdet interchangeable / 338 preparenondet item 2 / 338 preparenondet item 3，也不是已经 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事 bundled（338 item 1 余量） interchangeable / 338 preparenondet item 1 interchangeable，也不是已经必须确定（本页第一件事） interchangeable / 已经和 Process 同一把尺（本页第二件事） interchangeable。**  
   官方写：看见 Prepare 回了，不是已经交差。看见 PrepareProposal 回了，不是已经 settled interchangeable——本页钉 not already settled 单句。看见准备好的提案回来了，不是已经和 Process 同一把尺（本页第二件事） interchangeable——三件事分开钉。338 preparenondet vs process bundled unbundling 在本页 item 1 启动。

怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑那些「其它值或操作」是规范里的做法，本页不抄。Prepare nondet bundled（338）、两边 raw 一样不是已经是同一份提案（338 item 2 余量 / 768）、ExtendVote 没有确定性要求不是已经是同一份扩展（338 item 3 余量 / 769）、四门已经结算（33）、立刻整块执行已经离开关键路径（327）、验签拒收整张预提交（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **没有确定性要求 not already must-deterministic ≠ 338 / 33 interchangeable：** 官方把 Prepare 没有这道要求和已经必须确定分开。
- **可以依赖其它值 not already same-as-process ≠ 已经和 Process 同一把尺 interchangeable：** 官方把可以依赖其它值和 Process / Finalize 必须确定分开。
- **Prepare 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Prepare 回了和已经交差分开；338 preparenondet vs process bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没有确定性要求 | 不是 already must-deterministic | 不是四门已经结算 alone（33） |
| 可以依赖其它值 | 不是 already same-as-process | 不是立刻整块执行已经离开关键路径 alone（327） |
| Prepare 回了 | 不是 already settled | 不是两边 raw 一样就已经是同一份提案 alone（768） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事（338 余量），必须分开没有确定性要求 是不是 already must-deterministic interchangeable / 338 preparenondet bundled interchangeable / preparenondet-sold-as-deterministic interchangeable、可以依赖其它值 是不是 already same-as-process interchangeable、Prepare 回了 是不是 already settled interchangeable。可以跳过「看见可以不确定就必须确定 interchangeable / 就已经和 Process 同一把尺 interchangeable / 就已经交差 interchangeable」。不要把「其它值或操作」当不确定常数。不要另写怎样写 Prepare 或怎样写 ExtendVote。338 preparenondet vs process bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepare-notrawsame-vs-bundled.md`](worked-example-prepare-notrawsame-vs-bundled.md)（不变量 768 item 2）。

## 本页不抄

- 怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑其它值或操作。
- Prepare nondet bundled。那是不变量 338。
- 两边 raw 一样不是已经是同一份提案。那是不变量 338 item 2 余量 / 768。
- ExtendVote 没有确定性要求不是已经是同一份扩展。那是不变量 338 item 3 余量 / 769。
- 四门已经结算。那是不变量 33。
- 立刻整块执行已经离开关键路径。那是不变量 327。
- 验签拒收整张预提交。那是不变量 34。
