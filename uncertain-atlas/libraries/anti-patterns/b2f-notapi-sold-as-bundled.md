# 反模式：把 EIP-152 fixed-input not already generic-hash-API / not already digest / not already 199 正式三事（230 余量） 写成已经 已经是任意哈希 API / 已经返回一份摘要 / 已经是不变量 199

**层次**：实现 / EIP-152 fixed-input not already generic-hash-API / not already digest / not already 199 正式三事（230 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-152](https://eips.ethereum.org/EIPS/eip-152)（Final, Core, Add BLAKE2 compression function F precompile）。  
**对应**：[`../tracks/implementation/worked-example-b2f-notapi-vs-bundled.md`](../tracks/implementation/worked-example-b2f-notapi-vs-bundled.md)。

把 EIP-152 fixed-input not already generic-hash-API / not already digest / not already 199 正式三事（230 余量） 写成已经 已经是任意哈希 API / 已经返回一份摘要 / 已经是不变量 199，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-152 BLAKE2F 正式三事（230 余量），必须分开 not already hash、not already Equihash-live、not already generic-hash-API 三件事，不要和 230 / 221 / 199 / 1434 / 1435 糊成一句。

也不是：

- [b2f-nothash-sold-as-bundled](b2f-nothash-sold-as-bundled.md) 是 nothash 单句边界（1434），不是本页边界。
- [b2f-notprod-sold-as-bundled](b2f-notprod-sold-as-bundled.md) 是 notprod 单句边界（1435），不是本页边界。
- [sbal-notbal-sold-as-bundled](sbal-notbal-sold-as-bundled.md) 是 EIP-1884 SELFBALANCE 边界（229/1431），不是本页 BLAKE2F 边界。
