# 反模式：把 EIP-7917 lookahead-list not already preconfirm / not already safer / not already 134 正式三事（205 余量） 写成已经 已经是based预确认 / 已经更安全 / 已经是不变量 134

**层次**：实现 / EIP-7917 lookahead-list not already preconfirm / not already safer / not already 134 正式三事（205 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7917](https://eips.ethereum.org/EIPS/eip-7917)（Deterministic proposer lookahead）。  
**对应**：[`../tracks/consensus/worked-example-lkah-notpc-vs-bundled.md`](../tracks/consensus/worked-example-lkah-notpc-vs-bundled.md)。

把 EIP-7917 lookahead-list not already preconfirm / not already safer / not already 134 正式三事（205 余量） 写成已经 已经是based预确认 / 已经更安全 / 已经是不变量 134，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7917 lookahead 正式三事（205 余量），必须分开 not already schedule-locked、not already scheduled、not already preconfirm 三件事，不要和 205 / 27 / 134 / 1482 / 1483 糊成一句。

也不是：

- [lkah-notlock-sold-as-bundled](lkah-notlock-sold-as-bundled.md) 是 notlock 单句边界（1482），不是本页边界。
- [lkah-notbal-sold-as-bundled](lkah-notbal-sold-as-bundled.md) 是 notbal 单句边界（1483），不是本页边界。
- [exdom-notperm-sold-as-bundled](exdom-notperm-sold-as-bundled.md) 是 EIP-7044 退出域边界（213/1479），不是本页出块前瞻边界。
