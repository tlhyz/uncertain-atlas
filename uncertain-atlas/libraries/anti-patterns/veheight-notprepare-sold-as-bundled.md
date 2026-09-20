# 反模式：把到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事（330 余量）说成已经 Prepare 带了扩展 / 已经写进本高提议 / 已经在提议里

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[到了 H not already prepare-ext ≠ bundled（330）](../../tracks/implementation/worked-example-veheight-notprepare-vs-bundled.md)。

## 卖法

把到了 H / 高度到了 H / 配置高度 H 写成已经 Prepare 带了扩展 interchangeable / 已经 prepare-ext interchangeable / 已经 Prepare 带扩展交差 interchangeable / 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable；把已经叫了 ExtendVote / 调了 ExtendVote / 会调 ExtendVote 写成已经把扩展写进本高提议 interchangeable / 已经 extend-called-is-prepare interchangeable；把会调 VerifyVoteExtension / 扩展路径都开了 / 本高在扩展相关回调 写成已经在提议里 interchangeable / 已经 in-proposal interchangeable，或已经和 330 veheight bundled / veheight-sold-as-prepared interchangeable / 746 veheight-notprepare interchangeable。

## 为什么错

官方把到了 H 单句、already prepare-ext、already extend-called-is-prepare、already in-proposal 写成三件独立的实现事。把它们卖成 already prepare-ext interchangeable / already extend-called-is-prepare interchangeable / already in-proposal interchangeable，会把 not already prepare-ext、not already extend-called-is-prepare、not already in-proposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事（330 余量），必须分开 not already prepare-ext、not already extend-called-is-prepare、not already in-proposal 三件事，不要和 330 / 33 / 34 / 58 / 747 / 748 糊成一句。

## 和相邻反模式

- [veheight-notthissigned-sold-as-bundled](veheight-notthissigned-sold-as-bundled.md) 是本高度刚签（330 item 2），不是本页到了 H item 1 单句边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是 VoteExtensionsEnableHeight bundled 全段，不是本页到了 H item 1 单句边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交（34），不是本页 Prepare 带扩展边界。
- [query-notrequired-sold-as-bundled](query-notrequired-sold-as-bundled.md) 是实现了 Query 不是已经是正常运转必须有（329 item 3），不是本页到了 H 边界。
