# 反模式：把 blockstore not already settled / not already Commit / not three steps already atomic 正式三事（320 余量）说成已经交差 / 已经 Commit / 已经原子

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[blockstore not already settled ≠ bundled（320）](../../tracks/implementation/worked-example-crashsteps-notblockstore-vs-bundled.md)。

## 卖法

把块已经进 blockstore / 块存了 / block_stored 写成已经交差 interchangeable / 已经 settled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 320 crashsteps bundled interchangeable；把 Finalize 结果已经落盘 / CometBFT 存下 FinalizeBlockResponse / state_stored 写成已经 Commit interchangeable / 已经应用已经提交 interchangeable / 684 finpersist-notmustincommit interchangeable / 335 finpersist bundled interchangeable / 481 commitpersist interchangeable；把三步 / 块进 store + 结果落盘 + Commit 写成已经原子 interchangeable / 5 half-write atomic interchangeable / 298 wal-fsync interchangeable，或已经和 320 crashsteps bundled / crashsteps-sold-as-committed interchangeable / 687 crashsteps-notblockstore interchangeable。

## 为什么错

官方把 Crash Recovery 三步里块进 store 单句、already settled、already Commit、three steps already atomic（5）写成三件独立的实现事。把它们卖成 already settled interchangeable / already Commit interchangeable / three steps already atomic interchangeable，会把 not already settled、not already Commit、not three steps already atomic 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 blockstore not already settled / not already Commit / not three steps already atomic 正式三事（320 余量），必须分开 not already settled、not already Commit、not three steps already atomic 三件事，不要和 320 / 33 / 403 / 684 / 335 / 5 / 298 / 686 糊成一句。

## 和相邻反模式

- [crashsteps-notapptaller-sold-as-bundled](crashsteps-notapptaller-sold-as-bundled.md) 是 app taller than engine vs already allowed（320 item 1 余量 / 686），不是本页 blockstore item 2 单句边界。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是 Crash Recovery 三步 bundled 全段，不是本页块进 store item 2 单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 FinalizeBlock 落盘禁令 bundled，不是本页 Crash Recovery 三步中间一步边界。
