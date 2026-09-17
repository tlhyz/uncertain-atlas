# 例：看见到了 H is not already Prepare carrying extensions interchangeable / not already written into this-height proposal interchangeable / not already settled interchangeable

**层次**：实现 / 到了 H not already Prepare carrying extensions / not already written into this-height proposal / not already settled 正式三事（330 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「到了 H not already Prepare carrying extensions / not already written into this-height proposal / not already settled 正式三事（330 余量）/ not 926 ve-height-notprep interchangeable / not 330 ve-height-vs-prepare bundled interchangeable」，不是扩展启用 bundled（330），也不是验签拒收整张预提交（34），也不是填了两个就已经启用 PBTS（336/924）。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。

## 官方三件事

1. **看见到了 H / 看见已经叫了 ExtendVote 这份高度 is not already 已经 Prepare 带了扩展 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 926 ve-height-notprep interchangeable / 927 ve-height-notthis interchangeable / 330 ve-height item 2 H+1 interchangeable，也不是已经到了 H not already Prepare carrying extensions / not already written into this-height proposal / not already settled 正式三事 bundled（330 item 1 余量） interchangeable / 330 ve-height item 1 interchangeable。**  
   官方写：到了配置高度 H，PrepareProposal 还不会带投票扩展，但会调 ExtendVote 和 VerifyVoteExtension。看见高度到了 H，不是已经在 Prepare 里带了扩展 interchangeable——本页从 330 item 1 侧钉 not already Prepare carrying extensions 单句。330 ve-height vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见已经叫了 ExtendVote / 看见高度到了 H / 这份高度 is not already 已经把扩展写进本高提议 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 926 ve-height-notprep interchangeable / 330 ve-height item 3 h < H interchangeable / 928 ve-height-notlegal interchangeable，也不是已经验签拒收整张预提交 interchangeable / 34 verify-reject interchangeable。**  
   官方把已经叫了 ExtendVote 和已经把扩展写进本高提议分开——330 bundled 第一件事常与 34 混成「看见到了 H 就已经 Prepare 带了扩展或已经验签交差 interchangeable」，本页钉 not already written into this-height proposal 单句。

3. **看见已经叫了 ExtendVote / 看见到了 H / 这份高度 is not already 已经交差 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 926 ve-height-notprep interchangeable / 927 ve-height-notthis interchangeable，也不是已经填了两个就已经启用 PBTS interchangeable / 336/924 precision-noton interchangeable。**  
   官方把已经叫了 ExtendVote 和已经交差分开。看见已经叫了 ExtendVote，不是已经交差 interchangeable。330 ve-height vs prepare bundled unbundling 在本页 item 1 启动。

怎样设 VoteExtensionsEnableHeight、默认 0、怎样写空扩展是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **到了 H not already Prepare carrying extensions ≠ 已经 Prepare 带了扩展 interchangeable：** 官方把开始叫 ExtendVote 和 Prepare 开始带扩展分开。
- **看见已经叫了 ExtendVote not already written into this-height proposal ≠ 已经把扩展写进本高提议 interchangeable：** 官方把叫了 ExtendVote 和本高提议已经带了扩展分开。
- **看见已经叫了 ExtendVote not already settled ≠ 已经交差 interchangeable：** 官方把叫了 ExtendVote 和已经交差分开；330 ve-height vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 到了 H | 不是已经 Prepare 带了扩展，也不是已经写进本高提议 | 不是验签拒收整张预提交（34） |
| 看见已经叫了 ExtendVote | 不是已经写进本高提议 | 不是填了两个就已经启用 PBTS（336/924） |
| 看见到了 H | 不是已经交差 | 不是 H+1 带了扩展就已经是本高度刚签的（927） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看到了 H not already Prepare carrying extensions / not already written into this-height proposal / not already settled 正式三事（330 余量），必须分开是不是已经 Prepare 带了扩展、是不是已经写进本高提议、是不是已经交差。可以跳过「看见到了 H 就已经切到 ABCI 2.0」。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。330 ve-height vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-ve-height-notthis-vs-bundled.md`](worked-example-ve-height-notthis-vs-bundled.md)（不变量 927 item 2）。

## 本页不抄

- 怎样设 VoteExtensionsEnableHeight、默认 0、怎样写空扩展。
- 扩展启用 bundled。那是不变量 330。
- H+1 带了扩展就已经是本高度刚签的。那是不变量 330 item 2 余量 / 927。
- 验签拒收整张预提交。那是不变量 34。
