# 反模式：把 EIP-1559 basefee-burned not already paid-to-proposer / not already 145 / not already 158-bundled 正式三事（158 余量） 写成已经 已经给了出块者 / 已经是不变量 145 / 已经 158 bundled

**层次**：实现 / EIP-1559 basefee-burned not already paid-to-proposer / not already 145 / not already 158-bundled 正式三事（158 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)（Fee market change for ETH 1.0 chain）。  
**对应**：[`../tracks/mempool/worked-example-bfmkt-notpay-vs-bundled.md`](../tracks/mempool/worked-example-bfmkt-notpay-vs-bundled.md)。

把 EIP-1559 basefee-burned not already paid-to-proposer / not already 145 / not already 158-bundled 正式三事（158 余量） 写成已经 已经给了出块者 / 已经是不变量 145 / 已经 158 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1559 basefee-vs-tip 正式三事（158 余量），必须分开 not already paid-to-proposer、not already market-complete、not already mev-solved 三件事，不要和 158 / 145 / 144 / 1486 / 1487 糊成一句。

也不是：

- [bfmkt-notmkt-sold-as-bundled](bfmkt-notmkt-sold-as-bundled.md) 是 notmkt 单句边界（1486），不是本页边界。
- [bfmkt-notmev-sold-as-bundled](bfmkt-notmev-sold-as-bundled.md) 是 notmev 单句边界（1487），不是本页边界。
- [lkah-notlock-sold-as-bundled](lkah-notlock-sold-as-bundled.md) 是 EIP-7917 出块前瞻边界（205/1482），不是本页费用市场边界。
