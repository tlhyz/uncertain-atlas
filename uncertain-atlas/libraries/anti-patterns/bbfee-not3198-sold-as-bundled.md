# 反模式：把 EIP-7516 BLOBBASEFEE opcode not already 3198-basefee / not already 218-bundled / not already 219-bundled 正式三事（219 余量） 写成已经 已经是执行层基础费指令 / 已经是不变量 218 / 已经 219 bundled

**层次**：实现 / EIP-7516 BLOBBASEFEE opcode not already 3198-basefee / not already 218-bundled / not already 219-bundled 正式三事（219 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7516](https://eips.ethereum.org/EIPS/eip-7516)（Final, Core, BLOBBASEFEE instruction）。  
**对应**：[`../tracks/implementation/worked-example-bbfee-not3198-vs-bundled.md`](../tracks/implementation/worked-example-bbfee-not3198-vs-bundled.md)。

把 EIP-7516 BLOBBASEFEE opcode not already 3198-basefee / not already 218-bundled / not already 219-bundled 正式三事（219 余量） 写成已经 已经是执行层基础费指令 / 已经是不变量 218 / 已经 219 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7516 BLOBBASEFEE 正式三事（219 余量），必须分开 not already 3198-basefee、not already one-gas、not already 4844-changed 三件事，不要和 219 / 218 / 158 / 1402 / 1403 糊成一句。

也不是：

- [bbfee-notone-sold-as-bundled](bbfee-notone-sold-as-bundled.md) 是 notone 单句边界（1402），不是本页边界。
- [bbfee-not4844-sold-as-bundled](bbfee-not4844-sold-as-bundled.md) 是 not4844 单句边界（1403），不是本页边界。
- [bfee-notmkt-sold-as-bundled](bfee-notmkt-sold-as-bundled.md) 是 EIP-3198 基础费指令边界（218/1398），不是本页 BLOBBASEFEE 边界。
