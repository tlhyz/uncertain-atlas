# 例：看见 threshold-keycount is not already same-cap interchangeable / not already any-number interchangeable / not already settled interchangeable

**层次**：应用 / BIP-383 threshold-keycount not already same-cap / not already any-number / not already settled 正式三事（274 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-383](https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-383 threshold-keycount not already same-cap / not already any-number / not already settled 正式三事（274 余量）/ not 1143 desc383-notcap interchangeable / not 274 multi-vs-sortedmulti bundled interchangeable」，不是多签描述符 bundled（274），也不是付给脚本哈希就已经揭开赎回（170），也不是这一输入的微调就已经是盲签（1141）。不要另写怎样按字节排公钥。

## 官方三件事

1. **看见门限 / 看见钥数 这份栏 is not already 已经同一套上限 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1143 desc383-notcap interchangeable / 1142 desc383-notsort interchangeable / 274 multi item 1 multi-not-sorted interchangeable，也不是已经 BIP-383 threshold-keycount not already same-cap / not already any-number / not already settled 正式三事 bundled（274 item 2 余量） interchangeable / 274 multi item 2 interchangeable。**  
   官方写：能出现的钥数还要看外层描述符。用在顶层时，最多只能有三把。看见写了门限，不是已经过了外层那道界 interchangeable——本页从 274 item 2 侧钉 not already same-cap 单句。274 multi vs sortedmulti bundled unbundling 在本页 item 2 续。

2. **看见套进了脚本哈希 / 看见门限 / 这份栏 is not already 已经是顶层那三把 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1143 desc383-notcap interchangeable / 274 multi item 3 xpubs-not-own-index interchangeable / 1144 desc383-notidx interchangeable，也不是已经付给脚本哈希就已经揭开赎回 interchangeable / 170 hash interchangeable。**  
   官方把套在脚本哈希表达式里时钥数更少、未压缩钥更占地方写成另一道界。看见套进了脚本哈希，不是已经是顶层那三把 interchangeable。本页钉 not already any-number 单句。

3. **看见否则另有一把更大的上限 / 看见门限 / 这份栏 is not already 已经交差 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1143 desc383-notcap interchangeable / 1142 desc383-notsort interchangeable，也不是已经这一输入的微调就已经是盲签 interchangeable / 1141 del89-notblind interchangeable。**  
   官方按顶层、脚本哈希、其它外层分开写钥数界。看见否则另有一把更大的上限，不是已经交差 interchangeable。274 multi vs sortedmulti bundled unbundling 在本页 item 2 续。

函数名单、脚本模板、测试向量、怎样按字节排是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-383 threshold-keycount not already same-cap ≠ 已经同一套上限 interchangeable：** 官方按顶层、脚本哈希、其它外层分开写钥数界。
- **看见套进了脚本哈希 not already any-number ≠ 已经是顶层那三把 interchangeable：** 官方把套进脚本哈希时钥数更少写成另一道界。
- **看见否则另有一把更大的上限 not already settled ≠ 已经交差 interchangeable：** 官方把其它外层的更大上限写成独立限制；274 multi vs sortedmulti bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 门限 / 钥数 | 不是已经同一套上限 | 不是付给脚本哈希就已经揭开赎回（170） |
| 看见套进了脚本哈希 | 不是已经是顶层那三把 | 不是这一输入的微调就已经是盲签（1141） |
| 看见否则另有一把更大的上限 | 不是已经交差 | 不是多把扩展钥就已经各自编号（1144） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-383 threshold-keycount not already same-cap / not already any-number / not already settled 正式三事（274 余量），必须分开是不是已经同一套上限、是不是已经是顶层那三把、是不是已经交差。可以跳过「看见多签表达式就已经排过」。不要另写怎样按字节排公钥。274 multi vs sortedmulti bundled unbundling 在本页 item 2 续；续 [`worked-example-desc383-notidx-vs-bundled.md`](worked-example-desc383-notidx-vs-bundled.md)（不变量 1144 item 3）。

## 本页不抄

- 函数名单、脚本模板、测试向量、例钥、整数编码。
- 怎样按字典序排、怎样数赎回脚本字节、怎样选子下标。
- 多签描述符 bundled。那是不变量 274。
- 付给脚本哈希就已经揭开赎回。那是不变量 170。
