# 例：看见旧 PSBT 栏不是已经能装 MuSig2；看见 371 补了 Taproot 栏不是已经是本页；看见 174 那套栏不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-373 old-psbt-fields not already can-hold-musig / not already can-finish-rounds / not already settled 正式三事（284 余量）/ not 1172 mpsbt373-notold interchangeable / not 284 musig-psbt-vs-tap bundled interchangeable」，不是 MuSig2 工作包栏 bundled（284），也不是旧 PSBT 栏就已经能装 Taproot（1157），也不是聚合钥就已经是扩展公钥（1169）。不要另写怎样造 nonce 或部分签。

## 官方三件事

1. **看见旧 PSBT 栏 / 看见 371 那套 Taproot 栏 这份栏 is not already 已经能装 MuSig2 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1172 mpsbt373-notold interchangeable / 1173 mpsbt373-notout interchangeable / 284 mpsbt item 2 agg-not-out interchangeable，也不是已经 BIP-373 old-psbt-fields not already can-hold-musig / not already can-finish-rounds / not already settled 正式三事 bundled（284 item 1 余量） interchangeable / 284 mpsbt item 1 interchangeable。**  
   官方写：现有工作包栏没法支持 MuSig2，因为它引入了新概念，还要多几轮通信。看见 174 那套栏，不是已经能装。

2. **看见 371 补了 Taproot 栏 / 看见旧 PSBT 栏 / 这份栏 is not already 已经能走完多轮 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1172 mpsbt373-notold interchangeable / 284 mpsbt item 3 part-not-partial interchangeable / 1174 mpsbt373-notpartial interchangeable，也不是已经旧 PSBT 栏就已经能装 Taproot interchangeable / 1157 tap371-notold interchangeable。**  
   官方写：必须另定新栏，才能装出合法 MuSig2 签所需的信息。看见 371 补了 Taproot 栏，不是已经是本页，也不是已经能走完多轮。

3. **看见 174 那套栏 / 看见旧 PSBT 栏 / 这份栏 is not already 已经交差 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1172 mpsbt373-notold interchangeable / 1173 mpsbt373-notout interchangeable，也不是已经聚合钥就已经是扩展公钥 interchangeable / 1169 musig328-notxpub interchangeable。**  
   官方把新概念和多轮通信写成现有栏装不下。看见 174 那套栏，不是已经交差。

类型号、字节宽度、测试向量、例钥、算法名单是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **旧 PSBT 栏 不是已经能装 MuSig2：** 官方把现有栏写成装不下新概念和多轮。
- **371 Taproot 栏 不是已经能走完多轮：** 官方把另定新栏写成才能装 MuSig2。
- **174 那套栏 不是已经交差：** 官方把装不下写成独立一句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 旧栏 | 不是已经能装 MuSig2 | 不是已经能装 Taproot（1157） |
| 多轮 | 不是已经能走完多轮 | 不是已经有部分签（1174） |
| 交差 | 不是已经交差 | 不是已经是扩展公钥（1169） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-373 old-psbt-fields not already can-hold-musig / not already can-finish-rounds / not already settled 正式三事（284 余量），必须分开是不是已经能装 MuSig2、是不是已经能走完多轮、是不是已经交差。可以跳过「看见 Taproot 工作包栏就已经能签 MuSig2」。不要另写怎样造 nonce 或部分签。284 musig PSBT vs tap bundled unbundling 在本页 item 1 启动；续 [`worked-example-mpsbt373-notout-vs-bundled.md`](worked-example-mpsbt373-notout-vs-bundled.md)（不变量 1173 item 2）。

## 本页不抄

- 类型号、字节宽度、测试向量、例钥、算法名单。
- 怎样造 nonce、怎样聚合 nonce、怎样出部分签、怎样聚成 BIP-340 签。
