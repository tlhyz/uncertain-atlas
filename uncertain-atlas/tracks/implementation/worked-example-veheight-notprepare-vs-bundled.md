# 例：看见到了 H / 看见已经叫了 ExtendVote / 看见会调 VerifyVoteExtension is not already already prepare-ext interchangeable / already extend-called-is-prepare interchangeable / already in-proposal interchangeable

**层次**：实现 / 到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事（330 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事（330 余量）/ not 746 veheight-notprepare interchangeable / not 330 veheight bundled interchangeable」，不是 VoteExtensionsEnableHeight bundled（330），也不是 H+1 带了扩展不是已经是本高度刚签的（747 item 2 余量）或 h < H 带了扩展不是已经合法（748 item 3 余量）。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。

## 官方三件事

规范把 Requirements 里到了 H 仍不会在 Prepare 带扩展、会调 ExtendVote / VerifyVoteExtension 和「已经是到了 H 就已经 Prepare 带了扩展 interchangeable / 已经是叫了 ExtendVote 就已经把扩展写进本高提议 interchangeable / 已经是会调 Verify 就已经在提议里 interchangeable / 已经是 veheight bundled interchangeable」分开写成三件独立的实现事，不是「看见到了 H 就已经 Prepare 带了扩展 interchangeable / 就已经是叫了 ExtendVote 就写进提议 interchangeable / 就已经在提议里 interchangeable」一件事：

1. **看见到了 H / 看见高度到了 H / 看见配置高度 H is not already 已经 Prepare 带了扩展 interchangeable / 已经 prepare-ext interchangeable / 已经 Prepare 带扩展交差 interchangeable / 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 746 veheight-notprepare interchangeable / 330 veheight item 1 interchangeable，也不是已经到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事 bundled（330 item 1 余量） interchangeable / 330 veheight item 1 interchangeable，也不是已经 H+1 带了扩展不是已经是本高度刚签的（747） interchangeable / 748 veheight-notlegal interchangeable / 34 vote-extension interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：到了配置高度 **H**，`PrepareProposal` **还不会**带投票扩展。看见到了 H，不是已经 prepare-ext interchangeable——330 钉 bundled 三事，本页从 item 1 侧钉 not already prepare-ext 单句。看见高度到了 H，不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable——330 钉 bundled，本页钉 item 1 第一件事。看见配置高度 H，不是已经验签拒收整张预提交（34） interchangeable——34 另钉。330 veheight vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见已经叫了 ExtendVote / 看见调了 ExtendVote / 看见会调 ExtendVote is not already 已经把扩展写进本高提议 interchangeable / 已经 extend-called-is-prepare interchangeable / 已经写进提议交差 interchangeable / 330 veheight bundled interchangeable / 34 vote-extension interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 746 veheight-notprepare interchangeable / 330 veheight item 2 本高度刚签 interchangeable / 330 veheight item 3 合法 interchangeable，也不是已经到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事 bundled（330 item 1 余量） interchangeable / 330 veheight item 1 interchangeable，也不是已经 Prepare 带了扩展（本页第一件事） interchangeable。**  
   官方写：到了 H **会** 调 `ExtendVote` 和 `VerifyVoteExtension`；看见已经叫了 ExtendVote，不是已经把扩展写进本高提议。看见已经叫了 ExtendVote，不是已经 extend-called-is-prepare interchangeable——本页钉 not already extend-called-is-prepare 单句。看见调了 ExtendVote，不是已经空扩展仍验签（34） interchangeable——34 另钉。看见会调 ExtendVote，不是已经 Prepare 带了扩展（本页第一件事） interchangeable——三件事分开钉。330 veheight vs prepare bundled unbundling 在本页 item 1 启动。

3. **看见会调 VerifyVoteExtension / 看见扩展路径都开了 / 看见本高在扩展相关回调 is not already 已经在提议里 interchangeable / 已经 in-proposal interchangeable / 已经写进 Prepare 交差 interchangeable / 330 veheight bundled interchangeable / 58 enable-height interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 746 veheight-notprepare interchangeable / 330 veheight item 2 / 330 veheight item 3，也不是已经到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事 bundled（330 item 1 余量） interchangeable / 330 veheight item 1 interchangeable，也不是已经 Prepare 带了扩展（本页第一件事） interchangeable / 已经写进本高提议（本页第二件事） interchangeable。**  
   官方写：看见已经叫了 ExtendVote，不是已经把扩展写进本高提议。看见会调 VerifyVoteExtension，不是已经 in-proposal interchangeable——本页钉 not already in-proposal 单句。看见扩展路径都开了，不是已经治理改 enable-height 会 panic（58） interchangeable——58 另钉。看见本高在扩展相关回调，不是已经写进本高提议（本页第二件事） interchangeable——三件事分开钉。330 veheight vs prepare bundled unbundling 在本页 item 1 完成。

怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展是规范里的取值或做法，本页不抄。VoteExtensionsEnableHeight bundled（330）、H+1 带了扩展不是已经是本高度刚签的（330 item 2 余量 / 747）、h < H 带了扩展不是已经合法（330 item 3 余量 / 748）、验签拒收整张预提交（34）、治理改 enable-height 会 panic（58）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **到了 H not already prepare-ext ≠ 330 / 33 interchangeable：** 官方把到了 H 和 Prepare 已经带扩展分开。
- **已经叫了 ExtendVote not already extend-called-is-prepare ≠ 已经写进本高提议 interchangeable：** 官方把调 ExtendVote 和已经写进 Prepare 分开。
- **会调 VerifyVoteExtension not already in-proposal ≠ 已经在提议里 interchangeable：** 官方把扩展相关回调开了和已经在提议里分开；330 veheight vs prepare bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 到了 H | 不是 already prepare-ext | 不是验签拒收 alone（34） |
| 已经叫了 ExtendVote | 不是 already extend-called-is-prepare | 不是空扩展仍验签 alone（34） |
| 会调 VerifyVoteExtension | 不是 already in-proposal | 不是 enable-height panic alone（58） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事（330 余量），必须分开到了 H 是不是 already prepare-ext interchangeable / 330 veheight bundled interchangeable / veheight-sold-as-prepared interchangeable、已经叫了 ExtendVote 是不是 already extend-called-is-prepare interchangeable、会调 VerifyVoteExtension 是不是 already in-proposal interchangeable。可以跳过「看见到了 H 就已经 Prepare 带了扩展 interchangeable / 就已经写进本高提议 interchangeable / 就已经在提议里 interchangeable」。不要另写怎样设 VoteExtensionsEnableHeight。330 veheight vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-veheight-notthissigned-vs-bundled.md`](worked-example-veheight-notthissigned-vs-bundled.md)（不变量 747 item 2）。

## 本页不抄

- 怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展。
- VoteExtensionsEnableHeight bundled。那是不变量 330。
- H+1 带了扩展不是已经是本高度刚签的。那是不变量 330 item 2 余量 / 747。
- h < H 带了扩展不是已经合法。那是不变量 330 item 3 余量 / 748。
- 验签拒收整张预提交、空扩展仍验签。那是不变量 34。
- 治理改 enable-height 会 panic。那是不变量 58。
- 四门已经结算。那是不变量 33。
