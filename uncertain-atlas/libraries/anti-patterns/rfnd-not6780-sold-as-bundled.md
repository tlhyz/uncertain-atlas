# 反模式：把 EIP-3529 drop-selfdestruct-refund not already 6780-semantics / not already 160 / not already 1559 正式三事（223 余量） 写成已经 已经改了自毁语义 / 已经是不变量 160 / 已经是 1559

**层次**：实现 / EIP-3529 drop-selfdestruct-refund not already 6780-semantics / not already 160 / not already 1559 正式三事（223 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3529](https://eips.ethereum.org/EIPS/eip-3529)（Final, Core, Reduction in refunds）。  
**对应**：[`../tracks/implementation/worked-example-rfnd-not6780-vs-bundled.md`](../tracks/implementation/worked-example-rfnd-not6780-vs-bundled.md)。

把 EIP-3529 drop-selfdestruct-refund not already 6780-semantics / not already 160 / not already 1559 正式三事（223 余量） 写成已经 已经改了自毁语义 / 已经是不变量 160 / 已经是 1559，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3529 refund 正式三事（223 余量），必须分开 not already no-refund、not already 6780-semantics、not already mid-exec-spendable 三件事，不要和 223 / 160 / 159 / 1413 / 1415 糊成一句。

也不是：

- [rfnd-notgone-sold-as-bundled](rfnd-notgone-sold-as-bundled.md) 是 notgone 单句边界（1413），不是本页边界。
- [rfnd-notmid-sold-as-bundled](rfnd-notmid-sold-as-bundled.md) 是 notmid 单句边界（1415），不是本页边界。
- [mcpy-notid-sold-as-bundled](mcpy-notid-sold-as-bundled.md) 是 EIP-5656 内存拷边界（216/1410），不是本页退款边界。
