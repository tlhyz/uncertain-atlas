# 例：看见算术右移不是已经是有符号除不是已经是有符号除；看见SAR is not already signed division不是已经是同一条舍入；看见算术右移不是已经是有符号除不是已经和加减同一套操作数顺序

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-145](https://eips.ethereum.org/EIPS/eip-145)（Final, Core, bitwise shifting）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-145 SAR not already signed-div / not already same-rounding / not already same-operand-order 正式三事（231 余量）/ not 1405 shft-notsdiv interchangeable / not 231 shift-vs-arithmetic bundled interchangeable」，不是 shift vs arithmetic bundled（231），也不是已经 内存拷≠身份预编译（216），也不是已经 BLAKE2压缩≠已是哈希（230）。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。

## 官方三件事

1. **看见算术右移不是已经是有符号除 / 看见算术右移不是已经是有符号除 这份对象 is not already 已经是有符号除 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1405 shft-notsdiv interchangeable / 1404 shft-notarith interchangeable，也不是已经 EIP-145 SAR not already signed-div / not already same-rounding / not already same-operand-order 正式三事 bundled（231 item 2 余量） interchangeable / 231 shft item 2 interchangeable。**  
   官方把算术右移不是已经是有符号除和已经是有符号除写成两件。看见算术右移不是已经是有符号除，不是已经是有符号除。

2. **看见SAR is not already signed division / 看见算术右移不是已经是有符号除 / 这份对象 is not already 已经是同一条舍入 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1405 shft-notsdiv interchangeable / 1406 shft-notpack interchangeable，也不是已经 内存拷≠身份预编译 interchangeable / 216 内存拷≠身份预编译 interchangeable。**  
   官方把SAR is not already signed division和已经是同一条舍入写成两件。看见SAR is not already signed division，不是已经是同一条舍入。

3. **看见算术右移不是已经是有符号除 / 看见SAR is not already signed division / 这份对象 is not already 已经和加减同一套操作数顺序 interchangeable，也不是已经 shift vs arithmetic bundled（231） interchangeable / 1405 shft-notsdiv interchangeable / 1404 shft-notarith interchangeable，也不是已经 BLAKE2压缩≠已是哈希 interchangeable / 230 BLAKE2压缩≠已是哈希 interchangeable。**  
   官方把算术右移不是已经是有符号除和已经和加减同一套操作数顺序写成两件。看见算术右移不是已经是有符号除，不是已经和加减同一套操作数顺序。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。

## 官方为什么这样拆

- **算术右移不是已经是有符号除 interchangeable：官方写和有符号除舍入不同。**
- **看见能拼不是已经是同一条舍入。**
- **看见能移位不是已经和加减同一套操作数顺序。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是有符号除 | 不是已经是有符号除 | 不是已经内存拷≠身份预编译（216） |
| 已经是同一条舍入 | 不是已经是同一条舍入 | 不是已经BLAKE2压缩≠已是哈希（230） |
| 已经和加减同一套操作数顺序 | 不是已经和加减同一套操作数顺序 | 不是已经1404 shft-notarith |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-145 SAR not already signed-div / not already same-rounding / not already same-operand-order 正式三事（231 余量），必须分开是不是已经是有符号除、是不是已经是同一条舍入、是不是已经和加减同一套操作数顺序。可以跳过「看见 145 就已经和乘除同一条」。不要另写 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。231 SHIFT vs arithmetic bundled unbundling 在本页 item 2 续；续 [`worked-example-shft-notpack-vs-bundled.md`](worked-example-shft-notpack-vs-bundled.md)（不变量 1406 item 3）。

## 本页不抄

- 操作码号、气价档、测试向量、拼指令序列。
- 怎样做位域打包、怎样抽字段、怎样用移位代替哈希。
