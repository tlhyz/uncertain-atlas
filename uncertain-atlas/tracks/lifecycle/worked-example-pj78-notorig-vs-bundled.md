# 例：看见原始包不是已经是 Payjoin 提案；看见提案不是已经是 Payjoin 交易；看见一份能广播的原始包不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki)（Deployed, Applications, Specification）。取代 BIP-79。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-78 original not already proposal / not already payjoin-tx / not already settled 正式三事（290 余量）/ not 1185 pj78-notorig interchangeable / not 290 payjoin-vs-original bundled interchangeable」，不是 payjoin 付款 bundled（290），也不是部分签名包就已经能广播（179），也不是替换信号就已经换掉（166）。不要另写怎样构造提案或怎样加费。

## 官方三件事

1. **看见原始包 / 看见一份能广播的原始包 这份付款 is not already 已经是 Payjoin 提案 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1185 pj78-notorig interchangeable / 1184 pj78-noturi interchangeable / 290 pj item 1 uri-not-pay interchangeable，也不是已经 BIP-78 original not already proposal / not already payjoin-tx / not already settled 正式三事 bundled（290 item 2 余量） interchangeable / 290 pj item 2 interchangeable。**  
   官方给了三个名字。原始包：已经签过、已经定稿，必须能广播。Payjoin 提案：收款方自己签过的输入输出，加上发送方那些；必须用上原始包的全部输入；只定稿收款方新加的输入。看见一份能广播的原始包，不是已经是 payjoin。

2. **看见提案 / 看见原始包 / 这份付款 is not already 已经是 Payjoin 交易 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1185 pj78-notorig interchangeable / 290 pj item 3 add-not-other interchangeable / 1186 pj78-notmerge interchangeable，也不是已经部分签名包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方写：Payjoin 交易是发送方核过提案、重签自己的输入、再广播出去。看见提案，不是已经广播。

3. **看见一份能广播的原始包 / 看见原始包 / 这份付款 is not already 已经交差 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1185 pj78-notorig interchangeable / 1184 pj78-noturi interchangeable，也不是已经替换信号就已经换掉 interchangeable / 166 replace interchangeable。**  
   官方把原始包、提案、交易写成三道门。看见一份能广播的原始包，不是已经交差。

HTTP 配方、加费公式、发送方/收款方核对清单、怎样构造或下毒、混输入宽限期、版本不支持载荷是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **原始包 不是已经是 Payjoin 提案：** 官方把能广播的原始包和提案写成两件。
- **提案 不是已经是 Payjoin 交易：** 官方把核过再重签写成才是交易。
- **一份能广播的原始包 不是已经交差：** 官方把三道门写成三句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 提案 | 不是已经是提案 | 不是已经能广播（179） |
| 交易 | 不是已经是 Payjoin 交易 | 不是已经换掉（166） |
| 交差 | 不是已经交差 | 不是已经是付款（1184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-78 original not already proposal / not already payjoin-tx / not already settled 正式三事（290 余量），必须分开是不是已经是提案、是不是已经是 Payjoin 交易、是不是已经交差。可以跳过「看见 pj= 就已经是 payjoin 付款」。不要另写怎样构造提案或怎样加费。290 payjoin vs original bundled unbundling 在本页 item 2 续；续 [`worked-example-pj78-notmerge-vs-bundled.md`](worked-example-pj78-notmerge-vs-bundled.md)（不变量 1186 item 3）。

## 本页不抄

- HTTP POST / base64 / Content-Type / Access-Control-Allow-Origin、错误 JSON、加费公式、核对清单。
- 怎样构造提案、怎样加费、怎样下毒启发式、怎样混输入、怎样回版本不支持。
