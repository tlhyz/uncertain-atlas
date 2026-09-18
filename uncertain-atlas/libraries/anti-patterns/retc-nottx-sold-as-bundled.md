# 反模式：把 EIP-170 oog-fail not already whole-tx-illegal / not already leftover-gas / not already 177 正式三事（185 余量） 写成已经 已经整笔非法 / 已经是带回剩余气的回滚 / 已经是不变量 177

**层次**：实现 / EIP-170 oog-fail not already whole-tx-illegal / not already leftover-gas / not already 177 正式三事（185 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-170](https://eips.ethereum.org/EIPS/eip-170)（Final, Core, Contract code size limit）。  
**对应**：[`../tracks/implementation/worked-example-retc-nottx-vs-bundled.md`](../tracks/implementation/worked-example-retc-nottx-vs-bundled.md)。

把 EIP-170 oog-fail not already whole-tx-illegal / not already leftover-gas / not already 177 正式三事（185 余量） 写成已经 已经整笔非法 / 已经是带回剩余气的回滚 / 已经是不变量 177，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-170 returned 正式三事（185 余量），必须分开 not already initcode-bound、not already whole-tx-illegal、not already free-disk 三件事，不要和 185 / 177 / 176 / 1440 / 1442 糊成一句。

也不是：

- [retc-notinit-sold-as-bundled](retc-notinit-sold-as-bundled.md) 是 notinit 单句边界（1440），不是本页边界。
- [retc-notfree-sold-as-bundled](retc-notfree-sold-as-bundled.md) 是 notfree 单句边界（1442），不是本页边界。
- [icode-not170-sold-as-bundled](icode-not170-sold-as-bundled.md) 是 EIP-3860 initcode 边界（176/1437），不是本页返回代码边界。
