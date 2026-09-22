# 例：看见正确进程在一轮 r、高度 h 只能交出一份扩展 / 看见交了一份 / 看见又能换一轮 is not already already per-height interchangeable / already re-extend-round interchangeable / already req6-accept interchangeable

**层次**：实现 / 一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事（350 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事（350 余量）/ not 805 extend-notperheight interchangeable / not 350 extendonce bundled interchangeable」，不是一轮一份扩展 bundled（350），也不是一轮最多一张 Precommit 不是已经能再签一张（803 item 1 余量）或 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票（804 item 2 余量）。不要另写怎样写 ExtendVote。

## 官方三件事

规范把 Requirements 里正确进程在一轮 *r*、高度 *h* 只能交出一份扩展、交了一份 和「已经是交了一份就已经是每一高度一份 interchangeable / 已经是又能换一轮就已经这一轮能再交一份 interchangeable / 已经是交出来了就已经是 348 必须 Verify Accept interchangeable / 已经是 extendonce bundled interchangeable」分开写成三件独立的实现事，不是「看见交了一份就已经是每一高度一份 interchangeable / 就已经能再交一份 interchangeable / 就已经是必须 Accept interchangeable」一件事：

1. **看见正确进程在一轮 *r*、高度 *h* 只能交出一份扩展 / 看见交了一份 / 看见交出扩展 is not already 已经是每一高度一份 interchangeable / 已经 per-height interchangeable / 已经每高一份交差 interchangeable / 350 extendonce bundled interchangeable / 348 req6coherence interchangeable / extendonce-sold-as-height interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 805 extend-notperheight interchangeable / 350 extendonce item 3 interchangeable，也不是已经一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事 bundled（350 item 3 余量） interchangeable / 350 extendonce item 3 interchangeable，也不是已经一轮最多一张 Precommit（803） interchangeable / 804 extend-notnil interchangeable / 34 voteext interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable。**  
   官方写：因此正确进程在一轮 *r*、高度 *h* 只能交出一份扩展。看见交了一份，不是这一高度已经只能有一份。看见交了一份，不是已经 per-height interchangeable——350 钉 bundled 三事，本页从 item 3 侧钉 not already per-height 单句。看见正确进程在一轮 *r*、高度 *h* 只能交出一份扩展，不是已经一轮一份扩展 bundled（350） interchangeable——350 钉 bundled，本页钉 item 3 第一件事。看见交了一份，不是已经一轮最多一张 Precommit（803） interchangeable——803 另钉 item 1。看见交了一份，不是已经 ExtendVote 非 nil 才叫（804） interchangeable——804 另钉 item 2。350 extendonce vs round bundled unbundling 在本页 item 3 完成。

2. **看见又能换一轮 / 看见又能进下一轮 / 看见轮次还能走 is not already 已经这一轮能再交一份 interchangeable / 已经 re-extend-round interchangeable / 已经本轮再交交差 interchangeable / 350 extendonce bundled interchangeable / 34 voteext interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 805 extend-notperheight interchangeable / 350 extendonce item 1 再签 interchangeable / 350 extendonce item 2 非 nil interchangeable，也不是已经一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事 bundled（350 item 3 余量） interchangeable / 350 extendonce item 3 interchangeable，也不是已经是每一高度一份（本页第一件事） interchangeable。**  
   官方写：看见又能换一轮，不是这一轮已经能再交一份。看见又能进下一轮，不是已经 re-extend-round interchangeable——本页钉 not already re-extend-round 单句。看见轮次还能走，不是已经是每一高度一份（本页第一件事） interchangeable——三件事分开钉。350 extendonce vs round bundled unbundling 在本页 item 3 完成。

3. **看见交出来了 / 看见扩展交出来了 / 看见正确进程交出扩展 is not already 已经是 348 那种必须被 Verify Accept interchangeable / 已经 req6-accept interchangeable / 已经必须 Accept 交差 interchangeable / 350 extendonce bundled interchangeable / 348 req6coherence-sold-as-accept interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 805 extend-notperheight interchangeable / 350 extendonce item 1 / 350 extendonce item 2，也不是已经一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事 bundled（350 item 3 余量） interchangeable / 350 extendonce item 3 interchangeable，也不是已经是每一高度一份（本页第一件事） interchangeable / 已经这一轮能再交一份（本页第二件事） interchangeable。**  
   官方写：看见交出来了，不是已经是 348 那种必须被 Verify Accept。看见扩展交出来了，不是已经 req6-accept interchangeable——本页钉 not already req6-accept 单句。看见正确进程交出扩展，不是已经这一轮能再交一份（本页第二件事） interchangeable——三件事分开钉。350 extendonce vs round bundled unbundling 在本页 item 3 完成。

怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份是规范里的做法，本页不抄。一轮一份扩展 bundled（350）、一轮最多一张 Precommit 不是已经能再签一张（350 item 1 余量 / 803）、ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票（350 item 2 余量 / 804）、验签拒收整张预提交就已经是块非法（34）、同一块已经是同一份扩展（338）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）、Process 也会在提议者那边叫（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **一轮只能交出一份扩展 not already per-height ≠ 350 / 348 interchangeable：** 官方把交了一份和已经是每一高度一份分开。
- **又能换一轮 not already re-extend-round ≠ 已经这一轮能再交一份 interchangeable：** 官方把又能换一轮和这一轮已经能再交一份分开。
- **交出来了 not already req6-accept ≠ 已经是 348 必须 Accept interchangeable：** 官方把交出来了和已经是 Req 6 必须 Verify Accept 分开；350 extendonce vs round bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一轮只能交出一份扩展 | 不是 already per-height | 不是正确进程交出的扩展必须被正确接收者 Verify Accept alone（348） |
| 又能换一轮 | 不是 already re-extend-round | 不是一轮最多一张 already resign alone（803） |
| 交出来了 | 不是 already req6-accept | 不是 ExtendVote 非 nil 才叫 alone（804） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事（350 余量），必须分开一轮只能交出一份扩展 是不是 already per-height interchangeable / 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable、又能换一轮 是不是 already re-extend-round interchangeable、交出来了 是不是 already req6-accept interchangeable。可以跳过「看见交了一份就已经是每一高度一份 interchangeable / 就已经能再交一份 interchangeable / 就已经是必须 Accept interchangeable」。不要另写怎样写 ExtendVote。350 extendonce vs round bundled unbundling 在本页 item 3 完成（803 + 804 + 805）。

## 本页不抄

- 怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份。
- 一轮一份扩展 bundled。那是不变量 350。
- 一轮最多一张 Precommit 不是已经能再签一张。那是不变量 350 item 1 余量 / 803。
- ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票。那是不变量 350 item 2 余量 / 804。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 同一块已经是同一份扩展。那是不变量 338。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- Process 也会在提议者那边叫。那是不变量 351。
