# 例：看见优先级差被缩放 is not already per-head interchangeable / not already no-priority interchangeable / not already equal interchangeable

**层次**：共识 / 优先级差被缩放 not already per-head / not already no-priority / not already equal 正式三事（302 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应课文**：[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)、[L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「优先级差被缩放 not already per-head / not already no-priority / not already equal 正式三事（302 余量）/ not 997 roundset-notscale interchangeable / not 302 round-vs-set bundled interchangeable」，不是提议者选择 bundled（302），也不是 NPoS 当选已经按质押计票（129），也不是 InitChain 空名单就已经没有集合（318）。不要另写怎样算优先级或怎样缩放。

## 官方三件事

1. **看见优先级差被缩放 / 看见范围被压住 这份选择 is not already 已经按人头轮 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 997 roundset-notscale interchangeable / 995 roundset-notset interchangeable / 302 round item 1 换轮 interchangeable，也不是已经优先级差被缩放 not already per-head / not already no-priority / not already equal 正式三事 bundled（302 item 3 余量） interchangeable / 302 round item 3 interchangeable。**  
   官方写：优先级最小到最大的距离会被压住，免得低权的人永远追不上。看见差被缩放，不是已经按人头轮 interchangeable——本页从 302 item 3 侧钉 not already per-head 单句。302 round vs set bundled unbundling 在本页 item 3 完成。

2. **看见范围被压住 / 看见缩放 / 这份选择 is not already 已经没有优先级 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 997 roundset-notscale interchangeable / 302 round item 2 新加入 interchangeable / 996 roundset-notjump interchangeable，也不是已经 NPoS 当选已经按质押计票 interchangeable / 129 npos interchangeable。**  
   官方把范围被压住和已经没有优先级分开。看见范围被压住，不是已经没有优先级 interchangeable。本页钉 not already no-priority 单句。

3. **看见按票权往前走 / 看见缩放 / 这份选择 is not already 已经每人一轮 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 997 roundset-notscale interchangeable / 995 roundset-notset interchangeable，也不是已经 InitChain 空名单就已经没有集合 interchangeable / 318 validatorupdate interchangeable。**  
   官方把按票权往前走和已经每人一轮分开。看见按票权往前走，不是已经每人一轮 interchangeable。302 round vs set bundled unbundling 在本页 item 3 完成。

惩罚系数、缩放倍数、溢出处理是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **优先级差被缩放 not already per-head ≠ 已经按人头轮 interchangeable：** 官方把压住范围和按票权往前走分开。
- **看见范围被压住 not already no-priority ≠ 已经没有优先级 interchangeable：** 官方把范围被压住和已经没有优先级分开。
- **看见按票权往前走 not already equal ≠ 已经每人一轮 interchangeable：** 官方把按票权往前走和已经每人一轮分开；302 round vs set bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 优先级差被缩放 | 不是已经按人头轮 | 不是 NPoS 当选已经按质押计票（129） |
| 看见范围被压住 | 不是已经没有优先级 | 不是 InitChain 空名单就已经没有集合（318） |
| 看见按票权往前走 | 不是已经每人一轮 | 不是同一高度换轮就已经换了集合（995） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级差被缩放 not already per-head / not already no-priority / not already equal 正式三事（302 余量），必须分开是不是已经按人头轮、是不是已经没有优先级、是不是已经每人一轮。可以跳过「看见换轮就已经换了名单」。不要另写怎样算优先级或怎样缩放。302 round vs set bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 惩罚系数、缩放倍数、溢出处理、例表。
- 提议者选择 bundled。那是不变量 302。
- NPoS 当选已经按质押计票。那是不变量 129。
- InitChain 空名单就已经没有集合。那是不变量 318。
