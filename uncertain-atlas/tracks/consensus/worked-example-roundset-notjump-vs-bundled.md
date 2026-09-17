# 例：看见新验证者加进来 is not already jump interchangeable / not already washed interchangeable / not already fair-round interchangeable

**层次**：共识 / 新加入 not already jump / not already washed / not already fair-round 正式三事（302 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应课文**：[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)、[L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「新加入 not already jump / not already washed / not already fair-round 正式三事（302 余量）/ not 996 roundset-notjump interchangeable / not 302 round-vs-set bundled interchangeable」，不是提议者选择 bundled（302），也不是轻验集合已经对齐提议者字段（56），也不是空名单就已经没有集合（303/988）。不要另写怎样算优先级或怎样缩放。

## 官方三件事

1. **看见新验证者加进来 / 看见初始优先级被往后放 这份选择 is not already 已经能靠退出再加入跳到队头 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 996 roundset-notjump interchangeable / 995 roundset-notset interchangeable / 302 round item 1 换轮 interchangeable，也不是已经新加入 not already jump / not already washed / not already fair-round 正式三事 bundled（302 item 2 余量） interchangeable / 302 round item 2 interchangeable。**  
   官方写：刚当过提议者的人被放到队尾。若它退出再加入，会不公平地往前跳。所以新加入的初始优先级被往后放。看见加进来了，不是已经排到队头 interchangeable——本页从 302 item 2 侧钉 not already jump 单句。302 round vs set bundled unbundling 在本页 item 2 续。

2. **看见退出再加入 / 看见加进来 / 这份选择 is not already 已经洗掉队尾 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 996 roundset-notjump interchangeable / 302 round item 3 缩放 interchangeable / 997 roundset-notscale interchangeable，也不是已经轻验集合已经对齐提议者字段 interchangeable / 56 proposer field interchangeable。**  
   官方把退出再加入和已经洗掉队尾分开。看见退出再加入，不是已经洗掉队尾 interchangeable。本页钉 not already washed 单句。

3. **看见初始优先级有数 / 看见加进来 / 这份选择 is not already 已经公平当过一轮 interchangeable，也不是已经提议者选择 bundled（302） interchangeable / 996 roundset-notjump interchangeable / 995 roundset-notset interchangeable，也不是已经空名单就已经没有集合 interchangeable / 303/988 genesis-notset interchangeable。**  
   官方把初始优先级有数和已经公平当过一轮分开。看见初始优先级有数，不是已经公平当过一轮 interchangeable。302 round vs set bundled unbundling 在本页 item 2 续。

惩罚系数、缩放倍数、溢出处理是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **新加入 not already jump ≠ 已经能跳到队头 interchangeable：** 官方把防止退出再加入往前跳，和已经公平当过一轮分开。
- **看见退出再加入 not already washed ≠ 已经洗掉队尾 interchangeable：** 官方把退出再加入和已经洗掉队尾分开。
- **看见初始优先级有数 not already fair-round ≠ 已经公平当过一轮 interchangeable：** 官方把初始优先级有数和已经公平当过一轮分开；302 round vs set bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 新加入的初始优先级 | 不是已经能跳到队头 | 不是轻验集合已经对齐提议者字段（56） |
| 看见退出再加入 | 不是已经洗掉队尾 | 不是空名单就已经没有集合（303/988） |
| 看见初始优先级有数 | 不是已经公平当过一轮 | 不是缩放就已经按人头轮（997） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看新加入 not already jump / not already washed / not already fair-round 正式三事（302 余量），必须分开是不是已经能跳到队头、是不是已经洗掉队尾、是不是已经公平当过一轮。可以跳过「看见换轮就已经换了名单」。不要另写怎样算优先级或怎样缩放。302 round vs set bundled unbundling 在本页 item 2 续；续 [`worked-example-roundset-notscale-vs-bundled.md`](worked-example-roundset-notscale-vs-bundled.md)（不变量 997 item 3）。

## 本页不抄

- 惩罚系数、缩放倍数、溢出处理、例表。
- 提议者选择 bundled。那是不变量 302。
- 轻验集合已经对齐提议者字段。那是不变量 56。
- 空名单就已经没有集合。那是不变量 303/988。
