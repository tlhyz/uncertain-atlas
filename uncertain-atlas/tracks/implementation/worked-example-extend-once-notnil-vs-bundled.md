# 例：看见 ExtendVote 只在即将广播非 nil Precommit 时才叫 is not already signed nil interchangeable / not already every vote calls interchangeable / not already settled interchangeable

**层次**：实现 / ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil / not already every vote calls / not already settled 正式三事（350 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil / not already every vote calls / not already settled 正式三事（350 余量）/ not 864 extend-once-notnil interchangeable / not 350 extend-once-vs-round bundled interchangeable」，不是一轮一份扩展 bundled（350），也不是同一块已经是同一份扩展（338），也不是验签拒收整张预提交就已经是块非法（34）。不要另写怎样写 ExtendVote。

## 官方三件事

1. **看见 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫 / 看见叫了 ExtendVote 这份才叫 is not already 已经签了 nil 票 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 864 extend-once-notnil interchangeable / 863 extend-once-notresign interchangeable / 350 extend-once item 1 一张 interchangeable，也不是已经 ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil / not already every vote calls / not already settled 正式三事 bundled（350 item 2 余量） interchangeable / 350 extend-once item 2 interchangeable。**  
   官方写：Methods 里写过，`ExtendVote` 只在共识即将广播一张非 `nil` Precommit 时才叫。看见叫了 ExtendVote，不是已经在签 nil interchangeable——本页从 350 item 2 侧钉 not already signed nil 单句。350 extend-once vs round bundled unbundling 在本页 item 2 续。

2. **看见叫了 ExtendVote / 看见启用了扩展 / 这份才叫 is not already 已经每张票都会叫 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 864 extend-once-notnil interchangeable / 350 extend-once item 3 一份扩展 interchangeable / 865 extend-once-notperheight interchangeable，也不是已经同一块已经是同一份扩展 interchangeable / 338 samedext interchangeable。**  
   官方把启用了扩展和已经每张票都会叫分开——350 bundled 第二件事常与 338 混成「看见叫了 ExtendVote 就已经签了 nil 或已经每张票都会叫 interchangeable」，本页钉 not already every vote calls 单句。

3. **看见叫了 ExtendVote / 看见有一张票 / 这份才叫 is not already 已经交差 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 864 extend-once-notnil interchangeable / 863 extend-once-notresign interchangeable，也不是已经验签拒收整张预提交就已经是块非法 interchangeable / 34 voteext interchangeable。**  
   官方把有一张票和已经交差分开。看见有一张票，不是这张票已经带了扩展 interchangeable。350 extend-once vs round bundled unbundling 在本页 item 2 续。

怎样写 ExtendVote、怎样选空扩展、怎样测一轮一份是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil ≠ 已经签了 nil 票 interchangeable：** 官方把何时才叫 ExtendVote 和 nil 票分开。
- **看见启用了扩展 not already every vote calls ≠ 已经每张票都会叫 interchangeable：** 官方把启用了扩展和已经每张票都会叫分开。
- **看见有一张票 not already settled ≠ 已经交差 interchangeable：** 官方把有一张票和已经交差分开；350 extend-once vs round bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVote 只在即将广播非 nil Precommit 时才叫 | 不是已经签了 nil 票 | 不是同一块已经是同一份扩展（338） |
| 看见启用了扩展 | 不是已经每张票都会叫 | 不是验签拒收整张预提交就已经是块非法（34） |
| 看见有一张票 | 不是已经交差 | 不是一轮最多一张就已经能再签（863） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil / not already every vote calls / not already settled 正式三事（350 余量），必须分开是不是已经签了 nil 票、是不是已经每张票都会叫、是不是已经交差。可以跳过「看见叫了 ExtendVote 就已经签了 nil 票」。不要另写怎样写 ExtendVote。350 extend-once vs round bundled unbundling 在本页 item 2 续；续 [`worked-example-extend-once-notperheight-vs-bundled.md`](worked-example-extend-once-notperheight-vs-bundled.md)（不变量 865 item 3）。

## 本页不抄

- 怎样写 ExtendVote、怎样选空扩展、怎样测一轮一份。
- 一轮一份扩展 bundled。那是不变量 350。
- 一轮最多一张 Precommit。那是不变量 350 item 1 余量 / 863。
- 同一块已经是同一份扩展。那是不变量 338。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
