# 例：看见头上的txid Merkle不是已经承诺wtxid不是已经承诺wtxid；看见the header txid Merkle is not already the wtxid commitment不是已经是不变量 145；看见头上的txid Merkle不是已经承诺wtxid不是已经是不变量 174

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)（Segregated Witness Consensus layer）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-141 header-txid-merkle not already wtxid-commit / not already 145 / not already 174 正式三事（152 余量）/ not 1553 twid-notmer interchangeable / not 152 txid-vs-wtxid bundled interchangeable」，不是 txid vs wtxid bundled（152），也不是已经 BLOBHASH≠sidecar（145），也不是已经 地址≠已有输出（174）。不要另写 怎样改见证编码。

## 官方三件事

1. **看见头上的txid Merkle不是已经承诺wtxid / 看见头上的txid Merkle不是已经承诺wtxid 这份对象 is not already 已经承诺wtxid interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1553 twid-notmer interchangeable / 1551 twid-noteq interchangeable，也不是已经 BIP-141 header-txid-merkle not already wtxid-commit / not already 145 / not already 174 正式三事 bundled（152 item 3 余量） interchangeable / 152 twid item 3 interchangeable。**  
   官方把头上的txid Merkle不是已经承诺wtxid和已经承诺wtxid写成两件。看见头上的txid Merkle不是已经承诺wtxid，不是已经承诺wtxid。

2. **看见the header txid Merkle is not already the wtxid commitment / 看见头上的txid Merkle不是已经承诺wtxid / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1553 twid-notmer interchangeable / 1552 twid-notchg interchangeable，也不是已经 BLOBHASH≠sidecar interchangeable / 145 BLOBHASH≠sidecar interchangeable。**  
   官方把the header txid Merkle is not already the wtxid commitment和已经是不变量 145写成两件。看见the header txid Merkle is not already the wtxid commitment，不是已经是不变量 145。

3. **看见头上的txid Merkle不是已经承诺wtxid / 看见the header txid Merkle is not already the wtxid commitment / 这份对象 is not already 已经是不变量 174 interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1553 twid-notmer interchangeable / 1551 twid-noteq interchangeable，也不是已经 地址≠已有输出 interchangeable / 174 地址≠已有输出 interchangeable。**  
   官方把头上的txid Merkle不是已经承诺wtxid和已经是不变量 174写成两件。看见头上的txid Merkle不是已经承诺wtxid，不是已经是不变量 174。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样改见证编码。

## 官方为什么这样拆

- **头上的txid Merkle不是已经承诺wtxid interchangeable：官方写头上 Merkle 用各笔 txid，新规则另要 coinbase 承诺 wtxid 根。**
- **看见本页不是已经是不变量 145。**
- **看见本页不是已经是不变量 174。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经承诺wtxid | 不是已经承诺wtxid | 不是已经BLOBHASH≠sidecar（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经地址≠已有输出（174） |
| 已经是不变量 174 | 不是已经是不变量 174 | 不是已经1551 twid-noteq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-141 header-txid-merkle not already wtxid-commit / not already 145 / not already 174 正式三事（152 余量），必须分开是不是已经承诺wtxid、是不是已经是不变量 145、是不是已经是不变量 174。可以跳过「看见旧节点也验了见证」。不要另写 怎样改见证编码。152 txid vs wtxid bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：keypath-vs-scriptpath（153）。

## 本页不抄

- 承诺魔数、重量公式、版本0程序长度。
- 怎样改见证编码。
