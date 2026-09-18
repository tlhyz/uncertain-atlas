# 例：看见资金证明清单不是已经齐；看见清单不是已经没花；看见被证明过的清单不是已经是一笔付款

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.2](../../courses/level-01-crypto/L01-M02-signatures.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-322 proof-list not already complete / not already unspent / not already settled 正式三事（258 余量）/ not 1216 sig322-notfund interchangeable / not 258 signed-message-vs-control bundled interchangeable」，不是签消息 bundled（258），也不是付款 URI 就已经授权（255），也不是扩展公钥就已经能花（182）。不要另写怎样拼虚拟交易。

## 官方三件事

1. **看见资金证明清单 / 看见签名人自选一组 UTXO 这份指示 is not already 已经齐 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1216 sig322-notfund interchangeable / 1214 sig322-notctrl interchangeable / 258 signed item 1 signed-not-ctrl interchangeable，也不是已经 BIP-322 proof-list not already complete / not already unspent / not already settled 正式三事 bundled（258 item 3 余量） interchangeable / 258 signed item 3 interchangeable。**  
   官方写：资金证明变体让签名人自选一组 UTXO 来展示控制。这份清单不声称齐（不是「这个地址上的 UTXO 就这些」）。一份被证明过的清单，永远不能证明这个地址没有更多 UTXO。看见资金证明清单，不是已经齐。

2. **看见清单 / 看见资金证明清单 / 这份指示 is not already 已经没花 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1216 sig322-notfund interchangeable / 258 signed item 2 invoice-not-prev interchangeable / 1215 sig322-notprev interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方写：清单也不声称还没花（验证者必须去问链）。离线验证者只能核密码学是否成立，不能核链上状态。看见清单，不是已经没花。

3. **看见被证明过的清单 / 看见资金证明清单 / 这份指示 is not already 已经是一笔付款 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1216 sig322-notfund interchangeable / 1214 sig322-notctrl interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方写：看见资金证明清单，不是已经是一笔付款，也不是已经交差。

编码前缀、虚拟交易怎么拼、测试向量是规范里的取值，本页不抄。不要另写怎样拼虚拟交易。

## 官方为什么这样拆

- **资金证明清单 不是已经齐：** 官方把齐交给链，不交给这份清单。
- **清单 不是已经没花：** 官方把未花交给问链。
- **被证明过的清单 不是已经是一笔付款：** 官方把清单和付款写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 齐 | 不是已经齐 | 不是已经授权（255） |
| 没花 | 不是已经没花 | 不是已经能花（182） |
| 付款 | 不是已经是一笔付款 | 不是已经控制资金（1214） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-322 proof-list not already complete / not already unspent / not already settled 正式三事（258 余量），必须分开是不是已经齐、是不是已经没花、是不是已经是一笔付款。可以跳过「看见签过就已经能花」。不要另写怎样拼虚拟交易。258 signed message vs control bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 编码前缀、标签哈希、虚拟交易字段、PSBT 类型号、测试向量。
- 怎样拼能过验证器的签消息、怎样用资金证明假装齐或未花。
