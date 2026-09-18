# 反模式：把 BIP-127 por-tx not already spendable / not already confirmable / not already settled 正式三事（293 余量） 写成已经 已经能花 / 已经能确认 / 已经交差

**层次**：应用 / BIP-127 por-tx not already spendable / not already confirmable / not already settled 正式三事（293 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-127](https://github.com/bitcoin/bips/blob/master/bip-0127.mediawiki)（Complete, Applications, Specification）。  
**对应**：[`../tracks/lifecycle/worked-example-por127-notspend-vs-bundled.md`](../tracks/lifecycle/worked-example-por127-notspend-vs-bundled.md)。

把 BIP-127 por-tx not already spendable / not already confirmable / not already settled 正式三事（293 余量） 写成已经 已经能花 / 已经能确认 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看储备证明交易 正式三事（293 余量），必须分开 not already spendable、not already confirmable、not already settled 三件事，不要和 293 / 258 / 179 / 1197 / 1198 糊成一句。

也不是：

- [sig325-notsign-sold-as-bundled](sig325-notsign-sold-as-bundled.md) 是头上工作量仍未签过边界（265/1195），不是本页储备证明交易仍未能花边界。
- [por127-notctrl-sold-as-bundled](por127-notctrl-sold-as-bundled.md) 是其余输入签过仍未是 258 控制单句边界（1197 item 2），不是本页交易仍未能花边界。
