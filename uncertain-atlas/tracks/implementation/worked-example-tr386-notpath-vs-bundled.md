# 例：看见 tr-key-only is not already has-script-path interchangeable / not already same-tweak interchangeable / not already settled interchangeable

**层次**：应用 / BIP-386 tr-key-only not already has-script-path / not already same-tweak / not already settled 正式三事（275 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-386](https://github.com/bitcoin/bips/blob/master/bip-0386.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-386 tr-key-only not already has-script-path / not already same-tweak / not already settled 正式三事（275 余量）/ not 1145 tr386-notpath interchangeable / not 275 tr-vs-tree bundled interchangeable」，不是 tr 描述符 bundled（275），也不是派生钥就已经是输出钥（1136），也不是钥匙路径就已经揭开有没有树（153）。不要另写怎样算标签微调。

## 官方三件事

1. **看见 tr 只有钥 / 看见没有树参数 这份栏 is not already 已经有脚本路径 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1145 tr386-notpath interchangeable / 1146 tr386-notold interchangeable / 275 tr item 2 tree-not-old interchangeable，也不是已经 BIP-386 tr-key-only not already has-script-path / not already same-tweak / not already settled 正式三事 bundled（275 item 1 余量） interchangeable / 275 tr item 1 interchangeable。**  
   官方写：`tr` 只能当顶层表达式。只吃一把钥时，产出没有脚本路径的 P2TR 输出脚本。看见只写了钥，不是已经有脚本路径 interchangeable——本页从 275 item 1 侧钉 not already has-script-path 单句。275 tr vs tree bundled unbundling 在本页 item 1 启动。

2. **看见带了树 / 看见 tr 只有钥 / 这份栏 is not already 已经和带树那次同一套微调 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1145 tr386-notpath interchangeable / 275 tr item 3 key-not-xonly interchangeable / 1147 tr386-notxonly interchangeable，也不是已经派生钥就已经是输出钥 interchangeable / 1136 tap86-notout interchangeable。**  
   官方把带上树参数时才有脚本路径、树变成 341 里的脚本树再和内部钥合成输出钥写成另一种产出。看见带了树，不是已经是「没有脚本路径」那种微调 interchangeable。本页钉 not already same-tweak 单句。

3. **看见 tr 只能当顶层表达式 / 看见 tr 只有钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1145 tr386-notpath interchangeable / 1146 tr386-notold interchangeable，也不是已经钥匙路径就已经揭开有没有树 interchangeable / 153 keypath interchangeable。**  
   官方把只吃钥和再吃一棵树写成两种产出。看见 tr 只能当顶层表达式，不是已经交差 interchangeable。275 tr vs tree bundled unbundling 在本页 item 1 启动。

树写法、微调公式、测试向量、十六进制宽度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-386 tr-key-only not already has-script-path ≠ 已经有脚本路径 interchangeable：** 官方把只吃钥写成产出没有脚本路径的 P2TR。
- **看见带了树 not already same-tweak ≠ 已经和带树那次同一套微调 interchangeable：** 官方把带树时才算出默克尔根再合成输出钥写成另一种产出。
- **看见 tr 只能当顶层表达式 not already settled ≠ 已经交差 interchangeable：** 官方把只吃钥和再吃一棵树写成两种产出；275 tr vs tree bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| tr 只有钥 / 没有树参数 | 不是已经有脚本路径 | 不是派生钥就已经是输出钥（1136） |
| 看见带了树 | 不是已经和带树那次同一套微调 | 不是钥匙路径就已经揭开有没有树（153） |
| 看见 tr 只能当顶层表达式 | 不是已经交差 | 不是树表达式就已经是旧脚本套法（1146） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-386 tr-key-only not already has-script-path / not already same-tweak / not already settled 正式三事（275 余量），必须分开是不是已经有脚本路径、是不是已经和带树那次同一套微调、是不是已经交差。可以跳过「看见 tr 就已经有脚本树」。不要另写怎样算标签微调。275 tr vs tree bundled unbundling 在本页 item 1 启动；续 [`worked-example-tr386-notold-vs-bundled.md`](worked-example-tr386-notold-vs-bundled.md)（不变量 1146 item 2）。

## 本页不抄

- 树括号写法、微调公式、测试向量、十六进制宽度、例钥。
- 怎样算默克尔根、怎样 lift、怎样把压缩钥转成 x-only。
- tr 描述符 bundled。那是不变量 275。
- 派生钥就已经是输出钥。那是不变量 1136。
