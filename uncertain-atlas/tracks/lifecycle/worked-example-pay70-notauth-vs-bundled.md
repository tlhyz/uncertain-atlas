# 例：看见付款请求不是已经授权；看见商家常用名不是已经是链上地址；看见身份类型写成没有不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-70 payment-request not already authorized / not already that-address / not already settled 正式三事（295 余量）/ not 1202 pay70-notauth interchangeable / not 295 request-vs-ack bundled interchangeable」，不是付款协议 bundled（295），也不是付款 URI 就已经授权（255），也不是远程取单就已经验证（55）。不要另写怎样拼付款请求或怎样验证书链。不要另写 BIP-71 / BIP-72。

## 官方三件事

1. **看见付款请求 / 看见商家名字 这份协议 is not already 已经授权 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1202 pay70-notauth interchangeable / 1203 pay70-notack interchangeable / 295 pay item 2 msg-not-ack interchangeable，也不是已经 BIP-70 payment-request not already authorized / not already that-address / not already settled 正式三事 bundled（295 item 1 余量） interchangeable / 295 pay item 1 interchangeable。**  
   官方写：本页在旧的「复制地址或点一条付款链接」之上，另开一套商家和顾客之间的消息。钱包收到付款请求之后，必须先核商家身份和签名（若身份类型不是「没有」），必须核自己的时间还没过期，然后把商家身份拿给顾客看，问要不要提交付款。看见付款请求，不是已经授权。

2. **看见商家常用名 / 看见付款请求 / 这份协议 is not already 已经是那条地址 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1202 pay70-notauth interchangeable / 295 pay item 3 ack-not-final interchangeable / 1204 pay70-notfinal interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方写：看见商家常用名，不是已经是链上地址。看见身份类型写成「没有」，不是已经核过商家。

3. **看见身份类型写成没有 / 看见付款请求 / 这份协议 is not already 已经交差 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1202 pay70-notauth interchangeable / 1203 pay70-notack interchangeable，也不是已经远程取单就已经验证 interchangeable / 55 remote interchangeable。**  
   官方把核身份、核过期、再问顾客写成三步，不是看见请求就已经付。看见身份类型写成没有，不是已经交差。

消息编码、传输头、证书链拼法、体积上限是规范里的取值或做法，本页不抄。不要另写 BIP-71 / BIP-72。

## 官方为什么这样拆

- **付款请求 不是已经授权：** 官方把核身份、核过期、再问顾客写成三步。
- **商家常用名 不是已经是链上地址：** 官方把商家名字写成不是已经是地址。
- **身份类型写成没有 不是已经交差：** 官方把身份类型写成没有当成还没核过商家。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 授权 | 不是已经授权 | 不是已经授权（255） |
| 地址 | 不是已经是那条地址 | 不是已经验证（55） |
| 交差 | 不是已经交差 | 不是已经是回执（1203） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-70 payment-request not already authorized / not already that-address / not already settled 正式三事（295 余量），必须分开是不是已经授权、是不是已经是那条地址、是不是已经交差。可以跳过「看见商家请求就已经最终」。不要另写怎样拼付款请求或怎样验证书链。295 request vs ack bundled unbundling 在本页 item 1 启动；续 [`worked-example-pay70-notack-vs-bundled.md`](worked-example-pay70-notack-vs-bundled.md)（不变量 1203 item 2）。

## 本页不抄

- 消息编码、传输头、证书链拼法、体积上限、语言例句。
- 怎样拼付款请求、怎样验证书链、怎样构造回执。
