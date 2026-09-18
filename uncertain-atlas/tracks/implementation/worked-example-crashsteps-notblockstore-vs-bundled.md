# 例：看见块进 blockstore / Finalize 结果落盘 is not already already settled interchangeable / already Commit interchangeable / three steps already atomic interchangeable

**层次**：实现 / blockstore not already settled / not already Commit / not three steps already atomic 正式三事（320 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「blockstore not already settled / not already Commit / not three steps already atomic 正式三事（320 余量）/ not 687 crashsteps-notblockstore interchangeable / not 320 crashsteps bundled interchangeable」，不是 Crash Recovery 三步 bundled（320），也不是 app taller than engine（686 item 1 余量）或启动 Info 对上不是已经能跳步（688 item 3 余量）。不要另写怎样落盘、怎样写 Commit、怎样做 WAL 旋转。

## 官方三件事

规范把 Crash Recovery 里一个高度算持久化要走三步、最后一步才是应用的 `Commit`、也是应用**唯一**被指望持久化/提交自己状态的地方 和「已经是块进 store 就已经交差 interchangeable / 已经是 Finalize 结果落了就已经 Commit interchangeable / 已经是三步就已经原子 interchangeable / 已经是崩溃恢复三步已经交差 interchangeable」分开写成三件独立的实现事，不是「看见块进了 store 就已经交差 interchangeable / 就已经 Commit interchangeable / 就已经原子 interchangeable」一件事：

1. **看见块已经进 blockstore / 看见块存了 / 看见第一步 block_stored is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经 Finalize + Commit interchangeable / 33 four gates interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 320 crashsteps bundled interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 687 crashsteps-notblockstore interchangeable / 320 crashsteps item 2 interchangeable，也不是已经 blockstore not already settled / not already Commit / not three steps already atomic 正式三事 bundled（320 item 2 余量） interchangeable / 320 crashsteps item 2 interchangeable，也不是已经 app taller than engine（686） interchangeable / 688 crashsteps-notinfoskip interchangeable / 5 half-write atomic interchangeable，也不是已经崩溃恢复三步已经交差（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方 Crash Recovery 写：一个高度算持久化，要走三步，最后一步才是应用的 `Commit`。三步是：块进 blockstore；CometBFT 存下 `FinalizeBlockResponse` 回的状态；应用在 `Commit` 里提交。看见块存了，不是已经交差 interchangeable——320 钉 bundled 三事，本页从 item 2 侧钉 not already settled 单句。看见 block_stored，不是已经 app taller than engine（686） interchangeable——686 钉 item 1 不许领先，本页钉块进 store 单句。看见块进了 store，不是已经崩溃恢复三步已经交差（320） interchangeable——320 钉 bundled，本页钉 item 2 第一件事。320 crash recovery bundled unbundling 在本页 item 2 启动。

2. **看见 Finalize 结果已经落盘 / 看见 CometBFT 存下 FinalizeBlockResponse 回的状态 / 看见 state_stored is not already 已经 Commit interchangeable / 已经应用已经提交 interchangeable / 已经应用落盘 interchangeable / 335 finpersist bundled interchangeable / 684 finpersist-notmustincommit interchangeable / 481 commitpersist interchangeable / 645 fincommit-notpersist interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 687 crashsteps-notblockstore interchangeable / 320 crashsteps item 1 app taller interchangeable / 320 crashsteps item 3 Info not skip interchangeable，也不是已经 blockstore not already settled / not already Commit / not three steps already atomic 正式三事 bundled（320 item 2 余量） interchangeable / 320 crashsteps item 2 interchangeable，也不是已经 MUST persist in Commit（684） interchangeable / 683 finpersist-notmustnot interchangeable / 680 commitpersist-notfinpersist interchangeable，也不是已经 WAL 已经 fsync（298） interchangeable / 298 wal-fsync interchangeable。**  
   官方把三步中间一步（存 Finalize 结果）和应用已经 Commit / 已经提交路径分开——320 bundled 第二件事常与「看见结果存了 就已经 Commit interchangeable / 就已经应用已经提交 interchangeable」混成一句，本页钉 not already Commit 单句。看见 Finalize 结果落盘，不是已经应用唯一落盘点已经做完（684） interchangeable——684 钉 MUST persist in Commit，本页钉 Crash Recovery 三步里中间一步单句。看见 state_stored，不是已经启动 Info 对上就已经能跳步（688） interchangeable——688 另钉 item 3，本页钉 item 2 第二件事。320 crash recovery bundled unbundling 在本页 item 2 启动。

