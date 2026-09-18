# 反模式：把 BIP-322 invoice-control not already previous-tx / not already paid / not already settled 正式三事（258 余量） 写成已经 已经证明发过上一笔 / 已经付过 / 已经广播过上一笔

**层次**：应用 / BIP-322 invoice-control not already previous-tx / not already paid / not already settled 正式三事（258 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/lifecycle/worked-example-sig322-notprev-vs-bundled.md`](../tracks/lifecycle/worked-example-sig322-notprev-vs-bundled.md)。

把 BIP-322 invoice-control not already previous-tx / not already paid / not already settled 正式三事（258 余量） 写成已经 已经证明发过上一笔 / 已经付过 / 已经广播过上一笔，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发票地址将来控制 正式三事（258 余量），必须分开 not already previous-tx、not already paid、not already settled 三件事，不要和 258 / 179 / 174 / 1214 / 1216 糊成一句。

也不是：

- [sig322-notctrl-sold-as-bundled](sig322-notctrl-sold-as-bundled.md) 是签过仍未控制资金单句边界（1214 item 1），不是本页发票控制仍未证明上一笔边界。
- [sig322-notfund-sold-as-bundled](sig322-notfund-sold-as-bundled.md) 是清单仍未齐单句边界（1216 item 3），不是本页发票控制仍未证明上一笔边界。
