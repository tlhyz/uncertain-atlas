# 反模式：把 BIP-325 header-work not already signed / not already full-valid / not already settled 正式三事（265 余量） 写成已经 已经签过 / 已经全验证通过 / 已经交差

**层次**：应用 / BIP-325 header-work not already signed / not already full-valid / not already settled 正式三事（265 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/implementation/worked-example-sig325-notsign-vs-bundled.md`](../tracks/implementation/worked-example-sig325-notsign-vs-bundled.md)。

把 BIP-325 header-work not already signed / not already full-valid / not already settled 正式三事（265 余量） 写成已经 已经签过 / 已经全验证通过 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上工作量 正式三事（265 余量），必须分开 not already signed、not already full-valid、not already settled 三件事，不要和 265 / 1192 / 163 / 1193 / 1194 糊成一句。

也不是：

- [sig325-notreg-sold-as-bundled](sig325-notreg-sold-as-bundled.md) 是 signet 仍未是 regtest 单句边界（1194 item 2），不是本页头上工作量仍未签过边界。
- [tn94-notfollow-sold-as-bundled](tn94-notfollow-sold-as-bundled.md) 是会 Testnet 3 仍未能安全跟边界（292/1192），不是本页头上工作量仍未签过边界。
