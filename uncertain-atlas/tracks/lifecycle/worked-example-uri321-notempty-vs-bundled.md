# 例：看见路径没有链上地址不是已经没有付款指示；看见路径上有地址不是已经只有这一种付法；看见查询里另有指示不是已经交差

**层次**：生命周期 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-321](https://github.com/bitcoin/bips/blob/master/bip-0321.mediawiki)（Complete, Applications）。替换 BIP-21。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-321 empty-path not already no-instruction / not already only-one / not already settled 正式三事（255 余量）/ not 1212 uri321-notempty interchangeable / not 255 uri-vs-authorized bundled interchangeable」，不是付款 URI bundled（255），也不是地址串就已经有输出（174），也不是部分签名包就已经能广播（179）。不要另写怎样造能骗过旧钱包的必选参数。不要另写 BIP-21 当现行方案。

## 官方三件事

1. **看见路径没有链上地址 / 看见路径可以空 这份指示 is not already 已经没有付款指示 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1212 uri321-notempty interchangeable / 1211 uri321-notauth interchangeable / 255 uri item 1 uri-not-auth interchangeable，也不是已经 BIP-321 empty-path not already no-instruction / not already only-one / not already settled 正式三事 bundled（255 item 2 余量） interchangeable / 255 uri item 2 interchangeable。**  
   官方写：路径部分是比特币地址，查询部分给额外付款选项。路径上的地址必须是规定的几种链上地址，或是空的。路径可以空，只要查询里至少有一条付款指示。看见路径没有链上地址，不是已经没有付款指示，也不是已经非法。

2. **看见路径上有地址 / 看见路径没有链上地址 / 这份指示 is not already 已经只有这一种付法 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1212 uri321-notempty interchangeable / 255 uri item 3 req-not-pay interchangeable / 1213 uri321-notreq interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：以后的地址格式应当改放查询键。看见路径上有地址，不是已经只有这一种付法，也不是已经付到链上。

3. **看见查询里另有付款指示 / 看见路径没有链上地址 / 这份指示 is not already 已经交差 interchangeable，也不是已经付款 URI bundled（255） interchangeable / 1212 uri321-notempty interchangeable / 1211 uri321-notauth interchangeable，也不是已经部分签名包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方写：看见查询里另有付款指示，不是已经付过，也不是已经广播，也不是已经交差。

例地址、语法细则、金额写法是规范里的例子和格式，本页不抄。不要另写 BIP-21 当现行方案。

## 官方为什么这样拆

- **路径没有链上地址 不是已经没有付款指示：** 官方允许路径空、查询里至少有一条指示。
- **路径上有地址 不是已经只有这一种付法：** 官方把以后的地址格式写成改放查询键。
- **查询里另有付款指示 不是已经交差：** 官方把查询里另有指示写成不是已经付过。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 指示 | 不是已经没有付款指示 | 不是已经有输出（174） |
| 付法 | 不是已经只有这一种付法 | 不是已经能广播（179） |
| 交差 | 不是已经交差 | 不是已经授权（1211） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-321 empty-path not already no-instruction / not already only-one / not already settled 正式三事（255 余量），必须分开是不是已经没有付款指示、是不是已经只有这一种付法、是不是已经交差。可以跳过「看见付款 URI 就已经授权」。不要另写怎样造能骗过旧钱包的必选参数。不要另写 BIP-21 当现行方案。255 uri vs authorized bundled unbundling 在本页 item 2 续；续 [`worked-example-uri321-notreq-vs-bundled.md`](worked-example-uri321-notreq-vs-bundled.md)（不变量 1213 item 3）。

## 本页不抄

- 例地址、语法细则、金额写法、查询键取值、回执拼接步骤。
- 怎样造能骗过旧钱包的必选参数，怎样用回执把浏览器打开到收款方。
