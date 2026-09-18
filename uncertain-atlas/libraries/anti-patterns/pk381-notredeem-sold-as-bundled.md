# 反模式：把 BIP-381 sh-output not already have-redeem / not already spendable / not already settled 正式三事（276 余量） 写成已经 已经有赎回脚本 / 已经能花 / 已经交差

**层次**：应用 / BIP-381 sh-output not already have-redeem / not already spendable / not already settled 正式三事（276 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-381](https://github.com/bitcoin/bips/blob/master/bip-0381.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-pk381-notredeem-vs-bundled.md`](../tracks/implementation/worked-example-pk381-notredeem-vs-bundled.md)。

把 BIP-381 sh-output not already have-redeem / not already spendable / not already settled 正式三事（276 余量） 写成已经 已经有赎回脚本 / 已经能花 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 sh 产出 正式三事（276 余量），必须分开 not already have-redeem、not already spendable、not already settled 三件事，不要和 276 / 170 / 1142 / 1148 / 1150 糊成一句。

也不是：

- [pk381-notplace-sold-as-bundled](pk381-notplace-sold-as-bundled.md) 是 pk 仍未是同一套放置单句边界（1148 item 1），不是本页 sh 产出仍未有赎回边界。
- [pk381-notcompat-sold-as-bundled](pk381-notcompat-sold-as-bundled.md) 是熟悉脚本仍未兼容单句边界（1150 item 3），不是本页赎回边界。
