# 反模式：把 BIP-342 minimalif not already p2wsh-policy-only / not already 191 / not already 144 正式三事（189 余量） 写成已经 已经只是P2WSH策略 / 已经是不变量 191 / 已经是不变量 144

**层次**：实现 / BIP-342 minimalif not already p2wsh-policy-only / not already 191 / not already 144 正式三事（189 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki)（Validation of Taproot Scripts）。  
**对应**：[`../tracks/implementation/worked-example-tpsm-notmin-vs-bundled.md`](../tracks/implementation/worked-example-tpsm-notmin-vs-bundled.md)。

把 BIP-342 minimalif not already p2wsh-policy-only / not already 191 / not already 144 正式三事（189 余量） 写成已经 已经只是P2WSH策略 / 已经是不变量 191 / 已经是不变量 144，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-342 tapscript 正式三事（189 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 189 / 191 / 144 / 1557 / 1558 糊成一句。

也不是：

- [tpsm-notsem-sold-as-bundled](tpsm-notsem-sold-as-bundled.md) 是 notsem 单句边界（1557），不是本页边界。
- [tpsm-notdone-sold-as-bundled](tpsm-notdone-sold-as-bundled.md) 是 notdone 单句边界（1558），不是本页边界。
- [kpsp-notree-sold-as-bundled](kpsp-notree-sold-as-bundled.md) 是 BIP-341 钥路径边界（153/1554），不是本页 BIP-342 tapscript 语义边界。
