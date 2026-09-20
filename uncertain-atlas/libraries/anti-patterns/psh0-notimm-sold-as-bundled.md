# 反模式：把 EIP-3855 PUSH0 not already immediate-push0 / not already 216 / not already 217-bundled 正式三事（217 余量） 写成已经 已经是带立即数的压 0 / 已经是不变量 216 / 已经 217 bundled

**层次**：实现 / EIP-3855 PUSH0 not already immediate-push0 / not already 216 / not already 217-bundled 正式三事（217 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3855](https://eips.ethereum.org/EIPS/eip-3855)（Final, Core, PUSH0 instruction）。  
**对应**：[`../tracks/implementation/worked-example-psh0-notimm-vs-bundled.md`](../tracks/implementation/worked-example-psh0-notimm-vs-bundled.md)。

把 EIP-3855 PUSH0 not already immediate-push0 / not already 216 / not already 217-bundled 正式三事（217 余量） 写成已经 已经是带立即数的压 0 / 已经是不变量 216 / 已经 217 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3855 PUSH0 正式三事（217 余量），必须分开 not already immediate-push0、not already jumpdest-changed、not already old-byte-unchanged 三件事，不要和 217 / 216 / 208 / 1408 / 1409 糊成一句。

也不是：

- [psh0-notjump-sold-as-bundled](psh0-notjump-sold-as-bundled.md) 是 notjump 单句边界（1408），不是本页边界。
- [psh0-notold-sold-as-bundled](psh0-notold-sold-as-bundled.md) 是 notold 单句边界（1409），不是本页边界。
- [shft-notarith-sold-as-bundled](shft-notarith-sold-as-bundled.md) 是 EIP-145 原生移位边界（231/1404），不是本页 PUSH0 边界。
