# 反模式：把 EIP-1884 selfbalance not already BALANCE / not already stack-pop-balance / not already 229-bundled 正式三事（229 余量） 写成已经 已经是按地址查余额 / 已经改了余额语义 / 已经 229 bundled

**层次**：实现 / EIP-1884 selfbalance not already BALANCE / not already stack-pop-balance / not already 229-bundled 正式三事（229 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884)（Final, Core, Repricing for trie-size-dependent opcodes）。  
**对应**：[`../tracks/implementation/worked-example-sbal-notbal-vs-bundled.md`](../tracks/implementation/worked-example-sbal-notbal-vs-bundled.md)。

把 EIP-1884 selfbalance not already BALANCE / not already stack-pop-balance / not already 229-bundled 正式三事（229 余量） 写成已经 已经是按地址查余额 / 已经改了余额语义 / 已经 229 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1884 SELFBALANCE 正式三事（229 余量），必须分开 not already BALANCE、not already self-priced、not already cold-warm 三件事，不要和 229 / 169 / 221 / 1432 / 1433 糊成一句。

也不是：

- [sbal-notself-sold-as-bundled](sbal-notself-sold-as-bundled.md) 是 notself 单句边界（1432），不是本页边界。
- [sbal-notwarm-sold-as-bundled](sbal-notwarm-sold-as-bundled.md) 是 notwarm 单句边界（1433），不是本页边界。
- [bn128-notalgo-sold-as-bundled](bn128-notalgo-sold-as-bundled.md) 是 EIP-1108 bn128 降价边界（228/1428），不是本页 SELFBALANCE 边界。
