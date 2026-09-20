# 反模式：把 EIP-3860 create-tx-oversize not already CREATE-fail / not already 2681 / not already in-EVM 正式三事（176 余量） 写成已经 已经是 CREATE 指令失败 / 已经是 2681 序号上限 / 已经进 EVM 再失败

**层次**：实现 / EIP-3860 create-tx-oversize not already CREATE-fail / not already 2681 / not already in-EVM 正式三事（176 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3860](https://eips.ethereum.org/EIPS/eip-3860)（Final, Core, Limit and meter initcode）。  
**对应**：[`../tracks/implementation/worked-example-icode-nottx-vs-bundled.md`](../tracks/implementation/worked-example-icode-nottx-vs-bundled.md)。

把 EIP-3860 create-tx-oversize not already CREATE-fail / not already 2681 / not already in-EVM 正式三事（176 余量） 写成已经 已经是 CREATE 指令失败 / 已经是 2681 序号上限 / 已经进 EVM 再失败，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3860 initcode 正式三事（176 余量），必须分开 not already 170-runtime、not already CREATE-fail、not already ran-initcode 三件事，不要和 176 / 175 / 169 / 1437 / 1439 糊成一句。

也不是：

- [icode-not170-sold-as-bundled](icode-not170-sold-as-bundled.md) 是 not170 单句边界（1437），不是本页边界。
- [icode-notrun-sold-as-bundled](icode-notrun-sold-as-bundled.md) 是 notrun 单句边界（1439），不是本页边界。
- [b2f-nothash-sold-as-bundled](b2f-nothash-sold-as-bundled.md) 是 EIP-152 BLAKE2F 边界（230/1434），不是本页 initcode 边界。
