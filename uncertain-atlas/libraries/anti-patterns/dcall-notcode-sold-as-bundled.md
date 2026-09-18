# 反模式：把 EIP-7 DELEGATECALL not already CALLCODE / not already same-sender-CALLCODE / not already 233-bundled 正式三事（233 余量） 写成已经 已经是 CALLCODE / 已经是同一发送者的 CALLCODE / 已经 Homestead 委托 bundled

**层次**：实现 / EIP-7 DELEGATECALL not already CALLCODE / not already same-sender-CALLCODE / not already 233-bundled 正式三事（233 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7](https://eips.ethereum.org/EIPS/eip-7)（Final, Core, Homestead, DELEGATECALL）。  
**对应**：[`../tracks/implementation/worked-example-dcall-notcode-vs-bundled.md`](../tracks/implementation/worked-example-dcall-notcode-vs-bundled.md)。

把 EIP-7 DELEGATECALL not already CALLCODE / not already same-sender-CALLCODE / not already 233-bundled 正式三事（233 余量） 写成已经 已经是 CALLCODE / 已经是同一发送者的 CALLCODE / 已经 Homestead 委托 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（233 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 233 / 119 / 190 / 1378 / 1379 糊成一句。

也不是：

- [dcall-notcall-sold-as-bundled](dcall-notcall-sold-as-bundled.md) 是 notcall 单句边界（1378），不是本页边界。
- [dcall-not7702-sold-as-bundled](dcall-not7702-sold-as-bundled.md) 是 not7702 单句边界（1379），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
