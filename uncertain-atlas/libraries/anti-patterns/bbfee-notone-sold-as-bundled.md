# 反模式：把 EIP-7516 read-blobbasefee not already one-gas / not already 145-bundled / not already 201 正式三事（219 余量） 写成已经 已经并成一套气 / 已经是不变量 145 / 已经是不变量 201

**层次**：实现 / EIP-7516 read-blobbasefee not already one-gas / not already 145-bundled / not already 201 正式三事（219 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7516](https://eips.ethereum.org/EIPS/eip-7516)（Final, Core, BLOBBASEFEE instruction）。  
**对应**：[`../tracks/implementation/worked-example-bbfee-notone-vs-bundled.md`](../tracks/implementation/worked-example-bbfee-notone-vs-bundled.md)。

把 EIP-7516 read-blobbasefee not already one-gas / not already 145-bundled / not already 201 正式三事（219 余量） 写成已经 已经并成一套气 / 已经是不变量 145 / 已经是不变量 201，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7516 BLOBBASEFEE 正式三事（219 余量），必须分开 not already 3198-basefee、not already one-gas、not already 4844-changed 三件事，不要和 219 / 145 / 201 / 1401 / 1403 糊成一句。

也不是：

- [bbfee-not3198-sold-as-bundled](bbfee-not3198-sold-as-bundled.md) 是 not3198 单句边界（1401），不是本页边界。
- [bbfee-not4844-sold-as-bundled](bbfee-not4844-sold-as-bundled.md) 是 not4844 单句边界（1403），不是本页边界。
- [bfee-notmkt-sold-as-bundled](bfee-notmkt-sold-as-bundled.md) 是 EIP-3198 基础费指令边界（218/1398），不是本页 BLOBBASEFEE 边界。
