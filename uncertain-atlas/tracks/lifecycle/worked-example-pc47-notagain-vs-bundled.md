# 例：看见第一次付款不是已经不必再发通知；看见已经收过不是已经可以免通知；看见 352 不必通知不是已经是本页

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki)（Deployed, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-47 first-pay not already skip-notify / not already recovered / not already settled 正式三事（273 余量）/ not 1225 pc47-notagain interchangeable / not 273 payment-code-vs-notification bundled interchangeable」，不是付款码 bundled（273），也不是静默付款不必再通知（260），也不是签过就已经控制资金（258）。不要另写怎样做 ECDH 或怎样拼通知。

## 官方三件事

1. **看见第一次付款 / 看见已经收过 这份指示 is not already 已经不必再发通知 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1225 pc47-notagain interchangeable / 1223 pc47-notdep interchangeable / 273 paycode item 1 code-not-dep interchangeable，也不是已经 BIP-47 first-pay not already skip-notify / not already recovered / not already settled 正式三事 bundled（273 item 3 余量） interchangeable / 273 paycode item 3 interchangeable。**  
   官方写：即使鲍勃以前收过爱丽丝的钱，他第一次往回打仍必须先发通知。看见第一次付款，不是已经不必再发通知。

2. **看见已经收过 / 看见从种子找回 这份指示 is not already 已经可以免通知 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1225 pc47-notagain interchangeable / 273 paycode item 2 note-not-spend interchangeable / 1224 pc47-notnote interchangeable，也不是已经静默付款不必再通知 interchangeable / 260 silent interchangeable。**  
   官方写：从种子找回之后，必须当成新钱包再发通知；发出去的通知名单会丢。看见已经收过，不是已经可以免通知。

3. **看见 352 不必通知 / 看见第一次付款 / 这份指示 is not already 已经是本页 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1225 pc47-notagain interchangeable / 1223 pc47-notdep interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed interchangeable。**  
   官方写：这和 352 官方写成「不必再发链上通知」不是同一句。看见静默付款不必通知，不是已经是本页，也不是已经交差。

用途号、编码版本字节、共享秘密公式、通知脚本拼法、测试向量是规范里的取值或做法，本页不抄。不要另写怎样做 ECDH 或怎样拼通知。

## 官方为什么这样拆

- **第一次付款 不是已经不必再发通知：** 官方把第一次往回打仍必须先发通知写成硬规则。
- **已经收过 不是已经可以免通知：** 官方把种子找回后必须当成新钱包再通知写成另一句。
- **352 不必通知 不是已经是本页：** 官方把本页通知和 352 那种不必通知写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 免通知 | 不是已经不必再发通知 | 不是已经不必通知（260） |
| 找回 | 不是已经可以免通知 | 不是已经控制资金（258） |
| 本页 | 不是已经是本页 | 不是已经是存款地址（1223） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-47 first-pay not already skip-notify / not already recovered / not already settled 正式三事（273 余量），必须分开是不是已经不必再发通知、是不是已经可以免通知、是不是已经是本页。可以跳过「看见公开码就已经付到链上」。不要另写怎样做 ECDH 或怎样拼通知。273 payment code vs notification bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 用途号、编码版本字节、测试向量、例地址。
- 怎样做 ECDH、怎样盲化付款码、怎样拼通知脚本、怎样扫通知地址。
