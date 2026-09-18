# 例：看见CALL 气是常数不是已经没有按长度代价不是已经没有按长度的磁盘/证明代价；看见constant CALL gas is not already free of length cost不是已经是不变量 170；看见CALL 气是常数不是已经没有按长度代价不是已经免费

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-170](https://eips.ethereum.org/EIPS/eip-170)（Final, Core, Contract code size limit）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-170 constant-CALL-gas not already free-disk / not already no-proof-cost / not already 170-inv 正式三事（185 余量）/ not 1442 retc-notfree interchangeable / not 185 returned-vs-initcode bundled interchangeable」，不是 returned vs initcode bundled（185），也不是已经 哈希≠已揭开（170），也不是已经 initcode≠运行时代码（176）。不要另写 怎样造超长返回代码。

## 官方三件事

1. **看见CALL 气是常数不是已经没有按长度代价 / 看见CALL 气是常数不是已经没有按长度代价 这份对象 is not already 已经没有按长度的磁盘/证明代价 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1442 retc-notfree interchangeable / 1440 retc-notinit interchangeable，也不是已经 EIP-170 constant-CALL-gas not already free-disk / not already no-proof-cost / not already 170-inv 正式三事 bundled（185 item 3 余量） interchangeable / 185 retc item 3 interchangeable。**  
   官方把CALL 气是常数不是已经没有按长度代价和已经没有按长度的磁盘/证明代价写成两件。看见CALL 气是常数不是已经没有按长度代价，不是已经没有按长度的磁盘/证明代价。

2. **看见constant CALL gas is not already free of length cost / 看见CALL 气是常数不是已经没有按长度代价 / 这份对象 is not already 已经是不变量 170 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1442 retc-notfree interchangeable / 1441 retc-nottx interchangeable，也不是已经 哈希≠已揭开 interchangeable / 170 哈希≠已揭开 interchangeable。**  
   官方把constant CALL gas is not already free of length cost和已经是不变量 170写成两件。看见constant CALL gas is not already free of length cost，不是已经是不变量 170。

3. **看见CALL 气是常数不是已经没有按长度代价 / 看见constant CALL gas is not already free of length cost / 这份对象 is not already 已经免费 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1442 retc-notfree interchangeable / 1440 retc-notinit interchangeable，也不是已经 initcode≠运行时代码 interchangeable / 176 initcode≠运行时代码 interchangeable。**  
   官方把CALL 气是常数不是已经没有按长度代价和已经免费写成两件。看见CALL 气是常数不是已经没有按长度代价，不是已经免费。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长返回代码。

## 官方为什么这样拆

- **CALL 气是常数不是已经没有按长度代价 interchangeable：官方写调用气可以是常数，仍会按代码长度付出读盘、预处理、证明字节。**
- **看见规范编号不是已经是不变量 170。**
- **看见常数调用气不是已经免费。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经没有按长度的磁盘/证明代价 | 不是已经没有按长度的磁盘/证明代价 | 不是已经哈希≠已揭开（170） |
| 已经是不变量 170 | 不是已经是不变量 170 | 不是已经initcode≠运行时代码（176） |
| 已经免费 | 不是已经免费 | 不是已经1440 retc-notinit |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-170 constant-CALL-gas not already free-disk / not already no-proof-cost / not already 170-inv 正式三事（185 余量），必须分开是不是已经没有按长度的磁盘/证明代价、是不是已经是不变量 170、是不是已经免费。可以跳过「规范 170 就已经是不变量 170」。不要另写 怎样造超长返回代码。185 returned vs initcode bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：reserved-prefix（188）。

## 本页不抄

- 上限字节、分叉高度、链号、气价表。
- 怎样造超长返回代码。
