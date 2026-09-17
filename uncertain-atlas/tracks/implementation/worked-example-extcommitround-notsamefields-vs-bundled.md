# 例：看见 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根 is not already same fields interchangeable / not already swapped interchangeable / not already settled interchangeable

**层次**：实现 / Finalize 请求 next_validators_hash not already same fields / not already swapped / not already settled 正式三事（394 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendedCommitInfo / FinalizeBlock Request / Echo Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 请求 next_validators_hash not already same fields / not already swapped / not already settled 正式三事（394 余量）/ not 750 extcommitround-notsamefields interchangeable / not 394 extcommitround-vs-commitinfo bundled interchangeable」，不是 ExtendedCommitInfo 轮 bundled（394），也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359）。不要另写怎样写 ExtendedCommitInfo 轮。

## 官方三件事

1. **看见 Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash / Finalize 这份下一集合根 is not already 已经是 Prepare 那种字段名对上就已经跑过 Process interchangeable / 359 samefields interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 750 extcommitround-notsamefields interchangeable / 749 extcommitround-notcommitinfo interchangeable / 394 extcommitround item 1 round interchangeable，也不是已经 next_validators_hash not already same fields / not already swapped / not already settled 正式三事 bundled（394 item 2 余量） interchangeable / 394 extcommitround item 2 interchangeable。**  
   官方写：`next_validators_hash` 是下一验证者集合的默克尔根。看见填了 next_validators_hash，不是已经是字段名对上就已经跑过 Process interchangeable——本页从 394 item 2 侧钉 not already same fields 单句。394 extcommitround vs commitinfo bundled unbundling 在本页 item 2 续。

2. **看见填了 next_validators_hash / 看见有下一集合根 / Finalize 这份下一集合根 is not already 已经是 H+1 那种已经换了人 interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 750 extcommitround-notsamefields interchangeable / 394 extcommitround item 3 Echo Message interchangeable / 751 extcommitround-notflush interchangeable。**  
   官方把下一集合根和已经换了人分开——394 bundled 第二件事常与 359 混成「看见填了 next_validators_hash 就已经换了人 interchangeable」，本页钉 not already swapped 单句。

3. **看见填了 next_validators_hash / 看见能填 / Finalize 这份下一集合根 is not already 已经交差 interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 750 extcommitround-notsamefields interchangeable / 749 extcommitround-notcommitinfo interchangeable。**  
   官方把能填 next_validators_hash 和已经交差分开。看见能填，不是已经交差 interchangeable。394 extcommitround vs commitinfo bundled unbundling 在本页 item 2 续。

怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根是规范里的做法，本页不抄。

## 官方为什么这样拆

- **next_validators_hash not already same fields ≠ 359 interchangeable：** 官方把下一集合根和字段名对上就已经跑过 Process 分开。
- **next_validators_hash not already swapped ≠ 已经换了人 interchangeable：** 官方把有下一集合根和 H+1 就已经换了人分开。
- **next_validators_hash not already settled ≠ 已经交差 interchangeable：** 官方把能填 next_validators_hash 和已经交差分开；394 extcommitround vs commitinfo bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 请求 next_validators_hash 是下一验证者集合默克尔根 | 不是已经是同一套字段（359） | 不是 ExtendedCommitInfo.round（749/394 item 1） |
| 看见填了 next_validators_hash | 不是已经换了人 | 不是 ExtendedCommitInfo 轮 bundled（394） |
| 看见能填 | 不是已经交差 | 不是 Echo Message（751/394 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 请求 next_validators_hash not already same fields / not already swapped / not already settled 正式三事（394 余量），必须分开 next_validators_hash 是不是已经是同一套字段 interchangeable / 359、是不是已经换了人、是不是已经交差。可以跳过「看见填了 next_validators_hash 就已经是同一套字段」。不要另写怎样写 ExtendedCommitInfo 轮。394 extcommitround vs commitinfo bundled unbundling 在本页 item 2 续；完成 [`worked-example-extcommitround-notflush-vs-bundled.md`](worked-example-extcommitround-notflush-vs-bundled.md)（不变量 751 item 3）。

## 本页不抄

- 怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根。
- ExtendedCommitInfo 轮 bundled。那是不变量 394。
- ExtendedCommitInfo.round。那是不变量 394 item 1 余量 / 749。
- Echo 请求 Message。那是不变量 394 item 3 余量 / 751。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
