# 模式：点名 txcap-notpool 杠

**层次**：实现 / EIP-7825 pool-reject not already block-verified / not already 197 / not already 96 正式三事（203 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7825](https://eips.ethereum.org/EIPS/eip-7825)（Transaction Gas Limit Cap）。  
**对应**：[`../tracks/implementation/worked-example-txcap-notpool-vs-bundled.md`](../tracks/implementation/worked-example-txcap-notpool-vs-bundled.md)。

- **入池拒掉不是已经验过块 不是已经验过块：看见入池拒掉不是已经验过块，不是已经验过块 interchangeable / 1462 txcap-notpool interchangeable。**
- **pool reject is not already block-verified 不是已经是不变量 197：看见pool reject is not already block-verified，不是已经是不变量 197 interchangeable / 1462 txcap-notpool interchangeable。**
- **入池拒掉不是已经验过块 不是已经是不变量 96：看见入池拒掉不是已经验过块，不是已经是不变量 96 interchangeable / 1462 txcap-notpool interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7825 tx-gas-cap 正式三事（203 余量），必须分开 not already block-gas、not already block-verified、not already policy-only 三件事。
