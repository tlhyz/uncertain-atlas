# 反模式：把 EIP-211 this-page not already calldata / not already two-call-length / not already still-after-next 正式三事（232 余量） 写成已经 已经是 calldata / 已经用两次调用先问长度 / 下一次类调用之后缓冲还在

**层次**：实现 / EIP-211 this-page not already calldata / not already two-call-length / not already still-after-next 正式三事（232 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-211](https://eips.ethereum.org/EIPS/eip-211)（Final, Core, RETURNDATASIZE / RETURNDATACOPY）。  
**对应**：[`../tracks/implementation/worked-example-rdata-notcalld-vs-bundled.md`](../tracks/implementation/worked-example-rdata-notcalld-vs-bundled.md)。

把 EIP-211 this-page not already calldata / not already two-call-length / not already still-after-next 正式三事（232 余量） 写成已经 已经是 calldata / 已经用两次调用先问长度 / 下一次类调用之后缓冲还在，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（232 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 232 / 217 / 231 / 1386 / 1388 糊成一句。

也不是：

- [rdata-notmem-sold-as-bundled](rdata-notmem-sold-as-bundled.md) 是 notmem 单句边界（1386），不是本页边界。
- [rdata-not140-sold-as-bundled](rdata-not140-sold-as-bundled.md) 是 not140 单句边界（1388），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
