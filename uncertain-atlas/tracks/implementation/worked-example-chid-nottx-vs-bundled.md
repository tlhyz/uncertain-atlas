# 例：看见指令返回配置链号不是这笔已经带了 155 标识不是这笔交易已经带了 EIP-155 标识；看见config chainId is not already this-tx 155不是已经返回某个默认值；看见指令返回配置链号不是这笔已经带了 155 标识不是已经是不变量 161

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344)（Final, Core, CHAINID opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1344 config-chainid not already this-tx-155 / not already default-value / not already 161 正式三事（220 余量）/ not 1396 chid-nottx interchangeable / not 220 chainid-opcode-vs-signed bundled interchangeable」，不是 chainid opcode vs signed bundled（220），也不是已经 EIP-155 签名绑定（161），也不是已经 基础费指令≠已改市场（218）。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。

## 官方三件事

1. **看见指令返回配置链号不是这笔已经带了 155 标识 / 看见指令返回配置链号不是这笔已经带了 155 标识 这份对象 is not already 这笔交易已经带了 EIP-155 标识 interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1396 chid-nottx interchangeable / 1395 chid-not155 interchangeable，也不是已经 EIP-1344 config-chainid not already this-tx-155 / not already default-value / not already 161 正式三事 bundled（220 item 2 余量） interchangeable / 220 chid item 2 interchangeable。**  
   官方把指令返回配置链号不是这笔已经带了 155 标识和这笔交易已经带了 EIP-155 标识写成两件。看见指令返回配置链号不是这笔已经带了 155 标识，不是这笔交易已经带了 EIP-155 标识。

2. **看见config chainId is not already this-tx 155 / 看见指令返回配置链号不是这笔已经带了 155 标识 / 这份对象 is not already 已经返回某个默认值 interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1396 chid-nottx interchangeable / 1397 chid-notfork interchangeable，也不是已经 EIP-155 签名绑定 interchangeable / 161 EIP-155 签名绑定 interchangeable。**  
   官方把config chainId is not already this-tx 155和已经返回某个默认值写成两件。看见config chainId is not already this-tx 155，不是已经返回某个默认值。

3. **看见指令返回配置链号不是这笔已经带了 155 标识 / 看见config chainId is not already this-tx 155 / 这份对象 is not already 已经是不变量 161 interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1396 chid-nottx interchangeable / 1395 chid-not155 interchangeable，也不是已经 基础费指令≠已改市场 interchangeable / 218 基础费指令≠已改市场 interchangeable。**  
   官方把指令返回配置链号不是这笔已经带了 155 标识和已经是不变量 161写成两件。看见指令返回配置链号不是这笔已经带了 155 标识，不是已经是不变量 161。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。

## 官方为什么这样拆

- **指令返回配置链号不是这笔已经带了 155 标识 interchangeable：官方写没带 155 标识时仍返回配置链号。**
- **看见能读到不是已经返回某个默认值。**
- **看见合约读数不是已经是不变量 161。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 这笔交易已经带了 EIP-155 标识 | 不是这笔交易已经带了 EIP-155 标识 | 不是已经EIP-155 签名绑定（161） |
| 已经返回某个默认值 | 不是已经返回某个默认值 | 不是已经基础费指令≠已改市场（218） |
| 已经是不变量 161 | 不是已经是不变量 161 | 不是已经1395 chid-not155 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1344 config-chainid not already this-tx-155 / not already default-value / not already 161 正式三事（220 余量），必须分开是不是这笔交易已经带了 EIP-155 标识、是不是已经返回某个默认值、是不是已经是不变量 161。可以跳过「看见链号指令就已经绑了签名链号」。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。220 CHAINID opcode vs signed bundled unbundling 在本页 item 2 续；续 [`worked-example-chid-notfork-vs-bundled.md`](worked-example-chid-notfork-vs-bundled.md)（不变量 1397 item 3）。

## 本页不抄

- 操作码号、气价档、位宽、实现仓库、测试仓库指针。
- 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。
