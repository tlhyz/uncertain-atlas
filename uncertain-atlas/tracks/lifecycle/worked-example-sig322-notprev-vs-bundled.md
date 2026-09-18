# 例：看见签过的消息不是已经证明发过上一笔；看见本页覆盖发票地址将来控制不是已经付过；看见签过不是已经广播过上一笔

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.2](../../courses/level-01-crypto/L01-M02-signatures.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-322 invoice-control not already previous-tx / not already paid / not already settled 正式三事（258 余量）/ not 1215 sig322-notprev interchangeable / not 258 signed-message-vs-control bundled interchangeable」，不是签消息 bundled（258），也不是部分签名包就已经能广播（179），也不是地址串就已经有输出（174）。不要另写怎样拼虚拟交易。

## 官方三件事

1. **看见签过的消息 / 看见本页覆盖发票地址将来控制 这份指示 is not already 已经证明发过上一笔 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1215 sig322-notprev interchangeable / 1214 sig322-notctrl interchangeable / 258 signed item 1 signed-not-ctrl interchangeable，也不是已经 BIP-322 invoice-control not already previous-tx / not already paid / not already settled 正式三事 bundled（258 item 2 余量） interchangeable / 258 signed item 2 interchangeable。**  
   官方写：本页只处理签名人表明自己将能控制打到发票地址的资金。用本页证明签名人发过上一笔交易，做不到。看见签过的消息，不是已经证明发过上一笔。

2. **看见本页覆盖发票地址将来控制 / 看见签过的消息 / 这份指示 is not already 已经付过 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1215 sig322-notprev interchangeable / 258 signed item 3 list-not-full interchangeable / 1216 sig322-notfund interchangeable，也不是已经部分签名包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方写：看见签过的消息，不是已经证明付过款。本页只覆盖打到发票地址的将来控制。

3. **看见签过 / 看见本页覆盖发票地址将来控制 / 这份指示 is not already 已经广播过上一笔 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1215 sig322-notprev interchangeable / 1214 sig322-notctrl interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见签过，不是已经证明广播过上一笔，也不是已经交差。

编码前缀、虚拟交易怎么拼、测试向量是规范里的取值，本页不抄。不要另写怎样拼虚拟交易。

## 官方为什么这样拆

- **签过的消息 不是已经证明发过上一笔：** 官方明确写证明发过上一笔做不到。
- **发票地址将来控制 不是已经付过：** 官方只覆盖打到发票地址的将来控制。
- **签过 不是已经广播过上一笔：** 官方把签过和广播上一笔写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 上一笔 | 不是已经证明发过上一笔 | 不是已经能广播（179） |
| 付过 | 不是已经付过 | 不是已经有输出（174） |
| 广播 | 不是已经广播过上一笔 | 不是已经控制资金（1214） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-322 invoice-control not already previous-tx / not already paid / not already settled 正式三事（258 余量），必须分开是不是已经证明发过上一笔、是不是已经付过、是不是已经广播过上一笔。可以跳过「看见签过就已经能花」。不要另写怎样拼虚拟交易。258 signed message vs control bundled unbundling 在本页 item 2 续；续 [`worked-example-sig322-notfund-vs-bundled.md`](worked-example-sig322-notfund-vs-bundled.md)（不变量 1216 item 3）。

## 本页不抄

- 编码前缀、标签哈希、虚拟交易字段、PSBT 类型号、测试向量。
- 怎样拼能过验证器的签消息、怎样用资金证明假装齐或未花。
