# 例：看见编出版本和程序不是已经付过款不是已经付过款；看见encoding version and program is not already having paid不是已经是不变量 179；看见编出版本和程序不是已经付过款不是已经是不变量 181

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki)（Bech32 address format）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-173 encoded-program not already paid / not already 179 / not already 181 正式三事（174 余量）/ not 1538 adut-notpay interchangeable / not 174 address-vs-utxo bundled interchangeable」，不是 address vs utxo bundled（174），也不是已经 工作包≠已广播（179），也不是已经 后继校验≠旧方案（181）。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。

## 官方三件事

1. **看见编出版本和程序不是已经付过款 / 看见编出版本和程序不是已经付过款 这份对象 is not already 已经付过款 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1538 adut-notpay interchangeable / 1536 adut-notout interchangeable，也不是已经 BIP-173 encoded-program not already paid / not already 179 / not already 181 正式三事 bundled（174 item 3 余量） interchangeable / 174 adut item 3 interchangeable。**  
   官方把编出版本和程序不是已经付过款和已经付过款写成两件。看见编出版本和程序不是已经付过款，不是已经付过款。

2. **看见encoding version and program is not already having paid / 看见编出版本和程序不是已经付过款 / 这份对象 is not already 已经是不变量 179 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1538 adut-notpay interchangeable / 1537 adut-notchk interchangeable，也不是已经 工作包≠已广播 interchangeable / 179 工作包≠已广播 interchangeable。**  
   官方把encoding version and program is not already having paid和已经是不变量 179写成两件。看见encoding version and program is not already having paid，不是已经是不变量 179。

3. **看见编出版本和程序不是已经付过款 / 看见encoding version and program is not already having paid / 这份对象 is not already 已经是不变量 181 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1538 adut-notpay interchangeable / 1536 adut-notout interchangeable，也不是已经 后继校验≠旧方案 interchangeable / 181 后继校验≠旧方案 interchangeable。**  
   官方把编出版本和程序不是已经付过款和已经是不变量 181写成两件。看见编出版本和程序不是已经付过款，不是已经是不变量 181。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。

## 官方为什么这样拆

- **编出版本和程序不是已经付过款 interchangeable：官方写见证地址是把版本和程序编进格式，不是已经付过款。**
- **看见本页不是已经是不变量 179。**
- **看见本页不是已经是不变量 181。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经付过款 | 不是已经付过款 | 不是已经工作包≠已广播（179） |
| 已经是不变量 179 | 不是已经是不变量 179 | 不是已经后继校验≠旧方案（181） |
| 已经是不变量 181 | 不是已经是不变量 181 | 不是已经1536 adut-notout |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-173 encoded-program not already paid / not already 179 / not already 181 正式三事（174 余量），必须分开是不是已经付过款、是不是已经是不变量 179、是不是已经是不变量 181。可以跳过「看见地址就已经有输出」。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。174 address vs utxo bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：bech32m-vs-bech32（181）。

## 本页不抄

- 字符表、生成式、例地址、网络前缀常数、长度窗。
- 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。
