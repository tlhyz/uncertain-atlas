# 反模式：把 EIP-2929 retouch not already cold-again / not already forever-warm / not already 168 正式三事（169 余量） 写成已经 又是一次冷访问 / 已经永远热 / 已经是不变量 168

**层次**：实现 / EIP-2929 retouch not already cold-again / not already forever-warm / not already 168 正式三事（169 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2929](https://eips.ethereum.org/EIPS/eip-2929)（Final, Core, Gas cost increases for state access opcodes）。  
**对应**：[`../tracks/implementation/worked-example-cwarm-notrecold-vs-bundled.md`](../tracks/implementation/worked-example-cwarm-notrecold-vs-bundled.md)。

把 EIP-2929 retouch not already cold-again / not already forever-warm / not already 168 正式三事（169 余量） 写成已经 又是一次冷访问 / 已经永远热 / 已经是不变量 168，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2929 cold-vs-warm 正式三事（169 余量），必须分开 not already warm、not already cold-again、not already any-address-warm 三件事，不要和 169 / 168 / 101 / 1449 / 1451 糊成一句。

也不是：

- [cwarm-notwarm-sold-as-bundled](cwarm-notwarm-sold-as-bundled.md) 是 notwarm 单句边界（1449），不是本页边界。
- [cwarm-notany-sold-as-bundled](cwarm-notany-sold-as-bundled.md) 是 notany 单句边界（1451），不是本页边界。
- [cbase-notacc-sold-as-bundled](cbase-notacc-sold-as-bundled.md) 是 EIP-3651 出块者预填边界（187/1446），不是本页冷热边界。
