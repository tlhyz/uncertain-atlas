# 模式：点名 cwarm-notwarm 杠

**层次**：实现 / EIP-2929 first-touch not already warm / not already next-tx / not already 169-bundled 正式三事（169 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2929](https://eips.ethereum.org/EIPS/eip-2929)（Final, Core, Gas cost increases for state access opcodes）。  
**对应**：[`../tracks/implementation/worked-example-cwarm-notwarm-vs-bundled.md`](../tracks/implementation/worked-example-cwarm-notwarm-vs-bundled.md)。

- **本笔第一次碰不是已经是热的 不是已经是热的：看见本笔第一次碰不是已经是热的，不是已经是热的 interchangeable / 1449 cwarm-notwarm interchangeable。**
- **first touch this tx is not already warm 不是已经是下一笔还热：看见first touch this tx is not already warm，不是已经是下一笔还热 interchangeable / 1449 cwarm-notwarm interchangeable。**
- **本笔第一次碰不是已经是热的 不是已经 169 bundled：看见本笔第一次碰不是已经是热的，不是已经 169 bundled interchangeable / 1449 cwarm-notwarm interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2929 cold-vs-warm 正式三事（169 余量），必须分开 not already warm、not already cold-again、not already any-address-warm 三件事。
