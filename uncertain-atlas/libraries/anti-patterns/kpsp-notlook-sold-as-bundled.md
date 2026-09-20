# 反模式：把 BIP-341 taproot-output not already look-pubkey-or-script / not already 170 / not already 174 正式三事（153 余量） 写成已经 已经分辨付款给钥还是付款给脚本 / 已经是不变量 170 / 已经是不变量 174

**层次**：实现 / BIP-341 taproot-output not already look-pubkey-or-script / not already 170 / not already 174 正式三事（153 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)（Taproot: SegWit version 1 spending rules）。  
**对应**：[`../tracks/implementation/worked-example-kpsp-notlook-vs-bundled.md`](../tracks/implementation/worked-example-kpsp-notlook-vs-bundled.md)。

把 BIP-341 taproot-output not already look-pubkey-or-script / not already 170 / not already 174 正式三事（153 余量） 写成已经 已经分辨付款给钥还是付款给脚本 / 已经是不变量 170 / 已经是不变量 174，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-341 keypath-scriptpath 正式三事（153 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 153 / 170 / 174 / 1554 / 1555 糊成一句。

也不是：

- [kpsp-notree-sold-as-bundled](kpsp-notree-sold-as-bundled.md) 是 notree 单句边界（1554），不是本页边界。
- [kpsp-notall-sold-as-bundled](kpsp-notall-sold-as-bundled.md) 是 notall 单句边界（1555），不是本页边界。
- [twid-noteq-sold-as-bundled](twid-noteq-sold-as-bundled.md) 是 BIP-141 身份边界（152/1551），不是本页 BIP-341 花费路径边界。
