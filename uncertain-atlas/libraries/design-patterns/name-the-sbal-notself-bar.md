# 模式：点名 sbal-notself 杠

**层次**：实现 / EIP-1884 self-query not already self-priced / not already cheaper-BALANCE / not already 1884-done 正式三事（229 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884)（Final, Core, Repricing for trie-size-dependent opcodes）。  
**对应**：[`../tracks/implementation/worked-example-sbal-notself-vs-bundled.md`](../tracks/implementation/worked-example-sbal-notself-vs-bundled.md)。

- **给自己查余额不是已经按本账户价扣 不是已经按本账户价扣：看见给自己查余额不是已经按本账户价扣，不是已经按本账户价扣 interchangeable / 1432 sbal-notself interchangeable。**
- **self-query is not already self-priced 不是已经是更便宜的按地址查：看见self-query is not already self-priced，不是已经是更便宜的按地址查 interchangeable / 1432 sbal-notself interchangeable。**
- **给自己查余额不是已经按本账户价扣 不是已经做完 1884：看见给自己查余额不是已经按本账户价扣，不是已经做完 1884 interchangeable / 1432 sbal-notself interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1884 SELFBALANCE 正式三事（229 余量），必须分开 not already BALANCE、not already self-priced、not already cold-warm 三件事。
