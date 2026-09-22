# 反模式：把 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事（350 余量）说成已经在签 nil / 已经 prevote 会叫 / 已经这张票带了扩展

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed-nil ≠ bundled（350）](../../tracks/implementation/worked-example-extend-notnil-vs-bundled.md)。

## 卖法

把 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫 / 叫了 ExtendVote / 即将广播非 nil 写成已经在签 nil interchangeable / 已经 signed-nil interchangeable / 已经签 nil 交差 interchangeable / 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable；把启用了扩展 / 扩展功能开了 写成已经 prevote 会叫 interchangeable / 已经 prevote-calls interchangeable / 已经 prevote 交差 interchangeable；把有一张票 / 广播了一张票 写成已经这张票带了扩展 interchangeable / 已经 vote-has-ext interchangeable / 已经票带扩展交差 interchangeable，或已经和 350 extendonce bundled / extendonce-sold-as-height interchangeable / 804 extend-notnil interchangeable。

## 为什么错

官方把 ExtendVote 只在即将广播非 nil Precommit 时才叫、不是 prevote 已经会叫、不是这张票已经带了扩展写成三件独立的实现事。把它们卖成 already signed-nil interchangeable / already prevote-calls interchangeable / already vote-has-ext interchangeable，会把 not already signed-nil、not already prevote-calls、not already vote-has-ext 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事（350 余量），必须分开 not already signed-nil、not already prevote-calls、not already vote-has-ext 三件事，不要和 350 / 338 / 34 / 803 / 805 糊成一句。

## 和相邻反模式

- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮一份扩展 bundled 全段，不是本页 ExtendVote 非 nil 才叫 item 2 单句边界。
- [extend-notresign-sold-as-bundled](extend-notresign-sold-as-bundled.md) 是一轮最多一张 Precommit not already resign（350 item 1），不是本页 not already signed-nil 边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是同一块不是已经是同一份扩展（338），不是本页 not already signed-nil / not already vote-has-ext 边界。
