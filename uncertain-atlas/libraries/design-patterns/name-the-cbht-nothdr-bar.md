# 模式：点名 cbht-nothdr 杠

**层次**：实现 / BIP-34 coinbase-height not already header-field / not already 171 / not already 173-bundled 正式三事（173 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki)（Block v2, Height in Coinbase）。  
**对应**：[`../tracks/implementation/worked-example-cbht-nothdr-vs-bundled.md`](../tracks/implementation/worked-example-cbht-nothdr-vs-bundled.md)。

- **coinbase第一项写了高度不是头上已经有高度字段 不是已经有高度字段：看见coinbase第一项写了高度不是头上已经有高度字段，不是已经有高度字段 interchangeable / 1542 cbht-nothdr interchangeable。**
- **writing height in coinbase is not already a height field in the header 不是已经是不变量 171：看见writing height in coinbase is not already a height field in the header，不是已经是不变量 171 interchangeable / 1542 cbht-nothdr interchangeable。**
- **coinbase第一项写了高度不是头上已经有高度字段 不是已经 173 bundled：看见coinbase第一项写了高度不是头上已经有高度字段，不是已经 173 bundled interchangeable / 1542 cbht-nothdr interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-34 coinbase-height 正式三事（173 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事。
