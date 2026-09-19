# 反模式：把 EIP-7825 one-over-cap not already policy-only / not already safer / not already 101 正式三事（203 余量） 写成已经 已经只是策略拒绝 / 已经更安全 / 已经是不变量 101

**层次**：实现 / EIP-7825 one-over-cap not already policy-only / not already safer / not already 101 正式三事（203 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7825](https://eips.ethereum.org/EIPS/eip-7825)（Transaction Gas Limit Cap）。  
**对应**：[`../tracks/implementation/worked-example-txcap-notpol-vs-bundled.md`](../tracks/implementation/worked-example-txcap-notpol-vs-bundled.md)。

把 EIP-7825 one-over-cap not already policy-only / not already safer / not already 101 正式三事（203 余量） 写成已经 已经只是策略拒绝 / 已经更安全 / 已经是不变量 101，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7825 tx-gas-cap 正式三事（203 余量），必须分开 not already block-gas、not already block-verified、not already policy-only 三件事，不要和 203 / 211 / 101 / 1461 / 1462 糊成一句。

也不是：

- [txcap-notblk-sold-as-bundled](txcap-notblk-sold-as-bundled.md) 是 notblk 单句边界（1461），不是本页边界。
- [txcap-notpool-sold-as-bundled](txcap-notpool-sold-as-bundled.md) 是 notpool 单句边界（1462），不是本页边界。
- [dgas-notcap-sold-as-bundled](dgas-notcap-sold-as-bundled.md) 是 EIP-7935 客户端默认气限界（211/1458），不是本页单笔气帽边界。
