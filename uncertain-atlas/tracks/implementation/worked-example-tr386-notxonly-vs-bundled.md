# 例：看见 compressed-key is not already x-only interchangeable / not already uncompressed-ok interchangeable / not already settled interchangeable

**层次**：应用 / BIP-386 compressed-key not already x-only / not already uncompressed-ok / not already settled 正式三事（275 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-386](https://github.com/bitcoin/bips/blob/master/bip-0386.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-386 compressed-key not already x-only / not already uncompressed-ok / not already settled 正式三事（275 余量）/ not 1147 tr386-notxonly interchangeable / not 275 tr-vs-tree bundled interchangeable」，不是 tr 描述符 bundled（275），也不是已经是 tapscript 语义（189），也不是看见描述符就已经是地址（184）。不要另写怎样算标签微调。

## 官方三件事

1. **看见压缩钥 / 看见未压缩钥 这份栏 is not already 已经是 x-only interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1147 tr386-notxonly interchangeable / 1145 tr386-notpath interchangeable / 275 tr item 1 key-not-path interchangeable，也不是已经 BIP-386 compressed-key not already x-only / not already uncompressed-ok / not already settled 正式三事 bundled（275 item 3 余量） interchangeable / 275 tr item 3 interchangeable。**  
   官方写：`tr` 下面所有钥表达式都必须长出 x-only 公钥。压缩钥会隐式转成 x-only。看见压缩钥，不是已经是 x-only interchangeable——本页从 275 item 3 侧钉 not already x-only 单句。275 tr vs tree bundled unbundling 在本页 item 3 完成。

2. **看见未压缩钥 / 看见压缩钥 / 这份栏 is not already 已经允许未压缩 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1147 tr386-notxonly interchangeable / 275 tr item 2 tree-not-old interchangeable / 1146 tr386-notold interchangeable，也不是已经是 tapscript 语义 interchangeable / 189 tapscript interchangeable。**  
   官方写：未压缩钥不允许。看见未压缩钥，不是已经是本页 interchangeable。本页钉 not already uncompressed-ok 单句。

3. **看见从扩展钥派生出来的钥也必须按 x-only 序列化 / 看见压缩钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经 tr 描述符 bundled（275） interchangeable / 1147 tr386-notxonly interchangeable / 1145 tr386-notpath interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把本页还另开一种只在 tr 里用的钥表达式写成独立限制。看见从扩展钥派生出来的钥也必须按 x-only 序列化，不是已经交差 interchangeable。275 tr vs tree bundled unbundling 在本页 item 3 完成。

树写法、微调公式、测试向量、十六进制宽度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-386 compressed-key not already x-only ≠ 已经是 x-only interchangeable：** 官方把压缩写成隐式转换，不是已经是 x-only。
- **看见未压缩钥 not already uncompressed-ok ≠ 已经允许未压缩 interchangeable：** 官方禁止未压缩。
- **看见从扩展钥派生出来的钥也必须按 x-only 序列化 not already settled ≠ 已经交差 interchangeable：** 官方把派生钥也必须按 x-only 序列化写成独立限制；275 tr vs tree bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 压缩钥 / 未压缩钥 | 不是已经是 x-only | 不是已经是 tapscript 语义（189） |
| 看见未压缩钥 | 不是已经允许未压缩 | 不是看见描述符就已经是地址（184） |
| 看见从扩展钥派生出来的钥也必须按 x-only 序列化 | 不是已经交差 | 不是 tr 没有树就已经有脚本路径（1145） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-386 compressed-key not already x-only / not already uncompressed-ok / not already settled 正式三事（275 余量），必须分开是不是已经是 x-only、是不是已经允许未压缩、是不是已经交差。可以跳过「看见 tr 就已经有脚本树」。不要另写怎样算标签微调。275 tr vs tree bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 树括号写法、微调公式、测试向量、十六进制宽度、例钥。
- 怎样算默克尔根、怎样 lift、怎样把压缩钥转成 x-only。
- tr 描述符 bundled。那是不变量 275。
- 已经是 tapscript 语义。那是不变量 189。
