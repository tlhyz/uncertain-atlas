# 例：看见旧的 P2PKH 签消息习惯不是已经互操作；看见本页这种格式不是所有旧校验器已经肯收；看见覆盖了旧地址不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-137](https://github.com/bitcoin/bips/blob/master/bip-0137.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.2](../../courses/level-01-crypto/L01-M02-signatures.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-137 old-habit not already interoperable / not already old-verifiers / not already settled 正式三事（294 余量）/ not 1201 lsig137-nothabit interchangeable / not 294 legacy-sign-vs-322 bundled interchangeable」，不是旧式签消息 bundled（294），也不是签过就已经控制资金（258），也不是储备证明就已经能花（293）。不要另写怎样从头字节还原公钥。

## 官方三件事

1. **看见旧的 P2PKH 签消息习惯 / 看见本页这种格式 这份签 is not already 已经互操作 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1201 lsig137-nothabit interchangeable / 1199 lsig137-not322 interchangeable / 294 lsig item 1 sign-not-322 interchangeable，也不是已经 BIP-137 old-habit not already interoperable / not already old-verifiers / not already settled 正式三事 bundled（294 item 3 余量） interchangeable / 294 lsig item 3 interchangeable。**  
   官方写：用普通付给公钥哈希地址签消息，当时没有 BIP，可是做法大家大致懂；隔离见证进来之后（既有脚本哈希套法，也有原生编码），就分不清了。看见旧习惯还能用，不是已经是本页，也不是已经互操作。

2. **看见本页这种格式 / 看见旧的 P2PKH 签消息习惯 / 这份签 is not already 已经能被所有旧校验器收下 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1201 lsig137-nothabit interchangeable / 294 lsig item 2 header-not-addr interchangeable / 1200 lsig137-notaddr interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed-is-control interchangeable。**  
   官方写：本页还覆盖旧的付给公钥哈希，所以能往后兼容；可是有的软件会检查头字节落在哪一段，会把较新的隔离见证头当成错误。看见本页这种格式，不是所有旧校验器已经肯收。

3. **看见覆盖了旧地址 / 看见旧的 P2PKH 签消息习惯 / 这份签 is not already 已经交差 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1201 lsig137-nothabit interchangeable / 1199 lsig137-not322 interchangeable，也不是已经储备证明就已经能花 interchangeable / 293 por interchangeable。**  
   官方把旧习惯「大致懂」和隔离见证之后必须另定标准、以及旧校验器会拒新头写成不同对象。看见覆盖了旧地址，不是隔离见证那种头已经到处能过，也不是已经交差。

头字节取值、椭圆曲线背景、示例代码、怎样还原公钥是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **旧的 P2PKH 签消息习惯 不是已经互操作：** 官方把当时大致懂写成不是已经是本页。
- **本页这种格式 不是所有旧校验器已经肯收：** 官方把检查头字节落在哪一段写成会拒新头。
- **覆盖了旧地址 不是已经交差：** 官方把覆盖旧地址写成不是隔离见证头已经到处能过。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 互操作 | 不是已经互操作 | 不是已经控制资金（258） |
| 旧校验器 | 不是所有旧校验器已经肯收 | 不是已经能花（293） |
| 交差 | 不是已经交差 | 不是已经是 322（1199） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-137 old-habit not already interoperable / not already old-verifiers / not already settled 正式三事（294 余量），必须分开是不是已经互操作、是不是所有旧校验器已经肯收、是不是已经交差。可以跳过「看见用私钥签过就已经是 322」。不要另写怎样从头字节还原公钥。294 legacy sign vs 322 bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 头字节取值、椭圆曲线背景、示例代码、怎样还原公钥。
- 怎样签、怎样验、怎样从 recId 还原。
