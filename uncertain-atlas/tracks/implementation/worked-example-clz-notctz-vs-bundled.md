# 例：看见能表达最低位不是已经有数尾零不是已经有数尾零；看见expressing LSB is not already a CTZ opcode不是已经更安全；看见能表达最低位不是已经有数尾零不是已经是不变量 206

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7939](https://eips.ethereum.org/EIPS/eip-7939)（Count leading zeros (CLZ) opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7939 express-lsb not already ctz / not already safer / not already 206 正式三事（208 余量）/ not 1472 clz-notctz interchangeable / not 208 clz-vs-zk bundled interchangeable」，不是 clz vs zk bundled（208），也不是已经 P256≠k1（204），也不是已经 模幂长度帽≠已改计价（206）。不要另写 怎样用它拼数尾零、怎样压证明费。

## 官方三件事

1. **看见能表达最低位不是已经有数尾零 / 看见能表达最低位不是已经有数尾零 这份对象 is not already 已经有数尾零 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1472 clz-notctz interchangeable / 1470 clz-notzk interchangeable，也不是已经 EIP-7939 express-lsb not already ctz / not already safer / not already 206 正式三事 bundled（208 item 3 余量） interchangeable / 208 clz item 3 interchangeable。**  
   官方把能表达最低位不是已经有数尾零和已经有数尾零写成两件。看见能表达最低位不是已经有数尾零，不是已经有数尾零。

2. **看见expressing LSB is not already a CTZ opcode / 看见能表达最低位不是已经有数尾零 / 这份对象 is not already 已经更安全 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1472 clz-notctz interchangeable / 1471 clz-notpq interchangeable，也不是已经 P256≠k1 interchangeable / 204 P256≠k1 interchangeable。**  
   官方把expressing LSB is not already a CTZ opcode和已经更安全写成两件。看见expressing LSB is not already a CTZ opcode，不是已经更安全。

3. **看见能表达最低位不是已经有数尾零 / 看见expressing LSB is not already a CTZ opcode / 这份对象 is not already 已经是不变量 206 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1472 clz-notctz interchangeable / 1470 clz-notzk interchangeable，也不是已经 模幂长度帽≠已改计价 interchangeable / 206 模幂长度帽≠已改计价 interchangeable。**  
   官方把能表达最低位不是已经有数尾零和已经是不变量 206写成两件。看见能表达最低位不是已经有数尾零，不是已经是不变量 206。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用它拼数尾零、怎样压证明费。

## 官方为什么这样拆

- **能表达最低位不是已经有数尾零 interchangeable：官方写最低位可以再表达、反过来不行，不是已经有数尾零。**
- **看见能表达不是已经更安全。**
- **看见本页不是已经是不变量 206。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有数尾零 | 不是已经有数尾零 | 不是已经P256≠k1（204） |
| 已经更安全 | 不是已经更安全 | 不是已经模幂长度帽≠已改计价（206） |
| 已经是不变量 206 | 不是已经是不变量 206 | 不是已经1470 clz-notzk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7939 express-lsb not already ctz / not already safer / not already 206 正式三事（208 余量），必须分开是不是已经有数尾零、是不是已经更安全、是不是已经是不变量 206。可以跳过「看见 7939 就已经更便宜的 ZK」。不要另写 怎样用它拼数尾零、怎样压证明费。208 clz vs zk bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：modexp-bound（206）。

## 本页不抄

- 操作码号、气价、高级语言实现、测试向量。
- 怎样用它拼数尾零、怎样压证明费。
