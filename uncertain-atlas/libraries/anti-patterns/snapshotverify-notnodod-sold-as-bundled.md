# 反模式：把封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事（332 余量）说成已经没有快照 DoS / 已经是过滤已经收下 / 已经能挡所有有害快照

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[封禁邻居 not already no-snapshot-dos ≠ bundled（332）](../../tracks/implementation/worked-example-snapshotverify-notnodod-vs-bundled.md)。

## 卖法

把让引擎封禁邻居 / 封禁了 / 应用让 CometBFT 封禁 写成已经没有快照 DoS interchangeable / 已经 no-snapshot-dos interchangeable / 已经没有有害快照交差 interchangeable / 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable；把配了受信邻居名单 / P2P 只信一份 / 受信名单 写成已经是过滤已经收下 interchangeable / 已经 trusted-list-is-accept interchangeable；把能挡一家 / 封禁了一家 / 挡住这份有害快照 写成已经能挡所有有害快照 interchangeable / 已经 blocks-all-bad interchangeable，或已经和 332 snapshotverify bundled / snapshotverify-sold-as-early interchangeable / 754 snapshotverify-notnodod interchangeable。

## 为什么错

官方把封禁邻居单句、already no-snapshot-dos、already trusted-list-is-accept、already blocks-all-bad 写成三件独立的实现事。把它们卖成 already no-snapshot-dos interchangeable / already trusted-list-is-accept interchangeable / already blocks-all-bad interchangeable，会把 not already no-snapshot-dos、not already trusted-list-is-accept、not already blocks-all-bad 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事（332 余量），必须分开 not already no-snapshot-dos、not already trusted-list-is-accept、not already blocks-all-bad 三件事，不要和 332 / 33 / 326 / 752 / 753 糊成一句。

## 和相邻反模式

- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是 Snapshot Verification bundled 全段，不是本页封禁邻居 item 3 单句边界。
- [snapshotverify-notduringrestore-sold-as-bundled](snapshotverify-notduringrestore-sold-as-bundled.md) 是装完又对上 item 1，不是本页快照 DoS 边界。
- [snapshotverify-notuniqueapphash-sold-as-bundled](snapshotverify-notuniqueapphash-sold-as-bundled.md) 是唯一可信 AppHash item 2，不是本页封禁边界。
- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是发了 addr 过滤查询 ≠ 已经收下这个人（326），不是本页受信名单单句边界。
