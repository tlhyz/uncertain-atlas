# 例：看见本页这种签消息不是已经是 322；看见验过本页这种签不是已经控制资金；看见为了兼容还在用不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-137](https://github.com/bitcoin/bips/blob/master/bip-0137.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.2](../../courses/level-01-crypto/L01-M02-signatures.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-137 this-sign not already 322 / not already 258-control / not already settled 正式三事（294 余量）/ not 1199 lsig137-not322 interchangeable / not 294 legacy-sign-vs-322 bundled interchangeable」，不是旧式签消息 bundled（294），也不是签过就已经控制资金（258），也不是储备证明就已经能花（293）。不要另写怎样从头字节还原公钥。

## 官方三件事

1. **看见本页这种签消息 / 看见用私钥签过一条消息 这份签 is not already 已经是 322 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1199 lsig137-not322 interchangeable / 1200 lsig137-notaddr interchangeable / 294 lsig item 2 header-not-addr interchangeable，也不是已经 BIP-137 this-sign not already 322 / not already 258-control / not already settled 正式三事 bundled（294 item 1 余量） interchangeable / 294 lsig item 1 interchangeable。**  
   官方写：后来另有一套签消息格式，好处比本页多；本页留下来，是为了跟当时已经在场上的实现往后兼容。官方点名去看 322。看见本页这种签，不是已经走了 322。

2. **看见验过本页这种签 / 看见本页这种签消息 / 这份签 is not already 已经控制资金 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1199 lsig137-not322 interchangeable / 294 lsig item 3 habit-not-interop interchangeable / 1201 lsig137-nothabit interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed-is-control interchangeable。**  
   官方写：看见验过本页这种签，不是已经证明能控制资金。看见为了兼容还在用本页，不是 322 已经没必要。

3. **看见为了兼容还在用本页 / 看见本页这种签消息 / 这份签 is not already 已经交差 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1199 lsig137-not322 interchangeable / 1200 lsig137-notaddr interchangeable，也不是已经储备证明就已经能花 interchangeable / 293 por interchangeable。**  
   官方自己把本页写成兼容旧实现，把后继格式写成另一页。看见为了兼容还在用，不是已经交差。

头字节取值、椭圆曲线背景、示例代码、怎样还原公钥是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **本页这种签消息 不是已经是 322：** 官方把后继格式点名写成另一页。
- **验过本页这种签 不是已经控制资金：** 官方把验过本页这种签写成不是 258。
- **为了兼容还在用 不是已经交差：** 官方把留下来兼容写成不是 322 已经没必要。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 322 | 不是已经是 322 | 不是已经控制资金（258） |
| 控制 | 不是已经控制资金 | 不是已经能花（293） |
| 交差 | 不是已经交差 | 不是已经有地址（1200） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-137 this-sign not already 322 / not already 258-control / not already settled 正式三事（294 余量），必须分开是不是已经是 322、是不是已经控制资金、是不是已经交差。可以跳过「看见用私钥签过就已经是 322」。不要另写怎样从头字节还原公钥。294 legacy sign vs 322 bundled unbundling 在本页 item 1 启动；续 [`worked-example-lsig137-notaddr-vs-bundled.md`](worked-example-lsig137-notaddr-vs-bundled.md)（不变量 1200 item 2）。

## 本页不抄

- 头字节取值、椭圆曲线背景、示例代码、怎样还原公钥。
- 怎样签、怎样验、怎样从 recId 还原。
