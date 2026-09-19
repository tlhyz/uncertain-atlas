# 反模式：把 EIP-7823 input-bound not already price-changed / not already 227 / not already 206-bundled 正式三事（206 余量） 写成已经 已经改了计价公式 / 已经是不变量 227 / 已经 206 bundled

**层次**：实现 / EIP-7823 input-bound not already price-changed / not already 227 / not already 206-bundled 正式三事（206 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7823](https://eips.ethereum.org/EIPS/eip-7823)（Set upper bounds for MODEXP）。  
**对应**：[`../tracks/implementation/worked-example-mxbd-notprice-vs-bundled.md`](../tracks/implementation/worked-example-mxbd-notprice-vs-bundled.md)。

把 EIP-7823 input-bound not already price-changed / not already 227 / not already 206-bundled 正式三事（206 余量） 写成已经 已经改了计价公式 / 已经是不变量 227 / 已经 206 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7823 modexp-bound 正式三事（206 余量），必须分开 not already price-changed、not already success、not already evm-replaced 三件事，不要和 206 / 227 / 203 / 1474 / 1475 糊成一句。

也不是：

- [mxbd-notok-sold-as-bundled](mxbd-notok-sold-as-bundled.md) 是 notok 单句边界（1474），不是本页边界。
- [mxbd-notevm-sold-as-bundled](mxbd-notevm-sold-as-bundled.md) 是 notevm 单句边界（1475），不是本页边界。
- [clz-notzk-sold-as-bundled](clz-notzk-sold-as-bundled.md) 是 EIP-7939 数前导零边界（208/1470），不是本页模幂输入帽边界。
