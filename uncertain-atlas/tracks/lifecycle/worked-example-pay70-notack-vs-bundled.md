# 例：看见付款报文不是已经是回执；看见里面有签过的交易不是商家已经收下；看见送到了付款网址不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事（295 余量）/ not 1203 pay70-notack interchangeable / not 295 request-vs-ack bundled interchangeable」，不是付款协议 bundled（295），也不是 payjoin 提案（290），也不是地址串就已经有输出（174）。不要另写怎样拼付款请求或怎样验证书链。不要另写 BIP-71 / BIP-72。

## 官方三件事

1. **看见付款报文 / 看见里面有签过的交易 这份协议 is not already 已经是回执 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1203 pay70-notack interchangeable / 1202 pay70-notauth interchangeable / 295 pay item 1 req-not-auth interchangeable，也不是已经 BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事 bundled（295 item 2 余量） interchangeable / 295 pay item 2 interchangeable。**  
   官方写：顾客授权之后，钱包造出并签好能付清请求输出的交易，再广播到对等网。若请求里写了付款网址，还要把付款报文送到那里。看见付款报文，不是已经是回执。

2. **看见里面有签过的交易 / 看见付款报文 / 这份协议 is not already 已经商家收下 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1203 pay70-notack interchangeable / 295 pay item 3 ack-not-final interchangeable / 1204 pay70-notfinal interchangeable，也不是已经 payjoin 提案 interchangeable / 290 pj interchangeable。**  
   官方写：商家服务器收到付款报文，必须自己判断这些交易是否满足付款条件；只有满足，才应当再广播。同一份付款请求若收到多份相同的付款报文，必须每份都回。看见里面有签过的交易，不是商家已经收下。

3. **看见送到了付款网址 / 看见付款报文 / 这份协议 is not already 已经交差 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1203 pay70-notack interchangeable / 1202 pay70-notauth interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方把顾客广播、送到付款网址、商家自己判断是否满足写成不同对象。看见送到了付款网址，不是已经有确认，也不是已经交差。

消息编码、传输头、证书链拼法、体积上限是规范里的取值或做法，本页不抄。不要另写 BIP-71 / BIP-72。

## 官方为什么这样拆

- **付款报文 不是已经是回执：** 官方把送到付款网址写成不是已经是回执。
- **里面有签过的交易 不是商家已经收下：** 官方把商家自己判断是否满足写成另一步。
- **送到了付款网址 不是已经交差：** 官方把送到网址写成不是已经有确认。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回执 | 不是已经是回执 | 不是已经是提案（290） |
| 收下 | 不是商家已经收下 | 不是已经有输出（174） |
| 交差 | 不是已经交差 | 不是已经授权（1202） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事（295 余量），必须分开是不是已经是回执、是不是商家已经收下、是不是已经交差。可以跳过「看见商家请求就已经最终」。不要另写怎样拼付款请求或怎样验证书链。295 request vs ack bundled unbundling 在本页 item 2 续；续 [`worked-example-pay70-notfinal-vs-bundled.md`](worked-example-pay70-notfinal-vs-bundled.md)（不变量 1204 item 3）。

## 本页不抄

- 消息编码、传输头、证书链拼法、体积上限、语言例句。
- 怎样拼付款请求、怎样验证书链、怎样构造回执。
