# 例：看见 addr 不是已经能套进 sh / wsh；看见一个地址不是已经把输出脚本写在描述符里；看见用 addr 包住了地址不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-385](https://github.com/bitcoin/bips/blob/master/bip-0385.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-385 addr not already nestable-in-sh-wsh / not already output-script-written / not already settled 正式三事（282 余量）/ not 1167 raw385-notaddr interchangeable / not 282 raw-vs-named bundled interchangeable」，不是 raw / addr 描述符 bundled（282），也不是地址串就已经有这笔输出（174），也不是看见描述符就已经是地址（184）。不要另写怎样把地址解成脚本。

## 官方三件事

1. **看见 addr / 看见一个地址 这份栏 is not already 已经能套进 sh / wsh interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1167 raw385-notaddr interchangeable / 1166 raw385-notraw interchangeable / 282 raw item 1 raw-not-named interchangeable，也不是已经 BIP-385 addr not already nestable-in-sh-wsh / not already output-script-written / not already settled 正式三事 bundled（282 item 2 余量） interchangeable / 282 raw item 2 interchangeable。**  
   官方写：`addr(ADDR)` 只能当顶层描述符。它只吃一个地址。看见一个地址，不是已经是本页描述符。

2. **看见一个地址 / 看见 addr / 这份栏 is not already 已经把那份输出脚本写在描述符里 interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1167 raw385-notaddr interchangeable / 282 raw item 3 wrap-not-combo interchangeable / 1168 raw385-notwrap interchangeable，也不是已经地址串就已经有这笔输出 interchangeable / 174 address interchangeable。**  
   官方写：这份描述符产出的输出脚本，就是这个地址产出的那份输出脚本。看见用 addr 包住了地址，不是已经把脚本表达式写出来，也不是已经在链上有这笔输出。

3. **看见用 addr 包住了地址 / 看见 addr / 这份栏 is not already 已经交差 interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1167 raw385-notaddr interchangeable / 1166 raw385-notraw interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把地址和地址产出的脚本写成两步。看见用 addr 包住了地址，不是已经交差。

十六进制脚本、测试向量、例地址是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **addr 不是已经能套进 sh / wsh：** 官方把 addr 写成只能顶层。
- **一个地址 不是已经把输出脚本写在描述符里：** 官方把地址和产出脚本写成两步。
- **用 addr 包住了地址 不是已经交差：** 官方把包住和写了脚本写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 放置 | 不是已经能套进 sh / wsh | 不是已经在链上有输出（174） |
| 输出脚本 | 不是已经写在描述符里 | 不是已经是 raw 具名（1166） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-385 addr not already nestable-in-sh-wsh / not already output-script-written / not already settled 正式三事（282 余量），必须分开是不是已经能套进 sh / wsh、是不是已经把输出脚本写在描述符里、是不是已经交差。可以跳过「看见任意脚本或地址就已经是具名描述符」。不要另写怎样把地址解成脚本。282 raw vs named bundled unbundling 在本页 item 2 续；续 [`worked-example-raw385-notwrap-vs-bundled.md`](worked-example-raw385-notwrap-vs-bundled.md)（不变量 1168 item 3）。

## 本页不抄

- 十六进制脚本、测试向量、例地址。
- 怎样把地址解成脚本、怎样判断合法十六进制、怎样嵌套。
