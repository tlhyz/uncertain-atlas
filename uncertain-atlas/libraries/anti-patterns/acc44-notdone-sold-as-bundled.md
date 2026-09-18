# 反模式：把 BIP-44 zero-balance not already discovery-done / not already no-later-account / not already settled 正式三事（267 余量） 写成已经 已经发现完 / 已经没有后面的账户 / 已经交差

**层次**：应用 / BIP-44 zero-balance not already discovery-done / not already no-later-account / not already settled 正式三事（267 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)（Deployed, Applications）。  
**对应**：[`../tracks/implementation/worked-example-acc44-notdone-vs-bundled.md`](../tracks/implementation/worked-example-acc44-notdone-vs-bundled.md)。

把 BIP-44 zero-balance not already discovery-done / not already no-later-account / not already settled 正式三事（267 余量） 写成已经 已经发现完 / 已经没有后面的账户 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看余额为零 正式三事（267 余量），必须分开 not already discovery-done、not already no-later-account、not already settled 三件事，不要和 267 / 184 / 183 / 1115 / 1116 糊成一句。

也不是：

- [acc44-notpast-sold-as-bundled](acc44-notpast-sold-as-bundled.md) 是账户号仍未有过往单句边界（1116 item 2），不是本页余额为零仍未发现完边界。
- 描述符就已经知道脚本是不变量 184，不是本页停搜仍未没有后面的账户边界。
