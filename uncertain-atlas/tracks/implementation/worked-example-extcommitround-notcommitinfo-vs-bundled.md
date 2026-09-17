# 例：看见 ExtendedCommitInfo.round 是提交轮 is not already CommitInfo.round interchangeable / not already ranked interchangeable / not already settled interchangeable

**层次**：实现 / ExtendedCommitInfo.round not CommitInfo.round / not already ranked / not already settled 正式三事（394 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendedCommitInfo / FinalizeBlock Request / Echo Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedCommitInfo.round not CommitInfo.round / not already ranked / not already settled 正式三事（394 余量）/ not 749 extcommitround-notcommitinfo interchangeable / not 394 extcommitround-vs-commitinfo bundled interchangeable」，不是 ExtendedCommitInfo 轮 bundled（394），也不是 CommitInfo.round 就已经按投票权排过（392）。不要另写怎样写 ExtendedCommitInfo 轮。

## 官方三件事

1. **看见 ExtendedCommitInfo `round` 是提交轮 / 看见填了 round / Finalize 这份带扩展的提交轮 is not already 已经是 CommitInfo 那份提交轮 interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 749 extcommitround-notcommitinfo interchangeable / 750 extcommitround-notsamefields interchangeable / 394 extcommitround item 2 next_validators_hash interchangeable，也不是已经 round not CommitInfo.round / not already ranked / not already settled 正式三事 bundled（394 item 1 余量） interchangeable / 394 extcommitround item 1 interchangeable。**  
   官方写：`round` 是提交轮，反映上一高度块提议者决定时的那一轮。看见填了 round，不是已经是 CommitInfo 那份提交轮 interchangeable——本页从 394 item 1 侧钉 not CommitInfo.round 单句。394 extcommitround vs commitinfo bundled unbundling 在本页 item 1 启动。

2. **看见填了 round / 看见有轮次 / Finalize 这份带扩展的提交轮 is not already 已经按投票权降序排过 interchangeable / 392 initapphash interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 749 extcommitround-notcommitinfo interchangeable / 394 extcommitround item 3 Echo Message interchangeable / 751 extcommitround-notflush interchangeable。**  
   官方把带扩展的提交轮和已经按投票权排过分开——394 bundled 第一件事常与 392 混成「看见填了 ExtendedCommitInfo.round 就已经按投票权排过 interchangeable」，本页钉 not already ranked 单句。

3. **看见填了 round / 看见能填 / Finalize 这份带扩展的提交轮 is not already 已经交差 interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 749 extcommitround-notcommitinfo interchangeable / 750 extcommitround-notsamefields interchangeable。**  
   官方把能填 ExtendedCommitInfo.round 和已经交差分开。看见能填，不是已经交差 interchangeable。394 extcommitround vs commitinfo bundled unbundling 在本页 item 1 启动。

怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根是规范里的做法，本页不抄。

## 官方为什么这样拆

- **round not CommitInfo.round ≠ CommitInfo interchangeable：** 官方把带扩展的提交轮和不带扩展的提交轮分开。
- **round not already ranked ≠ 392 interchangeable：** 官方把有轮次和 CommitInfo.round 就已经按投票权排过分开。
- **round not already settled ≠ 已经交差 interchangeable：** 官方把能填 ExtendedCommitInfo.round 和已经交差分开；394 extcommitround vs commitinfo bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedCommitInfo.round 是提交轮 | 不是已经是 CommitInfo.round | 不是 next_validators_hash（750/394 item 2） |
| 看见填了 round | 不是已经按投票权排过（392） | 不是 ExtendedCommitInfo 轮 bundled（394） |
| 看见能填 | 不是已经交差 | 不是 Echo Message（751/394 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedCommitInfo.round not CommitInfo.round / not already ranked / not already settled 正式三事（394 余量），必须分开 round 是不是已经是 CommitInfo.round、是不是已经按投票权排过 interchangeable / 392、是不是已经交差。可以跳过「看见填了 ExtendedCommitInfo.round 就已经是 CommitInfo.round」。不要另写怎样写 ExtendedCommitInfo 轮。394 extcommitround vs commitinfo bundled unbundling 在本页 item 1 启动；续 [`worked-example-extcommitround-notsamefields-vs-bundled.md`](worked-example-extcommitround-notsamefields-vs-bundled.md)（不变量 750 item 2）。

## 本页不抄

- 怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根。
- ExtendedCommitInfo 轮 bundled。那是不变量 394。
- Finalize 请求 next_validators_hash。那是不变量 394 item 2 余量 / 750。
- Echo 请求 Message。那是不变量 394 item 3 余量 / 751。
- CommitInfo.round 就已经按投票权排过。那是不变量 392。
