# 例：看见 retain_height 默认 0 is not already pruning interchangeable / not already settled interchangeable / not already no history interchangeable

**层次**：实现 / retain_height 默认 0 not already pruning / not already settled / not already no history 正式三事（366 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「retain_height 默认 0 not already pruning / not already settled / not already no history 正式三事（366 余量）/ not 827 retain-notpruning interchangeable / not 366 retain-vs-kept bundled interchangeable」，不是 Commit 保留高度 bundled（366），也不是崩溃三步就已经 Commit（320），也不是 Commit Usage retain_height caution 默认就已经在剪（491/692），也不是 last_block 落盘就已经在剪（370/817）。不要另写怎样写 Commit 保留高度。

## 官方三件事

1. **看见 `retain_height` 默认 0、表示全留 / 看见没填 / 这份默认 is not already 已经在剪 interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 827 retain-notpruning interchangeable / 828 retain-nothistory interchangeable / 366 retain item 2 可删 interchangeable，也不是已经 retain_height 默认 0 not already pruning / not already settled / not already no history 正式三事 bundled（366 item 1 余量） interchangeable / 366 retain item 1 interchangeable。**  
   官方写：`CommitResponse.retain_height` 默认是 `0`，表示全留。看见没填，不是已经在剪 interchangeable——本页从 366 item 1 侧钉 not already pruning 单句。366 retain vs kept bundled unbundling 在本页 item 1 启动。

2. **看见没填 / 看见字段在 / 这份默认 is not already 已经交差 interchangeable / 320 crash interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 827 retain-notpruning interchangeable / 366 retain item 3 永久丢 interchangeable / 829 retain-notgenesis interchangeable，也不是已经崩溃三步就已经 Commit interchangeable / 320 crash interchangeable，也不是已经 Commit Usage retain_height caution 默认就已经在剪 interchangeable / 491 retaincaution / 692 commitretaincaution-notdefault interchangeable。**  
   官方把字段在和已经交差分开——366 bundled 第一件事常与 320 / 491 / 370 混成「看见没填就已经在剪或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见没填 / 看见 Commit 回了 / 这份默认 is not already 已经没有历史 interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 827 retain-notpruning interchangeable / 828 retain-nothistory interchangeable，也不是已经 last_block 落盘就已经在剪 interchangeable / 370 info / 817 info-notpersist interchangeable。**  
   官方把 Commit 回了和已经没有历史分开。看见 Commit 回了，不是已经没有历史 interchangeable。366 retain vs kept bundled unbundling 在本页 item 1 启动。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **retain_height 默认 0 not already pruning ≠ 已经在剪 interchangeable：** 官方把默认全留和已经在剪分开。
- **看见字段在 not already settled ≠ 已经交差 interchangeable：** 官方把字段在和已经交差分开。
- **看见 Commit 回了 not already no history ≠ 已经没有历史 interchangeable：** 官方把 Commit 回了和已经没有历史分开；366 retain vs kept bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| retain_height 默认 0 | 不是已经在剪 | 不是可删（828/366 item 2） |
| 看见字段在 | 不是已经交差 | 不是崩溃三步就已经 Commit（320） |
| 看见 Commit 回了 | 不是已经没有历史 | 不是 retain_height caution 默认（491/692） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 retain_height 默认 0 not already pruning / not already settled / not already no history 正式三事（366 余量），必须分开是不是已经在剪、是不是已经交差、是不是已经没有历史。可以跳过「看见没填就已经在剪」。不要另写怎样写 Commit 保留高度。366 retain vs kept bundled unbundling 在本页 item 1 启动；续 [`worked-example-retain-nothistory-vs-bundled.md`](worked-example-retain-nothistory-vs-bundled.md)（不变量 828 item 2）。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit 保留高度 bundled。那是不变量 366。
- 低于这个高度的块可以被删。那是不变量 366 item 2 余量 / 828。
- 崩溃三步就已经 Commit。那是不变量 320。
- Commit Usage retain_height caution 默认就已经在剪。那是不变量 491 / 692。
