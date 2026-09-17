# 反模式：把 CheckTx Usage before letting into its local mempool not tx source bundled / not mempool dedup / not Code≠0 rejected bundled 正式三事（490 余量）说成已经来源验完 / 已经去重保证 / 已经 Code≠0 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[before letting in not tx source bundled ≠ bundled（490）](../../tracks/implementation/worked-example-chktxguardusage-notsource-vs-bundled.md)。

## 卖法

把 before letting a transaction into its local mempool / 才让进本地池 写成已经 may come from external user or another node bundled 就代表来源已经验完 interchangeable / 488 chktxsource interchangeable；把看见才让进本地池写成已经内存池去重那种保证不重放 interchangeable / 313 replay interchangeable；把看见 Usage 这句写成已经 Code≠0 rejected bundled 就代表 Guardian 已经交差 interchangeable / 489 chktxcodereject interchangeable，或已经和 490 chktxguardusage-vs-optional bundled / chktxguardusage-notsource-sold-as-bundled interchangeable / 691 chktxguardusage-notsource interchangeable。

## 为什么错

官方把 CheckTx Usage 本地池入口、tx source、去重保证、Code≠0 bundled 写成三件独立的实现事。把它们卖成 tx source bundled interchangeable / mempool dedup interchangeable / Code≠0 rejected bundled interchangeable，会把 not tx source bundled、not mempool dedup、not Code≠0 rejected bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage before letting into local mempool 正式三事（490 余量），必须分开 not tx source bundled、not mempool dedup、not Code≠0 rejected bundled 三件事，不要和 490 / 488 / 313 / 489 / 689 / 690 糊成一句。

## 和相邻反模式

- [chktxguardusage-sold-as-fourgates](chktxguardusage-sold-as-fourgates.md) 是 CheckTx Usage Guardian bundled（490），不是本页 item 3 单句边界。
- [chktxguardusage-notgates-sold-as-bundled](chktxguardusage-notgates-sold-as-bundled.md) 是 every node 单句边界（690 item 2），不是本页 before letting in 边界。
