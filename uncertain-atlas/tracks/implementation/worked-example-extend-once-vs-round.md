# 例：看见一轮最多一张 Precommit 不是已经能再签一张；看见 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票；看见一轮只能交出一份扩展不是已经是每一高度一份

**层次**：实现 / 一轮一份扩展。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「一轮最多一张 Precommit 不是已经能再签一张 / ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票 / 一轮只能交出一份扩展不是已经是每一高度一份」，不是验签拒收整张预提交就已经是块非法，也不是正确进程交出的扩展必须被正确接收者 Verify Accept。不要另写怎样写 ExtendVote。350 extendonce vs round bundled unbundling 完成（803+804+805）；精读 [`worked-example-extend-notresign-vs-bundled.md`](worked-example-extend-notresign-vs-bundled.md)（不变量 803 item 1）；精读 [`worked-example-extend-notnil-vs-bundled.md`](worked-example-extend-notnil-vs-bundled.md)（不变量 804 item 2）；精读 [`worked-example-extend-notperheight-vs-bundled.md`](worked-example-extend-notperheight-vs-bundled.md)（不变量 805 item 3）。

## 官方三件事

规范把一轮能出几张 Precommit、何时才叫 ExtendVote、一轮能出几份扩展写成三件独立的实现事，不是「看见到了 Precommit 就已经能再签一张、已经签了 nil 票、已经是每一高度一份」一件事：

1. **看见正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit / 看见到了 Precommit 步 不是已经能再签一张，也不是已经是扩展本身。**  
   官方写：按 CometBFT 现在采用的 Tendermint 共识，正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit。看见到了这一步，不是已经能再签一张。看见有一张票，不是已经是扩展。看见还能换轮，不是这一轮已经能再出一张。
2. **看见 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫 / 看见叫了 ExtendVote 不是已经签了 nil 票，也不是每张票都会叫。**  
   官方写：Methods 里写过，`ExtendVote` 只在共识即将广播一张非 `nil` Precommit 时才叫。看见叫了 ExtendVote，不是已经在签 nil。看见启用了扩展，不是 prevote 已经会叫。看见有一张票，不是这张票已经带了扩展。
3. **看见正确进程在一轮 *r*、高度 *h* 只能交出一份扩展 / 看见交了一份 不是已经是每一高度一份，也不是已经是正确进程交出的扩展必须被正确接收者 Verify Accept。**  
   官方写：因此正确进程在一轮 *r*、高度 *h* 只能交出一份扩展。看见交了一份，不是这一高度已经只能有一份。看见又能换一轮，不是这一轮已经能再交一份。看见交出来了，不是已经是 348 那种必须被 Verify Accept。

怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份是规范里的做法，本页不抄。验签拒收整张预提交是不变量 34，本页不抄。

## 官方为什么这样拆

- **一轮最多一张 Precommit ≠ 已经能再签一张：** 官方把正确进程一轮最多一张 Precommit 和还能不能再签分开。
- **ExtendVote 只在即将广播非 nil Precommit 时才叫 ≠ 已经签了 nil 票：** 官方把何时才叫 ExtendVote 和 nil 票、prevote 分开。
- **一轮只能交出一份扩展 ≠ 已经是每一高度一份：** 官方把一轮一份和每一高度一份、Req 6 必须 Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一轮最多一张 Precommit | 不是已经能再签一张 | 不是验签拒收整张预提交就已经是块非法（34） |
| ExtendVote 只在即将广播非 nil Precommit 时才叫 | 不是已经签了 nil 票 | 不是同一块已经是同一份扩展（338） |
| 一轮只能交出一份扩展 | 不是已经是每一高度一份 | 不是正确进程交出的扩展必须被正确接收者 Verify Accept（348） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了 Precommit 就已经能再签一张、已经签了 nil 票、已经是每一高度一份」，必须分开一轮最多一张 Precommit 是不是已经能再签一张、ExtendVote 只在即将广播非 nil Precommit 时才叫是不是已经签了 nil 票、一轮只能交出一份扩展是不是已经是每一高度一份。可以跳过「看见到了 Precommit 就已经能再签一张」。不要另写怎样写 ExtendVote。350 extendonce vs round bundled unbundling 完成（803+804+805）。

## 本页不抄

- 怎样写 `ExtendVote`、怎样选空扩展、怎样测一轮一份。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 同一块已经是同一份扩展。那是不变量 338。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
