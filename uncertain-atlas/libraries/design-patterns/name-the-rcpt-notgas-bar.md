# 模式：点名 rcpt-notgas 杠

**层次**：实现 / EIP-658 gas not already success / not already failure / not already revert-177 正式三事（236 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-658](https://eips.ethereum.org/EIPS/eip-658)（Final, Core；依赖 EIP-140）。  
**对应**：[`../tracks/implementation/worked-example-rcpt-notgas-vs-bundled.md`](../tracks/implementation/worked-example-rcpt-notgas-vs-bundled.md)。

- **还剩气 不是已经成功：看见还剩气，不是已经成功 interchangeable / 1302 rcpt-notgas interchangeable。**
- **气烧光 不是已经失败：看见气烧光，不是已经失败 interchangeable / 1302 rcpt-notgas interchangeable。**
- **还剩气 不是已经写了带回剩余气的回滚：看见还剩气，不是已经写了带回剩余气的回滚 interchangeable / 1302 rcpt-notgas interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看收据状态码 / 交叉核对 正式三事（236 余量），必须分开 not already mid-root、not already success-from-gas、not already rpc-replay 三件事。
