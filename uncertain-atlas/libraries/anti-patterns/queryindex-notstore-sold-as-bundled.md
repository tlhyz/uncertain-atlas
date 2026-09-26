# 反模式：把 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事（380 余量）说成已经是按键查 / 已经对上 AppHash / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有下标 not already store ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notstore-vs-bundled.md)。

## 卖法

把有下标 / Query 回包 index 是树里这个键的下标 / 有 index 下标 写成已经是按键查 interchangeable / 已经 store interchangeable / 已经是按键查交差 interchangeable / 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable；把填了下标 / 填了 index / 下标有值 写成已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable；把有数 / 有下标数字 / index 是数 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 380 queryindex bundled / queryindex-sold-as-store interchangeable / 887 queryindex-notstore interchangeable。

## 为什么错

官方把有下标、不是已经对上 AppHash、不是已经交差写成三件独立的实现事。把它们卖成 already store interchangeable / already matched interchangeable / already settled interchangeable，会把 not already store、not already matched、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事（380 余量），必须分开 not already store、not already matched、not already settled 三件事，不要和 380 / 377 / 325 / 371 糊成一句。

## 和相邻反模式

- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 queryindex bundled 全段，不是本页有下标 item 1 单句边界。
- [querypath-sold-as-store](querypath-sold-as-store.md) / [querypath-notengine-sold-as-bundled](querypath-notengine-sold-as-bundled.md) 是 path /store 就必须按键查就已经是引擎在用（377），不是本页 not already store 边界。
- [queryprove-sold-as-proof](queryprove-sold-as-proof.md) 是 Query 回了 Proof 就已经对上 AppHash（325），不是本页 not already matched 单句。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query 可以对当前或过去高度查就已经是 QueryState（371），不是本页 not already settled 边界。
