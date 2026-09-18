# 例：看见回执不是已经最终；看见已收到那句备忘不是已经确认；看见退款输出不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-70 ack not already final / not already confirmed / not already refunded 正式三事（295 余量）/ not 1204 pay70-notfinal interchangeable / not 295 request-vs-ack bundled interchangeable」，不是付款协议 bundled（295），也不是付款 URI 就已经授权（255），也不是旧式签就已经是 322（294）。不要另写怎样拼付款请求或怎样验证书链。不要另写 BIP-71 / BIP-72。

## 官方三件事

1. **看见回执 / 看见已收到那句备忘 这份协议 is not already 已经最终 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1204 pay70-notfinal interchangeable / 1202 pay70-notauth interchangeable / 295 pay item 1 req-not-auth interchangeable，也不是已经 BIP-70 ack not already final / not already confirmed / not already refunded 正式三事 bundled（295 item 3 余量） interchangeable / 295 pay item 3 interchangeable。**  
   官方写：回执是这套协议的最后一条消息，备忘用来告诉顾客现在的状态，例如「已收下、正在处理」。看见回执，不是已经最终。

2. **看见已收到那句备忘 / 看见回执 / 这份协议 is not already 已经确认 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1204 pay70-notfinal interchangeable / 295 pay item 2 msg-not-ack interchangeable / 1203 pay70-notack interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方写：第二份及以后的回执可以改备忘，用来反映当前状态，例如网上已经看见几份确认。看见「已收到」，不是已经确认。

3. **看见退款输出 / 看见回执 / 这份协议 is not already 已经交差 interchangeable，也不是已经付款协议 bundled（295） interchangeable / 1204 pay70-notfinal interchangeable / 1202 pay70-notauth interchangeable，也不是已经旧式签就已经是 322 interchangeable / 294 lsig interchangeable。**  
   官方写：付款报文里的退款输出，是给商家在必要时把钱退回去用的，不是已经退过。看见退款输出，不是已经退过，也不是已经交差。

消息编码、传输头、证书链拼法、体积上限是规范里的取值或做法，本页不抄。不要另写 BIP-71 / BIP-72。

## 官方为什么这样拆

- **回执 不是已经最终：** 官方把回执备忘写成处理中的状态。
- **已收到那句备忘 不是已经确认：** 官方允许后继回执改确认数。
- **退款输出 不是已经交差：** 官方把退款输出写成不是已经退过。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 最终 | 不是已经最终 | 不是已经授权（255） |
| 确认 | 不是已经确认 | 不是已经是 322（294） |
| 交差 | 不是已经交差 | 不是已经是回执（1203） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-70 ack not already final / not already confirmed / not already refunded 正式三事（295 余量），必须分开是不是已经最终、是不是已经确认、是不是已经交差。可以跳过「看见商家请求就已经最终」。不要另写怎样拼付款请求或怎样验证书链。295 request vs ack bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 消息编码、传输头、证书链拼法、体积上限、语言例句。
- 怎样拼付款请求、怎样验证书链、怎样构造回执。
