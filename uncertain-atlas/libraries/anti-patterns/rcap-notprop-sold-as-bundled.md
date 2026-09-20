# 反模式：把 EIP-7934 gossip-drop not already el-illegal / not already 96 / not already 158 正式三事（202 余量） 写成已经 已经让执行层非法 / 已经是不变量 96 / 已经是不变量 158

**层次**：实现 / EIP-7934 gossip-drop not already el-illegal / not already 96 / not already 158 正式三事（202 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7934](https://eips.ethereum.org/EIPS/eip-7934)（RLP Execution Block Size Limit）。  
**对应**：[`../tracks/implementation/worked-example-rcap-notprop-vs-bundled.md`](../tracks/implementation/worked-example-rcap-notprop-vs-bundled.md)。

把 EIP-7934 gossip-drop not already el-illegal / not already 96 / not already 158 正式三事（202 余量） 写成已经 已经让执行层非法 / 已经是不变量 96 / 已经是不变量 158，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7934 rlp-cap 正式三事（202 余量），必须分开 not already gas-limit、not already el-illegal、not already one-encoding 三件事，不要和 202 / 96 / 158 / 1464 / 1466 糊成一句。

也不是：

- [rcap-notgas-sold-as-bundled](rcap-notgas-sold-as-bundled.md) 是 notgas 单句边界（1464），不是本页边界。
- [rcap-notone-sold-as-bundled](rcap-notone-sold-as-bundled.md) 是 notone 单句边界（1466），不是本页边界。
- [txcap-notblk-sold-as-bundled](txcap-notblk-sold-as-bundled.md) 是 EIP-7825 单笔气帽边界（203/1461），不是本页编码硬帽边界。
