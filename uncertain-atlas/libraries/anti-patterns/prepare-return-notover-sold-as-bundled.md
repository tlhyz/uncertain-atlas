# 反模式：把 聚合体积可以超过 max_tx_bytes not already can return oversize / not already pool already trimmed / not already settled 正式三事（345 余量） 卖成 已经能回超限列表 / 已经按这个上限裁过 / 已经交差

**层次**：实现 / PrepareProposal 回包上限。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-return-notover-vs-bundled.md](../../tracks/implementation/worked-example-prepare-return-notover-vs-bundled.md)。

官方把整池可见 / 聚合体积可以超过 max_tx_bytes / Req 2 保证回的列表不让块超字节上限 三条核心句写成三件独立的实现事。把它们卖成已经能回超限列表 / 已经按这个上限裁过 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看聚合体积可以超过 max_tx_bytes 正式三事（345 余量），必须分开 not already can return oversize、not already pool already trimmed、not already settled 三件事，不要和 345 / 299 / 33 / 878 / 880 糊成一句。

## 和相邻反模式

- [prepare-return-notsubset-sold-as-bundled](prepare-return-notsubset-sold-as-bundled.md) 是整池可见单句边界（878 item 1），不是本页聚合超限边界。
- 整池都给 Prepare 就已经没有上限是不变量 299，不是本页聚合超限边界。
