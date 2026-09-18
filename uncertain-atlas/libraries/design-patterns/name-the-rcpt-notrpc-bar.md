# 模式：点名 rcpt-notrpc 杠

**层次**：实现 / EIP-658 rpc not already in-receipt / not already light-checked / not already returndata 正式三事（236 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-658](https://eips.ethereum.org/EIPS/eip-658)（Final, Core；依赖 EIP-140）。  
**对应**：[`../tracks/implementation/worked-example-rcpt-notrpc-vs-bundled.md`](../tracks/implementation/worked-example-rcpt-notrpc-vs-bundled.md)。

- **RPC 能告诉你成没成 不是收据里已经有状态码：看见RPC 能告诉你成没成，不是收据里已经有状态码 interchangeable / 1303 rcpt-notrpc interchangeable。**
- **钱包绿了 不是轻客户端产品已经齐：看见钱包绿了，不是轻客户端产品已经齐 interchangeable / 1303 rcpt-notrpc interchangeable。**
- **RPC 能告诉你成没成 不是返回数据已经进了收据：看见RPC 能告诉你成没成，不是返回数据已经进了收据 interchangeable / 1303 rcpt-notrpc interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看收据状态码 / 交叉核对 正式三事（236 余量），必须分开 not already mid-root、not already success-from-gas、not already rpc-replay 三件事。
