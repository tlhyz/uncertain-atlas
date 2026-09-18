# 例：看见链号指令不是已经是签进哈希的链号不是已经是签进哈希的链号；看见CHAINID is not already signed chainId不是已经是钱包 JSON 里的 chainId；看见链号指令不是已经是签进哈希的链号不是已经 220 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344)（Final, Core, CHAINID opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1344 CHAINID opcode not already 155-signed / not already JSON-chainId / not already 220-bundled 正式三事（220 余量）/ not 1395 chid-not155 interchangeable / not 220 chainid-opcode-vs-signed bundled interchangeable」，不是 chainid opcode vs signed bundled（220），也不是已经 JSON chainId≠已签进哈希（161），也不是已经 FIPS ctx / 712 域（18）。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。

## 官方三件事

1. **看见链号指令不是已经是签进哈希的链号 / 看见链号指令不是已经是签进哈希的链号 这份对象 is not already 已经是签进哈希的链号 interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1395 chid-not155 interchangeable / 1396 chid-nottx interchangeable，也不是已经 EIP-1344 CHAINID opcode not already 155-signed / not already JSON-chainId / not already 220-bundled 正式三事 bundled（220 item 1 余量） interchangeable / 220 chid item 1 interchangeable。**  
   官方把链号指令不是已经是签进哈希的链号和已经是签进哈希的链号写成两件。看见链号指令不是已经是签进哈希的链号，不是已经是签进哈希的链号。

2. **看见CHAINID is not already signed chainId / 看见链号指令不是已经是签进哈希的链号 / 这份对象 is not already 已经是钱包 JSON 里的 chainId interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1395 chid-not155 interchangeable / 1397 chid-notfork interchangeable，也不是已经 JSON chainId≠已签进哈希 interchangeable / 161 JSON chainId≠已签进哈希 interchangeable。**  
   官方把CHAINID is not already signed chainId和已经是钱包 JSON 里的 chainId写成两件。看见CHAINID is not already signed chainId，不是已经是钱包 JSON 里的 chainId。

3. **看见链号指令不是已经是签进哈希的链号 / 看见CHAINID is not already signed chainId / 这份对象 is not already 已经 220 bundled interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1395 chid-not155 interchangeable / 1396 chid-nottx interchangeable，也不是已经 FIPS ctx / 712 域 interchangeable / 18 FIPS ctx / 712 域 interchangeable。**  
   官方把链号指令不是已经是签进哈希的链号和已经 220 bundled写成两件。看见链号指令不是已经是签进哈希的链号，不是已经 220 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。

## 官方为什么这样拆

- **链号指令不是已经是签进哈希的链号 interchangeable：官方把合约读本链号和 155 签名绑定写成两件。**
- **看见能读链号不是已经是钱包 JSON 里的 chainId。**
- **看见读链号旋钮不是已经 220 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是签进哈希的链号 | 不是已经是签进哈希的链号 | 不是已经JSON chainId≠已签进哈希（161） |
| 已经是钱包 JSON 里的 chainId | 不是已经是钱包 JSON 里的 chainId | 不是已经FIPS ctx / 712 域（18） |
| 已经 220 bundled | 不是已经 220 bundled | 不是已经1396 chid-nottx |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1344 CHAINID opcode not already 155-signed / not already JSON-chainId / not already 220-bundled 正式三事（220 余量），必须分开是不是已经是签进哈希的链号、是不是已经是钱包 JSON 里的 chainId、是不是已经 220 bundled。可以跳过「看见链号指令就已经绑了签名链号」。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。220 CHAINID opcode vs signed bundled unbundling 在本页 item 1 启动；续 [`worked-example-chid-nottx-vs-bundled.md`](worked-example-chid-nottx-vs-bundled.md)（不变量 1396 item 2）。

## 本页不抄

- 操作码号、气价档、位宽、实现仓库、测试仓库指针。
- 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。
