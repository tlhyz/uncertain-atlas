# 反模式：把 EIP-3860 initcode-bound not already 170-runtime / not already 1014 / not already 176-bundled 正式三事（176 余量） 写成已经 已经是部署代码超界 / 已经是 1014 哈希费 / 已经 176 bundled

**层次**：实现 / EIP-3860 initcode-bound not already 170-runtime / not already 1014 / not already 176-bundled 正式三事（176 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3860](https://eips.ethereum.org/EIPS/eip-3860)（Final, Core, Limit and meter initcode）。  
**对应**：[`../tracks/implementation/worked-example-icode-not170-vs-bundled.md`](../tracks/implementation/worked-example-icode-not170-vs-bundled.md)。

把 EIP-3860 initcode-bound not already 170-runtime / not already 1014 / not already 176-bundled 正式三事（176 余量） 写成已经 已经是部署代码超界 / 已经是 1014 哈希费 / 已经 176 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3860 initcode 正式三事（176 余量），必须分开 not already 170-runtime、not already CREATE-fail、not already ran-initcode 三件事，不要和 176 / 185 / 175 / 1438 / 1439 糊成一句。

也不是：

- [icode-nottx-sold-as-bundled](icode-nottx-sold-as-bundled.md) 是 nottx 单句边界（1438），不是本页边界。
- [icode-notrun-sold-as-bundled](icode-notrun-sold-as-bundled.md) 是 notrun 单句边界（1439），不是本页边界。
- [b2f-nothash-sold-as-bundled](b2f-nothash-sold-as-bundled.md) 是 EIP-152 BLAKE2F 边界（230/1434），不是本页 initcode 边界。
