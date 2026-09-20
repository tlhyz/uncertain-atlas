# 反模式：把 EIP-7642 history-window not already consensus-pruned / not already 23 / not already 207-bundled 正式三事（207 余量） 写成已经 已经改了共识历史 / 已经是不变量 23 / 已经 207 bundled

**层次**：实现 / EIP-7642 history-window not already consensus-pruned / not already 23 / not already 207-bundled 正式三事（207 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7642](https://eips.ethereum.org/EIPS/eip-7642)（history expiry and simpler receipts）。  
**对应**：[`../tracks/network/worked-example-hwin-notcons-vs-bundled.md`](../tracks/network/worked-example-hwin-notcons-vs-bundled.md)。

把 EIP-7642 history-window not already consensus-pruned / not already 23 / not already 207-bundled 正式三事（207 余量） 写成已经 已经改了共识历史 / 已经是不变量 23 / 已经 207 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7642 history-window 正式三事（207 余量），必须分开 not already consensus-pruned、not already consensus-receipt、not already sync-done 三件事，不要和 207 / 23 / 25 / 1489 / 1490 糊成一句。

也不是：

- [hwin-notenc-sold-as-bundled](hwin-notenc-sold-as-bundled.md) 是 notenc 单句边界（1489），不是本页边界。
- [hwin-notsync-sold-as-bundled](hwin-notsync-sold-as-bundled.md) 是 notsync 单句边界（1490），不是本页边界。
- [bfmkt-notpay-sold-as-bundled](bfmkt-notpay-sold-as-bundled.md) 是 EIP-1559 费用市场边界（158/1485），不是本页历史窗边界。
