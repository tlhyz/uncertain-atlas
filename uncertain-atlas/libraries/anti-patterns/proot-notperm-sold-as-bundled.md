# 反模式：把 EIP-4788 ring-expire not already permanent / not already 195 / not already 145 正式三事（156 余量） 写成已经 已经永久可查 / 已经是不变量 195 / 已经是不变量 145

**层次**：实现 / EIP-4788 ring-expire not already permanent / not already 195 / not already 145 正式三事（156 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788)（Beacon block root in the EVM）。  
**对应**：[`../tracks/light-clients/worked-example-proot-notperm-vs-bundled.md`](../tracks/light-clients/worked-example-proot-notperm-vs-bundled.md)。

把 EIP-4788 ring-expire not already permanent / not already 195 / not already 145 正式三事（156 余量） 写成已经 已经永久可查 / 已经是不变量 195 / 已经是不变量 145，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4788 parent-root 正式三事（156 余量），必须分开 not already current-head、not already finalized、not already permanent 三件事，不要和 156 / 195 / 145 / 1506 / 1507 糊成一句。

也不是：

- [proot-nothead-sold-as-bundled](proot-nothead-sold-as-bundled.md) 是 nothead 单句边界（1506），不是本页边界。
- [proot-notfin-sold-as-bundled](proot-notfin-sold-as-bundled.md) 是 notfin 单句边界（1507），不是本页边界。
- [bpof-notexec-sold-as-bundled](bpof-notexec-sold-as-bundled.md) 是 EIP-7892 BPO 边界（209/1503），不是本页父信标根边界。
