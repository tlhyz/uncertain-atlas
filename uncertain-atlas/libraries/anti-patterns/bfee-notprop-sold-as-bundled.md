# 反模式：把 EIP-3198 read-basefee not already paid-to-proposer / not already blob-basefee / not already 219 正式三事（218 余量） 写成已经 已经给了出块者 / 已经是 blob 基础费指令 / 已经是不变量 219

**层次**：实现 / EIP-3198 read-basefee not already paid-to-proposer / not already blob-basefee / not already 219 正式三事（218 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3198](https://eips.ethereum.org/EIPS/eip-3198)（Final, Core, BASEFEE opcode）。  
**对应**：[`../tracks/implementation/worked-example-bfee-notprop-vs-bundled.md`](../tracks/implementation/worked-example-bfee-notprop-vs-bundled.md)。

把 EIP-3198 read-basefee not already paid-to-proposer / not already blob-basefee / not already 219 正式三事（218 余量） 写成已经 已经给了出块者 / 已经是 blob 基础费指令 / 已经是不变量 219，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3198 BASEFEE 正式三事（218 余量），必须分开 not already 1559-market、not already paid-to-proposer、not already header-changed 三件事，不要和 218 / 158 / 219 / 1398 / 1400 糊成一句。

也不是：

- [bfee-notmkt-sold-as-bundled](bfee-notmkt-sold-as-bundled.md) 是 notmkt 单句边界（1398），不是本页边界。
- [bfee-nothdr-sold-as-bundled](bfee-nothdr-sold-as-bundled.md) 是 nothdr 单句边界（1400），不是本页边界。
- [chid-not155-sold-as-bundled](chid-not155-sold-as-bundled.md) 是 EIP-1344 链号指令边界（220/1395），不是本页 BASEFEE 边界。
