# 反模式：把 BIP-342 success-opcode not already executed / not already safe-upgrade / not already 189-bundled 正式三事（189 余量） 写成已经 已经执行完 / 已经安全升级 / 已经 189 bundled

**层次**：实现 / BIP-342 success-opcode not already executed / not already safe-upgrade / not already 189-bundled 正式三事（189 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki)（Validation of Taproot Scripts）。  
**对应**：[`../tracks/implementation/worked-example-tpsm-notdone-vs-bundled.md`](../tracks/implementation/worked-example-tpsm-notdone-vs-bundled.md)。

把 BIP-342 success-opcode not already executed / not already safe-upgrade / not already 189-bundled 正式三事（189 余量） 写成已经 已经执行完 / 已经安全升级 / 已经 189 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-342 tapscript 正式三事（189 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 189 / 153 / 191 / 1557 / 1559 糊成一句。

也不是：

- [tpsm-notsem-sold-as-bundled](tpsm-notsem-sold-as-bundled.md) 是 notsem 单句边界（1557），不是本页边界。
- [tpsm-notmin-sold-as-bundled](tpsm-notmin-sold-as-bundled.md) 是 notmin 单句边界（1559），不是本页边界。
- [kpsp-notree-sold-as-bundled](kpsp-notree-sold-as-bundled.md) 是 BIP-341 钥路径边界（153/1554），不是本页 BIP-342 tapscript 语义边界。
