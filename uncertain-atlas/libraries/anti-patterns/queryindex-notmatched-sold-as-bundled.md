# 反模式：把 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事（380 余量）说成已经对上 AppHash / 已经复制到各节点 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了值 not already matched ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notmatched-vs-bundled.md)。

## 卖法

把回了值 / Query 回包 value 是对上的那份数据的值 / 回了 value 写成已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable / 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable；把有字节 / 有 value 字节 / 有值内容 写成已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable；把能读 / 能读 value / 有 value 回包 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 380 queryindex bundled / queryindex-sold-as-store interchangeable / 889 queryindex-notmatched interchangeable。

## 为什么错

官方把回了值、不是已经复制到各节点、不是已经交差写成三件独立的实现事。把它们卖成 already matched interchangeable / already replicated interchangeable / already settled interchangeable，会把 not already matched、not already replicated、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事（380 余量），必须分开 not already matched、not already replicated、not already settled 三件事，不要和 380 / 325 / 887 / 888 糊成一句。

## 和相邻反模式

- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 queryindex bundled 全段，不是本页回了值 item 3 单句边界。
- [queryindex-notstore-sold-as-bundled](queryindex-notstore-sold-as-bundled.md) 是有下标 not already store（380 item 1），不是本页 not already matched 边界。
- [queryindex-notheight-sold-as-bundled](queryindex-notheight-sold-as-bundled.md) 是回了键 not already height（380 item 2），不是本页 not already matched 单句。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) / [queryprove-sold-as-proof](queryprove-sold-as-proof.md) 是 Query 回了 Proof 就已经对上 AppHash（325），不是本页 not already matched 边界。
