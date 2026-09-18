# 例：看见参与者钥不是已经有部分签；看见 nonce 不是已经有部分签；看见部分签不是已经是 371 那种 Taproot 签

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-373 participant-key not already have-partial / not already bip340-sig / not already settled 正式三事（284 余量）/ not 1174 mpsbt373-notpartial interchangeable / not 284 musig-psbt-vs-tap bundled interchangeable」，不是 MuSig2 工作包栏 bundled（284），也不是看见包就已经能广播（179），也不是旧栏就已经能装 Taproot（1157）。不要另写怎样造 nonce 或部分签。

## 官方三件事

1. **看见参与者钥 / 看见 nonce 栏 这份栏 is not already 已经有部分签 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1174 mpsbt373-notpartial interchangeable / 1172 mpsbt373-notold interchangeable / 284 mpsbt item 1 old-not-hold interchangeable，也不是已经 BIP-373 participant-key not already have-partial / not already bip340-sig / not already settled 正式三事 bundled（284 item 3 余量） interchangeable / 284 mpsbt item 3 interchangeable。**  
   官方写：没有 nonce 栏才去补 nonce；nonce 齐了才出部分签。看见参与者名单，不是已经有 nonce。看见 nonce，不是已经有部分签。

2. **看见部分签 / 看见参与者钥 / 这份栏 is not already 已经是 371 那种 Taproot 签 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1174 mpsbt373-notpartial interchangeable / 284 mpsbt item 2 agg-not-out interchangeable / 1173 mpsbt373-notout interchangeable，也不是已经旧栏就已经能装 Taproot interchangeable / 1157 tap371-notold interchangeable。**  
   官方写：部分签齐了，最后一位才可能聚成能放进 Taproot 签栏的 BIP-340 签。看见部分签，不是已经是 371 那种 Taproot 签。

3. **看见 nonce 栏 / 看见参与者钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经 MuSig2 工作包栏 bundled（284） interchangeable / 1174 mpsbt373-notpartial interchangeable / 1172 mpsbt373-notold interchangeable，也不是已经看见包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方把名单、nonce、部分签、最后那张 BIP-340 签写成四步。看见 nonce 栏，不是已经交差。

类型号、字节宽度、测试向量、例钥、算法名单是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **参与者钥 不是已经有部分签：** 官方把名单、nonce、部分签写成几步。
- **部分签 不是已经是 371 那种 Taproot 签：** 官方把最后一位才可能聚成 BIP-340 签写成另一步。
- **nonce 栏 不是已经交差：** 官方把四步写成四句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 部分签 | 不是已经有部分签 | 不是已经能广播（179） |
| BIP-340 签 | 不是已经是 371 那种签 | 不是已经能装 Taproot（1157） |
| 交差 | 不是已经交差 | 不是已经是输出钥（1173） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-373 participant-key not already have-partial / not already bip340-sig / not already settled 正式三事（284 余量），必须分开是不是已经有部分签、是不是已经是 371 那种 Taproot 签、是不是已经交差。可以跳过「看见 Taproot 工作包栏就已经能签 MuSig2」。不要另写怎样造 nonce 或部分签。284 musig PSBT vs tap bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 类型号、字节宽度、测试向量、例钥、算法名单。
- 怎样造 nonce、怎样聚合 nonce、怎样出部分签、怎样聚成 BIP-340 签。
