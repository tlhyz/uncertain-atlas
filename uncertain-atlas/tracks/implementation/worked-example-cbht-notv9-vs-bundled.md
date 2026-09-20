# 例：看见块version加大不是已经按BIP-9位向量激活不是已经按BIP-9激活；看见bumping block version is not already BIP-9 bitvector activation不是已经是不变量 171；看见块version加大不是已经按BIP-9位向量激活不是已经是不变量 172

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki)（Block v2, Height in Coinbase）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：`index/03` 共识行、M3.1、L3.1。本页是「BIP-34 block-version-bump not already bip9-bits / not already 171 / not already 172 正式三事（173 余量）/ not 1543 cbht-notv9 interchangeable / not 173 coinbase-height-vs-header bundled interchangeable」，不是 coinbase height vs header bundled（173），也不是已经 版本位≠已激活（171），也不是已经 验过≠已是DER（172）。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。

## 官方三件事

1. **看见块version加大不是已经按BIP-9位向量激活 / 看见块version加大不是已经按BIP-9位向量激活 这份对象 is not already 已经按BIP-9激活 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1543 cbht-notv9 interchangeable / 1542 cbht-nothdr interchangeable，也不是已经 BIP-34 block-version-bump not already bip9-bits / not already 171 / not already 172 正式三事 bundled（173 item 2 余量） interchangeable / 173 cbht item 2 interchangeable。**  
   官方把块version加大不是已经按BIP-9位向量激活和已经按BIP-9激活写成两件。看见块version加大不是已经按BIP-9位向量激活，不是已经按BIP-9激活。

2. **看见bumping block version is not already BIP-9 bitvector activation / 看见块version加大不是已经按BIP-9位向量激活 / 这份对象 is not already 已经是不变量 171 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1543 cbht-notv9 interchangeable / 1544 cbht-notmat interchangeable，也不是已经 版本位≠已激活 interchangeable / 171 版本位≠已激活 interchangeable。**  
   官方把bumping block version is not already BIP-9 bitvector activation和已经是不变量 171写成两件。看见bumping block version is not already BIP-9 bitvector activation，不是已经是不变量 171。

3. **看见块version加大不是已经按BIP-9位向量激活 / 看见bumping block version is not already BIP-9 bitvector activation / 这份对象 is not already 已经是不变量 172 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1543 cbht-notv9 interchangeable / 1542 cbht-nothdr interchangeable，也不是已经 验过≠已是DER interchangeable / 172 验过≠已是DER interchangeable。**  
   官方把块version加大不是已经按BIP-9位向量激活和已经是不变量 172写成两件。看见块version加大不是已经按BIP-9位向量激活，不是已经是不变量 172。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。

## 官方为什么这样拆

- **块version加大不是已经按BIP-9位向量激活 interchangeable：官方写激活走整数版本门槛，不要听成 BIP-9 的四态。**
- **看见本页不是已经是不变量 171。**
- **看见本页不是已经是不变量 172。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经按BIP-9激活 | 不是已经按BIP-9激活 | 不是已经版本位≠已激活（171） |
| 已经是不变量 171 | 不是已经是不变量 171 | 不是已经验过≠已是DER（172） |
| 已经是不变量 172 | 不是已经是不变量 172 | 不是已经1542 cbht-nothdr |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-34 block-version-bump not already bip9-bits / not already 171 / not already 172 正式三事（173 余量），必须分开是不是已经按BIP-9激活、是不是已经是不变量 171、是不是已经是不变量 172。可以跳过「看见头就已经有高度字段」。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。173 coinbase height vs header bundled unbundling 在本页 item 2 续；续 [`worked-example-cbht-notmat-vs-bundled.md`](worked-example-cbht-notmat-vs-bundled.md)（不变量 1544 item 3）。

## 本页不抄

- 激活票数、版本号常数、编码宽度、例高度。
- 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。
