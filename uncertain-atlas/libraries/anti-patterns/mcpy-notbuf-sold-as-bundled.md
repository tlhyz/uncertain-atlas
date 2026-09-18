# 反模式：把 EIP-5656 as-if-buffer not already real-alloc / not already DoS / not already 208 正式三事（216 余量） 写成已经 已经必须真分配一块缓冲 / 已经是拒绝服务面 / 已经是不变量 208

**层次**：实现 / EIP-5656 as-if-buffer not already real-alloc / not already DoS / not already 208 正式三事（216 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-5656](https://eips.ethereum.org/EIPS/eip-5656)（Final, Core, MCOPY instruction）。  
**对应**：[`../tracks/implementation/worked-example-mcpy-notbuf-vs-bundled.md`](../tracks/implementation/worked-example-mcpy-notbuf-vs-bundled.md)。

把 EIP-5656 as-if-buffer not already real-alloc / not already DoS / not already 208 正式三事（216 余量） 写成已经 已经必须真分配一块缓冲 / 已经是拒绝服务面 / 已经是不变量 208，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-5656 MCOPY 正式三事（216 余量），必须分开 not already identity-precompile、not already real-alloc、not already calldata-copy 三件事，不要和 216 / 208 / 176 / 1410 / 1412 糊成一句。

也不是：

- [mcpy-notid-sold-as-bundled](mcpy-notid-sold-as-bundled.md) 是 notid 单句边界（1410），不是本页边界。
- [mcpy-notcd-sold-as-bundled](mcpy-notcd-sold-as-bundled.md) 是 notcd 单句边界（1412），不是本页边界。
- [psh0-notimm-sold-as-bundled](psh0-notimm-sold-as-bundled.md) 是 EIP-3855 压零指令边界（217/1407），不是本页 MCOPY 边界。
