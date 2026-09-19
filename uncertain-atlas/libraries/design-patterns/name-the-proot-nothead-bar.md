# 模式：点名 proot-nothead 杠

**层次**：实现 / EIP-4788 parent-root not already current-head / not already 127 / not already 156-bundled 正式三事（156 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788)（Beacon block root in the EVM）。  
**对应**：[`../tracks/light-clients/worked-example-proot-nothead-vs-bundled.md`](../tracks/light-clients/worked-example-proot-nothead-vs-bundled.md)。

- **头里的父信标根不是当前信标头 不是已经是当前信标头：看见头里的父信标根不是当前信标头，不是已经是当前信标头 interchangeable / 1506 proot-nothead interchangeable。**
- **the parent beacon root is not already the current head 不是已经是不变量 127：看见the parent beacon root is not already the current head，不是已经是不变量 127 interchangeable / 1506 proot-nothead interchangeable。**
- **头里的父信标根不是当前信标头 不是已经 156 bundled：看见头里的父信标根不是当前信标头，不是已经 156 bundled interchangeable / 1506 proot-nothead interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4788 parent-root 正式三事（156 余量），必须分开 not already current-head、not already finalized、not already permanent 三件事。
