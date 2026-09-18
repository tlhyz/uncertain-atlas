# 模式：点名 sbal-notwarm 杠

**层次**：实现 / EIP-1884 reprice not already cold-warm / not already disk-O1 / not already 2929 正式三事（229 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884)（Final, Core, Repricing for trie-size-dependent opcodes）。  
**对应**：[`../tracks/implementation/worked-example-sbal-notwarm-vs-bundled.md`](../tracks/implementation/worked-example-sbal-notwarm-vs-bundled.md)。

- **树依赖涨价不是已经是本笔冷热 不是已经是本笔冷热：看见树依赖涨价不是已经是本笔冷热，不是已经是本笔冷热 interchangeable / 1433 sbal-notwarm interchangeable。**
- **trie-dependent reprice is not already cold-warm 不是已经是磁盘 O(1)：看见trie-dependent reprice is not already cold-warm，不是已经是磁盘 O(1) interchangeable / 1433 sbal-notwarm interchangeable。**
- **树依赖涨价不是已经是本笔冷热 不是已经是 2929：看见树依赖涨价不是已经是本笔冷热，不是已经是 2929 interchangeable / 1433 sbal-notwarm interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1884 SELFBALANCE 正式三事（229 余量），必须分开 not already BALANCE、not already self-priced、not already cold-warm 三件事。
