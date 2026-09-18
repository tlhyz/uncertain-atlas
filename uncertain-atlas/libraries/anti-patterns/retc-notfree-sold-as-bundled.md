# 反模式：把 EIP-170 constant-CALL-gas not already free-disk / not already no-proof-cost / not already 170-inv 正式三事（185 余量） 写成已经 已经没有按长度的磁盘/证明代价 / 已经是不变量 170 / 已经免费

**层次**：实现 / EIP-170 constant-CALL-gas not already free-disk / not already no-proof-cost / not already 170-inv 正式三事（185 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-170](https://eips.ethereum.org/EIPS/eip-170)（Final, Core, Contract code size limit）。  
**对应**：[`../tracks/implementation/worked-example-retc-notfree-vs-bundled.md`](../tracks/implementation/worked-example-retc-notfree-vs-bundled.md)。

把 EIP-170 constant-CALL-gas not already free-disk / not already no-proof-cost / not already 170-inv 正式三事（185 余量） 写成已经 已经没有按长度的磁盘/证明代价 / 已经是不变量 170 / 已经免费，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-170 returned 正式三事（185 余量），必须分开 not already initcode-bound、not already whole-tx-illegal、not already free-disk 三件事，不要和 185 / 170 / 176 / 1440 / 1441 糊成一句。

也不是：

- [retc-notinit-sold-as-bundled](retc-notinit-sold-as-bundled.md) 是 notinit 单句边界（1440），不是本页边界。
- [retc-nottx-sold-as-bundled](retc-nottx-sold-as-bundled.md) 是 nottx 单句边界（1441），不是本页边界。
- [icode-not170-sold-as-bundled](icode-not170-sold-as-bundled.md) 是 EIP-3860 initcode 边界（176/1437），不是本页返回代码边界。
