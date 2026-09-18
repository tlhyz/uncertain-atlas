# 例：看见门限不是已经同一套编码；看见 383 按外层限钥数不是已经是本页；看见钥数另有一把上限不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-387](https://github.com/bitcoin/bips/blob/master/bip-0387.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-387 threshold not already same-encoding / not already 383-outer-keycap / not already settled 正式三事（278 余量）/ not 1155 ma387-notenc interchangeable / not 278 multia-vs-tr bundled interchangeable」，不是 tapscript 多签描述符 bundled（278），也不是 383 那种门限已经同一套上限（1143），也不是看见描述符就已经是地址（184）。不要另写怎样按 x-only 排公钥。

## 官方三件事

1. **看见门限 / 看见钥数 这份栏 is not already 已经同一套编码 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1155 ma387-notenc interchangeable / 1154 ma387-not383 interchangeable / 278 ma item 1 ma-not-383 interchangeable，也不是已经 BIP-387 threshold not already same-encoding / not already 383-outer-keycap / not already settled 正式三事 bundled（278 item 2 余量） interchangeable / 278 ma item 2 interchangeable。**  
   官方写：产出的脚本还要看门限落在哪一档。门限不超过一小档时，用一档操作码写法；超过那一档时，改用另一套把门限推进去的写法。看见写了门限，不是已经是同一套编码。

2. **看见 383 按外层限钥数 / 看见门限 / 这份栏 is not already 已经是本页 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1155 ma387-notenc interchangeable / 278 ma item 3 sort-not-383 interchangeable / 1156 ma387-notsort interchangeable，也不是已经 383 那种门限已经同一套上限 interchangeable / 1143 desc383-notcap interchangeable。**  
   官方把钥数另写成一把上限。看见 383 按外层限钥数，不是已经是本页。

3. **看见钥数另有一把上限 / 看见门限 / 这份栏 is not already 已经交差 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1155 ma387-notenc interchangeable / 1154 ma387-not383 interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方按门限是否超过一小档写成两套写法。看见钥数另有一把上限，不是已经交差。

脚本模板、测试向量、例钥、门限档数字、钥数上限数字是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **门限 不是已经同一套编码：** 官方按门限档写成两套写法。
- **383 外层钥数界 不是已经是本页：** 官方把本页钥数上限写成另一句。
- **钥数另有一把上限 不是已经交差：** 官方把门限档和钥数上限写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 门限编码 | 不是已经同一套编码 | 不是已经是 383 那种上限（1143） |
| 外层钥数界 | 不是已经是本页 | 不是已经是 383 那种 multi（1154） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-387 threshold not already same-encoding / not already 383-outer-keycap / not already settled 正式三事（278 余量），必须分开是不是已经同一套编码、是不是已经是 383 那种外层钥数界、是不是已经交差。可以跳过「看见又一种 multi 就已经是 383」。不要另写怎样按 x-only 排公钥。278 multi_a vs tr bundled unbundling 在本页 item 2 续；续 [`worked-example-ma387-notsort-vs-bundled.md`](worked-example-ma387-notsort-vs-bundled.md)（不变量 1156 item 3）。

## 本页不抄

- 脚本模板、测试向量、例钥、门限档数字、钥数上限数字。
- 怎样按字典序排 x-only、怎样选门限档、怎样嵌进 tr。
