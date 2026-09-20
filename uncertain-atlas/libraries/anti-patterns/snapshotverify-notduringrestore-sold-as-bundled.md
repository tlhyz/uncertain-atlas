# 反模式：把装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事（332 余量）说成已经在装回当中验过 / 已经进了网 / 已经切进共识

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[装完又对上 not already incremental-verified ≠ bundled（332）](../../tracks/implementation/worked-example-snapshotverify-notduringrestore-vs-bundled.md)。

## 卖法

把装完又叫了 Info / LastBlockAppHash 对上轻客户端那份 / 装完又对上 写成已经在装回当中增量验过 interchangeable / 已经 incremental-verified interchangeable / 已经装回当中验过交差 interchangeable / 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable；把 Info 绿了 / 进网前核对绿了 / 应用有效确认 写成已经进了网 interchangeable / 已经 in-network interchangeable；把高度对上 / LastBlockHeight 对上 / 快照高度对上 写成已经切进共识 interchangeable / 已经 consensus-entered interchangeable，或已经和 332 snapshotverify bundled / snapshotverify-sold-as-early interchangeable / 752 snapshotverify-notduringrestore interchangeable。

## 为什么错

官方把装完又对上单句、already incremental-verified、already in-network、already consensus-entered 写成三件独立的实现事。把它们卖成 already incremental-verified interchangeable / already in-network interchangeable / already consensus-entered interchangeable，会把 not already incremental-verified、not already in-network、not already consensus-entered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事（332 余量），必须分开 not already incremental-verified、not already in-network、not already consensus-entered 三件事，不要和 332 / 33 / 321 / 323 / 38 / 753 / 754 糊成一句。

## 和相邻反模式

- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是 Snapshot Verification bundled 全段，不是本页装完又对上 item 1 单句边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下 ≠ 已经装完（321），不是本页进网前核对边界。
- [snapshotverify-notuniqueapphash-sold-as-bundled](snapshotverify-notuniqueapphash-sold-as-bundled.md) 是唯一可信 AppHash（332 item 2），不是本页装完又对上 item 1 单句边界。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是装完 ≠ 已经有完整历史（323），不是本页高度对上单句边界。
