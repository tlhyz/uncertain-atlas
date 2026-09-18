# 例：看见编译期写死的链号不是已经在硬分叉后仍安全不是已经在硬分叉后仍安全；看见compile-time chainId is not already fork-safe不是已经是 712 域；看见编译期写死的链号不是已经在硬分叉后仍安全不是已经处理好有争议的分裂

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344)（Final, Core, CHAINID opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1344 compile-time chainid not already fork-safe / not already 712-domain / not already split-handled 正式三事（220 余量）/ not 1397 chid-notfork interchangeable / not 220 chainid-opcode-vs-signed bundled interchangeable」，不是 chainid opcode vs signed bundled（220），也不是已经 EIP-3198 BASEFEE（218），也不是已经 blob 基础费指令（219）。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。

## 官方三件事

1. **看见编译期写死的链号不是已经在硬分叉后仍安全 / 看见编译期写死的链号不是已经在硬分叉后仍安全 这份对象 is not already 已经在硬分叉后仍安全 interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1397 chid-notfork interchangeable / 1395 chid-not155 interchangeable，也不是已经 EIP-1344 compile-time chainid not already fork-safe / not already 712-domain / not already split-handled 正式三事 bundled（220 item 3 余量） interchangeable / 220 chid item 3 interchangeable。**  
   官方把编译期写死的链号不是已经在硬分叉后仍安全和已经在硬分叉后仍安全写成两件。看见编译期写死的链号不是已经在硬分叉后仍安全，不是已经在硬分叉后仍安全。

2. **看见compile-time chainId is not already fork-safe / 看见编译期写死的链号不是已经在硬分叉后仍安全 / 这份对象 is not already 已经是 712 域 interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1397 chid-notfork interchangeable / 1396 chid-nottx interchangeable，也不是已经 EIP-3198 BASEFEE interchangeable / 218 EIP-3198 BASEFEE interchangeable。**  
   官方把compile-time chainId is not already fork-safe和已经是 712 域写成两件。看见compile-time chainId is not already fork-safe，不是已经是 712 域。

3. **看见编译期写死的链号不是已经在硬分叉后仍安全 / 看见compile-time chainId is not already fork-safe / 这份对象 is not already 已经处理好有争议的分裂 interchangeable，也不是已经 chainid opcode vs signed bundled（220） interchangeable / 1397 chid-notfork interchangeable / 1395 chid-not155 interchangeable，也不是已经 blob 基础费指令 interchangeable / 219 blob 基础费指令 interchangeable。**  
   官方把编译期写死的链号不是已经在硬分叉后仍安全和已经处理好有争议的分裂写成两件。看见编译期写死的链号不是已经在硬分叉后仍安全，不是已经处理好有争议的分裂。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。

## 官方为什么这样拆

- **编译期写死的链号不是已经在硬分叉后仍安全 interchangeable：官方写硬分叉后会出问题。**
- **看见 712 域写了链号不是已经是 712 域本身。**
- **看见本页不是已经处理好有争议的分裂。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在硬分叉后仍安全 | 不是已经在硬分叉后仍安全 | 不是已经EIP-3198 BASEFEE（218） |
| 已经是 712 域 | 不是已经是 712 域 | 不是已经blob 基础费指令（219） |
| 已经处理好有争议的分裂 | 不是已经处理好有争议的分裂 | 不是已经1395 chid-not155 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1344 compile-time chainid not already fork-safe / not already 712-domain / not already split-handled 正式三事（220 余量），必须分开是不是已经在硬分叉后仍安全、是不是已经是 712 域、是不是已经处理好有争议的分裂。可以跳过「看见链号指令就已经绑了签名链号」。不要另写 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。220 CHAINID opcode vs signed bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-3198 BASEFEE（218）。

## 本页不抄

- 操作码号、气价档、位宽、实现仓库、测试仓库指针。
- 怎样实现链号预言机、怎样处理 Plasma 分裂、怎样拿未绑链号的签去另一条链重放。
