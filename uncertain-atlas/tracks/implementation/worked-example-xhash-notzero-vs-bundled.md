# 例：看见返回 0 不是已经是没代码的账户不是已经是没代码的账户；看见return 0 is not already no-code account不是已经是空数据哈希；看见返回 0 不是已经是没代码的账户不是已经是 180 空户三灯

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1052](https://eips.ethereum.org/EIPS/eip-1052)（Final, Core, EXTCODEHASH）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1052 return-0 not already no-code-account / not already empty-data-hash / not already 180 正式三事（221 余量）/ not 1393 xhash-notzero interchangeable / not 221 extcodehash-vs-copy bundled interchangeable」，不是 extcodehash vs copy bundled（221），也不是已经 空户三灯（180），也不是已经 自毁≠已删（160）。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。

## 官方三件事

1. **看见返回 0 不是已经是没代码的账户 / 看见返回 0 不是已经是没代码的账户 这份对象 is not already 已经是没代码的账户 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1393 xhash-notzero interchangeable / 1392 xhash-notsee interchangeable，也不是已经 EIP-1052 return-0 not already no-code-account / not already empty-data-hash / not already 180 正式三事 bundled（221 item 2 余量） interchangeable / 221 xhash item 2 interchangeable。**  
   官方把返回 0 不是已经是没代码的账户和已经是没代码的账户写成两件。看见返回 0 不是已经是没代码的账户，不是已经是没代码的账户。

2. **看见return 0 is not already no-code account / 看见返回 0 不是已经是没代码的账户 / 这份对象 is not already 已经是空数据哈希 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1393 xhash-notzero interchangeable / 1394 xhash-notmiss interchangeable，也不是已经 空户三灯 interchangeable / 180 空户三灯 interchangeable。**  
   官方把return 0 is not already no-code account和已经是空数据哈希写成两件。看见return 0 is not already no-code account，不是已经是空数据哈希。

3. **看见返回 0 不是已经是没代码的账户 / 看见return 0 is not already no-code account / 这份对象 is not already 已经是 180 空户三灯 interchangeable，也不是已经 extcodehash vs copy bundled（221） interchangeable / 1393 xhash-notzero interchangeable / 1392 xhash-notsee interchangeable，也不是已经 自毁≠已删 interchangeable / 160 自毁≠已删 interchangeable。**  
   官方把返回 0 不是已经是没代码的账户和已经是 180 空户三灯写成两件。看见返回 0 不是已经是没代码的账户，不是已经是 180 空户三灯。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。

## 官方为什么这样拆

- **返回 0 不是已经是没代码的账户 interchangeable：官方把不存在或 161 空推 0。**
- **看见 0 不是已经是空数据哈希。**
- **看见 0 不是已经是 180 那三盏灯本身。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是没代码的账户 | 不是已经是没代码的账户 | 不是已经空户三灯（180） |
| 已经是空数据哈希 | 不是已经是空数据哈希 | 不是已经自毁≠已删（160） |
| 已经是 180 空户三灯 | 不是已经是 180 空户三灯 | 不是已经1392 xhash-notsee |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1052 return-0 not already no-code-account / not already empty-data-hash / not already 180 正式三事（221 余量），必须分开是不是已经是没代码的账户、是不是已经是空数据哈希、是不是已经是 180 空户三灯。可以跳过「看见代码哈希就已经看见代码」。不要另写 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。221 EXTCODEHASH vs copy bundled unbundling 在本页 item 2 续；续 [`worked-example-xhash-notmiss-vs-bundled.md`](worked-example-xhash-notmiss-vs-bundled.md)（不变量 1394 item 3）。

## 本页不抄

- 操作码号、气价、空代码哈希字面量、位宽、测试向量。
- 怎样用本页探账户是否存在、怎样按哈希白名单实现、怎样复制整份代码。
