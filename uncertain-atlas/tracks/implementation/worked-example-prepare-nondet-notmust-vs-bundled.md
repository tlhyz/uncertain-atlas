# 例：看见 Prepare 没有确定性要求 is not already must be deterministic interchangeable / not already same ruler as Process interchangeable / not already settled interchangeable

**层次**：实现 / Prepare 没有确定性要求 not already must be deterministic / not already same ruler as Process / not already settled 正式三事（338 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 没有确定性要求 not already must be deterministic / not already same ruler as Process / not already settled 正式三事（338 余量）/ not 896 prepare-nondet-notmust interchangeable / not 338 prepare-nondet-vs-process bundled interchangeable」，不是 Prepare/ExtendVote 确定性 bundled（338），也不是 Process 必须只依赖请求和上一份状态（340/893），也不是四门已经结算（33）。不要另写怎样写 Prepare 或怎样写 ExtendVote。

## 官方三件事

1. **看见 `PrepareProposal` 没有确定性要求 / 看见可以依赖其它值或操作 这份没有 is not already 已经必须确定 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 896 prepare-nondet-notmust interchangeable / 897 prepare-nondet-notraw interchangeable / 338 prepare-nondet item 2 raw interchangeable，也不是已经 Prepare 没有确定性要求 not already must be deterministic / not already same ruler as Process / not already settled 正式三事 bundled（338 item 1 余量） interchangeable / 338 prepare-nondet item 1 interchangeable。**  
   官方写：`PrepareProposal` 和 `ExtendVote` 都没有与确定性相关的要求。`PrepareProposal` 不被要求确定。准备好的提案 *u_p* 可以依赖 raw 提案 *v_p* 和已提交状态 *s_{p,h-1}*，也可以依赖其它值或操作。看见没有这道要求，不是已经必须确定 interchangeable——本页从 338 item 1 侧钉 not already must be deterministic 单句。338 prepare-nondet vs process bundled unbundling 在本页 item 1 启动。

2. **看见可以依赖其它值 / 看见 Prepare 回了 / 这份没有 is not already 已经和 Process / Finalize 同一把尺 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 896 prepare-nondet-notmust interchangeable / 338 prepare-nondet item 3 Extend interchangeable / 898 prepare-nondet-notext interchangeable，也不是已经 Process 必须只依赖请求和上一份状态 interchangeable / 340 / 893 process-det-notprep interchangeable。**  
   官方把可以依赖其它值和已经和 Process / Finalize 同一把尺分开——338 bundled 第一件事常与 340 混成「看见可以不确定就已经必须确定或已经同一把尺 interchangeable」，本页钉 not already same ruler as Process 单句。

3. **看见 Prepare 回了 / 看见没有这道要求 / 这份没有 is not already 已经交差 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 896 prepare-nondet-notmust interchangeable / 897 prepare-nondet-notraw interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把 Prepare 回了和已经交差分开。看见 Prepare 回了，不是已经交差 interchangeable。338 prepare-nondet vs process bundled unbundling 在本页 item 1 启动。

怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑那些「其它值或操作」是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Prepare 没有确定性要求 not already must be deterministic ≠ 已经必须确定 interchangeable：** 官方把 Prepare 没有这道要求和已经必须确定分开。
- **看见可以依赖其它值 not already same ruler as Process ≠ 已经和 Process 同一把尺 interchangeable：** 官方把 Prepare 可以不确定和 Process / Finalize 必须确定分开。
- **看见 Prepare 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Prepare 回了和已经交差分开；338 prepare-nondet vs process bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 没有确定性要求 | 不是已经必须确定 | 不是 Process 必须只依赖请求和上一份状态（340/893） |
| 看见可以依赖其它值 | 不是已经和 Process 同一把尺 | 不是四门已经结算（33） |
| 看见 Prepare 回了 | 不是已经交差 | 不是两边 raw 一样就已经同一份提案（897） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有确定性要求 not already must be deterministic / not already same ruler as Process / not already settled 正式三事（338 余量），必须分开是不是已经必须确定、是不是已经和 Process 同一把尺、是不是已经交差。可以跳过「看见可以不确定就必须确定」。不要把「其它值或操作」当不确定常数。不要另写怎样写 Prepare 或怎样写 ExtendVote。338 prepare-nondet vs process bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepare-nondet-notraw-vs-bundled.md`](worked-example-prepare-nondet-notraw-vs-bundled.md)（不变量 897 item 2）。

## 本页不抄

- 怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑其它值或操作。
- Prepare/ExtendVote 确定性 bundled。那是不变量 338。
- 两边 raw 一样。那是不变量 338 item 2 余量 / 897。
- Process 必须只依赖请求和上一份状态。那是不变量 340 / 893。
- 四门已经结算。那是不变量 33。
