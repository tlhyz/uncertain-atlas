# 反模式：把 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 余量）说成已经齐 / 已经交差 / 已经是同一份

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[列了块号 not already complete ≠ bundled（378）](../../tracks/implementation/worked-example-refetch-notcomplete-vs-bundled.md)。

## 卖法

把列了块号 / refetch_chunks 不论 result 都再拉再装、按顺序 / 列了块号字段 写成已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable；把再装 / 再按顺序装回去 / 再装块 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把按顺序 / 按顺序装回去 / 顺序列 写成已经是同一份 interchangeable / 已经 identical interchangeable / 已经是同一份交差 interchangeable，或已经和 378 refetch bundled / refetch-sold-as-restored interchangeable / 882 refetch-notcomplete interchangeable。

## 为什么错

官方把列了块号、不是已经交差、不是已经是同一份写成三件独立的实现事。把它们卖成 already complete interchangeable / already settled interchangeable / already identical interchangeable，会把 not already complete、not already settled、not already identical 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 余量），必须分开 not already complete、not already settled、not already identical 三件事，不要和 378 / 332 / 881 / 368 糊成一句。

## 和相邻反模式

- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch bundled 全段，不是本页列了块号 item 2 单句边界。
- [refetch-notbanned-sold-as-bundled](refetch-notbanned-sold-as-bundled.md) 是能再拉 not already banned（378 item 1），不是本页 not already complete 边界。
- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是封禁邻居就已经没有快照 DoS（332），不是本页 not already complete 单句。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是全字段对上就已经装完（368），不是本页 not already identical 边界。
