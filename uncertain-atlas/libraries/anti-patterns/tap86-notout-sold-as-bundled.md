# 反模式：把 BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事（272 余量） 写成已经 已经是输出钥 / 已经是见证里那 32 字节 / 已经交差

**层次**：应用 / BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事（272 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki)（Deployed, Applications）。  
**对应**：[`../tracks/implementation/worked-example-tap86-notout-vs-bundled.md`](../tracks/implementation/worked-example-tap86-notout-vs-bundled.md)。

把 BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事（272 余量） 写成已经 已经是输出钥 / 已经是见证里那 32 字节 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看派生钥 正式三事（272 余量），必须分开 not already output-key、not already witness-32、not already settled 三件事，不要和 272 / 153 / 1124 / 1137 / 1138 糊成一句。

也不是：

- [sort67-notuncomp-sold-as-bundled](sort67-notuncomp-sold-as-bundled.md) 是未压缩钥仍未是本页边界（270/1135），不是本页派生钥仍未是输出钥边界。
- 钥匙路径就已经揭开有没有树是不变量 153，不是本页内部钥仍未是见证里那 32 字节边界。
