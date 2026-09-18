# 反模式：把 EIP-658 gas not already success / not already failure / not already revert-177 正式三事（236 余量） 写成已经 已经成功 / 已经失败 / 已经写了带回剩余气的回滚

**层次**：实现 / EIP-658 gas not already success / not already failure / not already revert-177 正式三事（236 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-658](https://eips.ethereum.org/EIPS/eip-658)（Final, Core；依赖 EIP-140）。  
**对应**：[`../tracks/implementation/worked-example-rcpt-notgas-vs-bundled.md`](../tracks/implementation/worked-example-rcpt-notgas-vs-bundled.md)。

把 EIP-658 gas not already success / not already failure / not already revert-177 正式三事（236 余量） 写成已经 已经成功 / 已经失败 / 已经写了带回剩余气的回滚，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看收据状态码 / 交叉核对 正式三事（236 余量），必须分开 not already mid-root、not already success-from-gas、not already rpc-replay 三件事，不要和 236 / 177 / 207 / 1301 / 1303 糊成一句。

也不是：

- [rcpt-notroot-sold-as-bundled](rcpt-notroot-sold-as-bundled.md) 是 notroot 单句边界（1301），不是本页边界。
- [rcpt-notrpc-sold-as-bundled](rcpt-notrpc-sold-as-bundled.md) 是 notrpc 单句边界（1303），不是本页边界。
- [c63-notcap-sold-as-bundled](c63-notcap-sold-as-bundled.md) 是 EIP-150 建议气限仍未是协议帽边界（237/1300），不是本页收据状态边界。
