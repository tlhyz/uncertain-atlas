# 反模式：把 整池可见 not already only subset that fits / not already no limit / not already settled 正式三事（345 余量） 卖成 已经只能看见装得进一块的子集 / 已经没有上限 / 已经交差

**层次**：实现 / PrepareProposal 回包上限。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-return-notsubset-vs-bundled.md](../../tracks/implementation/worked-example-prepare-return-notsubset-vs-bundled.md)。

官方把整池可见 / 聚合体积可以超过 max_tx_bytes / Req 2 保证回的列表不让块超字节上限 三条核心句写成三件独立的实现事。把它们卖成已经只能看见装得进一块的子集 / 已经没有上限 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看整池可见 正式三事（345 余量），必须分开 not already only subset that fits、not already no limit、not already settled 三件事，不要和 345 / 299 / 337 / 879 / 880 糊成一句。

## 和相邻反模式

- [abci20-upgrade-notfield-sold-as-bundled](abci20-upgrade-notfield-sold-as-bundled.md) 是必须协调升级（346/875），不是本页整池可见边界。
- 整池都给 Prepare 就已经没有上限是不变量 299，不是本页整池可见边界。
