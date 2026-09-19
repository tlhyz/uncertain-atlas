# 反模式：把 BIP-350 successor-pass not already old-bech32 / not already 174 / not already 181-bundled 正式三事（181 余量） 写成已经 已经是旧校验那套地址 / 已经是不变量 174 / 已经 181 bundled

**层次**：实现 / BIP-350 successor-pass not already old-bech32 / not already 174 / not already 181-bundled 正式三事（181 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-350](https://github.com/bitcoin/bips/blob/master/bip-0350.mediawiki)（Bech32m format for v1+ witness addresses）。  
**对应**：[`../tracks/implementation/worked-example-b32m-notold-vs-bundled.md`](../tracks/implementation/worked-example-b32m-notold-vs-bundled.md)。

把 BIP-350 successor-pass not already old-bech32 / not already 174 / not already 181-bundled 正式三事（181 余量） 写成已经 已经是旧校验那套地址 / 已经是不变量 174 / 已经 181 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-350 Bech32m 正式三事（181 余量），必须分开 not already redeem-revealed、not already new-reran、not already inner-verified 三件事，不要和 181 / 174 / 170 / 1540 / 1541 糊成一句。

也不是：

- [b32m-notv0-sold-as-bundled](b32m-notv0-sold-as-bundled.md) 是 notv0 单句边界（1540），不是本页边界。
- [b32m-notutx-sold-as-bundled](b32m-notutx-sold-as-bundled.md) 是 notutx 单句边界（1541），不是本页边界。
- [adut-notout-sold-as-bundled](adut-notout-sold-as-bundled.md) 是 BIP-173 地址串边界（174/1536），不是本页 BIP-350 后继校验边界。
