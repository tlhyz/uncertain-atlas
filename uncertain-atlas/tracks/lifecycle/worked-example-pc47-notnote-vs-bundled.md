# 例：看见通知交易不是已经是付款；看见通知地址进了币不是已经付到存款地址；看见通知输出不是已经能花

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki)（Deployed, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-47 notification not already payment / not already spendable / not already settled 正式三事（273 余量）/ not 1224 pc47-notnote interchangeable / not 273 payment-code-vs-notification bundled interchangeable」，不是付款码 bundled（273），也不是地址串就已经有输出（174），也不是扩展公钥就已经能花（182）。不要另写怎样做 ECDH 或怎样拼通知。

## 官方三件事

1. **看见通知交易 / 看见通知地址上有输出 这份指示 is not already 已经是付款 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1224 pc47-notnote interchangeable / 1223 pc47-notdep interchangeable / 273 paycode item 1 code-not-dep interchangeable，也不是已经 BIP-47 notification not already payment / not already spendable / not already settled 正式三事 bundled（273 item 2 余量） interchangeable / 273 paycode item 2 interchangeable。**  
   官方写：爱丽丝第一次给鲍勃付款之前，必须先用通知交易把她的付款码告诉鲍勃。通知之后才可能继续付（最多付很多笔），之后不必再发通知。看见通知交易，不是已经是付款。

2. **看见通知地址进了币 / 看见通知交易 / 这份指示 is not already 已经付到存款地址 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1224 pc47-notnote interchangeable / 273 paycode item 3 first-not-skip interchangeable / 1225 pc47-notagain interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见通知地址进了币，不是已经付到存款地址。通知地址上收到的输出不得显示为可花余额，也不得拿去参与本页那种共享秘密计算。

3. **看见通知输出 / 看见通知交易 / 这份指示 is not already 已经能花 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1224 pc47-notnote interchangeable / 1223 pc47-notdep interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方写：看见通知输出，不是已经能花，也不是已经交差。

用途号、编码版本字节、共享秘密公式、通知脚本拼法、测试向量是规范里的取值或做法，本页不抄。不要另写怎样做 ECDH 或怎样拼通知。

## 官方为什么这样拆

- **通知交易 不是已经是付款：** 官方把通知写成第一次付款之前必须先发。
- **通知地址进了币 不是已经付到存款地址：** 官方把通知输出写成不得当可花余额。
- **通知输出 不是已经能花：** 官方把通知输出和能花写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 付款 | 不是已经是付款 | 不是已经有输出（174） |
| 存款地址 | 不是已经付到存款地址 | 不是已经能花（182） |
| 能花 | 不是已经能花 | 不是已经是存款地址（1223） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-47 notification not already payment / not already spendable / not already settled 正式三事（273 余量），必须分开是不是已经是付款、是不是已经付到存款地址、是不是已经能花。可以跳过「看见公开码就已经付到链上」。不要另写怎样做 ECDH 或怎样拼通知。273 payment code vs notification bundled unbundling 在本页 item 2 续；续 [`worked-example-pc47-notagain-vs-bundled.md`](worked-example-pc47-notagain-vs-bundled.md)（不变量 1225 item 3）。

## 本页不抄

- 用途号、编码版本字节、测试向量、例地址。
- 怎样做 ECDH、怎样盲化付款码、怎样拼通知脚本、怎样扫通知地址。
