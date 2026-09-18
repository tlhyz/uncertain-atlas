# 反模式：把 EIP-1344 compile-time chainid not already fork-safe / not already 712-domain / not already split-handled 正式三事（220 余量） 写成已经 已经在硬分叉后仍安全 / 已经是 712 域 / 已经处理好有争议的分裂

**层次**：实现 / EIP-1344 compile-time chainid not already fork-safe / not already 712-domain / not already split-handled 正式三事（220 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344)（Final, Core, CHAINID opcode）。  
**对应**：[`../tracks/implementation/worked-example-chid-notfork-vs-bundled.md`](../tracks/implementation/worked-example-chid-notfork-vs-bundled.md)。

把 EIP-1344 compile-time chainid not already fork-safe / not already 712-domain / not already split-handled 正式三事（220 余量） 写成已经 已经在硬分叉后仍安全 / 已经是 712 域 / 已经处理好有争议的分裂，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（220 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 220 / 218 / 219 / 1395 / 1396 糊成一句。

也不是：

- [chid-not155-sold-as-bundled](chid-not155-sold-as-bundled.md) 是 not155 单句边界（1395），不是本页边界。
- [chid-nottx-sold-as-bundled](chid-nottx-sold-as-bundled.md) 是 nottx 单句边界（1396），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
