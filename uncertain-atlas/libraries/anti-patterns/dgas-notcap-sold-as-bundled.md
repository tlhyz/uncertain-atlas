# 反模式：把 EIP-7935 default-gas not already protocol-cap / not already 203 / not already 211-bundled 正式三事（211 余量） 写成已经 已经是协议帽 / 已经是不变量 203 / 已经 211 bundled

**层次**：实现 / EIP-7935 default-gas not already protocol-cap / not already 203 / not already 211-bundled 正式三事（211 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7935](https://eips.ethereum.org/EIPS/eip-7935)（Informational, Set default gas limit to 60M）。  
**对应**：[`../tracks/implementation/worked-example-dgas-notcap-vs-bundled.md`](../tracks/implementation/worked-example-dgas-notcap-vs-bundled.md)。

把 EIP-7935 default-gas not already protocol-cap / not already 203 / not already 211-bundled 正式三事（211 余量） 写成已经 已经是协议帽 / 已经是不变量 203 / 已经 211 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7935 default-gas 正式三事（211 余量），必须分开 not already protocol-cap、not already consensus-changed、not already tx-gas-cap 三件事，不要和 211 / 203 / 202 / 1459 / 1460 糊成一句。

也不是：

- [dgas-notcons-sold-as-bundled](dgas-notcons-sold-as-bundled.md) 是 notcons 单句边界（1459），不是本页边界。
- [dgas-nottx-sold-as-bundled](dgas-nottx-sold-as-bundled.md) 是 nottx 单句边界（1460），不是本页边界。
- [tenv-notinner-sold-as-bundled](tenv-notinner-sold-as-bundled.md) 是 EIP-2718 类型信封边界（167/1455），不是本页默认气限边界。
