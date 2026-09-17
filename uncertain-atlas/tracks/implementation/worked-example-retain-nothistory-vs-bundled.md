# 例：看见低于这个高度的块可以被删 is not already no history interchangeable / not already snapshot truncated interchangeable / not already deleted interchangeable

**层次**：实现 / 低于这个高度可删 not already no history / not already snapshot truncated / not already deleted 正式三事（366 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「低于这个高度可删 not already no history / not already snapshot truncated / not already deleted 正式三事（366 余量）/ not 828 retain-nothistory interchangeable / not 366 retain-vs-kept bundled interchangeable」，不是 Commit 保留高度 bundled（366），也不是切进共识就已经有完整历史（323），也不是 Commit Usage retain_height caution Historical blocks（491/694），也不是崩溃三步就已经 Commit（320）。不要另写怎样写 Commit 保留高度。

## 官方三件事

1. **看见低于这个高度的块可以被删 / 看见回了高度 / 这份可删 is not already 已经没有历史 interchangeable / 323 history interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 828 retain-nothistory interchangeable / 827 retain-notpruning interchangeable / 366 retain item 1 默认 0 interchangeable，也不是已经低于这个高度可删 not already no history / not already snapshot truncated / not already deleted 正式三事 bundled（366 item 2 余量） interchangeable / 366 retain item 2 interchangeable。**  
   官方写：低于这个高度的块可以被删。看见回了高度，不是已经没有历史 interchangeable——本页从 366 item 2 侧钉 not already no history 单句。366 retain vs kept bundled unbundling 在本页 item 2 续。

2. **看见回了高度 / 看见能删 / 这份可删 is not already 已经是这个节点快照截断 interchangeable / 323 history interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 828 retain-nothistory interchangeable / 366 retain item 3 永久丢 interchangeable / 829 retain-notgenesis interchangeable，也不是已经切进共识就已经有完整历史 interchangeable / 323 history interchangeable，也不是已经 Commit Usage retain_height caution Historical blocks interchangeable / 491 retaincaution / 694 commitretaincaution-nothistorical interchangeable。**  
   官方把能删和已经是快照截断分开——366 bundled 第二件事常与 323 / 491 混成「看见回了高度就已经没有历史或已经是快照截断 interchangeable」，本页钉 not already snapshot truncated 单句。

3. **看见回了高度 / 看见能剪 / 这份可删 is not already 已经删完 interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 828 retain-nothistory interchangeable / 827 retain-notpruning interchangeable。**  
   官方把能剪和已经删完分开。看见能剪，不是已经删完 interchangeable。366 retain vs kept bundled unbundling 在本页 item 2 续。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **低于这个高度可删 not already no history ≠ 323 interchangeable：** 官方把可以删和已经没有历史分开。
- **看见能删 not already snapshot truncated ≠ 已经是快照截断 interchangeable：** 官方把能删和已经是快照截断分开。
- **看见能剪 not already deleted ≠ 已经删完 interchangeable：** 官方把能剪和已经删完分开；366 retain vs kept bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 低于这个高度的块可以被删 | 不是已经没有历史（323） | 不是默认 0（827/366 item 1） |
| 看见能删 | 不是已经是快照截断 | 不是 retain_height caution Historical blocks（491/694） |
| 看见能剪 | 不是已经删完 | 不是崩溃三步就已经 Commit（320） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看低于这个高度可删 not already no history / not already snapshot truncated / not already deleted 正式三事（366 余量），必须分开是不是已经没有历史 interchangeable / 323、是不是已经是快照截断、是不是已经删完。可以跳过「看见回了高度就已经没有历史」。不要另写怎样写 Commit 保留高度。366 retain vs kept bundled unbundling 在本页 item 2 续；续 [`worked-example-retain-notgenesis-vs-bundled.md`](worked-example-retain-notgenesis-vs-bundled.md)（不变量 829 item 3）。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit 保留高度 bundled。那是不变量 366。
- retain_height 默认 0。那是不变量 366 item 1 余量 / 827。
- 切进共识就已经有完整历史。那是不变量 323。
- Commit Usage retain_height caution Historical blocks。那是不变量 491 / 694。
