# 例：看见更高版本过了旧校验不是已经合法不是已经合法；看见a higher version passing old checksum is not already legal不是已经是不变量 174；看见更高版本过了旧校验不是已经合法不是已经是不变量 152

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-350](https://github.com/bitcoin/bips/blob/master/bip-0350.mediawiki)（Bech32m format for v1+ witness addresses）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-350 higher-ver-old-checksum not already legal / not already 174 / not already 152 正式三事（181 余量）/ not 1540 b32m-notv0 interchangeable / not 181 bech32m-vs-bech32 bundled interchangeable」，不是 bech32m vs bech32 bundled（181），也不是已经 地址≠已有输出（174），也不是已经 txid≠wtxid（152）。不要另写 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。

## 官方三件事

1. **看见更高版本过了旧校验不是已经合法 / 看见更高版本过了旧校验不是已经合法 这份对象 is not already 已经合法 interchangeable，也不是已经 bech32m vs bech32 bundled（181） interchangeable / 1540 b32m-notv0 interchangeable / 1539 b32m-notold interchangeable，也不是已经 BIP-350 higher-ver-old-checksum not already legal / not already 174 / not already 152 正式三事 bundled（181 item 2 余量） interchangeable / 181 b32m item 2 interchangeable。**  
   官方把更高版本过了旧校验不是已经合法和已经合法写成两件。看见更高版本过了旧校验不是已经合法，不是已经合法。

2. **看见a higher version passing old checksum is not already legal / 看见更高版本过了旧校验不是已经合法 / 这份对象 is not already 已经是不变量 174 interchangeable，也不是已经 bech32m vs bech32 bundled（181） interchangeable / 1540 b32m-notv0 interchangeable / 1541 b32m-notutx interchangeable，也不是已经 地址≠已有输出 interchangeable / 174 地址≠已有输出 interchangeable。**  
   官方把a higher version passing old checksum is not already legal和已经是不变量 174写成两件。看见a higher version passing old checksum is not already legal，不是已经是不变量 174。

3. **看见更高版本过了旧校验不是已经合法 / 看见a higher version passing old checksum is not already legal / 这份对象 is not already 已经是不变量 152 interchangeable，也不是已经 bech32m vs bech32 bundled（181） interchangeable / 1540 b32m-notv0 interchangeable / 1539 b32m-notold interchangeable，也不是已经 txid≠wtxid interchangeable / 152 txid≠wtxid interchangeable。**  
   官方把更高版本过了旧校验不是已经合法和已经是不变量 152写成两件。看见更高版本过了旧校验不是已经合法，不是已经是不变量 152。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。

## 官方为什么这样拆

- **更高版本过了旧校验不是已经合法 interchangeable：官方写必须核编码与版本是否配对，其它版本必须是后继。**
- **看见本页不是已经是不变量 174。**
- **看见本页不是已经是不变量 152。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经合法 | 不是已经合法 | 不是已经地址≠已有输出（174） |
| 已经是不变量 174 | 不是已经是不变量 174 | 不是已经txid≠wtxid（152） |
| 已经是不变量 152 | 不是已经是不变量 152 | 不是已经1539 b32m-notold |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-350 higher-ver-old-checksum not already legal / not already 174 / not already 152 正式三事（181 余量），必须分开是不是已经合法、是不是已经是不变量 174、是不是已经是不变量 152。可以跳过「看见过了校验就已经是同一套」。不要另写 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。181 bech32m vs bech32 bundled unbundling 在本页 item 2 续；续 [`worked-example-b32m-notutx-vs-bundled.md`](worked-example-b32m-notutx-vs-bundled.md)（不变量 1541 item 3）。

## 本页不抄

- 校验常数、字符表、例地址、长度窗、可读前缀。
- 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。
