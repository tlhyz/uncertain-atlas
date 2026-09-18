# 反模式：把 EIP-658 rpc not already in-receipt / not already light-checked / not already returndata 正式三事（236 余量） 写成已经 收据里已经有状态码 / 轻客户端产品已经齐 / 返回数据已经进了收据

**层次**：实现 / EIP-658 rpc not already in-receipt / not already light-checked / not already returndata 正式三事（236 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-658](https://eips.ethereum.org/EIPS/eip-658)（Final, Core；依赖 EIP-140）。  
**对应**：[`../tracks/implementation/worked-example-rcpt-notrpc-vs-bundled.md`](../tracks/implementation/worked-example-rcpt-notrpc-vs-bundled.md)。

把 EIP-658 rpc not already in-receipt / not already light-checked / not already returndata 正式三事（236 余量） 写成已经 收据里已经有状态码 / 轻客户端产品已经齐 / 返回数据已经进了收据，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看收据状态码 / 交叉核对 正式三事（236 余量），必须分开 not already mid-root、not already success-from-gas、not already rpc-replay 三件事，不要和 236 / 232 / 207 / 1301 / 1302 糊成一句。

也不是：

- [rcpt-notroot-sold-as-bundled](rcpt-notroot-sold-as-bundled.md) 是 notroot 单句边界（1301），不是本页边界。
- [rcpt-notgas-sold-as-bundled](rcpt-notgas-sold-as-bundled.md) 是 notgas 单句边界（1302），不是本页边界。
- [c63-notcap-sold-as-bundled](c63-notcap-sold-as-bundled.md) 是 EIP-150 建议气限仍未是协议帽边界（237/1300），不是本页收据状态边界。
