# 例：看见正确进程在一轮 r、高度 h 最多广播一张 Precommit / 看见到了 Precommit 步 / 看见有一张票 is not already already resign interchangeable / already is-extension interchangeable / already re-emit interchangeable

**层次**：实现 / 一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事（350 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事（350 余量）/ not 803 extend-notresign interchangeable / not 350 extendonce bundled interchangeable」，不是一轮一份扩展 bundled（350），也不是 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票（804 item 2 余量）或一轮只能交出一份扩展不是已经是每一高度一份（805 item 3 余量）。不要另写怎样写 ExtendVote。

## 官方三件事

规范把 Requirements 里正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit、到了 Precommit 步 和「已经是到了 Precommit 就已经能再签一张 interchangeable / 已经是有一张票就已经是扩展本身 interchangeable / 已经是还能换轮就已经这一轮能再出一张 interchangeable / 已经是 extendonce bundled interchangeable」分开写成三件独立的实现事，不是「看见到了 Precommit 就已经能再签一张 interchangeable / 就已经是扩展 interchangeable / 就已经能再出一张 interchangeable」一件事：

1. **看见正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit / 看见到了 Precommit 步 / 看见到了这一步 is not already 已经能再签一张 interchangeable / 已经 resign interchangeable / 已经再签交差 interchangeable / 350 extendonce bundled interchangeable / 34 voteext interchangeable / extendonce-sold-as-height interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 803 extend-notresign interchangeable / 350 extendonce item 1 interchangeable，也不是已经一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事 bundled（350 item 1 余量） interchangeable / 350 extendonce item 1 interchangeable，也不是已经 ExtendVote 只在非 nil 时才叫（804） interchangeable / 805 extend-notperheight interchangeable / 348 req6coherence interchangeable，也不是已经验签拒收整张预提交就已经是块非法（34） interchangeable。**  
   官方写：按 CometBFT 现在采用的 Tendermint 共识，正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit。看见到了这一步，不是已经能再签一张。看见到了 Precommit 步，不是已经 resign interchangeable——350 钉 bundled 三事，本页从 item 1 侧钉 not already resign 单句。看见正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit，不是已经一轮一份扩展 bundled（350） interchangeable——350 钉 bundled，本页钉 item 1 第一件事。看见到了这一步，不是已经验签拒收整张预提交就已经是块非法（34） interchangeable——34 另钉。350 extendonce vs round bundled unbundling 在本页 item 1 启动。

2. **看见有一张票 / 看见广播了一张 Precommit / 看见这一轮有票 is not already 已经是扩展本身 interchangeable / 已经 is-extension interchangeable / 已经票即扩展交差 interchangeable / 350 extendonce bundled interchangeable / 338 preparenondet interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 803 extend-notresign interchangeable / 350 extendonce item 2 非 nil interchangeable / 350 extendonce item 3 一份扩展 interchangeable，也不是已经一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事 bundled（350 item 1 余量） interchangeable / 350 extendonce item 1 interchangeable，也不是已经能再签一张（本页第一件事） interchangeable。**  
   官方写：看见有一张票，不是已经是扩展。看见广播了一张 Precommit，不是已经 is-extension interchangeable——本页钉 not already is-extension 单句。看见这一轮有票，不是已经能再签一张（本页第一件事） interchangeable——三件事分开钉。350 extendonce vs round bundled unbundling 在本页 item 1 启动。

3. **看见还能换轮 / 看见又能进下一轮 / 看见轮次还能走 is not already 已经这一轮能再出一张 interchangeable / 已经 re-emit interchangeable / 已经本轮再出交差 interchangeable / 350 extendonce bundled interchangeable / 34 voteext interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 803 extend-notresign interchangeable / 350 extendonce item 2 / 350 extendonce item 3，也不是已经一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事 bundled（350 item 1 余量） interchangeable / 350 extendonce item 1 interchangeable，也不是已经能再签一张（本页第一件事） interchangeable / 已经是扩展本身（本页第二件事） interchangeable。**  
   官方写：看见还能换轮，不是这一轮已经能再出一张。看见又能进下一轮，不是已经 re-emit interchangeable——本页钉 not already re-emit 单句。看见轮次还能走，不是已经是扩展本身（本页第二件事） interchangeable——三件事分开钉。350 extendonce vs round bundled unbundling 在本页 item 1 启动。

怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份是规范里的做法，本页不抄。一轮一份扩展 bundled（350）、ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票（350 item 2 余量 / 804）、一轮只能交出一份扩展不是已经是每一高度一份（350 item 3 余量 / 805）、验签拒收整张预提交就已经是块非法（34）、同一块已经是同一份扩展（338）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）是另外那套，本页不抄。

## 官方为什么这样拆

- **一轮最多一张 Precommit not already resign ≠ 350 / 34 interchangeable：** 官方把到了 Precommit 步和已经能再签一张分开。
- **有一张票 not already is-extension ≠ 已经是扩展本身 interchangeable：** 官方把有一张票和已经是扩展本身分开。
- **还能换轮 not already re-emit ≠ 已经这一轮能再出一张 interchangeable：** 官方把还能换轮和这一轮已经能再出一张分开；350 extendonce vs round bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一轮最多一张 Precommit | 不是 already resign | 不是验签拒收整张预提交就已经是块非法 alone（34） |
| 有一张票 | 不是 already is-extension | 不是 ExtendVote 非 nil 才叫 alone（804） |
| 还能换轮 | 不是 already re-emit | 不是一轮一份扩展 already per-height alone（805） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事（350 余量），必须分开一轮最多一张 Precommit 是不是 already resign interchangeable / 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable、有一张票 是不是 already is-extension interchangeable、还能换轮 是不是 already re-emit interchangeable。可以跳过「看见到了 Precommit 就已经能再签一张 interchangeable / 就已经是扩展 interchangeable / 就已经能再出一张 interchangeable」。不要另写怎样写 ExtendVote。350 extendonce vs round bundled unbundling 在本页 item 1 启动；续 [`worked-example-extend-notnil-vs-bundled.md`](worked-example-extend-notnil-vs-bundled.md)（不变量 804 item 2）；完成见 805。

## 本页不抄

- 怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份。
- 一轮一份扩展 bundled。那是不变量 350。
- ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票。那是不变量 350 item 2 余量 / 804。
- 一轮只能交出一份扩展不是已经是每一高度一份。那是不变量 350 item 3 余量 / 805。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 同一块已经是同一份扩展。那是不变量 338。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
