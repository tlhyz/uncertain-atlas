# 模式：把 blockstore not already settled / not already Commit / not three steps already atomic 正式三事（320 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**例**：[blockstore not already settled ≠ bundled（320）](../../tracks/implementation/worked-example-crashsteps-notblockstore-vs-bundled.md)。

## 三个名字

1. **块进 blockstore 不是 already settled：** 看见块存了 / block_stored，不是已经交差 interchangeable / 已经 Finalize + Commit interchangeable，不是 33 four gates interchangeable / 403 finafter interchangeable / 320 crashsteps bundled interchangeable。

2. **Finalize 结果落盘 不是 already Commit：** 看见 CometBFT 存下 FinalizeBlockResponse / state_stored，不是已经应用已经提交 interchangeable / 已经 Commit interchangeable，不是 684 finpersist-notmustincommit interchangeable / 335 finpersist bundled interchangeable / 481 commitpersist interchangeable。

3. **三步 不是 three steps already atomic：** 看见块进 store + 结果落盘 + Commit 三步，不是已经原子 interchangeable / 已经半写已经原子 interchangeable，不是 5 half-write atomic interchangeable / 298 wal-fsync interchangeable。

官方把 Crash Recovery 三步里块进 store 单句、already settled、already Commit、three steps already atomic（5）写成三个名字。把它们叫成一个「看见块进了 store 就已经交差 interchangeable / 就已经 Commit interchangeable / 就已经原子 interchangeable」，会把 not already settled、not already Commit、not three steps already atomic 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 blockstore not already settled / not already Commit / not three steps already atomic 正式三事（320 余量），先数清问的是块进 store 是不是 already settled / 33 / 403，是不是 Finalize 结果落盘 是不是 already Commit / 684 / 335，还是三步 是不是 already atomic / 5 / 298，再决定要不要同一次发布。320 crash recovery bundled unbundling 在本页 item 2 完成。
