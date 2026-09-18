# 模式：点名 mcpy-notcd 杠

**层次**：实现 / EIP-5656 overlap-copy not already calldata-copy / not already CALL-changed / not already 169 正式三事（216 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-5656](https://eips.ethereum.org/EIPS/eip-5656)（Final, Core, MCOPY instruction）。  
**对应**：[`../tracks/implementation/worked-example-mcpy-notcd-vs-bundled.md`](../tracks/implementation/worked-example-mcpy-notcd-vs-bundled.md)。

- **能重叠拷不是已经是 calldata / 返回数据拷 不是已经是 calldata / 返回数据拷：看见能重叠拷不是已经是 calldata / 返回数据拷，不是已经是 calldata / 返回数据拷 interchangeable / 1412 mcpy-notcd interchangeable。**
- **overlap copy is not already calldata copy 不是已经改了 CALL 的效果：看见overlap copy is not already calldata copy，不是已经改了 CALL 的效果 interchangeable / 1412 mcpy-notcd interchangeable。**
- **能重叠拷不是已经是 calldata / 返回数据拷 不是已经是不变量 169：看见能重叠拷不是已经是 calldata / 返回数据拷，不是已经是不变量 169 interchangeable / 1412 mcpy-notcd interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-5656 MCOPY 正式三事（216 余量），必须分开 not already identity-precompile、not already real-alloc、not already calldata-copy 三件事。
