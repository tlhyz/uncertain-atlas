# 反模式：把已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事（315 余量）说成已经按气验过 / 已经共识守了 / 已经默认卡气

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[块已经提交 not already gas-checked ≠ bundled（315）](../../tracks/implementation/worked-example-maxgas-notcommitted-vs-bundled.md)。

## 卖法

把块已经提交 / 已提交块 / 旧版只在内存池管气 写成已经按气验过 interchangeable / 已经 gas-checked interchangeable / 已经保证这块守了气限 interchangeable / 315 maxgas bundled interchangeable / 33 four gates interchangeable / maxgas-sold-as-enforced interchangeable；把池子守了 / 内存池管了气 / 只在内存池管 写成已经共识守了 interchangeable / 已经 consensus-enforced interchangeable；把有了 Prepare / Process / v0.37.x 有了 PrepareProposal ProcessProposal 写成已经默认在卡气 interchangeable / 已经 default Prepare Process capping interchangeable，或已经和 315 maxgas bundled / maxgas-sold-as-enforced interchangeable / 706 maxgas-notcommitted interchangeable。

## 为什么错

官方把块已经提交单句、already gas-checked、already consensus-enforced、already default Prepare Process capping 写成三件独立的实现事。把它们卖成 already gas-checked interchangeable / already consensus-enforced interchangeable / already default Prepare Process capping interchangeable，会把 not already gas-checked、not already consensus-enforced、not already default Prepare Process capping 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事（315 余量），必须分开 not already gas-checked、not already consensus-enforced、not already default Prepare Process capping 三件事，不要和 315 / 704 / 705 / 299 / 33 糊成一句。

## 和相邻反模式

- [maxgas-sold-as-enforced](maxgas-sold-as-enforced.md) 是 MaxGas vs enforced bundled 全段，不是本页块已经提交 item 3 单句边界。
- [maxgas-notgasused-sold-as-bundled](maxgas-notgasused-sold-as-bundled.md) 是有 GasUsed item 2，不是本页已提交按气验边界。
- [maxgas-notenforced-sold-as-bundled](maxgas-notenforced-sold-as-bundled.md) 是字段在 item 1，不是本页 Prepare/Process 默认卡气边界。
