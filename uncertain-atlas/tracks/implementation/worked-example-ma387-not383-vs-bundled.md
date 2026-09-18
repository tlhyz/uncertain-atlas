# 例：看见 multi_a 不是已经是 383 那种 multi；看见能套进描述符不是已经能当顶层；看见只能写在 tr 里面不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-387](https://github.com/bitcoin/bips/blob/master/bip-0387.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-387 multi_a not already 383-multi / not already toplevel / not already nestable-in-sh-wsh 正式三事（278 余量）/ not 1154 ma387-not383 interchangeable / not 278 multia-vs-tr bundled interchangeable」，不是 tapscript 多签描述符 bundled（278），也不是 multi 就已经是 sortedmulti（1142），也不是 tr 没有树就已经有脚本路径（1145）。不要另写怎样按 x-only 排公钥。

## 官方三件事

1. **看见 multi_a / 看见 sortedmulti_a 这份栏 is not already 已经是 383 那种 multi interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1154 ma387-not383 interchangeable / 1155 ma387-notenc interchangeable / 278 ma item 2 thresh-not-enc interchangeable，也不是已经 BIP-387 multi_a not already 383-multi / not already toplevel / not already nestable-in-sh-wsh 正式三事 bundled（278 item 1 余量） interchangeable / 278 ma item 1 interchangeable。**  
   官方写：这两种表达式只产出 tapscript，也只允许出现在 tapscript 上下文。看见写了多签表达式，不是已经是 383。

2. **看见能套进描述符 / 看见 multi_a / 这份栏 is not already 已经能当顶层 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1154 ma387-not383 interchangeable / 278 ma item 3 sort-not-383 interchangeable / 1156 ma387-notsort interchangeable，也不是已经 multi 就已经是 sortedmulti interchangeable / 1142 desc383-notsort interchangeable。**  
   官方写：它们只能写在 `tr` 里面。看见能套进描述符，不是已经能当顶层，也不是已经能套进 `sh` 或 `wsh`。

3. **看见只能写在 tr 里面 / 看见 multi_a / 这份栏 is not already 已经交差 interchangeable，也不是已经 tapscript 多签描述符 bundled（278） interchangeable / 1154 ma387-not383 interchangeable / 1155 ma387-notenc interchangeable，也不是已经 tr 没有树就已经有脚本路径 interchangeable / 1145 tr386-notpath interchangeable。**  
   官方把本页写成只产出 tapscript、只许出现在 `tr` 里。看见只能写在 `tr` 里面，不是已经交差。

脚本模板、测试向量、例钥、门限档数字、钥数上限数字是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **multi_a 不是已经是 383：** 官方把本页写成只产出 tapscript。
- **能套进描述符 不是已经能当顶层：** 官方把本页写成只能写在 tr 里。
- **只能写在 tr 里面 不是已经交差：** 官方把放置写成独立一句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 是不是 383 | 不是已经是 383 那种 multi | 不是已经是 sortedmulti（1142） |
| 顶层 | 不是已经能当顶层 | 不是已经同一套编码（1155） |
| 交差 | 不是已经交差 | 不是已经有脚本路径（1145） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-387 multi_a not already 383-multi / not already toplevel / not already nestable-in-sh-wsh 正式三事（278 余量），必须分开是不是已经是 383、是不是已经能当顶层、是不是已经交差。可以跳过「看见又一种 multi 就已经是 383」。不要另写怎样按 x-only 排公钥。278 multi_a vs tr bundled unbundling 在本页 item 1 启动；续 [`worked-example-ma387-notenc-vs-bundled.md`](worked-example-ma387-notenc-vs-bundled.md)（不变量 1155 item 2）。

## 本页不抄

- 脚本模板、测试向量、例钥、门限档数字、钥数上限数字。
- 怎样按字典序排 x-only、怎样选门限档、怎样嵌进 tr。
