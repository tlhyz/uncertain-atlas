# 例：看见代码哈希指令不是已经看见代码不是已经看见代码本身；看见EXTCODEHASH is not already saw code不是已经是整份拷代码；看见代码哈希指令不是已经看见代码不是已经 221 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1052](https://eips.ethereum.org/EIPS/eip-1052)（Final, Core, EXTCODEHASH）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1052 code-hash opcode not already saw-code / not already EXTCODECOPY / not already 221-bundled 正式三事（221 余量）/ not 1392 xhash-notsee interchangeable / not 221 extcodehash-vs-copy bundled interchangeable」，不是 extcodehash vs copy bundled（221），也不是已经 空≠已经不存在（180），也不是已经 发送者已有代码≠能发（162）。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。

## 官方三件事

1. **看见代码哈希指令不是已经看见代码 / 看见代码哈希指令不是已经看见代码 这份对象 is not already 已经看见代码本身 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1392 xhash-notsee interchangeable / 1393 xhash-notzero interchangeable，也不是已经 EIP-1052 code-hash opcode not already saw-code / not already EXTCODECOPY / not already 221-bundled 正式三事 bundled（221 item 1 余量） interchangeable / 221 xhash item 1 interchangeable。**  
   官方把代码哈希指令不是已经看见代码和已经看见代码本身写成两件。看见代码哈希指令不是已经看见代码，不是已经看见代码本身。

2. **看见EXTCODEHASH is not already saw code / 看见代码哈希指令不是已经看见代码 / 这份对象 is not already 已经是整份拷代码 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1392 xhash-notsee interchangeable / 1394 xhash-notmiss interchangeable，也不是已经 空≠已经不存在 interchangeable / 180 空≠已经不存在 interchangeable。**  
   官方把EXTCODEHASH is not already saw code和已经是整份拷代码写成两件。看见EXTCODEHASH is not already saw code，不是已经是整份拷代码。

3. **看见代码哈希指令不是已经看见代码 / 看见EXTCODEHASH is not already saw code / 这份对象 is not already 已经 221 bundled interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1392 xhash-notsee interchangeable / 1393 xhash-notzero interchangeable，也不是已经 发送者已有代码≠能发 interchangeable / 162 发送者已有代码≠能发 interchangeable。**  
   官方把代码哈希指令不是已经看见代码和已经 221 bundled写成两件。看见代码哈希指令不是已经看见代码，不是已经 221 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。

## 官方为什么这样拆

- **代码哈希指令不是已经看见代码 interchangeable：官方把只要哈希和整份拷写成两件。**
- **看见能读哈希不是已经是整份拷代码。**
- **看见读哈希旋钮不是已经 221 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经看见代码本身 | 不是已经看见代码本身 | 不是已经空≠已经不存在（180） |
| 已经是整份拷代码 | 不是已经是整份拷代码 | 不是已经发送者已有代码≠能发（162） |
| 已经 221 bundled | 不是已经 221 bundled | 不是已经1393 xhash-notzero |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1052 code-hash opcode not already saw-code / not already EXTCODECOPY / not already 221-bundled 正式三事（221 余量），必须分开是不是已经看见代码本身、是不是已经是整份拷代码、是不是已经 221 bundled。可以跳过「看见代码哈希就已经看见代码」。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。221 EXTCODEHASH vs copy bundled unbundling 在本页 item 1 启动；续 [`worked-example-xhash-notzero-vs-bundled.md`](worked-example-xhash-notzero-vs-bundled.md)（不变量 1393 item 2）。

## 本页不抄

- 操作码号、气价、空代码哈希字面量、位宽、测试向量。
- 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。
