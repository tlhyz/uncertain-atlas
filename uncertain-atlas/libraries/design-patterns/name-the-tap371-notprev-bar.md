# 模式：点名 tap371-notprev 杠

**层次**：应用 / BIP-371 taproot-input not already must-prev-tx / not already same-utxo-fields / not already settled 正式三事（279 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-tap371-notprev-vs-bundled.md`](../tracks/implementation/worked-example-tap371-notprev-vs-bundled.md)。

- **Taproot 输入 不是已经必须带整笔前交易：** 看见 Taproot 输入，不是已经必须带整笔前交易 interchangeable / 1159 tap371-notprev interchangeable。
- **只带了见证 UTXO 不是已经是旧输入那套：** 看见只带了见证 UTXO，不是已经是旧输入那套 interchangeable / 1159 tap371-notprev interchangeable。
- **174 建议带整笔前交易 不是已经交差：** 看见 174 建议带整笔前交易，不是已经交差 interchangeable / 1159 tap371-notprev interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Taproot 输入 UTXO 栏 正式三事（279 余量），必须分开 not already must-prev-tx、not already same-utxo-fields、not already settled 三件事。
