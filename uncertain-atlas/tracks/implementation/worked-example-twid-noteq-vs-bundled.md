# 例：看见txid不是wtxid不是已经是wtxid；看见txid is not already wtxid不是已经是不变量 248；看见txid不是wtxid不是已经 152 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)（Segregated Witness Consensus layer）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-141 txid not already wtxid / not already 248 / not already 152-bundled 正式三事（152 余量）/ not 1551 twid-noteq interchangeable / not 152 txid-vs-wtxid bundled interchangeable」，不是 txid vs wtxid bundled（152），也不是已经 wtxid通告≠已有（248），也不是已经 策略≠共识（144）。不要另写 怎样改见证编码。

## 官方三件事

1. **看见txid不是wtxid / 看见txid不是wtxid 这份对象 is not already 已经是wtxid interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1551 twid-noteq interchangeable / 1552 twid-notchg interchangeable，也不是已经 BIP-141 txid not already wtxid / not already 248 / not already 152-bundled 正式三事 bundled（152 item 1 余量） interchangeable / 152 twid item 1 interchangeable。**  
   官方把txid不是wtxid和已经是wtxid写成两件。看见txid不是wtxid，不是已经是wtxid。

2. **看见txid is not already wtxid / 看见txid不是wtxid / 这份对象 is not already 已经是不变量 248 interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1551 twid-noteq interchangeable / 1553 twid-notmer interchangeable，也不是已经 wtxid通告≠已有 interchangeable / 248 wtxid通告≠已有 interchangeable。**  
   官方把txid is not already wtxid和已经是不变量 248写成两件。看见txid is not already wtxid，不是已经是不变量 248。

3. **看见txid不是wtxid / 看见txid is not already wtxid / 这份对象 is not already 已经 152 bundled interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1551 twid-noteq interchangeable / 1552 twid-notchg interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把txid不是wtxid和已经 152 bundled写成两件。看见txid不是wtxid，不是已经 152 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样改见证编码。

## 官方为什么这样拆

- **txid不是wtxid interchangeable：官方写每笔交易有 2 个 ID，txid 是传统序列化，wtxid 是带见证的新序列化。**
- **看见本页不是已经是不变量 248。**
- **看见两套哈希不是已经 152 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是wtxid | 不是已经是wtxid | 不是已经wtxid通告≠已有（248） |
| 已经是不变量 248 | 不是已经是不变量 248 | 不是已经策略≠共识（144） |
| 已经 152 bundled | 不是已经 152 bundled | 不是已经1552 twid-notchg |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-141 txid not already wtxid / not already 248 / not already 152-bundled 正式三事（152 余量），必须分开是不是已经是wtxid、是不是已经是不变量 248、是不是已经 152 bundled。可以跳过「看见旧节点也验了见证」。不要另写 怎样改见证编码。152 txid vs wtxid bundled unbundling 在本页 item 1 启动；续 [`worked-example-twid-notchg-vs-bundled.md`](worked-example-twid-notchg-vs-bundled.md)（不变量 1552 item 2）。

## 本页不抄

- 承诺魔数、重量公式、版本0程序长度。
- 怎样改见证编码。
