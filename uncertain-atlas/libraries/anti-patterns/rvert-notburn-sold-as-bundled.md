# 反模式：把 EIP-140 leftover-gas revert not already INVALID-burn / not already OOG-burn / not already 177-bundled 正式三事（177 余量） 写成已经 已经像非法指令那样烧光剩余气 / 已经是气耗尽烧光 / 已经 177 bundled

**层次**：实现 / EIP-140 leftover-gas revert not already INVALID-burn / not already OOG-burn / not already 177-bundled 正式三事（177 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-140](https://eips.ethereum.org/EIPS/eip-140)（Final, Core, REVERT instruction）。  
**对应**：[`../tracks/implementation/worked-example-rvert-notburn-vs-bundled.md`](../tracks/implementation/worked-example-rvert-notburn-vs-bundled.md)。

把 EIP-140 leftover-gas revert not already INVALID-burn / not already OOG-burn / not already 177-bundled 正式三事（177 余量） 写成已经 已经像非法指令那样烧光剩余气 / 已经是气耗尽烧光 / 已经 177 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（177 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 177 / 103 / 232 / 1381 / 1382 糊成一句。

也不是：

- [rvert-notfee-sold-as-bundled](rvert-notfee-sold-as-bundled.md) 是 notfee 单句边界（1381），不是本页边界。
- [rvert-notdep-sold-as-bundled](rvert-notdep-sold-as-bundled.md) 是 notdep 单句边界（1382），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
