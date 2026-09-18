# 反模式：把 EIP-3529 refund-counter not already mid-exec-spendable / not already gaslimit-cap / not already 158 正式三事（223 余量） 写成已经 已经能在执行当中用 / 已经是本块实际能烧掉的上限 / 已经是不变量 158

**层次**：实现 / EIP-3529 refund-counter not already mid-exec-spendable / not already gaslimit-cap / not already 158 正式三事（223 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3529](https://eips.ethereum.org/EIPS/eip-3529)（Final, Core, Reduction in refunds）。  
**对应**：[`../tracks/implementation/worked-example-rfnd-notmid-vs-bundled.md`](../tracks/implementation/worked-example-rfnd-notmid-vs-bundled.md)。

把 EIP-3529 refund-counter not already mid-exec-spendable / not already gaslimit-cap / not already 158 正式三事（223 余量） 写成已经 已经能在执行当中用 / 已经是本块实际能烧掉的上限 / 已经是不变量 158，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3529 refund 正式三事（223 余量），必须分开 not already no-refund、not already 6780-semantics、not already mid-exec-spendable 三件事，不要和 223 / 158 / 169 / 1413 / 1414 糊成一句。

也不是：

- [rfnd-notgone-sold-as-bundled](rfnd-notgone-sold-as-bundled.md) 是 notgone 单句边界（1413），不是本页边界。
- [rfnd-not6780-sold-as-bundled](rfnd-not6780-sold-as-bundled.md) 是 not6780 单句边界（1414），不是本页边界。
- [mcpy-notid-sold-as-bundled](mcpy-notid-sold-as-bundled.md) 是 EIP-5656 内存拷边界（216/1410），不是本页退款边界。
