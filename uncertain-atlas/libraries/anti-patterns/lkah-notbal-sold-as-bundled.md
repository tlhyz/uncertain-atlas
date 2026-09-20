# 反模式：把 EIP-7917 balance-still-moves not already scheduled / not already 196 / not already 27 正式三事（205 余量） 写成已经 已经排完 / 已经是不变量 196 / 已经是不变量 27

**层次**：实现 / EIP-7917 balance-still-moves not already scheduled / not already 196 / not already 27 正式三事（205 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7917](https://eips.ethereum.org/EIPS/eip-7917)（Deterministic proposer lookahead）。  
**对应**：[`../tracks/consensus/worked-example-lkah-notbal-vs-bundled.md`](../tracks/consensus/worked-example-lkah-notbal-vs-bundled.md)。

把 EIP-7917 balance-still-moves not already scheduled / not already 196 / not already 27 正式三事（205 余量） 写成已经 已经排完 / 已经是不变量 196 / 已经是不变量 27，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7917 lookahead 正式三事（205 余量），必须分开 not already schedule-locked、not already scheduled、not already preconfirm 三件事，不要和 205 / 196 / 27 / 1482 / 1484 糊成一句。

也不是：

- [lkah-notlock-sold-as-bundled](lkah-notlock-sold-as-bundled.md) 是 notlock 单句边界（1482），不是本页边界。
- [lkah-notpc-sold-as-bundled](lkah-notpc-sold-as-bundled.md) 是 notpc 单句边界（1484），不是本页边界。
- [exdom-notperm-sold-as-bundled](exdom-notperm-sold-as-bundled.md) 是 EIP-7044 退出域边界（213/1479），不是本页出块前瞻边界。
