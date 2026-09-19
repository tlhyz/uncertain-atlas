# 例：看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码不是已经是操作码；看见the CSV soft-fork name is not already the CHECKSEQUENCEVERIFY opcode不是已经是不变量 41；看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码不是已经是不变量 164

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki)（CHECKSEQUENCEVERIFY）。对照 [BIP-68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-112 csv-deploy not already opcode / not already 41 / not already 164 正式三事（165 余量）/ not 1529 csvd-notdep interchangeable / not 165 csv-vs-cltv bundled interchangeable」，不是 csv vs cltv bundled（165），也不是已经 MTP三把尺（41），也不是已经 CLTV≠nLockTime已锁（164）。不要另写 怎样绕过相对锁。

## 官方三件事

1. **看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码 / 看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码 这份对象 is not already 已经是操作码 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1529 csvd-notdep interchangeable / 1527 csvd-notseq interchangeable，也不是已经 BIP-112 csv-deploy not already opcode / not already 41 / not already 164 正式三事 bundled（165 item 3 余量） interchangeable / 165 csvd item 3 interchangeable。**  
   官方把CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码和已经是操作码写成两件。看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码，不是已经是操作码。

2. **看见the CSV soft-fork name is not already the CHECKSEQUENCEVERIFY opcode / 看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码 / 这份对象 is not already 已经是不变量 41 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1529 csvd-notdep interchangeable / 1528 csvd-notabs interchangeable，也不是已经 MTP三把尺 interchangeable / 41 MTP三把尺 interchangeable。**  
   官方把the CSV soft-fork name is not already the CHECKSEQUENCEVERIFY opcode和已经是不变量 41写成两件。看见the CSV soft-fork name is not already the CHECKSEQUENCEVERIFY opcode，不是已经是不变量 41。

3. **看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码 / 看见the CSV soft-fork name is not already the CHECKSEQUENCEVERIFY opcode / 这份对象 is not already 已经是不变量 164 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1529 csvd-notdep interchangeable / 1527 csvd-notseq interchangeable，也不是已经 CLTV≠nLockTime已锁 interchangeable / 164 CLTV≠nLockTime已锁 interchangeable。**  
   官方把CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码和已经是不变量 164写成两件。看见CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码，不是已经是不变量 164。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样绕过相对锁。

## 官方为什么这样拆

- **CSV软分叉部署不是已经在讲CHECKSEQUENCEVERIFY操作码 interchangeable：官方写必须和 BIP-68、BIP-113 同一机制同时部署。**
- **看见本页不是已经是不变量 41。**
- **看见本页不是已经是不变量 164。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是操作码 | 不是已经是操作码 | 不是已经MTP三把尺（41） |
| 已经是不变量 41 | 不是已经是不变量 41 | 不是已经CLTV≠nLockTime已锁（164） |
| 已经是不变量 164 | 不是已经是不变量 164 | 不是已经1527 csvd-notseq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-112 csv-deploy not already opcode / not already 41 / not already 164 正式三事（165 余量），必须分开是不是已经是操作码、是不是已经是不变量 41、是不是已经是不变量 164。可以跳过「看见 CSV 就已经是 CLTV」。不要另写 怎样绕过相对锁。165 csv vs cltv bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：cltv-vs-nlocktime（164）。

## 本页不抄

- 位旗、粒度、例脚本。
- 怎样绕过相对锁。
