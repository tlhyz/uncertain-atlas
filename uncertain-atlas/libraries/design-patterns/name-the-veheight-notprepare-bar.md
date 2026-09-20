# 模式：把到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事（330 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**例**：[到了 H not already prepare-ext ≠ bundled（330）](../../tracks/implementation/worked-example-veheight-notprepare-vs-bundled.md)。

## 三个名字

1. **到了 H 不是 already prepare-ext：** 看见到了 H / 高度到了 H / 配置高度 H，不是已经 Prepare 带了扩展 interchangeable / 已经 Prepare 带扩展交差 interchangeable，不是 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable。

2. **已经叫了 ExtendVote 不是 already extend-called-is-prepare：** 看见已经叫了 ExtendVote / 调了 ExtendVote / 会调 ExtendVote，不是已经把扩展写进本高提议 interchangeable / 已经写进提议交差 interchangeable，不是 34 vote-extension interchangeable / 330 veheight item 2 interchangeable。

3. **会调 VerifyVoteExtension 不是 already in-proposal：** 看见会调 VerifyVoteExtension / 扩展路径都开了 / 本高在扩展相关回调，不是已经在提议里 interchangeable / 已经写进 Prepare 交差 interchangeable，不是 58 enable-height interchangeable / 330 veheight item 3 interchangeable。

官方把到了 H 单句、already prepare-ext、already extend-called-is-prepare、already in-proposal 写成三个名字。把它们叫成一个「看见到了 H 就已经 Prepare 带了扩展 interchangeable / 就已经写进本高提议 interchangeable / 就已经在提议里 interchangeable」，会把 not already prepare-ext、not already extend-called-is-prepare、not already in-proposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看到了 H 不是已经 Prepare 带了扩展 not already prepare-ext / not already extend-called-is-prepare / not already in-proposal 正式三事（330 余量），先数清问的是到了 H 是不是 already prepare-ext / 330 / veheight-sold-as-prepared，是不是已经叫了 ExtendVote 是不是 already extend-called-is-prepare，还是会调 VerifyVoteExtension 是不是 already in-proposal，再决定要不要同一次发布。330 veheight vs prepare bundled unbundling 在本页 item 1 启动。
