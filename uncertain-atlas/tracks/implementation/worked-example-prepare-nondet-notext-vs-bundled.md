# 例：看见 ExtendVote 没有确定性要求 is not already same extension interchangeable / not already same ruler as Verify interchangeable / not already settled interchangeable

**层次**：实现 / ExtendVote 没有确定性要求 not already same extension / not already same ruler as Verify / not already settled 正式三事（338 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVote 没有确定性要求 not already same extension / not already same ruler as Verify / not already settled 正式三事（338 余量）/ not 898 prepare-nondet-notext interchangeable / not 338 prepare-nondet-vs-process bundled interchangeable」，不是 Prepare/ExtendVote 确定性 bundled（338），也不是 Verify 必须只依赖扩展这块和上一份状态（341/890），也不是验签拒收整张预提交（34）。不要另写怎样写 Prepare 或怎样写 ExtendVote。

## 官方三件事

1. **看见 `ExtendVote` 没有确定性要求 / 看见同一块 这份扩展 is not already 已经是同一份扩展 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 898 prepare-nondet-notext interchangeable / 896 prepare-nondet-notmust interchangeable / 338 prepare-nondet item 1 没有要求 interchangeable，也不是已经 ExtendVote 没有确定性要求 not already same extension / not already same ruler as Verify / not already settled 正式三事 bundled（338 item 3 余量） interchangeable / 338 prepare-nondet item 3 interchangeable。**  
   官方写：`ExtendVote` 也可以不确定。扩展 *e^r_p* 可以依赖这块 *w^r_p* 和 *s_{p,h-1}*，也可以依赖其它值或操作。*w^r_p = w^r_q* 并不蕴涵 *e^r_p = e^r_q*。看见没有确定性要求，不是已经必须确定 interchangeable——本页从 338 item 3 侧钉 not already same extension 单句。338 prepare-nondet vs process bundled unbundling 在本页 item 3 完成。

2. **看见同一块 / 看见能签扩展 / 这份扩展 is not already 已经和 VerifyVoteExtension 必须确定同一把尺 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 898 prepare-nondet-notext interchangeable / 338 prepare-nondet item 2 raw interchangeable / 897 prepare-nondet-notraw interchangeable，也不是已经 Verify 必须只依赖扩展这块和上一份状态 interchangeable / 341 / 890 verify-det-notext interchangeable。**  
   官方把同一块和已经同一份扩展 / 已经和 Verify 同一把尺分开——338 bundled 第三件事常与 341 混成「看见同一块就已经同一份扩展或已经和 Verify 同一把尺 interchangeable」，本页钉 not already same ruler as Verify 单句。

3. **看见能签扩展 / 看见没有确定性要求 / 这份扩展 is not already 已经交差 interchangeable，也不是已经 Prepare/ExtendVote 确定性 bundled（338） interchangeable / 898 prepare-nondet-notext interchangeable / 896 prepare-nondet-notmust interchangeable，也不是已经验签拒收整张预提交 interchangeable / 34 sig-reject interchangeable。**  
   官方把能签扩展和已经交差分开。看见能签扩展，不是已经交差 interchangeable。338 prepare-nondet vs process bundled unbundling 在本页 item 3 完成。

怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑那些「其它值或操作」是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVote 没有确定性要求 not already same extension ≠ 已经是同一份扩展 interchangeable：** 官方把同一块和同一份扩展分开。
- **看见同一块 not already same ruler as Verify ≠ 已经和 Verify 同一把尺 interchangeable：** 官方把 ExtendVote 可以不确定和 Verify 必须确定分开。
- **看见能签扩展 not already settled ≠ 已经交差 interchangeable：** 官方把能签扩展和已经交差分开；338 prepare-nondet vs process bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVote 没有确定性要求 | 不是已经是同一份扩展 | 不是 Verify 必须只依赖扩展这块和上一份状态（341/890） |
| 看见同一块 | 不是已经和 Verify 同一把尺 | 不是验签拒收整张预提交（34） |
| 看见能签扩展 | 不是已经交差 | 不是 Prepare 没有确定性要求就已经必须确定（896） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 没有确定性要求 not already same extension / not already same ruler as Verify / not already settled 正式三事（338 余量），必须分开是不是已经是同一份扩展、是不是已经和 Verify 同一把尺、是不是已经交差。可以跳过「看见同一块就已经同一份扩展」。不要把「其它值或操作」当不确定常数。不要另写怎样写 Prepare 或怎样写 ExtendVote。338 prepare-nondet vs process bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑其它值或操作。
- Prepare/ExtendVote 确定性 bundled。那是不变量 338。
- Prepare 没有确定性要求。那是不变量 338 item 1 余量 / 896。
- Verify 必须只依赖扩展这块和上一份状态。那是不变量 341 / 890。
- 验签拒收整张预提交。那是不变量 34。
