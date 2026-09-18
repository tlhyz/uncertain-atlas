# 模式：点名 wpkh382-notuncomp 杠

**层次**：应用 / BIP-382 uncompressed-key not already allowed-in-wpkh / not already allowed-under-wsh / not already settled 正式三事（277 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-wpkh382-notuncomp-vs-bundled.md`](../tracks/implementation/worked-example-wpkh382-notuncomp-vs-bundled.md)。

- **未压缩钥 不是已经允许进 wpkh：** 看见未压缩钥，不是已经允许进 wpkh interchangeable / 1152 wpkh382-notuncomp interchangeable。
- **任意钥 不是已经允许出现在 wsh 下面：** 看见任意钥，不是已经允许出现在 wsh 下面 interchangeable / 1152 wpkh382-notuncomp interchangeable。
- **381 还收未压缩 不是已经交差：** 看见 381 还收未压缩，不是已经交差 interchangeable / 1152 wpkh382-notuncomp interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看未压缩钥 正式三事（277 余量），必须分开 not already allowed-in-wpkh、not already allowed-under-wsh、not already settled 三件事。
