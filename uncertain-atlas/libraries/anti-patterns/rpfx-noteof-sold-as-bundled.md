# 反模式：把 EIP-3541 reserved-prefix not already EOF-deployed / not already validated / not already 188-bundled 正式三事（188 余量） 写成已经 已经是对象格式已经部署 / 已经按新格式验过 / 已经 188 bundled

**层次**：实现 / EIP-3541 reserved-prefix not already EOF-deployed / not already validated / not already 188-bundled 正式三事（188 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-3541](https://eips.ethereum.org/EIPS/eip-3541)（Final, Core, Reject new contract code starting with the reserved format byte）。  
**对应**：[`../tracks/implementation/worked-example-rpfx-noteof-vs-bundled.md`](../tracks/implementation/worked-example-rpfx-noteof-vs-bundled.md)。

把 EIP-3541 reserved-prefix not already EOF-deployed / not already validated / not already 188-bundled 正式三事（188 余量） 写成已经 已经是对象格式已经部署 / 已经按新格式验过 / 已经 188 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3541 reserved-prefix 正式三事（188 余量），必须分开 not already EOF-deployed、not already rewritten、not already this-fail 三件事，不要和 188 / 185 / 176 / 1444 / 1445 糊成一句。

也不是：

- [rpfx-notold-sold-as-bundled](rpfx-notold-sold-as-bundled.md) 是 notold 单句边界（1444），不是本页边界。
- [rpfx-notinit-sold-as-bundled](rpfx-notinit-sold-as-bundled.md) 是 notinit 单句边界（1445），不是本页边界。
- [retc-notinit-sold-as-bundled](retc-notinit-sold-as-bundled.md) 是 EIP-170 返回代码边界（185/1440），不是本页保留首字节边界。
