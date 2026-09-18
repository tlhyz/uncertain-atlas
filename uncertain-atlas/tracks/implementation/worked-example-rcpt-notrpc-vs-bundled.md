# 例：看见RPC 能告诉你成没成不是收据里已经有状态码；看见钱包绿了不是轻客户端产品已经齐；看见RPC 能告诉你成没成不是返回数据已经进了收据

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-658](https://eips.ethereum.org/EIPS/eip-658)（Final, Core；依赖 EIP-140）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-658 rpc not already in-receipt / not already light-checked / not already returndata 正式三事（236 余量）/ not 1303 rcpt-notrpc interchangeable / not 236 receipt-status-vs-gas bundled interchangeable」，不是 receipt status vs gas bundled（236），也不是已经 returndata（232），也不是已经 history-window（207）。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。

## 官方三件事

1. **看见RPC 能告诉你成没成 / 看见RPC 能告诉你成没成 这份对象 is not already 收据里已经有状态码 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1303 rcpt-notrpc interchangeable / 1301 rcpt-notroot interchangeable，也不是已经 EIP-658 rpc not already in-receipt / not already light-checked / not already returndata 正式三事 bundled（236 item 3 余量） interchangeable / 236 rcpt item 3 interchangeable。**  
   官方把RPC 能告诉你成没成和收据里已经有状态码写成两件。看见RPC 能告诉你成没成，不是收据里已经有状态码。

2. **看见钱包绿了 / 看见RPC 能告诉你成没成 / 这份对象 is not already 轻客户端产品已经齐 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1303 rcpt-notrpc interchangeable / 1302 rcpt-notgas interchangeable，也不是已经 returndata interchangeable / 232 returndata interchangeable。**  
   官方把钱包绿了和轻客户端产品已经齐写成两件。看见钱包绿了，不是轻客户端产品已经齐。

3. **看见RPC 能告诉你成没成 / 看见钱包绿了 / 这份对象 is not already 返回数据已经进了收据 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1303 rcpt-notrpc interchangeable / 1301 rcpt-notroot interchangeable，也不是已经 history-window interchangeable / 207 history-window interchangeable。**  
   官方把RPC 能告诉你成没成和返回数据已经进了收据写成两件。看见RPC 能告诉你成没成，不是返回数据已经进了收据。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。

## 官方为什么这样拆

- **RPC 能告诉你成没成 不是收据里已经有状态码：官方把重放标成非共识。**
- **钱包绿了 不是轻客户端产品已经齐：快同步只能对自己的枢轴之后重放，轻节点根本做不到。**
- **状态码 不是返回数据已经进了收据：返回缓冲是另一对象。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收据里已经有状态码 | 不是收据里已经有状态码 | 不是已经returndata（232） |
| 轻客户端产品已经齐 | 不是轻客户端产品已经齐 | 不是已经history-window（207） |
| 返回数据已经进了收据 | 不是返回数据已经进了收据 | 不是已经1301 rcpt-notroot |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-658 rpc not already in-receipt / not already light-checked / not already returndata 正式三事（236 余量），必须分开是不是收据里已经有状态码、是不是轻客户端产品已经齐、是不是返回数据已经进了收据。可以跳过「看见还剩气就已经知道成功」。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。236 receipt status vs gas bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 分叉高度、状态码取值。
- 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。
