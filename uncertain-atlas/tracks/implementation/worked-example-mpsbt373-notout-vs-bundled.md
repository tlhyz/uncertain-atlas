# 例：看见聚合钥栏不是已经是 Taproot 输出钥；看见压缩不是已经是 371 那种 x-only；看见栏里有聚合钥不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-373 aggregate-key-field not already tap-output-key / not already x-only-or-internal / not already settled 正式三事（284 余量）/ not 1173 mpsbt373-notout interchangeable / not 284 musig-psbt-vs-tap bundled interchangeable」，不是 MuSig2 工作包栏 bundled（284），也不是聚合钥就已经是扩展公钥（1169），也不是输出脚本钥就已经是内部钥（1158）。不要另写怎样造 nonce 或部分签。

## 官方三件事

1. **看见聚合钥栏 / 看见压缩聚合钥 这份栏 is not already 已经是 Taproot 输出钥 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1173 mpsbt373-notout interchangeable / 1172 mpsbt373-notold interchangeable / 284 mpsbt item 1 old-not-hold interchangeable，也不是已经 BIP-373 aggregate-key-field not already tap-output-key / not already x-only-or-internal / not already settled 正式三事 bundled（284 item 2 余量） interchangeable / 284 mpsbt item 2 interchangeable。**  
   官方写：这份聚合钥不一定以 x-only 出现在输出钥、内部钥或脚本里。它也可以是派生出那些钥的父钥。看见栏里有聚合钥，不是已经对上输出脚本里那把。

2. **看见压缩 / 看见聚合钥栏 / 这份栏 is not already 已经是 371 那种 x-only interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1173 mpsbt373-notout interchangeable / 284 mpsbt item 3 part-not-partial interchangeable / 1174 mpsbt373-notpartial interchangeable，也不是已经输出脚本钥就已经是内部钥 interchangeable / 1158 tap371-notinner interchangeable。**  
   官方另写：32 那种扩展公钥要带偶奇字节，指纹还要用到纵坐标，所以本页聚合钥必须用压缩公钥，不能只用 x-only。看见压缩，不是已经是 371 那种 x-only。

3. **看见栏里有聚合钥 / 看见聚合钥栏 / 这份栏 is not already 已经交差 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1173 mpsbt373-notout interchangeable / 1172 mpsbt373-notold interchangeable，也不是已经聚合钥就已经是扩展公钥 interchangeable / 1169 musig328-notxpub interchangeable。**  
   官方把这份钥写成可能只是父钥，而且必须压缩。看见栏里有聚合钥，不是已经交差。

类型号、字节宽度、测试向量、例钥、算法名单是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **聚合钥栏 不是已经是输出钥：** 官方把这份钥写成可能只是父钥。
- **压缩 不是已经是 371 那种 x-only：** 官方把本页写成必须用压缩公钥。
- **栏里有聚合钥 不是已经交差：** 官方把父钥和压缩写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 输出钥 | 不是已经是 Taproot 输出钥 | 不是已经是内部钥（1158） |
| x-only | 不是已经是 371 那种 x-only | 不是已经是合成扩展公钥（1169） |
| 交差 | 不是已经交差 | 不是已经能装旧栏（1172） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-373 aggregate-key-field not already tap-output-key / not already x-only-or-internal / not already settled 正式三事（284 余量），必须分开是不是已经是输出钥、是不是已经是 371 那种 x-only、是不是已经交差。可以跳过「看见 Taproot 工作包栏就已经能签 MuSig2」。不要另写怎样造 nonce 或部分签。284 musig PSBT vs tap bundled unbundling 在本页 item 2 续；续 [`worked-example-mpsbt373-notpartial-vs-bundled.md`](worked-example-mpsbt373-notpartial-vs-bundled.md)（不变量 1174 item 3）。

## 本页不抄

- 类型号、字节宽度、测试向量、例钥、算法名单。
- 怎样造 nonce、怎样聚合 nonce、怎样出部分签、怎样聚成 BIP-340 签。
