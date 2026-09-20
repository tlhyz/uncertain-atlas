# 模式：点名 mcpy-notbuf 杠

**层次**：实现 / EIP-5656 as-if-buffer not already real-alloc / not already DoS / not already 208 正式三事（216 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-5656](https://eips.ethereum.org/EIPS/eip-5656)（Final, Core, MCOPY instruction）。  
**对应**：[`../tracks/implementation/worked-example-mcpy-notbuf-vs-bundled.md`](../tracks/implementation/worked-example-mcpy-notbuf-vs-bundled.md)。

- **「像用了中间缓冲」不是已经必须真分配一块缓冲 不是已经必须真分配一块缓冲：看见「像用了中间缓冲」不是已经必须真分配一块缓冲，不是已经必须真分配一块缓冲 interchangeable / 1411 mcpy-notbuf interchangeable。**
- **as-if-buffer is not already real allocation 不是已经是拒绝服务面：看见as-if-buffer is not already real allocation，不是已经是拒绝服务面 interchangeable / 1411 mcpy-notbuf interchangeable。**
- **「像用了中间缓冲」不是已经必须真分配一块缓冲 不是已经是不变量 208：看见「像用了中间缓冲」不是已经必须真分配一块缓冲，不是已经是不变量 208 interchangeable / 1411 mcpy-notbuf interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-5656 MCOPY 正式三事（216 余量），必须分开 not already identity-precompile、not already real-alloc、not already calldata-copy 三件事。