3. **看见三步 / 看见块进 store + 结果落盘 + Commit / 看见一个高度算持久化要走三步 is not already 已经原子 interchangeable / 已经 three steps already atomic interchangeable / 5 half-write atomic interchangeable / 298 wal-fsync interchangeable / 335 finpersist bundled interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 687 crashsteps-notblockstore interchangeable / 320 crashsteps item 1 / 320 crashsteps item 3，也不是已经 blockstore not already settled / not already Commit / not three steps already atomic 正式三事 bundled（320 item 2 余量） interchangeable / 320 crashsteps item 2 interchangeable，也不是已经 app taller than engine（686） interchangeable / 685 finpersist-notrememberheight interchangeable，也不是已经崩溃恢复三步已经交差（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方把三步清单和三步就已经原子路径分开——320 bundled 第二件事常与 5 混成「看见三步 就已经原子 interchangeable / 就已经半写已经原子 interchangeable」，本页钉 not three steps already atomic 单句。看见三步，不是已经半写已经原子（5） interchangeable——5 钉半写原子，本页钉 Crash Recovery item 2 第三件事。看见块进 store + 结果 + Commit，不是已经 WAL 已经 fsync（298） interchangeable——298 另钉 WAL fsync，本页钉 item 2 第三件事。320 crash recovery bundled unbundling 在本页 item 2 完成。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的做法，本页不抄。Crash Recovery 三步 bundled（320）、app taller than engine（320 item 1 余量 / 686）、启动 Info 对上不是已经能跳步（320 item 3 余量 / 688）、半写已经原子（5）、WAL 已经 fsync（298）、MUST persist in Commit（684）、FinalizeBlock 落盘禁令 bundled（335）是另外那套，本页不抄。

## 官方为什么这样拆

- **blockstore not already settled ≠ 33 / 403 interchangeable：** 官方把块进 store 单句和已经交差 / 四门已经结算路径分开。
- **Finalize 结果落盘 not already Commit ≠ 684 / 335 interchangeable：** 官方把中间一步存结果和应用已经 Commit 路径分开。
- **三步 not three steps already atomic ≠ 5 half-write atomic interchangeable：** 官方把三步清单和三步就已经原子路径分开；320 crash recovery bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 块进 blockstore | 不是 already settled | 不是 app taller alone（686） |
| Finalize 结果落盘 | 不是 already Commit | 不是 MUST persist in Commit alone（684） |
| 三步 | 不是 three steps already atomic（5） | 不是 Info not skip alone（688） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 blockstore not already settled / not already Commit / not three steps already atomic 正式三事（320 余量），必须分开块进 store 是不是 already settled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable、Finalize 结果落盘 是不是 already Commit interchangeable / 684 finpersist-notmustincommit interchangeable / 335 finpersist bundled interchangeable、三步 是不是 already atomic interchangeable / 5 half-write atomic interchangeable / 298 wal-fsync interchangeable。可以跳过「看见块进了 store 就已经交差 interchangeable / 就已经 Commit interchangeable / 就已经原子 interchangeable」。不要另写怎样落盘。320 crash recovery bundled unbundling 在本页 item 2 完成；续 [`worked-example-crashsteps-notinfoskip-vs-bundled.md`](worked-example-crashsteps-notinfoskip-vs-bundled.md)（不变量 688 item 3）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- Crash Recovery 三步 bundled。那是不变量 320。
- app taller than engine。那是不变量 320 item 1 余量 / 686。
- 启动 Info 对上不是已经能跳步。那是不变量 320 item 3 余量 / 688。
- 半写已经原子。那是不变量 5。
- WAL 已经 fsync。那是不变量 298。
- MUST persist in Commit。那是不变量 684。
- FinalizeBlock 落盘禁令 bundled。那是不变量 335。
