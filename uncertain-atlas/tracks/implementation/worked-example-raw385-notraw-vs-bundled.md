# 例：看见 raw 不是已经能套进 sh / wsh；看见交出了脚本字节不是已经是具名表达式；看见一串十六进制脚本不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-385](https://github.com/bitcoin/bips/blob/master/bip-0385.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-385 raw not already nestable-in-sh-wsh / not already named-expr / not already settled 正式三事（282 余量）/ not 1166 raw385-notraw interchangeable / not 282 raw-vs-named bundled interchangeable」，不是 raw / addr 描述符 bundled（282），也不是 combo 就已经一种脚本（1163），也不是看见描述符就已经是地址（184）。不要另写怎样把地址解成脚本。

## 官方三件事

1. **看见 raw / 看见一串十六进制脚本 这份栏 is not already 已经能套进 sh / wsh interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1166 raw385-notraw interchangeable / 1167 raw385-notaddr interchangeable / 282 raw item 2 addr-not-script interchangeable，也不是已经 BIP-385 raw not already nestable-in-sh-wsh / not already named-expr / not already settled 正式三事 bundled（282 item 1 余量） interchangeable / 282 raw item 1 interchangeable。**  
   官方写：`raw(HEX)` 只能当顶层描述符。参数是一串表示 Bitcoin 脚本的十六进制。看见写了 raw，不是已经能再套进 `sh` 或 `wsh`。

2. **看见交出了脚本字节 / 看见 raw / 这份栏 is not already 已经写了 381 那种具名函数 interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1166 raw385-notraw interchangeable / 282 raw item 3 wrap-not-combo interchangeable / 1168 raw385-notwrap interchangeable，也不是已经 combo 就已经一种脚本 interchangeable / 1163 combo384-notone interchangeable。**  
   官方写：这份描述符产出的输出脚本，就是 HEX 表示的那条脚本。看见交出了脚本字节，不是已经写了 381 那种具名函数。

3. **看见一串十六进制脚本 / 看见 raw / 这份栏 is not already 已经交差 interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1166 raw385-notraw interchangeable / 1167 raw385-notaddr interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把它写成只能顶层，参数就是脚本本身。看见一串十六进制脚本，不是已经交差。

十六进制脚本、测试向量、例地址是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **raw 不是已经能套进 sh / wsh：** 官方把 raw 写成只能顶层。
- **交出了脚本字节 不是已经是具名表达式：** 官方把参数写成脚本本身，不是具名函数。
- **一串十六进制脚本 不是已经交差：** 官方把放置和具名写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 放置 | 不是已经能套进 sh / wsh | 不是已经是 combo 一种脚本（1163） |
| 具名 | 不是已经是 pk / sh 那种具名 | 不是已经是地址（184） |
| 交差 | 不是已经交差 | 不是已经是一份包装（1168） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-385 raw not already nestable-in-sh-wsh / not already named-expr / not already settled 正式三事（282 余量），必须分开是不是已经能套进 sh / wsh、是不是已经是具名表达式、是不是已经交差。可以跳过「看见任意脚本或地址就已经是具名描述符」。不要另写怎样把地址解成脚本。282 raw vs named bundled unbundling 在本页 item 1 启动；续 [`worked-example-raw385-notaddr-vs-bundled.md`](worked-example-raw385-notaddr-vs-bundled.md)（不变量 1167 item 2）。

## 本页不抄

- 十六进制脚本、测试向量、例地址。
- 怎样把地址解成脚本、怎样判断合法十六进制、怎样嵌套。
