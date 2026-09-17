# 例：看见一轮最多一张 Precommit is not already can sign another interchangeable / not already is the extension interchangeable / not already settled interchangeable

**层次**：实现 / 一轮最多一张 Precommit not already can sign another / not already is the extension / not already settled 正式三事（350 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「一轮最多一张 Precommit not already can sign another / not already is the extension / not already settled 正式三事（350 余量）/ not 863 extend-once-notresign interchangeable / not 350 extend-once-vs-round bundled interchangeable」，不是一轮一份扩展 bundled（350），也不是验签拒收整张预提交就已经是块非法（34），也不是 Process 也会在提议者那边叫（351/860）。不要另写怎样写 ExtendVote。

## 官方三件事

1. **看见正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit / 看见到了 Precommit 步 这份一张 is not already 已经能再签一张 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 863 extend-once-notresign interchangeable / 864 extend-once-notnil interchangeable / 350 extend-once item 2 才叫 interchangeable，也不是已经一轮最多一张 Precommit not already can sign another / not already is the extension / not already settled 正式三事 bundled（350 item 1 余量） interchangeable / 350 extend-once item 1 interchangeable。**  
   官方写：按 CometBFT 现在采用的 Tendermint 共识，正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit。看见到了这一步，不是已经能再签一张 interchangeable——本页从 350 item 1 侧钉 not already can sign another 单句。350 extend-once vs round bundled unbundling 在本页 item 1 启动。

2. **看见到了 Precommit 步 / 看见有一张票 / 这份一张 is not already 已经是扩展本身 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 863 extend-once-notresign interchangeable / 350 extend-once item 3 一份扩展 interchangeable / 865 extend-once-notperheight interchangeable，也不是已经验签拒收整张预提交就已经是块非法 interchangeable / 34 voteext interchangeable。**  
   官方把有一张票和已经是扩展本身分开——350 bundled 第一件事常与 34 混成「看见到了 Precommit 就已经能再签一张或已经是扩展 interchangeable」，本页钉 not already is the extension 单句。

3. **看见到了 Precommit 步 / 看见还能换轮 / 这份一张 is not already 已经交差 interchangeable，也不是已经一轮一份扩展 bundled（350） interchangeable / 863 extend-once-notresign interchangeable / 864 extend-once-notnil interchangeable，也不是已经 Process 也会在提议者那边叫 interchangeable / 351 process-also / 860 process-also-notskip interchangeable。**  
   官方把还能换轮和已经交差分开。看见还能换轮，不是这一轮已经能再出一张 interchangeable。350 extend-once vs round bundled unbundling 在本页 item 1 启动。

怎样写 ExtendVote、怎样选空扩展、怎样测一轮一份是规范里的做法，本页不抄。

## 官方为什么这样拆

- **一轮最多一张 Precommit not already can sign another ≠ 已经能再签一张 interchangeable：** 官方把正确进程一轮最多一张 Precommit 和还能不能再签分开。
- **看见有一张票 not already is the extension ≠ 已经是扩展本身 interchangeable：** 官方把有一张票和已经是扩展本身分开。
- **看见还能换轮 not already settled ≠ 已经交差 interchangeable：** 官方把还能换轮和已经交差分开；350 extend-once vs round bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一轮最多一张 Precommit | 不是已经能再签一张 | 不是验签拒收整张预提交就已经是块非法（34） |
| 看见有一张票 | 不是已经是扩展本身 | 不是同一块已经是同一份扩展（338） |
| 看见还能换轮 | 不是已经交差 | 不是 Process 也会在提议者那边叫（351/860） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮最多一张 Precommit not already can sign another / not already is the extension / not already settled 正式三事（350 余量），必须分开是不是已经能再签一张、是不是已经是扩展本身、是不是已经交差。可以跳过「看见到了 Precommit 就已经能再签一张」。不要另写怎样写 ExtendVote。350 extend-once vs round bundled unbundling 在本页 item 1 启动；续 [`worked-example-extend-once-notnil-vs-bundled.md`](worked-example-extend-once-notnil-vs-bundled.md)（不变量 864 item 2）。

## 本页不抄

- 怎样写 ExtendVote、怎样选空扩展、怎样测一轮一份。
- 一轮一份扩展 bundled。那是不变量 350。
- ExtendVote 只在即将广播非 nil Precommit 时才叫。那是不变量 350 item 2 余量 / 864。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- Process 也会在提议者那边叫。那是不变量 351 / 860。
