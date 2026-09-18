# 例：看见静默付款地址不是已经有一笔链上输出；看见专用编码过了校验不是已经是旧见证地址；看见码不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-352 silent-address not already output / not already paid / not already settled 正式三事（260 余量）/ not 1217 sil352-notout interchangeable / not 260 silent-payment-vs-output bundled interchangeable」，不是静默付款 bundled（260），也不是地址串就已经有输出（174），也不是付款 URI 就已经授权（255）。不要另写怎样派生输出。

## 官方三件事

1. **看见静默付款地址 / 看见一条静态收款码 这份指示 is not already 已经有一笔链上输出 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1217 sil352-notout interchangeable / 1218 sil352-notscan interchangeable / 260 silent item 2 scan-not-recv interchangeable，也不是已经 BIP-352 silent-address not already output / not already paid / not already settled 正式三事 bundled（260 item 1 余量） interchangeable / 260 silent item 1 interchangeable。**  
   官方写：本页给比特币写一种静态付款地址，链上不必把各次付款连在一起，也不必再发链上通知。外面的观察者不能把交易连回这条静默付款地址。每一次静默付款都走到一个新的地址，免得误复用。看见一条静默付款地址，不是已经有一笔链上输出，也不是已经付过。

2. **看见专用编码过了校验 / 看见静默付款地址 / 这份指示 is not already 已经是旧的见证地址方案 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1217 sil352-notout interchangeable / 260 silent item 3 reuse-not-same interchangeable / 1219 sil352-notreuse interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见专用编码过了校验，不是已经是旧的见证地址方案，也不是已经能当普通见证地址去花。

3. **看见码 / 看见静默付款地址 / 这份指示 is not already 已经交差 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1217 sil352-notout interchangeable / 1218 sil352-notscan interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方把「静态收款码」和「已经付到链上」写成两件事。看见码，不是已经交差。

派生怎么算、编码字符、测试向量是规范里的取值，本页不抄。不要另写怎样派生输出。

## 官方为什么这样拆

- **静默付款地址 不是已经有一笔链上输出：** 官方把每次走到新地址写成目标。
- **专用编码过了校验 不是已经是旧见证地址：** 官方把本页编码和旧见证地址方案写成两件。
- **码 不是已经交差：** 官方把看见码和已经付到链上写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 链上输出 | 不是已经有一笔链上输出 | 不是已经有输出（174） |
| 旧方案 | 不是已经是旧见证地址 | 不是已经授权（255） |
| 交差 | 不是已经交差 | 不是已经收到（1218） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-352 silent-address not already output / not already paid / not already settled 正式三事（260 余量），必须分开是不是已经有一笔链上输出、是不是已经是旧见证地址、是不是已经交差。可以跳过「看见收款码就已经付到链上」。不要另写怎样派生输出。260 silent payment vs output bundled unbundling 在本页 item 1 启动；续 [`worked-example-sil352-notscan-vs-bundled.md`](worked-example-sil352-notscan-vs-bundled.md)（不变量 1218 item 2）。

## 本页不抄

- 派生公式、标签哈希、可读前缀字面量、例地址、测试向量。
- 怎样扫链、怎样从输入拼共享秘密、怎样用标签把付款连起来。
