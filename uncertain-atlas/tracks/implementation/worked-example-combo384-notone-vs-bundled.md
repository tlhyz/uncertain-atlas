# 例：看见 combo 不是已经能套进 sh / wsh；看见一把钥不是已经是一种输出脚本；看见只能当顶层不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-384](https://github.com/bitcoin/bips/blob/master/bip-0384.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-384 combo not already nestable-in-sh-wsh / not already one-script / not already settled 正式三事（281 余量）/ not 1163 combo384-notone interchangeable / not 281 combo-vs-one-script bundled interchangeable」，不是 combo 描述符 bundled（281），也不是 381 那种同一套放置（1148），也不是钱包策略就已经是一条描述符（1160）。不要另写怎样拼那几份输出脚本。

## 官方三件事

1. **看见 combo / 看见一把钥 这份栏 is not already 已经能套进 sh / wsh interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1163 combo384-notone interchangeable / 1164 combo384-notwitpair interchangeable / 281 combo item 2 key-not-witpair interchangeable，也不是已经 BIP-384 combo not already nestable-in-sh-wsh / not already one-script / not already settled 正式三事 bundled（281 item 1 余量） interchangeable / 281 combo item 1 interchangeable。**  
   官方写：`combo(KEY)` 只能当顶层表达式。它只吃一把钥表达式。看见写了 combo，不是已经能再套进 `sh` 或 `wsh`。

2. **看见一把钥 / 看见 combo / 这份栏 is not already 已经是一种输出脚本 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1163 combo384-notone interchangeable / 281 combo item 3 combo-not-pol interchangeable / 1165 combo384-notpol interchangeable，也不是已经 381 那种同一套放置 interchangeable / 1148 pk381-notplace interchangeable。**  
   官方写：看见一把钥，不是已经是 381 那种只产出一种脚本的表达式。

3. **看见只能当顶层 / 看见 combo / 这份栏 is not already 已经交差 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1163 combo384-notone interchangeable / 1164 combo384-notwitpair interchangeable，也不是已经钱包策略就已经是一条描述符 interchangeable / 1160 pol388-notdesc interchangeable。**  
   官方把它写成只能顶层，并且按钥产出两份或四份。看见只能当顶层，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **combo 不是已经能套进 sh / wsh：** 官方把 combo 写成只能顶层。
- **一把钥 不是已经是一种输出脚本：** 官方把 combo 写成按钥产出两份或四份。
- **只能当顶层 不是已经交差：** 官方把放置和份数写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 放置 | 不是已经能套进 sh / wsh | 不是已经是 381 那种放置（1148） |
| 一种脚本 | 不是已经是一种输出脚本 | 不是已经是一份钱包策略（1165） |
| 交差 | 不是已经交差 | 不是已经是一条描述符（1160） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-384 combo not already nestable-in-sh-wsh / not already one-script / not already settled 正式三事（281 余量），必须分开是不是已经能套进 sh / wsh、是不是已经是一种输出脚本、是不是已经交差。可以跳过「看见一把钥就已经是一种输出脚本」。不要另写怎样拼那几份输出脚本。281 combo vs one-script bundled unbundling 在本页 item 1 启动；续 [`worked-example-combo384-notwitpair-vs-bundled.md`](worked-example-combo384-notwitpair-vs-bundled.md)（不变量 1164 item 2）。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样拼 P2PK / P2PKH / P2WPKH / P2SH-P2WPKH、怎样判断压缩、怎样嵌套。
