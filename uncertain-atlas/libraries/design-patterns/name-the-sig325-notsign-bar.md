# 模式：点名 sig325-notsign 杠

**层次**：应用 / BIP-325 header-work not already signed / not already full-valid / not already settled 正式三事（265 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/implementation/worked-example-sig325-notsign-vs-bundled.md`](../tracks/implementation/worked-example-sig325-notsign-vs-bundled.md)。

- **头上有合法工作量 不是已经签过：** 看见头上有合法工作量，不是已经签过 interchangeable / 1195 sig325-notsign interchangeable。
- **只加了网络参数 不是已经全验证通过：** 看见只加了网络参数，不是已经全验证通过 interchangeable / 1195 sig325-notsign interchangeable。
- **同一份创世 不是已经交差：** 看见同一份创世，不是已经交差 interchangeable / 1195 sig325-notsign interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上工作量 正式三事（265 余量），必须分开 not already signed、not already full-valid、not already settled 三件事。
