# 反模式：把有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事（326 余量）说成已经三条都在用 / 已经是过滤 / 已经两道过滤带了数据

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有 /store not already all-paths-used ≠ bundled（326）](../../tracks/implementation/worked-example-peerfilter-notenginepath-vs-bundled.md)。

## 卖法

把规范写了三条路径 / 有 `/p2p`、`/store`、`/app` / 高层路径表 写成已经三条都在用 interchangeable / 已经 all-paths-used interchangeable / 已经引擎三条都开交差 interchangeable / 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable；把有 /store / 有 `/app` / 路径名在表里 写成已经是过滤 interchangeable / 已经 is-filter interchangeable；把能带数据 / Query 还可以另带数据 / 路径外还能带数据 写成已经两道过滤带了数据 interchangeable / 已经 filter-has-data interchangeable，或已经和 326 peerfilter bundled / peerfilter-sold-as-connected interchangeable / 736 peerfilter-notenginepath interchangeable。

## 为什么错

官方把规范写了三条路径单句、already all-paths-used、already is-filter、already filter-has-data 写成三件独立的实现事。把它们卖成 already all-paths-used interchangeable / already is-filter interchangeable / already filter-has-data interchangeable，会把 not already all-paths-used、not already is-filter、not already filter-has-data 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事（326 余量），必须分开 not already all-paths-used、not already is-filter、not already filter-has-data 三件事，不要和 326 / 33 / 734 / 735 / 305 / 50 / 314 糊成一句。

## 和相邻反模式

- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是 Peer Filtering bundled 全段，不是本页路径表 item 3 单句边界。
- [peerfilter-notaddrpassed-sold-as-bundled](peerfilter-notaddrpassed-sold-as-bundled.md) 是 id 第二道 item 2，不是本页 `/store` 与过滤边界。
- [peerfilter-notaccepted-sold-as-bundled](peerfilter-notaccepted-sold-as-bundled.md) 是 addr 第一道 item 1，不是本页引擎只用 `/p2p` 边界。
