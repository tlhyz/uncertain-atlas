# 例：看见一轮只能交出一份扩展 is not already one per height interchangeable / not already must Accept interchangeable / not already settled interchangeable

**层次**：实现 / 一轮只能交出一份扩展 not already one per height / not already must Accept / not already settled 正式三事（350 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「一轮只能交出一份扩展 not already one per height / not already must Accept / not already settled 正式三事（350 余量）/ not 865 extend-once-notperheight interchangeable / not 350 extend-once-vs-round bundled interchangeable」，不是一轮一份扩展 bundled（350），也不是正确进程交出的扩展必须被正确接收者 Verify Accept（348），也不是同一块已经是同一份扩展（338）。不要另写怎样写 ExtendVote。

## 官方三件事

1. **看见正确进程在一轮 *r*、高度 *h* 只能交出一份扩展 / 看见交了一份 这份一份 is not already 已经是每一高度一份 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 865 extend-once-notperheight interchangeable / 863 extend-once-notresign interchangeable / 350 extend-once item 1 一张 interchangeable，也不是已经一轮只能交出一份扩展 not already one per height / not already must Accept / not already settled 正式三事 bundled（350 item 3 余量） interchangeable / 350 extend-once item 3 interchangeable。**  
   官方写：因此正确进程在一轮 *r*、高度 *h* 只能交出一份扩展。看见交了一份，不是这一高度已经只能有一份 interchangeable——本页从 350 item 3 侧钉 not already one per height 单句。350 extend-once vs round bundled unbundling 在本页 item 3 完成。

2. **看见交了一份 / 看见交出来了 / 这份一份 is not already 已经是正确进程交出的扩展必须被正确接收者 Verify Accept interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 865 extend-once-notperheight interchangeable / 350 extend-once item 2 才叫 interchangeable / 864 extend-once-notnil interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept interchangeable / 348 req6 interchangeable。**  
   官方把交出来了和已经是 Req 6 必须 Accept 分开——350 bundled 第三件事常与 348 混成「看见交了一份就已经是每一高度一份或已经必须 Accept interchangeable」，本页钉 not already must Accept 单句。

3. **看见交了一份 / 看见又能换一轮 / 这份一份 is not already 已经交差 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 865 extend-once-notperheight interchangeable / 863 extend-once-notresign interchangeable，也不是已经同一块已经是同一份扩展 interchangeable / 338 samedext interchangeable。**  
   官方把又能换一轮和已经交差分开。看见又能换一轮，不是这一轮已经能再交一份 interchangeable。350 extend-once vs round bundled unbundling 在本页 item 3 完成。

怎样写 ExtendVote、怎样选空扩展、怎样测一轮一份是规范里的做法，本页不抄。

## 官方为什么这样拆

- **一轮只能交出一份扩展 not already one per height ≠ 已经是每一高度一份 interchangeable：** 官方把一轮一份和每一高度一份分开。
- **看见交出来了 not already must Accept ≠ 已经是 Req 6 必须 Accept interchangeable：** 官方把交出来了和已经必须 Accept 分开。
- **看见又能换一轮 not already settled ≠ 已经交差 interchangeable：** 官方把又能换一轮和已经交差分开；350 extend-once vs round bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一轮只能交出一份扩展 | 不是已经是每一高度一份 | 不是正确进程交出的扩展必须被正确接收者 Verify Accept（348） |
| 看见交出来了 | 不是已经必须 Accept | 不是同一块已经是同一份扩展（338） |
| 看见又能换一轮 | 不是已经交差 | 不是一轮最多一张就已经能再签（863） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮只能交出一份扩展 not already one per height / not already must Accept / not already settled 正式三事（350 余量），必须分开是不是已经是每一高度一份、是不是已经必须 Accept、是不是已经交差。可以跳过「看见交了一份就已经是每一高度一份」。不要另写怎样写 ExtendVote。350 extend-once vs round bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendVote、怎样选空扩展、怎样测一轮一份。
- 一轮一份扩展 bundled。那是不变量 350。
- 一轮最多一张 Precommit。那是不变量 350 item 1 余量 / 863。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- 同一块已经是同一份扩展。那是不变量 338。
