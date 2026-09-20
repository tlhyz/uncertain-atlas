# 反模式：把 EIP-4788 contract-root not already finalized / not already 149 / not already 154 正式三事（156 余量） 写成已经 已经finalized / 已经是不变量 149 / 已经是不变量 154

**层次**：实现 / EIP-4788 contract-root not already finalized / not already 149 / not already 154 正式三事（156 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788)（Beacon block root in the EVM）。  
**对应**：[`../tracks/light-clients/worked-example-proot-notfin-vs-bundled.md`](../tracks/light-clients/worked-example-proot-notfin-vs-bundled.md)。

把 EIP-4788 contract-root not already finalized / not already 149 / not already 154 正式三事（156 余量） 写成已经 已经finalized / 已经是不变量 149 / 已经是不变量 154，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4788 parent-root 正式三事（156 余量），必须分开 not already current-head、not already finalized、not already permanent 三件事，不要和 156 / 149 / 154 / 1506 / 1508 糊成一句。

也不是：

- [proot-nothead-sold-as-bundled](proot-nothead-sold-as-bundled.md) 是 nothead 单句边界（1506），不是本页边界。
- [proot-notperm-sold-as-bundled](proot-notperm-sold-as-bundled.md) 是 notperm 单句边界（1508），不是本页边界。
- [bpof-notexec-sold-as-bundled](bpof-notexec-sold-as-bundled.md) 是 EIP-7892 BPO 边界（209/1503），不是本页父信标根边界。
