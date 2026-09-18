# 例：看见定长输入不是已经是任意哈希 API不是已经是任意哈希 API；看见fixed-length input is not already a generic hash API不是已经返回一份摘要；看见定长输入不是已经是任意哈希 API不是已经是不变量 199

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-152](https://eips.ethereum.org/EIPS/eip-152)（Final, Core, Add BLAKE2 compression function F precompile）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-152 fixed-input not already generic-hash-API / not already digest / not already 199 正式三事（230 余量）/ not 1436 b2f-notapi interchangeable / not 230 blake2f-vs-hash bundled interchangeable」，不是 blake2f vs hash bundled（230），也不是已经 代码哈希指令≠已看见代码（221），也不是已经 预编译算术≠已验 BLS（199）。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。

## 官方三件事

1. **看见定长输入不是已经是任意哈希 API / 看见定长输入不是已经是任意哈希 API 这份对象 is not already 已经是任意哈希 API interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1436 b2f-notapi interchangeable / 1434 b2f-nothash interchangeable，也不是已经 EIP-152 fixed-input not already generic-hash-API / not already digest / not already 199 正式三事 bundled（230 item 3 余量） interchangeable / 230 b2f item 3 interchangeable。**  
   官方把定长输入不是已经是任意哈希 API和已经是任意哈希 API写成两件。看见定长输入不是已经是任意哈希 API，不是已经是任意哈希 API。

2. **看见fixed-length input is not already a generic hash API / 看见定长输入不是已经是任意哈希 API / 这份对象 is not already 已经返回一份摘要 interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1436 b2f-notapi interchangeable / 1435 b2f-notprod interchangeable，也不是已经 代码哈希指令≠已看见代码 interchangeable / 221 代码哈希指令≠已看见代码 interchangeable。**  
   官方把fixed-length input is not already a generic hash API和已经返回一份摘要写成两件。看见fixed-length input is not already a generic hash API，不是已经返回一份摘要。

3. **看见定长输入不是已经是任意哈希 API / 看见fixed-length input is not already a generic hash API / 这份对象 is not already 已经是不变量 199 interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1436 b2f-notapi interchangeable / 1434 b2f-nothash interchangeable，也不是已经 预编译算术≠已验 BLS interchangeable / 199 预编译算术≠已验 BLS interchangeable。**  
   官方把定长输入不是已经是任意哈希 API和已经是不变量 199写成两件。看见定长输入不是已经是任意哈希 API，不是已经是不变量 199。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。

## 官方为什么这样拆

- **定长输入不是已经是任意哈希 API interchangeable：官方写输入必须刚好是那一档，返回的是状态向量。**
- **看见返回状态向量不是已经返回一份摘要。**
- **看见本页不是已经是不变量 199。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是任意哈希 API | 不是已经是任意哈希 API | 不是已经代码哈希指令≠已看见代码（221） |
| 已经返回一份摘要 | 不是已经返回一份摘要 | 不是已经预编译算术≠已验 BLS（199） |
| 已经是不变量 199 | 不是已经是不变量 199 | 不是已经1434 b2f-nothash |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-152 fixed-input not already generic-hash-API / not already digest / not already 199 正式三事（230 余量），必须分开是不是已经是任意哈希 API、是不是已经返回一份摘要、是不是已经是不变量 199。可以跳过「看见 152 就已经能验 Equihash」。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。230 blake2f vs hash bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：initcode（176）。

## 本页不抄

- 预编译地址、输入宽度、每轮气价、测试向量。
- 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。
