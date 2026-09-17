# 反模式：把 CheckTx 可选 not already four gates settled / not already settled / not already deleted from pool 正式三事（373 余量） 卖成 已经是四门已经结算 / 已经交差 / 已经从池里删掉

**层次**：实现 / CheckTx 可选。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktxopt-notsettled-vs-bundled.md](../../tracks/implementation/worked-example-checktxopt-notsettled-vs-bundled.md)。

官方把 CheckTx 技术上可选 / Code ≠ 0 拒收 / 回包码不再另有含义三条核心句写成三件独立的实现事。把它们卖成已经是四门已经结算 / 已经交差 / 已经从池里删掉，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 可选 正式三事（373 余量），必须分开 not already four gates settled、not already settled、not already deleted from pool 三件事，不要和 373 / 33 / 339 / 486 / 682 / 807 / 808 糊成一句。

## 和相邻反模式

- [chktxvalidate-notoptional-sold-as-bundled](chktxvalidate-notoptional-sold-as-bundled.md) 是 Usage validate-no-apply 就已经可选（486/682），不是本页可选边界。
- [checktxweak-sold-as-consensus](checktxweak-sold-as-consensus.md) 是弱过滤器就已经验完（339），不是本页可选边界。
