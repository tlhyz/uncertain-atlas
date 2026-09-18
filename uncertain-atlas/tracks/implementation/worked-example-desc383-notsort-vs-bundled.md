# 例：看见 multi is not already sortedmulti interchangeable / not already lex-sorted interchangeable / not already settled interchangeable

**层次**：应用 / BIP-383 multi not already sortedmulti / not already lex-sorted / not already settled 正式三事（274 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-383](https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-383 multi not already sortedmulti / not already lex-sorted / not already settled 正式三事（274 余量）/ not 1142 desc383-notsort interchangeable / not 274 multi-vs-sortedmulti bundled interchangeable」，不是多签描述符 bundled（274），也不是同一套钥就已经是同一条 P2SH 地址（1133），也不是本页多签就已经不排序（1129）。不要另写怎样按字节排公钥。

## 官方三件事

1. **看见 multi / 看见按书写顺序放钥 这份栏 is not already 已经是 sortedmulti interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1142 desc383-notsort interchangeable / 1143 desc383-notcap interchangeable / 274 multi item 2 thresh-not-same-cap interchangeable，也不是已经 BIP-383 multi not already sortedmulti / not already lex-sorted / not already settled 正式三事 bundled（274 item 1 余量） interchangeable / 274 multi item 1 interchangeable。**  
   官方写：两种表达式都吃门限和一把或多把公钥，产出同一套模板的多签输出脚本。`multi` 按描述符里给出的顺序把公钥写进输出脚本。看见写了多签表达式，不是已经排过 interchangeable——本页从 274 item 1 侧钉 not already sortedmulti 单句。274 multi vs sortedmulti bundled unbundling 在本页 item 1 启动。

2. **看见门限一样 / 看见 multi / 这份栏 is not already 已经按字典序排 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1142 desc383-notsort interchangeable / 274 multi item 3 xpubs-not-own-index interchangeable / 1144 desc383-notidx interchangeable，也不是已经同一套钥就已经是同一条 P2SH 地址 interchangeable / 1133 sort67-notaddr interchangeable。**  
   官方把 `sortedmulti` 在产出输出脚本时按字典序排公钥写成另一种表达式。看见门限一样，不是已经是同一种表达式 interchangeable。本页钉 not already lex-sorted 单句。

3. **看见这种排序排的是即将写进输出脚本的那些钥 / 看见 multi / 这份栏 is not already 已经交差 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1142 desc383-notsort interchangeable / 1143 desc383-notcap interchangeable，也不是已经本页多签就已经不排序 interchangeable / 1129 msig48-notsort interchangeable。**  
   官方把这种排序排的是扩展钥都派生完之后即将写进输出脚本的那些钥写成独立限制。看见这种排序排的是即将写进输出脚本的那些钥，不是已经交差 interchangeable。274 multi vs sortedmulti bundled unbundling 在本页 item 1 启动。

函数名单、脚本模板、测试向量、怎样按字节排是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-383 multi not already sortedmulti ≠ 已经是 sortedmulti interchangeable：** 官方把书写顺序和产出时再排写成两种表达式。
- **看见门限一样 not already lex-sorted ≠ 已经按字典序排 interchangeable：** 官方把门限一样和已经是同一种表达式分开。
- **看见这种排序排的是即将写进输出脚本的那些钥 not already settled ≠ 已经交差 interchangeable：** 官方把派生完之后再排写成独立限制；274 multi vs sortedmulti bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| multi / 按书写顺序放钥 | 不是已经是 sortedmulti | 不是同一套钥就已经是同一条 P2SH 地址（1133） |
| 看见门限一样 | 不是已经按字典序排 | 不是本页多签就已经不排序（1129） |
| 看见这种排序排的是即将写进输出脚本的那些钥 | 不是已经交差 | 不是门限就已经同一套上限（1143） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-383 multi not already sortedmulti / not already lex-sorted / not already settled 正式三事（274 余量），必须分开是不是已经是 sortedmulti、是不是已经按字典序排、是不是已经交差。可以跳过「看见多签表达式就已经排过」。不要另写怎样按字节排公钥。274 multi vs sortedmulti bundled unbundling 在本页 item 1 启动；续 [`worked-example-desc383-notcap-vs-bundled.md`](worked-example-desc383-notcap-vs-bundled.md)（不变量 1143 item 2）。

## 本页不抄

- 函数名单、脚本模板、测试向量、例钥、整数编码。
- 怎样按字典序排、怎样数赎回脚本字节、怎样选子下标。
- 多签描述符 bundled。那是不变量 274。
- 同一套钥就已经是同一条 P2SH 地址。那是不变量 1133。
