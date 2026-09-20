# 模式：点名 proot-notperm 杠

**层次**：实现 / EIP-4788 ring-expire not already permanent / not already 195 / not already 145 正式三事（156 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788)（Beacon block root in the EVM）。  
**对应**：[`../tracks/light-clients/worked-example-proot-notperm-vs-bundled.md`](../tracks/light-clients/worked-example-proot-notperm-vs-bundled.md)。

- **环缓冲过期不是根已经永久可查 不是已经永久可查：看见环缓冲过期不是根已经永久可查，不是已经永久可查 interchangeable / 1508 proot-notperm interchangeable。**
- **a ring-buffer expiry is not already a permanent root 不是已经是不变量 195：看见a ring-buffer expiry is not already a permanent root，不是已经是不变量 195 interchangeable / 1508 proot-notperm interchangeable。**
- **环缓冲过期不是根已经永久可查 不是已经是不变量 145：看见环缓冲过期不是根已经永久可查，不是已经是不变量 145 interchangeable / 1508 proot-notperm interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4788 parent-root 正式三事（156 余量），必须分开 not already current-head、not already finalized、not already permanent 三件事。
