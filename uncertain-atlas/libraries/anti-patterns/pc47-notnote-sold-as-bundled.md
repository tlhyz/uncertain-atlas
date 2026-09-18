# 反模式：把 BIP-47 notification not already payment / not already spendable / not already settled 正式三事（273 余量） 写成已经 已经是付款 / 已经付到存款地址 / 已经能花

**层次**：应用 / BIP-47 notification not already payment / not already spendable / not already settled 正式三事（273 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki)（Deployed, Applications）。  
**对应**：[`../tracks/lifecycle/worked-example-pc47-notnote-vs-bundled.md`](../tracks/lifecycle/worked-example-pc47-notnote-vs-bundled.md)。

把 BIP-47 notification not already payment / not already spendable / not already settled 正式三事（273 余量） 写成已经 已经是付款 / 已经付到存款地址 / 已经能花，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通知输出 正式三事（273 余量），必须分开 not already payment、not already spendable、not already settled 三件事，不要和 273 / 174 / 182 / 1223 / 1225 糊成一句。

也不是：

- [pc47-notdep-sold-as-bundled](pc47-notdep-sold-as-bundled.md) 是付款码仍未是存款地址单句边界（1223 item 1），不是本页通知仍未是付款边界。
- [pc47-notagain-sold-as-bundled](pc47-notagain-sold-as-bundled.md) 是第一次仍未免通知单句边界（1225 item 3），不是本页通知仍未是付款边界。
