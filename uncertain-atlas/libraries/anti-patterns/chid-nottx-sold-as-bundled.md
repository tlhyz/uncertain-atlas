# 反模式：把 EIP-1344 config-chainid not already this-tx-155 / not already default-value / not already 161 正式三事（220 余量） 写成已经 这笔交易已经带了 EIP-155 标识 / 已经返回某个默认值 / 已经是不变量 161

**层次**：实现 / EIP-1344 config-chainid not already this-tx-155 / not already default-value / not already 161 正式三事（220 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344)（Final, Core, CHAINID opcode）。  
**对应**：[`../tracks/implementation/worked-example-chid-nottx-vs-bundled.md`](../tracks/implementation/worked-example-chid-nottx-vs-bundled.md)。

把 EIP-1344 config-chainid not already this-tx-155 / not already default-value / not already 161 正式三事（220 余量） 写成已经 这笔交易已经带了 EIP-155 标识 / 已经返回某个默认值 / 已经是不变量 161，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（220 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 220 / 161 / 218 / 1395 / 1397 糊成一句。

也不是：

- [chid-not155-sold-as-bundled](chid-not155-sold-as-bundled.md) 是 not155 单句边界（1395），不是本页边界。
- [chid-notfork-sold-as-bundled](chid-notfork-sold-as-bundled.md) 是 notfork 单句边界（1397），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
