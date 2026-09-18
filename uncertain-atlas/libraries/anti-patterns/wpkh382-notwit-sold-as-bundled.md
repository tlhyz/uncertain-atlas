# 反模式：把 BIP-382 wsh-output not already have-witness-script / not already 381-redeem / not already settled 正式三事（277 余量） 写成已经 已经有见证脚本 / 已经是 381 赎回 / 已经交差

**层次**：应用 / BIP-382 wsh-output not already have-witness-script / not already 381-redeem / not already settled 正式三事（277 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-wpkh382-notwit-vs-bundled.md`](../tracks/implementation/worked-example-wpkh382-notwit-vs-bundled.md)。

把 BIP-382 wsh-output not already have-witness-script / not already 381-redeem / not already settled 正式三事（277 余量） 写成已经 已经有见证脚本 / 已经是 381 赎回 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 wsh 产出 正式三事（277 余量），必须分开 not already have-witness-script、not already 381-redeem、not already settled 三件事，不要和 277 / 1149 / 170 / 1151 / 1152 糊成一句。

也不是：

- [wpkh382-notuncomp-sold-as-bundled](wpkh382-notuncomp-sold-as-bundled.md) 是未压缩钥仍未允许单句边界（1152 item 2），不是本页 wsh 产出仍未有见证脚本边界。
- [pk381-notredeem-sold-as-bundled](pk381-notredeem-sold-as-bundled.md) 是 381 sh 产出仍未有赎回边界（276/1149），不是本页见证脚本边界。
