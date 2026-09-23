# 反模式：把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事（355 余量）说成已经还能按 t1 查到 / 已经有人知道来源 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[把 t1 改成 t2 not already t1-lookup ≠ bundled（355）](../../tracks/implementation/worked-example-retarget-nottraceable-vs-bundled.md)。

## 卖法

把 t1 改成 t2 / t1 没进块 / t1 没进已提交块 写成已经还能按 t1 查到 interchangeable / 已经 t1-lookup interchangeable / 已经按 t1 查到交差 interchangeable / 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable；把 t2 进了块 / t2 在已提交块里 写成已经有人知道 t2 来自 t1 interchangeable / 已经 origin-known interchangeable / 已经来源已知交差 interchangeable；把改了 / 拿掉再加 / 改了列表 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 355 preparedrop bundled / preparedrop-sold-as-evicted interchangeable / 820 retarget-nottraceable interchangeable。

## 为什么错

官方把 t1 没进块、不是已经有人知道来源、不是已经交差写成三件独立的实现事。把它们卖成 already t1-lookup interchangeable / already origin-known interchangeable / already settled interchangeable，会把 not already t1-lookup、not already origin-known、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事（355 余量），必须分开 not already t1-lookup、not already origin-known、not already settled 三件事，不要和 355 / 301 / 345 / 818 / 819 糊成一句。

## 和相邻反模式

- [preparedrop-sold-as-evicted](preparedrop-sold-as-evicted.md) 是 Prepare 改列表 bundled 全段，不是本页 t1 没进块 item 3 单句边界。
- [add-notmempool-sold-as-bundled](add-notmempool-sold-as-bundled.md) 是往提案加了一笔新的 not already in-pool（355 item 2），不是本页 not already t1-lookup 边界。
- [drop-notmempool-sold-as-bundled](drop-notmempool-sold-as-bundled.md) 是从提案拿掉 tx not already out-of-pool（355 item 1），不是本页 not already settled 边界。
