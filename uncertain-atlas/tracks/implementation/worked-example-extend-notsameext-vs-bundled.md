# 例：看见同一块 / 看见 ExtendVote 没有确定性要求 / 看见能签扩展 is not already already same-extension interchangeable / already must-same-e interchangeable / already same-as-verify interchangeable

**层次**：实现 / ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事（338 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事（338 余量）/ not 769 extend-notsameext interchangeable / not 338 preparenondet bundled interchangeable」，不是 Prepare nondet bundled（338），也不是 PrepareProposal 没有确定性要求不是已经必须确定（767 item 1 余量）或两边 raw 一样不是已经是同一份提案（768 item 2 余量）。不要另写怎样写 Prepare 或怎样写 ExtendVote。

## 官方三件事

规范把 Requirements 里 `ExtendVote` 没有确定性要求、同一块 *w^r_p = w^r_q* 和「已经是同一块就已经是同一份扩展 interchangeable / 已经是没有确定性要求就必须同一份 interchangeable / 已经是能签扩展就已经和 Verify 同一把尺 interchangeable / 已经是 preparenondet bundled interchangeable」分开写成三件独立的实现事，不是「看见同一块就已经是同一份扩展 interchangeable / 就已经必须同一份 interchangeable / 就已经和 Verify 同一把尺 interchangeable」一件事：

1. **看见同一块 / 看见 *w^r_p = w^r_q* / 看见同一份块 is not already 已经是同一份扩展 interchangeable / 已经 same-extension interchangeable / 已经同一份扩展交差 interchangeable / 338 preparenondet bundled interchangeable / 34 vote-extension interchangeable / preparenondet-sold-as-deterministic interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 769 extend-notsameext interchangeable / 338 preparenondet item 3 interchangeable，也不是已经 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事 bundled（338 item 3 余量） interchangeable / 338 preparenondet item 3 interchangeable，也不是已经 PrepareProposal 没有确定性要求不是已经必须确定（767） interchangeable / 768 prepare-notrawsame interchangeable / 33 four gates interchangeable，也不是已经验签拒收整张预提交（34） interchangeable。**  
   官方写：*w^r_p = w^r_q* **并不蕴涵** *e^r_p = e^r_q*。两个正确进程拿到同一块，各自 ExtendVote 可以回不同的扩展。看见同一块，不是已经 same-extension interchangeable——338 钉 bundled 三事，本页从 item 3 侧钉 not already same-extension 单句。看见 *w^r_p = w^r_q*，不是已经 Prepare nondet bundled（338） interchangeable——338 钉 bundled，本页钉 item 3 第一件事。看见同一份块，不是已经验签拒收整张预提交（34） interchangeable——34 另钉。338 preparenondet vs process bundled unbundling 在本页 item 3 完成。

2. **看见 ExtendVote 没有确定性要求 / 看见 ExtendVote 也可以不确定 / 看见没有这道要求 is not already 已经必须同一份 interchangeable / 已经 must-same-e interchangeable / 已经必须同一份交差 interchangeable / 338 preparenondet bundled interchangeable / 341 verifydet interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 769 extend-notsameext interchangeable / 338 preparenondet item 1 必须确定 interchangeable / 338 preparenondet item 2 raw 一样 interchangeable，也不是已经 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事 bundled（338 item 3 余量） interchangeable / 338 preparenondet item 3 interchangeable，也不是已经是同一份扩展（本页第一件事） interchangeable。**  
   官方写：`ExtendVote` 也可以不确定。看见没有确定性要求，不是已经必须同一份。看见 ExtendVote 也可以不确定，不是已经 must-same-e interchangeable——本页钉 not already must-same-e 单句。看见没有这道要求，不是已经是同一份扩展（本页第一件事） interchangeable——三件事分开钉。338 preparenondet vs process bundled unbundling 在本页 item 3 完成。

3. **看见能签扩展 / 看见扩展可以依赖其它值或操作 / 看见能签 is not already 已经和 VerifyVoteExtension 必须确定同一把尺 interchangeable / 已经 same-as-verify interchangeable / 已经同一把尺交差 interchangeable / 338 preparenondet bundled interchangeable / 341 verifydet interchangeable，也不是已经 Prepare nondet bundled（338） interchangeable / 769 extend-notsameext interchangeable / 338 preparenondet item 1 / 338 preparenondet item 2，也不是已经 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事 bundled（338 item 3 余量） interchangeable / 338 preparenondet item 3 interchangeable，也不是已经是同一份扩展（本页第一件事） interchangeable / 已经必须同一份（本页第二件事） interchangeable。**  
   官方写：扩展 *e^r_p* 可以依赖这块 *w^r_p* 和 *s_{p,h-1}*，也可以依赖其它值或操作。看见能签扩展，不是已经和 `VerifyVoteExtension` 必须确定同一把尺。看见扩展可以依赖其它值或操作，不是已经 same-as-verify interchangeable——本页钉 not already same-as-verify 单句。看见能签，不是已经必须同一份（本页第二件事） interchangeable——三件事分开钉。338 preparenondet vs process bundled unbundling 在本页 item 3 完成。

怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑那些「其它值或操作」是规范里的做法，本页不抄。Prepare nondet bundled（338）、PrepareProposal 没有确定性要求不是已经必须确定（338 item 1 余量 / 767）、两边 raw 一样不是已经是同一份提案（338 item 2 余量 / 768）、四门已经结算（33）、立刻整块执行已经离开关键路径（327）、验签拒收整张预提交（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **同一块 not already same-extension ≠ 338 / 34 interchangeable：** 官方把同一块和同一份扩展分开。
- **没有确定性要求 not already must-same-e ≠ 已经必须同一份 interchangeable：** 官方把 ExtendVote 没有这道要求和已经必须同一份分开。
- **能签扩展 not already same-as-verify ≠ 已经和 Verify 同一把尺 interchangeable：** 官方把能签扩展和 VerifyVoteExtension 必须确定分开；338 preparenondet vs process bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一块 | 不是 already same-extension | 不是验签拒收整张预提交 alone（34） |
| 没有确定性要求 | 不是 already must-same-e | 不是 Prepare 没有确定性要求就已经必须确定 alone（767） |
| 能签扩展 | 不是 already same-as-verify | 不是两边 raw 一样就已经是同一份提案 alone（768） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事（338 余量），必须分开同一块 是不是 already same-extension interchangeable / 338 preparenondet bundled interchangeable / preparenondet-sold-as-deterministic interchangeable、没有确定性要求 是不是 already must-same-e interchangeable、能签扩展 是不是 already same-as-verify interchangeable。可以跳过「看见同一块就已经是同一份扩展 interchangeable / 就已经必须同一份 interchangeable / 就已经和 Verify 同一把尺 interchangeable」。不要把「其它值或操作」当不确定常数。不要另写怎样写 Prepare 或怎样写 ExtendVote。338 preparenondet vs process bundled unbundling 在本页 item 3 完成（767 + 768 + 769）。

## 本页不抄

- 怎样写 `PrepareProposal`、怎样写 `ExtendVote`、怎样挑其它值或操作。
- Prepare nondet bundled。那是不变量 338。
- PrepareProposal 没有确定性要求不是已经必须确定。那是不变量 338 item 1 余量 / 767。
- 两边 raw 一样不是已经是同一份提案。那是不变量 338 item 2 余量 / 768。
- 四门已经结算。那是不变量 33。
- 立刻整块执行已经离开关键路径。那是不变量 327。
- 验签拒收整张预提交。那是不变量 34。
