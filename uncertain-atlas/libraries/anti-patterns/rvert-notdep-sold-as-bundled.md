# 反模式：把 EIP-140 create-revert not already deployed / not already occupied / not already starknet-reverted 正式三事（177 余量） 写成已经 已经部署 / 已经占址 / 已经是另一条链的 REVERTED 档

**层次**：实现 / EIP-140 create-revert not already deployed / not already occupied / not already starknet-reverted 正式三事（177 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-140](https://eips.ethereum.org/EIPS/eip-140)（Final, Core, REVERT instruction）。  
**对应**：[`../tracks/implementation/worked-example-rvert-notdep-vs-bundled.md`](../tracks/implementation/worked-example-rvert-notdep-vs-bundled.md)。

把 EIP-140 create-revert not already deployed / not already occupied / not already starknet-reverted 正式三事（177 余量） 写成已经 已经部署 / 已经占址 / 已经是另一条链的 REVERTED 档，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（177 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 177 / 138 / 178 / 1380 / 1381 糊成一句。

也不是：

- [rvert-notburn-sold-as-bundled](rvert-notburn-sold-as-bundled.md) 是 notburn 单句边界（1380），不是本页边界。
- [rvert-notfee-sold-as-bundled](rvert-notfee-sold-as-bundled.md) 是 notfee 单句边界（1381），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
