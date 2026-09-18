# 反模式：把 BIP-382 uncompressed-key not already allowed-in-wpkh / not already allowed-under-wsh / not already settled 正式三事（277 余量） 写成已经 已经允许进 wpkh / 已经允许出现在 wsh 下面 / 已经交差

**层次**：应用 / BIP-382 uncompressed-key not already allowed-in-wpkh / not already allowed-under-wsh / not already settled 正式三事（277 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-wpkh382-notuncomp-vs-bundled.md`](../tracks/implementation/worked-example-wpkh382-notuncomp-vs-bundled.md)。

把 BIP-382 uncompressed-key not already allowed-in-wpkh / not already allowed-under-wsh / not already settled 正式三事（277 余量） 写成已经 已经允许进 wpkh / 已经允许出现在 wsh 下面 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看未压缩钥 正式三事（277 余量），必须分开 not already allowed-in-wpkh、not already allowed-under-wsh、not already settled 三件事，不要和 277 / 1147 / 184 / 1151 / 1153 糊成一句。

也不是：

- [wpkh382-nottop-sold-as-bundled](wpkh382-nottop-sold-as-bundled.md) 是隔离见证仍未只能顶层单句边界（1151 item 1），不是本页未压缩钥仍未允许边界。
- [wpkh382-notwit-sold-as-bundled](wpkh382-notwit-sold-as-bundled.md) 是 wsh 产出仍未有见证脚本单句边界（1153 item 3），不是本页压缩条件边界。
