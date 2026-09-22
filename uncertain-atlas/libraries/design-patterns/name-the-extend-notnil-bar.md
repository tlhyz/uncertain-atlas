# 模式：把 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事（350 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**例**：[ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed-nil ≠ bundled（350）](../../tracks/implementation/worked-example-extend-notnil-vs-bundled.md)。

## 三个名字

1. **ExtendVote 只在即将广播非 nil Precommit 时才叫 不是 already signed-nil：** 看见 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫 / 叫了 ExtendVote / 即将广播非 nil，不是已经在签 nil interchangeable / 已经 signed-nil interchangeable / 已经签 nil 交差 interchangeable，不是 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable。

2. **启用了扩展 不是 already prevote-calls：** 看见启用了扩展 / 扩展功能开了 / VoteExtensions 启用，不是已经 prevote 会叫 interchangeable / 已经 prevote-calls interchangeable / 已经 prevote 交差 interchangeable，不是 34 voteext interchangeable / 338 preparenondet interchangeable。

3. **有一张票 不是 already vote-has-ext：** 看见有一张票 / 广播了一张票 / 这一轮有票，不是已经这张票带了扩展 interchangeable / 已经 vote-has-ext interchangeable / 已经票带扩展交差 interchangeable，不是 803 extend-notresign interchangeable / 805 extend-notperheight interchangeable。

官方把 ExtendVote 只在即将广播非 nil Precommit 时才叫、不是 prevote 已经会叫、不是这张票已经带了扩展写成三个名字。把它们叫成一个「看见叫了 ExtendVote 就已经签了 nil interchangeable / 就已经 prevote 会叫 interchangeable / 就已经带了扩展 interchangeable」，会把 not already signed-nil、not already prevote-calls、not already vote-has-ext 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事（350 余量），先数清问的是 ExtendVote 只在即将广播非 nil Precommit 时才叫 是不是 already signed-nil / 350 / extendonce-sold-as-height，是不是启用了扩展 是不是 already prevote-calls，还是有一张票 是不是 already vote-has-ext，再决定要不要同一次发布。350 extendonce vs round bundled unbundling 在本页 item 2 续。
