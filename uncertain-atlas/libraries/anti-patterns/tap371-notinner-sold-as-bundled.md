# 反模式：把 BIP-371 output-script-key not already internal-key / not already same-key / not already settled 正式三事（279 余量） 写成已经 已经是内部钥 / 已经不必再给内部钥 / 已经交差

**层次**：应用 / BIP-371 output-script-key not already internal-key / not already same-key / not already settled 正式三事（279 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-tap371-notinner-vs-bundled.md`](../tracks/implementation/worked-example-tap371-notinner-vs-bundled.md)。

把 BIP-371 output-script-key not already internal-key / not already same-key / not already settled 正式三事（279 余量） 写成已经 已经是内部钥 / 已经不必再给内部钥 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看内部钥 正式三事（279 余量），必须分开 not already internal-key、not already same-key、not already settled 三件事，不要和 279 / 1136 / 153 / 1157 / 1159 糊成一句。

也不是：

- [tap371-notold-sold-as-bundled](tap371-notold-sold-as-bundled.md) 是旧栏仍未装得下 Taproot 单句边界（1157 item 1），不是本页内部钥边界。
- [tap371-notprev-sold-as-bundled](tap371-notprev-sold-as-bundled.md) 是 Taproot 输入仍未必须带整笔前交易单句边界（1159 item 3），不是本页内部钥边界。
