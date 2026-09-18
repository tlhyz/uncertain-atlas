# 例：看见付款 URI 不是已经授权；看见扫了码不是已经付了；看见链接不是已经交差

**层次**：生命周期 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-321](https://github.com/bitcoin/bips/blob/master/bip-0321.mediawiki)（Complete, Applications）。替换 BIP-21。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-321 uri not already authorized / not already paid / not already settled 正式三事（255 余量）/ not 1211 uri321-notauth interchangeable / not 255 uri-vs-authorized bundled interchangeable」，不是付款 URI bundled（255），也不是远程取单就已经验证（55），也不是带 pj= 就已经是 payjoin 付款（290）。不要另写怎样造能骗过旧钱包的必选参数。不要另写 BIP-21 当现行方案。

## 官方三件事

1. **看见付款 URI / 看见扫了码 这份指示 is not already 已经授权 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1211 uri321-notauth interchangeable / 1212 uri321-notempty interchangeable / 255 uri item 2 path-not-empty interchangeable，也不是已经 BIP-321 uri not already authorized / not already paid / not already settled 正式三事 bundled（255 item 1 余量） interchangeable / 255 uri item 1 interchangeable。**  
   官方写：本页给比特币付款指示写一种 URI。动机是让用户点网页或扫码就能付。官方还写：比特币客户端没有得到用户授权，不得按 URI 行事。应当要求用户一笔一笔手批。看见一条付款 URI，不是已经授权。

2. **看见扫了码 / 看见付款 URI / 这份指示 is not already 已经付了 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1211 uri321-notauth interchangeable / 255 uri item 3 req-not-pay interchangeable / 1213 uri321-notreq interchangeable，也不是已经远程取单就已经验证 interchangeable / 55 remote interchangeable。**  
   官方写：看见一条付款 URI，不是已经付了，也不是已经广播。看见扫了码，不是已经点了发送。

3. **看见链接 / 看见付款 URI / 这份指示 is not already 已经交差 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1211 uri321-notauth interchangeable / 1212 uri321-notempty interchangeable，也不是已经带 pj= 就已经是 payjoin 付款 interchangeable / 290 pj interchangeable。**  
   官方把「描述付款指示」和「用户批了」写成两件事。看见链接，不是已经交差。

例地址、语法细则、金额写法是规范里的例子和格式，本页不抄。不要另写 BIP-21 当现行方案。

## 官方为什么这样拆

- **付款 URI 不是已经授权：** 官方把没有用户授权不得按 URI 行事写成另一句。
- **扫了码 不是已经付了：** 官方把扫码写成不是已经点了发送。
- **链接 不是已经交差：** 官方把描述指示和用户批了写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 授权 | 不是已经授权 | 不是已经验证（55） |
| 付了 | 不是已经付了 | 不是已经是 payjoin（290） |
| 交差 | 不是已经交差 | 不是已经没有指示（1212） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-321 uri not already authorized / not already paid / not already settled 正式三事（255 余量），必须分开是不是已经授权、是不是已经付了、是不是已经交差。可以跳过「看见付款 URI 就已经授权」。不要另写怎样造能骗过旧钱包的必选参数。不要另写 BIP-21 当现行方案。255 uri vs authorized bundled unbundling 在本页 item 1 启动；续 [`worked-example-uri321-notempty-vs-bundled.md`](worked-example-uri321-notempty-vs-bundled.md)（不变量 1212 item 2）。

## 本页不抄

- 例地址、语法细则、金额写法、查询键取值、回执拼接步骤。
- 怎样造能骗过旧钱包的必选参数，怎样用回执把浏览器打开到收款方。
