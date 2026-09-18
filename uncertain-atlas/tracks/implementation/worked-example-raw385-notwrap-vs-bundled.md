# 例：看见一份 raw 或 addr 不是已经是一份 combo；看见能包住今天在用的脚本或地址不是已经是一份钱包策略；看见一份包装不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-385](https://github.com/bitcoin/bips/blob/master/bip-0385.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-385 one-wrap not already combo / not already wallet-policy / not already settled 正式三事（282 余量）/ not 1168 raw385-notwrap interchangeable / not 282 raw-vs-named bundled interchangeable」，不是 raw / addr 描述符 bundled（282），也不是一份 combo 就已经是一份钱包策略（1165），也不是钱包策略就已经是一条描述符（1160）。不要另写怎样把地址解成脚本。

## 官方三件事

1. **看见一份 raw 或 addr 包住一个对象 这份栏 is not already 已经是一份 combo interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1168 raw385-notwrap interchangeable / 1166 raw385-notraw interchangeable / 282 raw item 1 raw-not-named interchangeable，也不是已经 BIP-385 one-wrap not already combo / not already wallet-policy / not already settled 正式三事 bundled（282 item 3 余量） interchangeable / 282 raw item 3 interchangeable。**  
   官方写：raw 把任意输出脚本包成描述符；addr 把一个地址包成描述符。看见一份包装，不是已经是 384 那种一把钥产出两份或四份。

2. **看见能包住今天在用的脚本或地址 / 看见一份包装 / 这份栏 is not already 已经是一份钱包策略 interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1168 raw385-notwrap interchangeable / 282 raw item 2 addr-not-script interchangeable / 1167 raw385-notaddr interchangeable，也不是已经一份 combo 就已经是一份钱包策略 interchangeable / 1165 combo384-notpol interchangeable。**  
   官方写：看见能包住今天在用的脚本或地址，不是已经是 388 那种账户所需的全部描述符，也不是已经是地址。

3. **看见一份包装 / 看见 raw 或 addr / 这份栏 is not already 已经交差 interchangeable，也不是已经 raw / addr 描述符 bundled（282） interchangeable / 1168 raw385-notwrap interchangeable / 1166 raw385-notraw interchangeable，也不是已经钱包策略就已经是一条描述符 interchangeable / 1160 pol388-notdesc interchangeable。**  
   官方把本页写成包一个对象，不是一把钥上的几份传统脚本。看见一份包装，不是已经交差。

十六进制脚本、测试向量、例地址是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **一份包装 不是已经是 combo：** 官方把本页写成包一个对象。
- **能包住今天在用的脚本或地址 不是已经是钱包策略：** 官方把包装和账户全部描述符写成两句。
- **一份包装 不是已经交差：** 官方把 combo 和策略写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| combo | 不是已经是一份 combo | 不是已经是 384 那种多份脚本（1165） |
| 钱包策略 | 不是已经是一份钱包策略 | 不是已经是 388 那种策略（1160） |
| 交差 | 不是已经交差 | 不是已经是 raw 具名（1166） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-385 one-wrap not already combo / not already wallet-policy / not already settled 正式三事（282 余量），必须分开是不是已经是一份 combo、是不是已经是一份钱包策略、是不是已经交差。可以跳过「看见任意脚本或地址就已经是具名描述符」。不要另写怎样把地址解成脚本。282 raw vs named bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 十六进制脚本、测试向量、例地址。
- 怎样把地址解成脚本、怎样判断合法十六进制、怎样嵌套。
