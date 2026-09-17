# 例：看见 Finalize 改了状态 is not already persisted interchangeable / not already Commit interchangeable / not already settled interchangeable

**层次**：实现 / Finalize 改了状态 not already persisted / not already Commit / not already settled 正式三事（335 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 改了状态 not already persisted / not already Commit / not already settled 正式三事（335 余量）/ not 902 finalize-persist-notdisk interchangeable / not 335 finalize-persist-vs-commit bundled interchangeable」，不是 Finalize 落盘禁令 bundled（335），也不是 persist decision 已经 executes block v（478/605），也不是崩溃恢复三步已经交差（320）。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

1. **看见 `FinalizeBlock` 改了状态 / 看见决定块已经交给应用 这份转移 is not already 已经落盘 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 902 finalize-persist-notdisk interchangeable / 903 finalize-persist-notfin interchangeable / 335 finalize-persist item 2 Commit 落盘 interchangeable，也不是已经 Finalize 改了状态 not already persisted / not already Commit / not already settled 正式三事 bundled（335 item 1 余量） interchangeable / 335 finalize-persist item 1 interchangeable。**  
   官方写：共识算法决定一块之后，CometBFT 用 `FinalizeBlock` 把决定块交给应用，应用用它转移状态，但 MUST NOT 持久化。看见改了状态，不是已经写盘 interchangeable——本页从 335 item 1 侧钉 not already persisted 单句。335 finalize-persist vs commit bundled unbundling 在本页 item 1 启动。

2. **看见决定块来了 / 看见能转移 / 这份转移 is not already 已经 Commit interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 902 finalize-persist-notdisk interchangeable / 335 finalize-persist item 3 记住高度 interchangeable / 904 finalize-persist-notskip interchangeable，也不是已经 persist decision 已经 executes block v interchangeable / 478 / 605 finpersist-notpersist interchangeable。**  
   官方把决定块来了和已经 Commit 分开——335 bundled 第一件事常与 478 混成「看见 Finalize 改了就已经落盘或已经是 persist decision 那句 interchangeable」，本页钉 not already Commit 单句。

3. **看见能转移 / 看见改了状态 / 这份转移 is not already 已经交差 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 902 finalize-persist-notdisk interchangeable / 903 finalize-persist-notfin interchangeable，也不是已经半写已经原子 interchangeable / 5 half-write interchangeable。**  
   官方把能转移和已经和半写已经原子同一句 / 已经交差分开。看见能转移，不是已经交差 interchangeable。335 finalize-persist vs commit bundled unbundling 在本页 item 1 启动。

怎样落盘、怎样写 `Commit`、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Finalize 改了状态 not already persisted ≠ 已经落盘 interchangeable：** 官方把转移状态和禁止在 Finalize 持久化分开。
- **看见决定块来了 not already Commit ≠ 已经 Commit interchangeable：** 官方把决定块交给应用和已经 Commit 分开。
- **看见能转移 not already settled ≠ 已经交差 interchangeable：** 官方把能转移和已经交差分开；335 finalize-persist vs commit bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 改了状态 | 不是已经落盘 | 不是 persist decision 已经 executes block v（478/605） |
| 看见决定块来了 | 不是已经 Commit | 不是崩溃恢复三步已经交差（320） |
| 看见能转移 | 不是已经交差 | 不是必须在 Commit 落盘就已经在 Finalize 落了（903） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 改了状态 not already persisted / not already Commit / not already settled 正式三事（335 余量），必须分开是不是已经落盘、是不是已经 Commit、是不是已经交差。可以跳过「看见 Finalize 改了就已经交差」。不要把造出 s_h 当已经落盘。不要另写怎样落盘或怎样写 Commit。335 finalize-persist vs commit bundled unbundling 在本页 item 1 启动；续 [`worked-example-finalize-persist-notfin-vs-bundled.md`](worked-example-finalize-persist-notfin-vs-bundled.md)（不变量 903 item 2）。

## 本页不抄

- 怎样落盘、怎样写 `Commit`、怎样做 WAL 旋转。
- Finalize 落盘禁令 bundled。那是不变量 335。
- 必须在 Commit 落盘就已经在 Finalize 落了。那是不变量 335 item 2 余量 / 903。
- persist decision 已经 executes block v。那是不变量 478 / 605。
- 崩溃恢复三步已经交差。那是不变量 320。
- 半写已经原子。那是不变量 5。
