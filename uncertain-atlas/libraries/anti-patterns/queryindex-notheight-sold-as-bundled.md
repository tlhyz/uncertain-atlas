# 反模式：把 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（380 余量）说成已经是 Query 高度 / 已经新鲜 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了键 not already height ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notheight-vs-bundled.md)。

## 卖法

把回了键 / Query 回包 key 是对上的那份数据的键 / 回了 key 写成已经是 Query 高度 interchangeable / 已经 height interchangeable / 已经是 Query 高度交差 interchangeable / 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable；把有键 / 有对上的那份数据的键 / 有 key 字段 写成已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable；把能回 / 能回 key / 有 key 回包 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 380 queryindex bundled / queryindex-sold-as-store interchangeable / 888 queryindex-notheight interchangeable。

## 为什么错

官方把回了键、不是已经新鲜、不是已经交差写成三件独立的实现事。把它们卖成 already height interchangeable / already fresh interchangeable / already settled interchangeable，会把 not already height、not already fresh、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（380 余量），必须分开 not already height、not already fresh、not already settled 三件事，不要和 380 / 371 / 887 / 325 糊成一句。

## 和相邻反模式

- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 queryindex bundled 全段，不是本页回了键 item 2 单句边界。
- [queryindex-notstore-sold-as-bundled](queryindex-notstore-sold-as-bundled.md) 是有下标 not already store（380 item 1），不是本页 not already height 边界。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query 可以对当前或过去高度查就已经是 QueryState（371），不是本页 not already height 单句。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash（325），不是本页 not already settled 边界。
