# 例：看见不认识的必选参数不是已经能付；看见打开了回执不是已经确认；看见必选回执却是浏览器方案不是已经交差

**层次**：生命周期 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-321](https://github.com/bitcoin/bips/blob/master/bip-0321.mediawiki)（Complete, Applications）。替换 BIP-21。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-321 required-param not already payable / not already confirmed / not already settled 正式三事（255 余量）/ not 1213 uri321-notreq interchangeable / not 255 uri-vs-authorized bundled interchangeable」，不是付款 URI bundled（255），也不是后继校验就已经是旧方案（181），也不是远程取单就已经验证（55）。不要另写怎样造能骗过旧钱包的必选参数。不要另写 BIP-21 当现行方案。

## 官方三件事

1. **看见不认识的必选参数 / 看见不认识但不是必选的参数 这份指示 is not already 已经能付 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1213 uri321-notreq interchangeable / 1211 uri321-notauth interchangeable / 255 uri item 1 uri-not-auth interchangeable，也不是已经 BIP-321 required-param not already payable / not already confirmed / not already settled 正式三事 bundled（255 item 3 余量） interchangeable / 255 uri item 3 interchangeable。**  
   官方写：键前面加了必选前缀的，客户端若不实现，必须把整条 URI 当成非法。没加这个前缀、自己又不实现的，可以安全忽略。看见不认识的必选参数，不是已经能付。看见不认识但不是必选的参数，不是已经非法。

2. **看见打开了回执 / 看见不认识的必选参数 / 这份指示 is not already 已经确认 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1213 uri321-notreq interchangeable / 255 uri item 2 path-not-empty interchangeable / 1212 uri321-notempty interchangeable，也不是已经后继校验就已经是旧方案 interchangeable / 181 bech32m interchangeable。**  
   官方写：可选回执参数让发起付款的应用在付完之后拿到证明。钱包必须先核回执方案不是浏览器会打开的那几类，才可以打开。看见打开了回执，不是已经确认，也不是已经写进共识。

3. **看见必选回执却是浏览器方案 / 看见不认识的必选参数 / 这份指示 is not already 已经交差 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1213 uri321-notreq interchangeable / 1211 uri321-notauth interchangeable，也不是已经远程取单就已经验证 interchangeable / 55 remote interchangeable。**  
   官方写：若不会打开回执、而参数又是必选回执，钱包不得发起付款。看见必选回执却是浏览器方案，不是已经该付，也不是已经交差。

例地址、语法细则、金额写法是规范里的例子和格式，本页不抄。不要另写 BIP-21 当现行方案。

## 官方为什么这样拆

- **不认识的必选参数 不是已经能付：** 官方把不认识的必选参数写成整条非法。
- **打开了回执 不是已经确认：** 官方把回执写成不是已经确认。
- **必选回执却是浏览器方案 不是已经交差：** 官方把浏览器方案写成不得打开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能付 | 不是已经能付 | 不是已经是旧方案（181） |
| 确认 | 不是已经确认 | 不是已经验证（55） |
| 交差 | 不是已经交差 | 不是已经授权（1211） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-321 required-param not already payable / not already confirmed / not already settled 正式三事（255 余量），必须分开是不是已经能付、是不是已经确认、是不是已经交差。可以跳过「看见付款 URI 就已经授权」。不要另写怎样造能骗过旧钱包的必选参数。不要另写 BIP-21 当现行方案。255 uri vs authorized bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 例地址、语法细则、金额写法、查询键取值、回执拼接步骤。
- 怎样造能骗过旧钱包的必选参数，怎样用回执把浏览器打开到收款方。
