# 例：看见 ExtendVote 只在即将广播非 nil Precommit 时才叫 / 看见叫了 ExtendVote / 看见启用了扩展 is not already already signed-nil interchangeable / already prevote-calls interchangeable / already vote-has-ext interchangeable

**层次**：实现 / ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事（350 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事（350 余量）/ not 804 extend-notnil interchangeable / not 350 extendonce bundled interchangeable」，不是一轮一份扩展 bundled（350），也不是一轮最多一张 Precommit 不是已经能再签一张（803 item 1 余量）或一轮只能交出一份扩展不是已经是每一高度一份（805 item 3 余量）。不要另写怎样写 ExtendVote。

## 官方三件事

规范把 Requirements 里 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫、叫了 ExtendVote 和「已经是叫了 ExtendVote 就已经在签 nil interchangeable / 已经是启用了扩展就已经 prevote 会叫 interchangeable / 已经是有一张票就已经带了扩展 interchangeable / 已经是 extendonce bundled interchangeable」分开写成三件独立的实现事，不是「看见叫了 ExtendVote 就已经签了 nil interchangeable / 就已经 prevote 会叫 interchangeable / 就已经带了扩展 interchangeable」一件事：

1. **看见 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫 / 看见叫了 ExtendVote / 看见即将广播非 nil is not already 已经在签 nil interchangeable / 已经 signed-nil interchangeable / 已经签 nil 交差 interchangeable / 350 extendonce bundled interchangeable / 338 preparenondet interchangeable / extendonce-sold-as-height interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 804 extend-notnil interchangeable / 350 extendonce item 2 interchangeable，也不是已经 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事 bundled（350 item 2 余量） interchangeable / 350 extendonce item 2 interchangeable，也不是已经一轮最多一张 Precommit（803） interchangeable / 805 extend-notperheight interchangeable / 34 voteext interchangeable，也不是已经同一块已经是同一份扩展（338） interchangeable。**  
   官方写：Methods 里写过，`ExtendVote` 只在共识即将广播一张非 `nil` Precommit 时才叫。看见叫了 ExtendVote，不是已经在签 nil。看见叫了 ExtendVote，不是已经 signed-nil interchangeable——350 钉 bundled 三事，本页从 item 2 侧钉 not already signed-nil 单句。看见 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫，不是已经一轮一份扩展 bundled（350） interchangeable——350 钉 bundled，本页钉 item 2 第一件事。看见叫了 ExtendVote，不是已经一轮最多一张 Precommit（803） interchangeable——803 另钉 item 1。看见叫了 ExtendVote，不是已经同一块已经是同一份扩展（338） interchangeable——338 另钉。350 extendonce vs round bundled unbundling 在本页 item 2 续。

2. **看见启用了扩展 / 看见扩展功能开了 / 看见 VoteExtensions 启用 is not already 已经 prevote 会叫 interchangeable / 已经 prevote-calls interchangeable / 已经 prevote 交差 interchangeable / 350 extendonce bundled interchangeable / 34 voteext interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 804 extend-notnil interchangeable / 350 extendonce item 1 再签 interchangeable / 350 extendonce item 3 一份扩展 interchangeable，也不是已经 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事 bundled（350 item 2 余量） interchangeable / 350 extendonce item 2 interchangeable，也不是已经在签 nil（本页第一件事） interchangeable。**  
   官方写：看见启用了扩展，不是 prevote 已经会叫。看见扩展功能开了，不是已经 prevote-calls interchangeable——本页钉 not already prevote-calls 单句。看见 VoteExtensions 启用，不是已经在签 nil（本页第一件事） interchangeable——三件事分开钉。350 extendonce vs round bundled unbundling 在本页 item 2 续。

3. **看见有一张票 / 看见广播了一张票 / 看见这一轮有票 is not already 已经这张票带了扩展 interchangeable / 已经 vote-has-ext interchangeable / 已经票带扩展交差 interchangeable / 350 extendonce bundled interchangeable / 338 preparenondet interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 804 extend-notnil interchangeable / 350 extendonce item 1 / 350 extendonce item 3，也不是已经 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事 bundled（350 item 2 余量） interchangeable / 350 extendonce item 2 interchangeable，也不是已经在签 nil（本页第一件事） interchangeable / 已经 prevote 会叫（本页第二件事） interchangeable。**  
   官方写：看见有一张票，不是这张票已经带了扩展。看见广播了一张票，不是已经 vote-has-ext interchangeable——本页钉 not already vote-has-ext 单句。看见这一轮有票，不是已经 prevote 会叫（本页第二件事） interchangeable——三件事分开钉。350 extendonce vs round bundled unbundling 在本页 item 2 续。

怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份是规范里的做法，本页不抄。一轮一份扩展 bundled（350）、一轮最多一张 Precommit 不是已经能再签一张（350 item 1 余量 / 803）、一轮只能交出一份扩展不是已经是每一高度一份（350 item 3 余量 / 805）、验签拒收整张预提交就已经是块非法（34）、同一块已经是同一份扩展（338）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）是另外那套，本页不抄。

## 官方为什么这样拆

- **ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed-nil ≠ 350 / 338 interchangeable：** 官方把叫了 ExtendVote 和已经在签 nil 分开。
- **启用了扩展 not already prevote-calls ≠ 已经 prevote 会叫 interchangeable：** 官方把启用了扩展和 prevote 已经会叫分开。
- **有一张票 not already vote-has-ext ≠ 已经这张票带了扩展 interchangeable：** 官方把有一张票和这张票已经带了扩展分开；350 extendonce vs round bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVote 只在即将广播非 nil Precommit 时才叫 | 不是 already signed-nil | 不是同一块已经是同一份扩展 alone（338） |
| 启用了扩展 | 不是 already prevote-calls | 不是一轮最多一张 already resign alone（803） |
| 有一张票 | 不是 already vote-has-ext | 不是一轮一份扩展 already per-height alone（805） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 not already signed-nil / not already prevote-calls / not already vote-has-ext 正式三事（350 余量），必须分开 ExtendVote 只在即将广播非 nil Precommit 时才叫 是不是 already signed-nil interchangeable / 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable、启用了扩展 是不是 already prevote-calls interchangeable、有一张票 是不是 already vote-has-ext interchangeable。可以跳过「看见叫了 ExtendVote 就已经签了 nil interchangeable / 就已经 prevote 会叫 interchangeable / 就已经带了扩展 interchangeable」。不要另写怎样写 ExtendVote。350 extendonce vs round bundled unbundling 在本页 item 2 续（803 + 804）；续 [`worked-example-extend-notperheight-vs-bundled.md`](worked-example-extend-notperheight-vs-bundled.md)（不变量 805 item 3）；完成见 805。

## 本页不抄

- 怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份。
- 一轮一份扩展 bundled。那是不变量 350。
- 一轮最多一张 Precommit 不是已经能再签一张。那是不变量 350 item 1 余量 / 803。
- 一轮只能交出一份扩展不是已经是每一高度一份。那是不变量 350 item 3 余量 / 805。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 同一块已经是同一份扩展。那是不变量 338。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
