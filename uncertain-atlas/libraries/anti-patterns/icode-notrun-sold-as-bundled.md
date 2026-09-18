# 反模式：把 EIP-3860 jumpdest-fee not already ran-initcode / not already CREATE2-hash-fee / not already created 正式三事（176 余量） 写成已经 已经跑完 initcode / 已经是 CREATE2 算地址的哈希费 / 已经创建

**层次**：实现 / EIP-3860 jumpdest-fee not already ran-initcode / not already CREATE2-hash-fee / not already created 正式三事（176 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3860](https://eips.ethereum.org/EIPS/eip-3860)（Final, Core, Limit and meter initcode）。  
**对应**：[`../tracks/implementation/worked-example-icode-notrun-vs-bundled.md`](../tracks/implementation/worked-example-icode-notrun-vs-bundled.md)。

把 EIP-3860 jumpdest-fee not already ran-initcode / not already CREATE2-hash-fee / not already created 正式三事（176 余量） 写成已经 已经跑完 initcode / 已经是 CREATE2 算地址的哈希费 / 已经创建，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3860 initcode 正式三事（176 余量），必须分开 not already 170-runtime、not already CREATE-fail、not already ran-initcode 三件事，不要和 176 / 185 / 188 / 1437 / 1438 糊成一句。

也不是：

- [icode-not170-sold-as-bundled](icode-not170-sold-as-bundled.md) 是 not170 单句边界（1437），不是本页边界。
- [icode-nottx-sold-as-bundled](icode-nottx-sold-as-bundled.md) 是 nottx 单句边界（1438），不是本页边界。
- [b2f-nothash-sold-as-bundled](b2f-nothash-sold-as-bundled.md) 是 EIP-152 BLAKE2F 边界（230/1434），不是本页 initcode 边界。
