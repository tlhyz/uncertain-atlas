# 反模式：把 EIP-3651 warm-start not already 169-prefill / not already 2930 / not already 163 正式三事（187 余量） 写成已经 已经是 169 预填覆盖出块者 / 已经是 2930 名单 / 已经是不变量 163

**层次**：实现 / EIP-3651 warm-start not already 169-prefill / not already 2930 / not already 163 正式三事（187 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3651](https://eips.ethereum.org/EIPS/eip-3651)（Final, Core, Warm COINBASE）。  
**对应**：[`../tracks/implementation/worked-example-cbase-not169-vs-bundled.md`](../tracks/implementation/worked-example-cbase-not169-vs-bundled.md)。

把 EIP-3651 warm-start not already 169-prefill / not already 2930 / not already 163 正式三事（187 余量） 写成已经 已经是 169 预填覆盖出块者 / 已经是 2930 名单 / 已经是不变量 163，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3651 coinbase 正式三事（187 余量），必须分开 not already accessed、not already paid、not already 169-prefill 三件事，不要和 187 / 169 / 163 / 1446 / 1447 糊成一句。

也不是：

- [cbase-notacc-sold-as-bundled](cbase-notacc-sold-as-bundled.md) 是 notacc 单句边界（1446），不是本页边界。
- [cbase-notpay-sold-as-bundled](cbase-notpay-sold-as-bundled.md) 是 notpay 单句边界（1447），不是本页边界。
- [rpfx-noteof-sold-as-bundled](rpfx-noteof-sold-as-bundled.md) 是 EIP-3541 保留首字节边界（188/1443），不是本页出块者预填边界。
