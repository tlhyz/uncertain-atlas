# 反模式：把 BIP-129 fingerprint not already verified-key / not already same-confirm / not already settled 正式三事（287 余量） 写成已经 已经核过 KEY / 已经各方确认同一份 / 已经交差

**层次**：应用 / BIP-129 fingerprint not already verified-key / not already same-confirm / not already settled 正式三事（287 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-129](https://github.com/bitcoin/bips/blob/master/bip-0129.mediawiki)（Complete, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-bsms129-notkey-vs-bundled.md`](../tracks/implementation/worked-example-bsms129-notkey-vs-bundled.md)。

把 BIP-129 fingerprint not already verified-key / not already same-confirm / not already settled 正式三事（287 余量） 写成已经 已经核过 KEY / 已经各方确认同一份 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看指纹对上 正式三事（287 余量），必须分开 not already verified-key、not already same-confirm、not already settled 三件事，不要和 287 / 184 / 1162 / 1178 / 1180 糊成一句。

也不是：

- [bsms129-notsetup-sold-as-bundled](bsms129-notsetup-sold-as-bundled.md) 是部分签名包仍未是开户单句边界（1178 item 1），不是本页指纹仍未核过 KEY 边界。
- [bsms129-nottoken-sold-as-bundled](bsms129-nottoken-sold-as-bundled.md) 是 TOKEN 仍未是钱包种子单句边界（1180 item 3），不是本页指纹仍未核过 KEY 边界。
