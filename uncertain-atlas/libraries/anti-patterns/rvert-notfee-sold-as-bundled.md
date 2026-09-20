# 反模式：把 EIP-140 unpaid-self-fee not already leftover-semantics / not already 103 / not already free 正式三事（177 余量） 写成已经 已经按回滚语义留下剩余气 / 已经是 103 空户回滚 / 已经免费

**层次**：实现 / EIP-140 unpaid-self-fee not already leftover-semantics / not already 103 / not already free 正式三事（177 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-140](https://eips.ethereum.org/EIPS/eip-140)（Final, Core, REVERT instruction）。  
**对应**：[`../tracks/implementation/worked-example-rvert-notfee-vs-bundled.md`](../tracks/implementation/worked-example-rvert-notfee-vs-bundled.md)。

把 EIP-140 unpaid-self-fee not already leftover-semantics / not already 103 / not already free 正式三事（177 余量） 写成已经 已经按回滚语义留下剩余气 / 已经是 103 空户回滚 / 已经免费，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（177 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事，不要和 177 / 103 / 176 / 1380 / 1382 糊成一句。

也不是：

- [rvert-notburn-sold-as-bundled](rvert-notburn-sold-as-bundled.md) 是 notburn 单句边界（1380），不是本页边界。
- [rvert-notdep-sold-as-bundled](rvert-notdep-sold-as-bundled.md) 是 notdep 单句边界（1382），不是本页边界。
- [hstead-notfee-sold-as-bundled](hstead-notfee-sold-as-bundled.md) 是 Homestead 创建费边界（234/1346），不是本页 DELEGATECALL 边界。
