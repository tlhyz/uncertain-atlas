# 反模式：把 BIP-371 taproot-input not already must-prev-tx / not already same-utxo-fields / not already settled 正式三事（279 余量） 写成已经 已经必须带整笔前交易 / 已经是旧输入那套 / 已经交差

**层次**：应用 / BIP-371 taproot-input not already must-prev-tx / not already same-utxo-fields / not already settled 正式三事（279 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-tap371-notprev-vs-bundled.md`](../tracks/implementation/worked-example-tap371-notprev-vs-bundled.md)。

把 BIP-371 taproot-input not already must-prev-tx / not already same-utxo-fields / not already settled 正式三事（279 余量） 写成已经 已经必须带整笔前交易 / 已经是旧输入那套 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Taproot 输入 UTXO 栏 正式三事（279 余量），必须分开 not already must-prev-tx、not already same-utxo-fields、not already settled 三件事，不要和 279 / 186 / 179 / 1157 / 1158 糊成一句。

也不是：

- [tap371-notinner-sold-as-bundled](tap371-notinner-sold-as-bundled.md) 是输出脚本钥仍未是内部钥单句边界（1158 item 2），不是本页见证 UTXO 边界。
- [tap86-notout-sold-as-bundled](tap86-notout-sold-as-bundled.md) 是派生钥仍未是输出钥边界（272/1136），不是本页必须带整笔前交易边界。
