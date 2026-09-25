# 反模式：把 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事（371 余量）说成已经是 QueryState / 已经复制到各节点 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[能查 not already querystate ≠ bundled（371）](../../tracks/implementation/worked-example-queryheight-notquerystate-vs-bundled.md)。

## 卖法

把能查 / Query 可以对当前或过去高度查 / 能查高度 写成已经是 QueryState interchangeable / 已经 querystate interchangeable / 已经是 QueryState 交差 interchangeable / 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable；把填了高度 / 填了当前或过去高度 / 有高度参数 写成已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable；把能回 / 能回 Query / 回得了 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 371 queryheight bundled / queryheight-sold-as-committed interchangeable / 860 queryheight-notquerystate interchangeable。

## 为什么错

官方把能查、不是已经复制到各节点、不是已经交差写成三件独立的实现事。把它们卖成 already querystate interchangeable / already replicated interchangeable / already settled interchangeable，会把 not already querystate、not already replicated、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事（371 余量），必须分开 not already querystate、not already replicated、not already settled 三件事，不要和 371 / 314 / 329 / 861 / 862 糊成一句。

## 和相邻反模式

- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 queryheight bundled 全段，不是本页能查 item 1 单句边界。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState 就已经是 ExecuteTxState（314），不是本页 not already querystate 单句边界。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是 Query 回了就已经复制到各节点（329），不是本页 not already replicated 边界。
