# 反模式：把 CheckTx Usage may come from external user or another node not mempool dedup / not app replay protection / not CheckTx guard bundled 正式三事（488 余量）说成已经去重保证 / 已经应用级保护 / 已经守卫 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[source not mempool dedup ≠ bundled（488）](../../tracks/implementation/worked-example-chktxsource-notreplay-vs-bundled.md)。

## 卖法

把 may come from an external user or another node / 看见送来了 写成已经内存池去重那种保证不重放 interchangeable / 313 replay interchangeable / 已经索引器滤过就保证不重放 interchangeable；把能来自用户或邻居写成已经过了 CheckTx 就有应用级重放保护 interchangeable / 313 app replay interchangeable；把看见 Usage 这句写成已经 CheckTx 守卫余量 bundled 第二句 interchangeable / 405 checktxguard interchangeable，或已经和 488 chktxsource-vs-recheck bundled / chktxsource-notreplay-sold-as-bundled interchangeable / 685 chktxsource-notreplay interchangeable。

## 为什么错

官方把 CheckTx Usage 来源、内存池去重、应用级保护、守卫 bundled 写成三件独立的实现事。把它们卖成 mempool dedup interchangeable / app replay protection interchangeable / CheckTx guard bundled interchangeable，会把 not mempool dedup、not app replay protection、not CheckTx guard bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from external user or another node 正式三事（488 余量），必须分开 not mempool dedup、not app replay protection、not CheckTx guard bundled 三件事，不要和 488 / 313 / 405 / 301 / 683 / 684 糊成一句。

## 和相邻反模式

- [chktxsource-sold-as-replay](chktxsource-sold-as-replay.md) 是 CheckTx Usage tx source bundled（488），不是本页 item 3 单句边界。
- [chktxsource-notremoved-sold-as-bundled](chktxsource-notremoved-sold-as-bundled.md) 是 another node 单句边界（684 item 2），不是本页 replay 边界。
