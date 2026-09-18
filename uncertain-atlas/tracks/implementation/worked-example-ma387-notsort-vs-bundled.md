# 例：看见 sortedmulti_a 不是已经是 383 那种排序；看见排的是公钥不是已经排的是同一类钥；看见按字典序排 x-only 不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-387](https://github.com/bitcoin/bips/blob/master/bip-0387.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-387 sortedmulti_a not already 383-sort / not already same-key-class / not already settled 正式三事（278 余量）/ not 1156 ma387-notsort interchangeable / not 278 multia-vs-tr bundled interchangeable」，不是 tapscript 多签描述符 bundled（278），也不是 383 那种 multi 已经按字典序排（1142），也不是压缩钥就已经是 x-only（1147）。不要另写怎样按 x-only 排公钥。

## 官方三件事

1. **看见 sortedmulti_a / 看见按字典序排 这份栏 is not already 已经是 383 那种排序 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1156 ma387-notsort interchangeable / 1154 ma387-not383 interchangeable / 278 ma item 1 ma-not-383 interchangeable，也不是已经 BIP-387 sortedmulti_a not already 383-sort / not already same-key-class / not already settled 正式三事 bundled（278 item 3 余量） interchangeable / 278 ma item 3 interchangeable。**  
   官方写：`sortedmulti_a` 唯一的改动，是在造输出脚本之前按字典序排 x-only 公钥。看见排过了，不是已经是 383 那种多签排序。

2. **看见排的是公钥 / 看见 sortedmulti_a / 这份栏 is not already 已经排的是同一类钥 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1156 ma387-notsort interchangeable / 278 ma item 2 thresh-not-enc interchangeable / 1155 ma387-notenc interchangeable，也不是已经 383 那种 multi 已经按字典序排 interchangeable / 1142 desc383-notsort interchangeable。**  
   官方写：这种排序排的是即将写进输出脚本的那些钥，也就是扩展钥都派生完之后。看见排的是公钥，不是已经排的是同一类钥。

3. **看见按字典序排 x-only / 看见 sortedmulti_a / 这份栏 is not already 已经交差 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1156 ma387-notsort interchangeable / 1154 ma387-not383 interchangeable，也不是已经压缩钥就已经是 x-only interchangeable / 1147 tr386-notxonly interchangeable。**  
   官方把本页排序写成排 x-only 公钥。看见按字典序排 x-only，不是已经交差。

脚本模板、测试向量、例钥、门限档数字、钥数上限数字是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **sortedmulti_a 不是已经是 383 那种排序：** 官方把本页排序写成排 x-only。
- **排的是公钥 不是已经排的是同一类钥：** 官方把排序对象写成派生完之后的那些钥。
- **按字典序排 x-only 不是已经交差：** 官方把排序写成独立一句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 排序种类 | 不是已经是 383 那种排序 | 不是已经是 383 sortedmulti（1142） |
| 钥类 | 不是已经排的是同一类钥 | 不是已经同一套编码（1155） |
| 交差 | 不是已经交差 | 不是已经是 x-only（1147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-387 sortedmulti_a not already 383-sort / not already same-key-class / not already settled 正式三事（278 余量），必须分开是不是已经是 383 那种排序、是不是已经排的是同一类钥、是不是已经交差。可以跳过「看见又一种 multi 就已经是 383」。不要另写怎样按 x-only 排公钥。278 multi_a vs tr bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 脚本模板、测试向量、例钥、门限档数字、钥数上限数字。
- 怎样按字典序排 x-only、怎样选门限档、怎样嵌进 tr。
