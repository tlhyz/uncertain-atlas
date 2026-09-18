# 模式：点名 wpkh382-notwit 杠

**层次**：应用 / BIP-382 wsh-output not already have-witness-script / not already 381-redeem / not already settled 正式三事（277 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-wpkh382-notwit-vs-bundled.md`](../tracks/implementation/worked-example-wpkh382-notwit-vs-bundled.md)。

- **wsh 产出 不是已经有见证脚本：** 看见 P2WSH 输出脚本，不是已经有见证脚本 interchangeable / 1153 wpkh382-notwit interchangeable。
- **381 赎回脚本 不是已经是本页见证脚本：** 看见 381 另造了赎回脚本，不是已经是本页这份见证脚本 interchangeable / 1153 wpkh382-notwit interchangeable。
- **P2WSH 输出脚本 不是已经交差：** 看见 P2WSH 输出脚本，不是已经交差 interchangeable / 1153 wpkh382-notwit interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 wsh 产出 正式三事（277 余量），必须分开 not already have-witness-script、not already 381-redeem、not already settled 三件事。
