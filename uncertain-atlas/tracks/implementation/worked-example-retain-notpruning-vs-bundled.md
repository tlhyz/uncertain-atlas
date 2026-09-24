# 例：看见默认 0 全留 / 看见没填 / 看见字段在 is not already already pruning interchangeable / already settled interchangeable / already no-history interchangeable

**层次**：实现 / retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事（366 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事（366 余量）/ not 845 retain-notpruning interchangeable / not 366 retain bundled interchangeable」，不是 retain bundled（366），也不是低于这个高度的块可以被删不是已经没有历史（846 item 2 余量）或全网都删了会永久丢不是已经能从创世再装（847 item 3 余量）。不要另写怎样写 Commit 保留高度。

## 官方三件事

规范把 Methods 里 `CommitResponse.retain_height` 默认是 `0`、表示全留 和「已经是默认 0 全留就已经在剪 interchangeable / 已经是没填就已经交差 interchangeable / 已经是 Commit 回了就已经没有历史 interchangeable / 已经是 retain bundled interchangeable」分开写成三件独立的实现事，不是「看见默认 0 全留就已经在剪 interchangeable / 就已经交差 interchangeable / 就已经没有历史 interchangeable」一件事：

1. **看见默认 0 全留 / 看见 `retain_height` 默认是 `0`、表示全留 / 看见字段在 is not already 已经在剪 interchangeable / 已经 pruning interchangeable / 已经在剪交差 interchangeable / 366 retain bundled interchangeable / 320 crashsteps interchangeable / retain-sold-as-kept interchangeable，也不是已经 retain bundled（366） interchangeable / 845 retain-notpruning interchangeable / 366 retain item 1 interchangeable，也不是已经 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事 bundled（366 item 1 余量） interchangeable / 366 retain item 1 interchangeable，也不是已经能剪就没有历史（846） interchangeable / 847 retain-notgenesis interchangeable / 481 commitpersist interchangeable，也不是已经崩溃三步就已经 Commit（320） interchangeable。**  
   官方写：`CommitResponse.retain_height` 默认是 `0`，表示全留。看见默认 0 全留，不是已经在剪。看见默认 0 全留，不是已经 pruning interchangeable——366 钉 bundled 三事，本页从 item 1 侧钉 not already pruning 单句。看见 `retain_height` 默认是 `0`、表示全留，不是已经 retain bundled（366） interchangeable——366 钉 bundled，本页钉 item 1 第一件事。看见默认 0 全留，不是已经能剪就没有历史（846） interchangeable——846 另钉 item 2。看见默认 0 全留，不是已经全网都删能从创世再装（847） interchangeable——847 另钉 item 3。366 retain-vs-kept bundled unbundling 在本页 item 1 启动。

2. **看见没填 / 看见没填 retain_height / 看见字段在没回非零 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 366 retain bundled interchangeable / 335 finpersist interchangeable，也不是已经 retain bundled（366） interchangeable / 845 retain-notpruning interchangeable / 366 retain item 2 可删 interchangeable / 366 retain item 3 永久丢 interchangeable，也不是已经 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事 bundled（366 item 1 余量） interchangeable / 366 retain item 1 interchangeable，也不是已经在剪（本页第一件事） interchangeable。**  
   官方写：看见没填，不是已经交差。看见没填 retain_height，不是已经 settled interchangeable——本页钉 not already settled 单句。看见字段在没回非零，不是已经在剪（本页第一件事） interchangeable——三件事分开钉。366 retain-vs-kept bundled unbundling 在本页 item 1 启动。

3. **看见 Commit 回了 / 看见 Commit 回了高度 / 看见回了字段 is not already 已经没有历史 interchangeable / 已经 no-history interchangeable / 已经没有历史交差 interchangeable / 366 retain bundled interchangeable / 323 full-history interchangeable，也不是已经 retain bundled（366） interchangeable / 845 retain-notpruning interchangeable / 366 retain item 2 / 366 retain item 3，也不是已经 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事 bundled（366 item 1 余量） interchangeable / 366 retain item 1 interchangeable，也不是已经在剪（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见 Commit 回了，不是已经没有历史。看见 Commit 回了高度，不是已经 no-history interchangeable——本页钉 not already no-history 单句。看见回了字段，不是已经交差（本页第二件事） interchangeable——三件事分开钉。366 retain-vs-kept bundled unbundling 在本页 item 1 启动。

怎样填 `retain_height`、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。retain bundled（366）、低于这个高度的块可以被删不是已经没有历史（366 item 2 余量 / 846）、全网都删了会永久丢不是已经能从创世再装（366 item 3 余量 / 847）、崩溃三步就已经 Commit（320）、切进共识就已经有完整历史（323）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **默认 0 全留 not already pruning ≠ 366 / 320 interchangeable：** 官方把默认全留和已经在剪分开。
- **没填 not already settled ≠ 已经交差 interchangeable：** 官方把没填和已经交差分开。
- **Commit 回了 not already no-history ≠ 已经没有历史 interchangeable：** 官方把 Commit 回了和已经没有历史分开；366 retain-vs-kept bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 默认 0 全留 | 不是 already pruning | 不是崩溃三步就已经 Commit alone（320） |
| 没填 | 不是 already settled | 不是能删 already no-history alone（846） |
| Commit 回了 | 不是 already no-history | 不是全网都删 already genesis-replay alone（847） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事（366 余量），必须分开默认 0 全留 是不是 already pruning interchangeable / 366 retain bundled interchangeable / retain-sold-as-kept interchangeable、没填 是不是 already settled interchangeable、Commit 回了 是不是 already no-history interchangeable。可以跳过「看见默认 0 全留就已经在剪 interchangeable / 就已经交差 interchangeable / 就已经没有历史 interchangeable」。不要另写怎样写 Commit 保留高度。366 retain-vs-kept bundled unbundling 在本页 item 1 启动；完成 [`worked-example-retain-notdeleted-vs-bundled.md`](worked-example-retain-notdeleted-vs-bundled.md)（不变量 846 item 2）；完成 [`worked-example-retain-notgenesis-vs-bundled.md`](worked-example-retain-notgenesis-vs-bundled.md)（不变量 847 item 3）。

## 本页不抄

- 怎样填 `retain_height`、怎样删块、怎样开 state sync。
- retain bundled。那是不变量 366。
- 低于这个高度的块可以被删不是已经没有历史。那是不变量 366 item 2 余量 / 846。
- 全网都删了会永久丢不是已经能从创世再装。那是不变量 366 item 3 余量 / 847。
- 崩溃三步就已经 Commit。那是不变量 320。
- 切进共识就已经有完整历史。那是不变量 323。
- 应用快照就已经从创世重放。那是不变量 38。
