# 例：看见校验过不是见证程序已经在链上不是已经在链上；看见passing the checksum is not already the witness program being on chain不是已经是不变量 170；看见校验过不是见证程序已经在链上不是已经是不变量 152

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki)（Bech32 address format）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-173 checksum-pass not already program-on-chain / not already 170 / not already 152 正式三事（174 余量）/ not 1537 adut-notchk interchangeable / not 174 address-vs-utxo bundled interchangeable」，不是 address vs utxo bundled（174），也不是已经 哈希≠已揭开（170），也不是已经 txid≠wtxid（152）。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。

## 官方三件事

1. **看见校验过不是见证程序已经在链上 / 看见校验过不是见证程序已经在链上 这份对象 is not already 已经在链上 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1537 adut-notchk interchangeable / 1536 adut-notout interchangeable，也不是已经 BIP-173 checksum-pass not already program-on-chain / not already 170 / not already 152 正式三事 bundled（174 item 2 余量） interchangeable / 174 adut item 2 interchangeable。**  
   官方把校验过不是见证程序已经在链上和已经在链上写成两件。看见校验过不是见证程序已经在链上，不是已经在链上。

2. **看见passing the checksum is not already the witness program being on chain / 看见校验过不是见证程序已经在链上 / 这份对象 is not already 已经是不变量 170 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1537 adut-notchk interchangeable / 1538 adut-notpay interchangeable，也不是已经 哈希≠已揭开 interchangeable / 170 哈希≠已揭开 interchangeable。**  
   官方把passing the checksum is not already the witness program being on chain和已经是不变量 170写成两件。看见passing the checksum is not already the witness program being on chain，不是已经是不变量 170。

3. **看见校验过不是见证程序已经在链上 / 看见passing the checksum is not already the witness program being on chain / 这份对象 is not already 已经是不变量 152 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1537 adut-notchk interchangeable / 1536 adut-notout interchangeable，也不是已经 txid≠wtxid interchangeable / 152 txid≠wtxid interchangeable。**  
   官方把校验过不是见证程序已经在链上和已经是不变量 152写成两件。看见校验过不是见证程序已经在链上，不是已经是不变量 152。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。

## 官方为什么这样拆

- **校验过不是见证程序已经在链上 interchangeable：官方写校验不含信息，合法串必须过校验谓词，不是程序已经上链。**
- **看见本页不是已经是不变量 170。**
- **看见本页不是已经是不变量 152。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在链上 | 不是已经在链上 | 不是已经哈希≠已揭开（170） |
| 已经是不变量 170 | 不是已经是不变量 170 | 不是已经txid≠wtxid（152） |
| 已经是不变量 152 | 不是已经是不变量 152 | 不是已经1536 adut-notout |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-173 checksum-pass not already program-on-chain / not already 170 / not already 152 正式三事（174 余量），必须分开是不是已经在链上、是不是已经是不变量 170、是不是已经是不变量 152。可以跳过「看见地址就已经有输出」。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。174 address vs utxo bundled unbundling 在本页 item 2 续；续 [`worked-example-adut-notpay-vs-bundled.md`](worked-example-adut-notpay-vs-bundled.md)（不变量 1538 item 3）。

## 本页不抄

- 字符表、生成式、例地址、网络前缀常数、长度窗。
- 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。
