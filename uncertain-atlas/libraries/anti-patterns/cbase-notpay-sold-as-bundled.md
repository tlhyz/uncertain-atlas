# 反模式：把 EIP-3651 warm-start not already paid / not already 1559 / not already 158 正式三事（187 余量） 写成已经 已经付给出块者 / 已经是 1559 小费 / 已经是不变量 158

**层次**：实现 / EIP-3651 warm-start not already paid / not already 1559 / not already 158 正式三事（187 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3651](https://eips.ethereum.org/EIPS/eip-3651)（Final, Core, Warm COINBASE）。  
**对应**：[`../tracks/implementation/worked-example-cbase-notpay-vs-bundled.md`](../tracks/implementation/worked-example-cbase-notpay-vs-bundled.md)。

把 EIP-3651 warm-start not already paid / not already 1559 / not already 158 正式三事（187 余量） 写成已经 已经付给出块者 / 已经是 1559 小费 / 已经是不变量 158，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3651 coinbase 正式三事（187 余量），必须分开 not already accessed、not already paid、not already 169-prefill 三件事，不要和 187 / 158 / 169 / 1446 / 1448 糊成一句。

也不是：

- [cbase-notacc-sold-as-bundled](cbase-notacc-sold-as-bundled.md) 是 notacc 单句边界（1446），不是本页边界。
- [cbase-not169-sold-as-bundled](cbase-not169-sold-as-bundled.md) 是 not169 单句边界（1448），不是本页边界。
- [rpfx-noteof-sold-as-bundled](rpfx-noteof-sold-as-bundled.md) 是 EIP-3541 保留首字节边界（188/1443），不是本页出块者预填边界。
