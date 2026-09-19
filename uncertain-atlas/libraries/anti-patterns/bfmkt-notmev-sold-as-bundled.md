# 反模式：把 EIP-1559 burn not already mev-solved / not already safer / not already 144 正式三事（158 余量） 写成已经 已经解决MEV / 已经更安全 / 已经是不变量 144

**层次**：实现 / EIP-1559 burn not already mev-solved / not already safer / not already 144 正式三事（158 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)（Fee market change for ETH 1.0 chain）。  
**对应**：[`../tracks/mempool/worked-example-bfmkt-notmev-vs-bundled.md`](../tracks/mempool/worked-example-bfmkt-notmev-vs-bundled.md)。

把 EIP-1559 burn not already mev-solved / not already safer / not already 144 正式三事（158 余量） 写成已经 已经解决MEV / 已经更安全 / 已经是不变量 144，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1559 basefee-vs-tip 正式三事（158 余量），必须分开 not already paid-to-proposer、not already market-complete、not already mev-solved 三件事，不要和 158 / 167 / 187 / 1485 / 1486 糊成一句。

也不是：

- [bfmkt-notpay-sold-as-bundled](bfmkt-notpay-sold-as-bundled.md) 是 notpay 单句边界（1485），不是本页边界。
- [bfmkt-notmkt-sold-as-bundled](bfmkt-notmkt-sold-as-bundled.md) 是 notmkt 单句边界（1486），不是本页边界。
- [lkah-notlock-sold-as-bundled](lkah-notlock-sold-as-bundled.md) 是 EIP-7917 出块前瞻边界（205/1482），不是本页费用市场边界。
