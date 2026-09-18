# 例：看见空数据哈希不是已经是账户不存在不是已经是账户不存在；看见empty-data hash is not already missing不是已经改了 161；看见空数据哈希不是已经是账户不存在不是已经是 3607 发送者规则

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1052](https://eips.ethereum.org/EIPS/eip-1052)（Final, Core, EXTCODEHASH）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1052 empty-data-hash not already missing / not already 161-changed / not already 3607 正式三事（221 余量）/ not 1394 xhash-notmiss interchangeable / not 221 extcodehash-vs-copy bundled interchangeable」，不是 extcodehash vs copy bundled（221），也不是已经 EIP-3607 发送者（162），也不是已经 链号指令≠已签（220）。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。

## 官方三件事

1. **看见空数据哈希不是已经是账户不存在 / 看见空数据哈希不是已经是账户不存在 这份对象 is not already 已经是账户不存在 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1394 xhash-notmiss interchangeable / 1392 xhash-notsee interchangeable，也不是已经 EIP-1052 empty-data-hash not already missing / not already 161-changed / not already 3607 正式三事 bundled（221 item 3 余量） interchangeable / 221 xhash item 3 interchangeable。**  
   官方把空数据哈希不是已经是账户不存在和已经是账户不存在写成两件。看见空数据哈希不是已经是账户不存在，不是已经是账户不存在。

2. **看见empty-data hash is not already missing / 看见空数据哈希不是已经是账户不存在 / 这份对象 is not already 已经改了 161 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1394 xhash-notmiss interchangeable / 1393 xhash-notzero interchangeable，也不是已经 EIP-3607 发送者 interchangeable / 162 EIP-3607 发送者 interchangeable。**  
   官方把empty-data hash is not already missing和已经改了 161写成两件。看见empty-data hash is not already missing，不是已经改了 161。

3. **看见空数据哈希不是已经是账户不存在 / 看见empty-data hash is not already missing / 这份对象 is not already 已经是 3607 发送者规则 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1394 xhash-notmiss interchangeable / 1392 xhash-notsee interchangeable，也不是已经 链号指令≠已签 interchangeable / 220 链号指令≠已签 interchangeable。**  
   官方把空数据哈希不是已经是账户不存在和已经是 3607 发送者规则写成两件。看见空数据哈希不是已经是账户不存在，不是已经是 3607 发送者规则。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。

## 官方为什么这样拆

- **空数据哈希不是已经是账户不存在 interchangeable：官方把没代码和地址不存在分开。**
- **看见本页不是已经改了 161。**
- **看见任意地址读哈希不是已经是 3607 发送者规则。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是账户不存在 | 不是已经是账户不存在 | 不是已经EIP-3607 发送者（162） |
| 已经改了 161 | 不是已经改了 161 | 不是已经链号指令≠已签（220） |
| 已经是 3607 发送者规则 | 不是已经是 3607 发送者规则 | 不是已经1392 xhash-notsee |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1052 empty-data-hash not already missing / not already 161-changed / not already 3607 正式三事（221 余量），必须分开是不是已经是账户不存在、是不是已经改了 161、是不是已经是 3607 发送者规则。可以跳过「看见代码哈希就已经看见代码」。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。221 EXTCODEHASH vs copy bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-1344 CHAINID（220）。

## 本页不抄

- 操作码号、气价、空代码哈希字面量、位宽、测试向量。
- 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。
