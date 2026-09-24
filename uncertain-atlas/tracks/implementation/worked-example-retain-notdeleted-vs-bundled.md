# 例：看见能删 / 看见回了高度 / 看见能剪 is not already already deleted interchangeable / already snapshot-trunc interchangeable / already no-history interchangeable

**层次**：实现 / 低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 余量）/ not 846 retain-notdeleted interchangeable / not 366 retain bundled interchangeable」，不是 retain bundled（366），也不是 retain_height 默认 0 不是已经在剪（845 item 1 余量）或全网都删了会永久丢不是已经能从创世再装（847 item 3 余量）。不要另写怎样写 Commit 保留高度。

## 官方三件事

规范把 Methods 里低于这个高度的块可以被删 和「已经是能删就已经删完 interchangeable / 已经是回了高度就已经是快照截断 interchangeable / 已经是能剪就已经没有历史 interchangeable / 已经是 retain bundled interchangeable」分开写成三件独立的实现事，不是「看见能删就已经删完 interchangeable / 就已经是快照截断 interchangeable / 就已经没有历史 interchangeable」一件事：

1. **看见能删 / 看见低于这个高度的块可以被删 / 看见回了高度可删 is not already 已经删完 interchangeable / 已经 deleted interchangeable / 已经删完交差 interchangeable / 366 retain bundled interchangeable / 323 full-history interchangeable / retain-sold-as-kept interchangeable，也不是已经 retain bundled（366） interchangeable / 846 retain-notdeleted interchangeable / 366 retain item 2 interchangeable，也不是已经低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事 bundled（366 item 2 余量） interchangeable / 366 retain item 2 interchangeable，也不是已经默认 0 全留就已经在剪（845） interchangeable / 847 retain-notgenesis interchangeable / 320 crashsteps interchangeable，也不是已经切进共识就已经有完整历史（323） interchangeable。**  
   官方写：低于这个高度的块可以被删。看见能删，不是已经删完。看见能删，不是已经 deleted interchangeable——366 钉 bundled 三事，本页从 item 2 侧钉 not already deleted 单句。看见低于这个高度的块可以被删，不是已经 retain bundled（366） interchangeable——366 钉 bundled，本页钉 item 2 第一件事。看见能删，不是已经默认 0 全留就已经在剪（845） interchangeable——845 另钉 item 1。看见能删，不是已经全网都删能从创世再装（847） interchangeable——847 另钉 item 3。366 retain-vs-kept bundled unbundling 在本页 item 2 续。

2. **看见回了高度 / 看见回了高度可删 / 看见能删 is not already 已经是这个节点快照截断 interchangeable / 已经 snapshot-trunc interchangeable / 已经快照截断交差 interchangeable / 366 retain bundled interchangeable / 323 full-history interchangeable，也不是已经 retain bundled（366） interchangeable / 846 retain-notdeleted interchangeable / 366 retain item 1 默认 0 interchangeable / 366 retain item 3 永久丢 interchangeable，也不是已经低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事 bundled（366 item 2 余量） interchangeable / 366 retain item 2 interchangeable，也不是已经删完（本页第一件事） interchangeable。**  
   官方写：看见回了高度，不是已经是这个节点快照截断。看见回了高度可删，不是已经 snapshot-trunc interchangeable——本页钉 not already snapshot-trunc 单句。看见能删，不是已经删完（本页第一件事） interchangeable——三件事分开钉。366 retain-vs-kept bundled unbundling 在本页 item 2 续。

3. **看见能剪 / 看见能删就等于能剪 / 看见低于这个高度可剪 is not already 已经没有历史 interchangeable / 已经 no-history interchangeable / 已经没有历史交差 interchangeable / 366 retain bundled interchangeable / 38 genesis-replay interchangeable，也不是已经 retain bundled（366） interchangeable / 846 retain-notdeleted interchangeable / 366 retain item 1 / 366 retain item 3，也不是已经低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事 bundled（366 item 2 余量） interchangeable / 366 retain item 2 interchangeable，也不是已经删完（本页第一件事） interchangeable / 已经是快照截断（本页第二件事） interchangeable。**  
   官方写：看见能剪，不是已经没有历史。看见能删就等于能剪，不是已经 no-history interchangeable——本页钉 not already no-history 单句。看见低于这个高度可剪，不是已经是快照截断（本页第二件事） interchangeable——三件事分开钉。366 retain-vs-kept bundled unbundling 在本页 item 2 续。

怎样填 `retain_height`、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。retain bundled（366）、retain_height 默认 0 不是已经在剪（366 item 1 余量 / 845）、全网都删了会永久丢不是已经能从创世再装（366 item 3 余量 / 847）、崩溃三步就已经 Commit（320）、切进共识就已经有完整历史（323）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **能删 not already deleted ≠ 366 / 323 interchangeable：** 官方把可以删和已经删完分开。
- **回了高度 not already snapshot-trunc ≠ 已经是快照截断 interchangeable：** 官方把回了高度和已经是快照截断分开。
- **能剪 not already no-history ≠ 已经没有历史 interchangeable：** 官方把能剪和已经没有历史分开；366 retain-vs-kept bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能删 | 不是 already deleted | 不是切进共识就已经有完整历史 alone（323） |
| 回了高度 | 不是 already snapshot-trunc | 不是默认 0 全留 already pruning alone（845） |
| 能剪 | 不是 already no-history | 不是全网都删 already genesis-replay alone（847） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 余量），必须分开能删 是不是 already deleted interchangeable / 366 retain bundled interchangeable / retain-sold-as-kept interchangeable、回了高度 是不是 already snapshot-trunc interchangeable、能剪 是不是 already no-history interchangeable。可以跳过「看见能删就已经删完 interchangeable / 就已经是快照截断 interchangeable / 就已经没有历史 interchangeable」。不要另写怎样写 Commit 保留高度。366 retain-vs-kept bundled unbundling 在本页 item 2 续。

## 本页不抄

- 怎样填 `retain_height`、怎样删块、怎样开 state sync。
- retain bundled。那是不变量 366。
- retain_height 默认 0 不是已经在剪。那是不变量 366 item 1 余量 / 845。
- 全网都删了会永久丢不是已经能从创世再装。那是不变量 366 item 3 余量 / 847。
- 崩溃三步就已经 Commit。那是不变量 320。
- 切进共识就已经有完整历史。那是不变量 323。
- 应用快照就已经从创世重放。那是不变量 38。
