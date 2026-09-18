# 例：看见更便宜不是已经是位域打包产品不是已经是位域打包产品；看见cheaper is not already a bitfield product不是已经改了旧字节码；看见更便宜不是已经是位域打包产品不是已经是不变量 208

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-145](https://eips.ethereum.org/EIPS/eip-145)（Final, Core, bitwise shifting）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-145 cheaper not already bitfield-product / not already old-bytecode-changed / not already 208 正式三事（231 余量）/ not 1406 shft-notpack interchangeable / not 231 shift-vs-arithmetic bundled interchangeable」，不是 shift vs arithmetic bundled（231），也不是已经 数前导零（208），也不是已经 压零（217）。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。

## 官方三件事

1. **看见更便宜不是已经是位域打包产品 / 看见更便宜不是已经是位域打包产品 这份对象 is not already 已经是位域打包产品 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1406 shft-notpack interchangeable / 1404 shft-notarith interchangeable，也不是已经 EIP-145 cheaper not already bitfield-product / not already old-bytecode-changed / not already 208 正式三事 bundled（231 item 3 余量） interchangeable / 231 shft item 3 interchangeable。**  
   官方把更便宜不是已经是位域打包产品和已经是位域打包产品写成两件。看见更便宜不是已经是位域打包产品，不是已经是位域打包产品。

2. **看见cheaper is not already a bitfield product / 看见更便宜不是已经是位域打包产品 / 这份对象 is not already 已经改了旧字节码 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1406 shft-notpack interchangeable / 1405 shft-notsdiv interchangeable，也不是已经 数前导零 interchangeable / 208 数前导零 interchangeable。**  
   官方把cheaper is not already a bitfield product和已经改了旧字节码写成两件。看见cheaper is not already a bitfield product，不是已经改了旧字节码。

3. **看见更便宜不是已经是位域打包产品 / 看见cheaper is not already a bitfield product / 这份对象 is not already 已经是不变量 208 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1406 shft-notpack interchangeable / 1404 shft-notarith interchangeable，也不是已经 压零 interchangeable / 217 压零 interchangeable。**  
   官方把更便宜不是已经是位域打包产品和已经是不变量 208写成两件。看见更便宜不是已经是位域打包产品，不是已经是不变量 208。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。

## 官方为什么这样拆

- **更便宜不是已经是位域打包产品 interchangeable：官方把主机更省写成动机，不是产品已经上线。**
- **看见新指令不是已经改了旧字节码。**
- **看见本页不是已经是不变量 208。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是位域打包产品 | 不是已经是位域打包产品 | 不是已经数前导零（208） |
| 已经改了旧字节码 | 不是已经改了旧字节码 | 不是已经压零（217） |
| 已经是不变量 208 | 不是已经是不变量 208 | 不是已经1404 shft-notarith |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-145 cheaper not already bitfield-product / not already old-bytecode-changed / not already 208 正式三事（231 余量），必须分开是不是已经是位域打包产品、是不是已经改了旧字节码、是不是已经是不变量 208。可以跳过「看见 145 就已经和乘除同一条」。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。231 SHIFT vs arithmetic bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-3855 PUSH0（217）。

## 本页不抄

- 操作码号、气价档、测试向量、拼指令序列。
- 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。
