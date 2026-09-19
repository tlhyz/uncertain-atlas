# 例：看见付给脚本哈希不是已经揭开赎回脚本不是已经揭开赎回脚本；看见paying a script hash is not already revealing the redeem script不是已经是不变量 297；看见付给脚本哈希不是已经揭开赎回脚本不是已经 170 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki)（Pay to Script Hash）。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-16 hash-output not already redeem-revealed / not already 297 / not already 170-bundled 正式三事（170 余量）/ not 1533 phsh-notrev interchangeable / not 170 p2sh-hash-vs-redeem bundled interchangeable」，不是 p2sh hash vs redeem bundled（170），也不是已经 P2SH地址≠赎回（297），也不是已经 钥匙路径≠揭树（153）。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。

## 官方三件事

1. **看见付给脚本哈希不是已经揭开赎回脚本 / 看见付给脚本哈希不是已经揭开赎回脚本 这份对象 is not already 已经揭开赎回脚本 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1533 phsh-notrev interchangeable / 1534 phsh-notrun interchangeable，也不是已经 BIP-16 hash-output not already redeem-revealed / not already 297 / not already 170-bundled 正式三事 bundled（170 item 1 余量） interchangeable / 170 phsh item 1 interchangeable。**  
   官方把付给脚本哈希不是已经揭开赎回脚本和已经揭开赎回脚本写成两件。看见付给脚本哈希不是已经揭开赎回脚本，不是已经揭开赎回脚本。

2. **看见paying a script hash is not already revealing the redeem script / 看见付给脚本哈希不是已经揭开赎回脚本 / 这份对象 is not already 已经是不变量 297 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1533 phsh-notrev interchangeable / 1535 phsh-notinr interchangeable，也不是已经 P2SH地址≠赎回 interchangeable / 297 P2SH地址≠赎回 interchangeable。**  
   官方把paying a script hash is not already revealing the redeem script和已经是不变量 297写成两件。看见paying a script hash is not already revealing the redeem script，不是已经是不变量 297。

3. **看见付给脚本哈希不是已经揭开赎回脚本 / 看见paying a script hash is not already revealing the redeem script / 这份对象 is not already 已经 170 bundled interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1533 phsh-notrev interchangeable / 1534 phsh-notrun interchangeable，也不是已经 钥匙路径≠揭树 interchangeable / 153 钥匙路径≠揭树 interchangeable。**  
   官方把付给脚本哈希不是已经揭开赎回脚本和已经 170 bundled写成两件。看见付给脚本哈希不是已经揭开赎回脚本，不是已经 170 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。

## 官方为什么这样拆

- **付给脚本哈希不是已经揭开赎回脚本 interchangeable：官方写付款人用固定长度哈希付钱，责任挪到花费人，不是赎回已经在链上。**
- **看见本页不是已经是不变量 297。**
- **看见哈希承诺不是已经 170 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经揭开赎回脚本 | 不是已经揭开赎回脚本 | 不是已经P2SH地址≠赎回（297） |
| 已经是不变量 297 | 不是已经是不变量 297 | 不是已经钥匙路径≠揭树（153） |
| 已经 170 bundled | 不是已经 170 bundled | 不是已经1534 phsh-notrun |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-16 hash-output not already redeem-revealed / not already 297 / not already 170-bundled 正式三事（170 余量），必须分开是不是已经揭开赎回脚本、是不是已经是不变量 297、是不是已经 170 bundled。可以跳过「看见哈希对上就已经验过内层」。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。170 p2sh hash vs redeem bundled unbundling 在本页 item 1 启动；续 [`worked-example-phsh-notrun-vs-bundled.md`](worked-example-phsh-notrun-vs-bundled.md)（不变量 1534 item 2）。

## 本页不抄

- 激活票数、字节上限、例脚本、时间戳、操作码号。
- 怎样构造旧合法新非法的赎回、一确认攻击。
