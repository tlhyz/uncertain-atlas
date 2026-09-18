# 例：看见付款码不是已经是存款地址；看见公开身份不是已经付过；看见码不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki)（Deployed, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-47 payment-code not already deposit / not already paid / not already settled 正式三事（273 余量）/ not 1223 pc47-notdep interchangeable / not 273 payment-code-vs-notification bundled interchangeable」，不是付款码 bundled（273），也不是静默付款地址就已经有输出（260），也不是付款 URI 就已经授权（255）。不要另写怎样做 ECDH 或怎样拼通知。

## 官方三件事

1. **看见付款码 / 看见一把扩展公钥加上元数据 这份指示 is not already 已经是存款地址 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1223 pc47-notdep interchangeable / 1224 pc47-notnote interchangeable / 273 paycode item 2 note-not-spend interchangeable，也不是已经 BIP-47 payment-code not already deposit / not already paid / not already settled 正式三事 bundled（273 item 1 余量） interchangeable / 273 paycode item 1 interchangeable。**  
   官方写：付款码是一把扩展公钥加上元数据，和某个身份或账户绑在一起。存款地址是通知之后才派生的一次性付款脚本哈希地址。看见付款码，不是已经有一笔链上输出，也不是已经是存款地址。

2. **看见公开身份 / 看见付款码 / 这份指示 is not already 已经付过 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1223 pc47-notdep interchangeable / 273 paycode item 3 first-not-skip interchangeable / 1225 pc47-notagain interchangeable，也不是已经静默付款地址就已经有输出 interchangeable / 260 silent interchangeable。**  
   官方写：看见公开身份，不是已经付过。

3. **看见码 / 看见付款码 / 这份指示 is not already 已经交差 interchangeable，也不是已经付款码 bundled（273） interchangeable / 1223 pc47-notdep interchangeable / 1224 pc47-notnote interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方把「可复用付款码」和「已经付到链上」写成两件事。看见码，不是已经交差。

用途号、编码版本字节、共享秘密公式、通知脚本拼法、测试向量是规范里的取值或做法，本页不抄。不要另写怎样做 ECDH 或怎样拼通知。

## 官方为什么这样拆

- **付款码 不是已经是存款地址：** 官方把存款地址写成通知之后才派生。
- **公开身份 不是已经付过：** 官方把公开身份和已经付过写成两件。
- **码 不是已经交差：** 官方把看见公开码和已经付到链上写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 存款地址 | 不是已经是存款地址 | 不是已经有输出（260） |
| 付过 | 不是已经付过 | 不是已经授权（255） |
| 交差 | 不是已经交差 | 不是已经能花（1224） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-47 payment-code not already deposit / not already paid / not already settled 正式三事（273 余量），必须分开是不是已经是存款地址、是不是已经付过、是不是已经交差。可以跳过「看见公开码就已经付到链上」。不要另写怎样做 ECDH 或怎样拼通知。273 payment code vs notification bundled unbundling 在本页 item 1 启动；续 [`worked-example-pc47-notnote-vs-bundled.md`](worked-example-pc47-notnote-vs-bundled.md)（不变量 1224 item 2）。

## 本页不抄

- 用途号、编码版本字节、测试向量、例地址。
- 怎样做 ECDH、怎样盲化付款码、怎样拼通知脚本、怎样扫通知地址。
