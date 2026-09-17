# 例：看见同一高度换轮 is not already new-set interchangeable / not already this-height interchangeable / not already applied interchangeable

**层次**：共识 / 同一高度换轮 not already new-set / not already this-height / not already applied 正式三事（302 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应课文**：[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)、[L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「同一高度换轮 not already new-set / not already this-height / not already applied 正式三事（302 余量）/ not 995 roundset-notset interchangeable / not 302 round-vs-set bundled interchangeable」，不是提议者选择 bundled（302），也不是 H 的更新已经在 H+1 计票（35），也不是提案收了就已经从池里删掉（301/992）。不要另写怎样算优先级或怎样缩放。

## 官方三件事

1. **看见同一高度换轮 / 看见还用同一套验证者 这份选择 is not already 已经换成应用刚回的那套 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 995 roundset-notset interchangeable / 996 roundset-notjump interchangeable / 302 round item 2 新加入 interchangeable，也不是已经同一高度换轮 not already new-set / not already this-height / not already applied 正式三事 bundled（302 item 1 余量） interchangeable / 302 round item 1 interchangeable。**  
   官方写：同一高度里，各轮提议者选择用同一套验证者。集合更新是高度之间的事，由应用在 EndBlock 给出。看见换轮了，不是这高度已经换了名单 interchangeable——本页从 302 item 1 侧钉 not already new-set 单句。302 round vs set bundled unbundling 在本页 item 1 启动。

2. **看见应用回了更新 / 看见换轮 / 这份选择 is not already 本高度各轮已经用上 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 995 roundset-notset interchangeable / 302 round item 3 缩放 interchangeable / 997 roundset-notscale interchangeable，也不是已经 H 的更新已经在 H+1 计票 interchangeable / 35 validator-delay interchangeable。**  
   官方把应用回了更新和本高度各轮已经用上分开。看见应用回了更新，不是本高度各轮已经用上 interchangeable。本页钉 not already this-height 单句。

3. **看见下一轮换了人 / 看见换轮 / 这份选择 is not already 集合已经变了 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 995 roundset-notset interchangeable / 996 roundset-notjump interchangeable，也不是已经提案收了就已经从池里删掉 interchangeable / 301/992 proposed-notdel interchangeable。**  
   官方把下一轮换了人和集合已经变了分开。看见下一轮换了人，不是集合已经变了 interchangeable。302 round vs set bundled unbundling 在本页 item 1 启动。

惩罚系数、缩放倍数、溢出处理是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **同一高度换轮 not already new-set ≠ 已经换成应用刚回的那套 interchangeable：** 官方把各轮共用一套和高度之间才改集合分开。
- **看见应用回了更新 not already this-height ≠ 本高度各轮已经用上 interchangeable：** 官方把应用回了更新和本高度各轮已经用上分开。
- **看见下一轮换了人 not already applied ≠ 集合已经变了 interchangeable：** 官方把下一轮换了人和集合已经变了分开；302 round vs set bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一高度各轮 | 不是已经换成应用刚回的那套 | 不是 H 的更新已经在 H+1 计票（35） |
| 看见应用回了更新 | 不是本高度各轮已经用上 | 不是提案收了就已经从池里删掉（301/992） |
| 看见下一轮换了人 | 不是集合已经变了 | 不是新加入就已经能跳到队头（996） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度换轮 not already new-set / not already this-height / not already applied 正式三事（302 余量），必须分开是不是已经换成应用刚回的那套、是不是本高度各轮已经用上、是不是集合已经变了。可以跳过「看见换轮就已经换了名单」。不要另写怎样算优先级或怎样缩放。302 round vs set bundled unbundling 在本页 item 1 启动；续 [`worked-example-roundset-notjump-vs-bundled.md`](worked-example-roundset-notjump-vs-bundled.md)（不变量 996 item 2）。

## 本页不抄

- 惩罚系数、缩放倍数、溢出处理、例表。
- 提议者选择 bundled。那是不变量 302。
- H 的更新已经在 H+1 计票。那是不变量 35。
- 提案收了就已经从池里删掉。那是不变量 301/992。
