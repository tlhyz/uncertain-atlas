# 反模式：把 EIP-2929 first-touch not already warm / not already next-tx / not already 169-bundled 正式三事（169 余量） 写成已经 已经是热的 / 已经是下一笔还热 / 已经 169 bundled

**层次**：实现 / EIP-2929 first-touch not already warm / not already next-tx / not already 169-bundled 正式三事（169 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2929](https://eips.ethereum.org/EIPS/eip-2929)（Final, Core, Gas cost increases for state access opcodes）。  
**对应**：[`../tracks/implementation/worked-example-cwarm-notwarm-vs-bundled.md`](../tracks/implementation/worked-example-cwarm-notwarm-vs-bundled.md)。

把 EIP-2929 first-touch not already warm / not already next-tx / not already 169-bundled 正式三事（169 余量） 写成已经 已经是热的 / 已经是下一笔还热 / 已经 169 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2929 cold-vs-warm 正式三事（169 余量），必须分开 not already warm、not already cold-again、not already any-address-warm 三件事，不要和 169 / 168 / 187 / 1450 / 1451 糊成一句。

也不是：

- [cwarm-notrecold-sold-as-bundled](cwarm-notrecold-sold-as-bundled.md) 是 notrecold 单句边界（1450），不是本页边界。
- [cwarm-notany-sold-as-bundled](cwarm-notany-sold-as-bundled.md) 是 notany 单句边界（1451），不是本页边界。
- [cbase-notacc-sold-as-bundled](cbase-notacc-sold-as-bundled.md) 是 EIP-3651 出块者预填边界（187/1446），不是本页冷热边界。
