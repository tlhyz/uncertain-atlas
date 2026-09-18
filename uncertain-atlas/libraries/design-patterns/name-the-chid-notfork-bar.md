# 模式：点名 chid-notfork 杠

**层次**：实现 / EIP-1344 compile-time chainid not already fork-safe / not already 712-domain / not already split-handled 正式三事（220 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344)（Final, Core, CHAINID opcode）。  
**对应**：[`../tracks/implementation/worked-example-chid-notfork-vs-bundled.md`](../tracks/implementation/worked-example-chid-notfork-vs-bundled.md)。

- **编译期写死的链号不是已经在硬分叉后仍安全 不是已经在硬分叉后仍安全：看见编译期写死的链号不是已经在硬分叉后仍安全，不是已经在硬分叉后仍安全 interchangeable / 1397 chid-notfork interchangeable。**
- **compile-time chainId is not already fork-safe 不是已经是 712 域：看见compile-time chainId is not already fork-safe，不是已经是 712 域 interchangeable / 1397 chid-notfork interchangeable。**
- **编译期写死的链号不是已经在硬分叉后仍安全 不是已经处理好有争议的分裂：看见编译期写死的链号不是已经在硬分叉后仍安全，不是已经处理好有争议的分裂 interchangeable / 1397 chid-notfork interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（220 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事。
