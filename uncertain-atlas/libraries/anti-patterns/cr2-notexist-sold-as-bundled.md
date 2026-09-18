# 反模式：把 EIP-1014 salt-address not already created / not already has-code / not already paid-create 正式三事（222 余量） 写成已经 已经创建 / 已经有那份代码 / 已经付过创建费

**层次**：实现 / EIP-1014 salt-address not already created / not already has-code / not already paid-create 正式三事（222 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1014](https://eips.ethereum.org/EIPS/eip-1014)（Final, Core, Skinny CREATE2）。  
**对应**：[`../tracks/implementation/worked-example-cr2-notexist-vs-bundled.md`](../tracks/implementation/worked-example-cr2-notexist-vs-bundled.md)。

把 EIP-1014 salt-address not already created / not already has-code / not already paid-create 正式三事（222 余量） 写成已经 已经创建 / 已经有那份代码 / 已经付过创建费，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（222 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 222 / 160 / 221 / 1389 / 1391 糊成一句。

也不是：

- [cr2-notcre-sold-as-bundled](cr2-notcre-sold-as-bundled.md) 是 notcre 单句边界（1389），不是本页边界。
- [cr2-notover-sold-as-bundled](cr2-notover-sold-as-bundled.md) 是 notover 单句边界（1391），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
