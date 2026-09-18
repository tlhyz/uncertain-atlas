# 例：看见原生移位指令不是已经用算术拼过移位不是已经用算术拼过移位；看见native shift is not already arithmetic-composed不是已经只有一条移位；看见原生移位指令不是已经用算术拼过移位不是已经 231 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-145](https://eips.ethereum.org/EIPS/eip-145)（Final, Core, bitwise shifting）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-145 native-shift not already arith-composed / not already one-shift / not already 231-bundled 正式三事（231 余量）/ not 1404 shft-notarith interchangeable / not 231 shift-vs-arithmetic bundled interchangeable」，不是 shift vs arithmetic bundled（231），也不是已经 数前导零≠已便宜 ZK（208），也不是已经 压零≠带立即数的压 0（217）。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。

## 官方三件事

1. **看见原生移位指令不是已经用算术拼过移位 / 看见原生移位指令不是已经用算术拼过移位 这份对象 is not already 已经用算术拼过移位 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1404 shft-notarith interchangeable / 1405 shft-notsdiv interchangeable，也不是已经 EIP-145 native-shift not already arith-composed / not already one-shift / not already 231-bundled 正式三事 bundled（231 item 1 余量） interchangeable / 231 shft item 1 interchangeable。**  
   官方把原生移位指令不是已经用算术拼过移位和已经用算术拼过移位写成两件。看见原生移位指令不是已经用算术拼过移位，不是已经用算术拼过移位。

2. **看见native shift is not already arithmetic-composed / 看见原生移位指令不是已经用算术拼过移位 / 这份对象 is not already 已经只有一条移位 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1404 shft-notarith interchangeable / 1406 shft-notpack interchangeable，也不是已经 数前导零≠已便宜 ZK interchangeable / 208 数前导零≠已便宜 ZK interchangeable。**  
   官方把native shift is not already arithmetic-composed和已经只有一条移位写成两件。看见native shift is not already arithmetic-composed，不是已经只有一条移位。

3. **看见原生移位指令不是已经用算术拼过移位 / 看见native shift is not already arithmetic-composed / 这份对象 is not already 已经 231 bundled interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1404 shft-notarith interchangeable / 1405 shft-notsdiv interchangeable，也不是已经 压零≠带立即数的压 0 interchangeable / 217 压零≠带立即数的压 0 interchangeable。**  
   官方把原生移位指令不是已经用算术拼过移位和已经 231 bundled写成两件。看见原生移位指令不是已经用算术拼过移位，不是已经 231 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。

## 官方为什么这样拆

- **原生移位指令不是已经用算术拼过移位 interchangeable：官方写能用算术拼，但更贵，不是同一条指令。**
- **看见三条指令不是已经只有一条移位。**
- **看见读数旋钮不是已经 231 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经用算术拼过移位 | 不是已经用算术拼过移位 | 不是已经数前导零≠已便宜 ZK（208） |
| 已经只有一条移位 | 不是已经只有一条移位 | 不是已经压零≠带立即数的压 0（217） |
| 已经 231 bundled | 不是已经 231 bundled | 不是已经1405 shft-notsdiv |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-145 native-shift not already arith-composed / not already one-shift / not already 231-bundled 正式三事（231 余量），必须分开是不是已经用算术拼过移位、是不是已经只有一条移位、是不是已经 231 bundled。可以跳过「看见 145 就已经和乘除同一条」。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。231 SHIFT vs arithmetic bundled unbundling 在本页 item 1 启动；续 [`worked-example-shft-notsdiv-vs-bundled.md`](worked-example-shft-notsdiv-vs-bundled.md)（不变量 1405 item 2）。

## 本页不抄

- 操作码号、气价档、测试向量、拼指令序列。
- 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。
