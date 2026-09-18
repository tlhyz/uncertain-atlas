# 例：看见 tree-expr is not already old-wrap interchangeable / not already any-old-expr interchangeable / not already settled interchangeable

**层次**：应用 / BIP-386 tree-expr not already old-wrap / not already any-old-expr / not already settled 正式三事（275 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-386](https://github.com/bitcoin/bips/blob/master/bip-0386.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-386 tree-expr not already old-wrap / not already any-old-expr / not already settled 正式三事（275 余量）/ not 1146 tr386-notold interchangeable / not 275 tr-vs-tree bundled interchangeable」，不是 tr 描述符 bundled（275），也不是看见描述符就已经换了一门语言（191），也不是 multi 就已经是 sortedmulti（1142）。不要另写怎样算标签微调。

## 官方三件事

1. **看见树表达式 / 看见一对花括号 这份栏 is not already 已经是旧的脚本哈希套法 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1146 tr386-notold interchangeable / 1145 tr386-notpath interchangeable / 275 tr item 1 key-not-path interchangeable，也不是已经 BIP-386 tree-expr not already old-wrap / not already any-old-expr / not already settled 正式三事 bundled（275 item 2 余量） interchangeable / 275 tr item 2 interchangeable。**  
   官方写：树表达式可以是这一层允许的脚本表达式，也可以是一对树表达式。看见一对花括号，不是已经是旧的脚本哈希套法 interchangeable——本页从 275 item 2 侧钉 not already old-wrap 单句。275 tr vs tree bundled unbundling 在本页 item 2 续。

2. **看见旧表达式 / 看见树表达式 / 这份栏 is not already 已经都能进树 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1146 tr386-notold interchangeable / 275 tr item 3 key-not-xonly interchangeable / 1147 tr386-notxonly interchangeable，也不是已经看见描述符就已经换了一门语言 interchangeable / 191 miniscript interchangeable。**  
   官方写：本页写成时，旧脚本表达式里只有 `pk` 能进树。后来能进树的是 379 的 Miniscript 片段，以及 387 的 `multi_a` / `sortedmulti_a`。看见旧表达式，不是已经都能进树 interchangeable。本页钉 not already any-old-expr 单句。

3. **看见树表达式可以是一对树表达式 / 看见树表达式 / 这份栏 is not already 已经交差 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1146 tr386-notold interchangeable / 1145 tr386-notpath interchangeable，也不是已经 multi 就已经是 sortedmulti interchangeable / 1142 desc383-notsort interchangeable。**  
   官方把树写成脚本或一对树，并写明当时只有 `pk` 能进树。看见树表达式可以是一对树表达式，不是已经交差 interchangeable。275 tr vs tree bundled unbundling 在本页 item 2 续。

树写法、微调公式、测试向量、十六进制宽度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-386 tree-expr not already old-wrap ≠ 已经是旧的脚本哈希套法 interchangeable：** 官方把树写成脚本或一对树，不是旧脚本哈希套法。
- **看见旧表达式 not already any-old-expr ≠ 已经都能进树 interchangeable：** 官方把当时只有 pk 能进树写成独立限制。
- **看见树表达式可以是一对树表达式 not already settled ≠ 已经交差 interchangeable：** 官方把一对树和已经交差分开；275 tr vs tree bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 树表达式 / 一对花括号 | 不是已经是旧的脚本哈希套法 | 不是看见描述符就已经换了一门语言（191） |
| 看见旧表达式 | 不是已经都能进树 | 不是 multi 就已经是 sortedmulti（1142） |
| 看见树表达式可以是一对树表达式 | 不是已经交差 | 不是压缩钥就已经是 x-only（1147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-386 tree-expr not already old-wrap / not already any-old-expr / not already settled 正式三事（275 余量），必须分开是不是已经是旧的脚本哈希套法、是不是已经都能进树、是不是已经交差。可以跳过「看见 tr 就已经有脚本树」。不要另写怎样算标签微调。275 tr vs tree bundled unbundling 在本页 item 2 续；续 [`worked-example-tr386-notxonly-vs-bundled.md`](worked-example-tr386-notxonly-vs-bundled.md)（不变量 1147 item 3）。

## 本页不抄

- 树括号写法、微调公式、测试向量、十六进制宽度、例钥。
- 怎样算默克尔根、怎样 lift、怎样把压缩钥转成 x-only。
- tr 描述符 bundled。那是不变量 275。
- 看见描述符就已经换了一门语言。那是不变量 191。
