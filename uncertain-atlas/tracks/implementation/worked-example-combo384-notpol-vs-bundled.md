# 例：看见一份 combo 不是已经是一份钱包策略；看见产出和 pk / pkh / wpkh / sh(wpkh) 一样不是已经写了那几条表达式；看见两份或四份脚本不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-384](https://github.com/bitcoin/bips/blob/master/bip-0384.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-384 one-combo not already wallet-policy / not already those-named-exprs / not already settled 正式三事（281 余量）/ not 1165 combo384-notpol interchangeable / not 281 combo-vs-one-script bundled interchangeable」，不是 combo 描述符 bundled（281），也不是钱包策略就已经是一条描述符（1160），也不是看见描述符就已经是地址（184）。不要另写怎样拼那几份输出脚本。

## 官方三件事

1. **看见一份 combo 产出两份或四份脚本 这份栏 is not already 已经是一份钱包策略 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1165 combo384-notpol interchangeable / 1163 combo384-notone interchangeable / 281 combo item 1 combo-not-one interchangeable，也不是已经 BIP-384 one-combo not already wallet-policy / not already those-named-exprs / not already settled 正式三事 bundled（281 item 3 余量） interchangeable / 281 combo item 3 interchangeable。**  
   官方写：一份 combo 按这把钥产出两份或四份输出脚本。看见一份表达式，不是已经是 388 那种「一个账户所需的全部描述符」。

2. **看见产出和 pk / pkh / wpkh / sh(wpkh) 一样的脚本 / 看见一份 combo / 这份栏 is not already 已经写了那几条表达式 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1165 combo384-notpol interchangeable / 281 combo item 2 key-not-witpair interchangeable / 1164 combo384-notwitpair interchangeable，也不是已经钱包策略就已经是一条描述符 interchangeable / 1160 pol388-notdesc interchangeable。**  
   官方写：看见产出和 `pk` / `pkh` / `wpkh` / `sh(wpkh)` 一样的脚本，不是已经写了那几条表达式，也不是已经是地址。

3. **看见两份或四份脚本 / 看见一份 combo / 这份栏 is not already 已经交差 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1165 combo384-notpol interchangeable / 1163 combo384-notone interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把本页写成一把钥上的几份传统脚本，不是账户上的全部描述符。看见两份或四份脚本，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **一份 combo 不是已经是一份钱包策略：** 官方把本页写成一把钥上的几份传统脚本。
- **产出一样的脚本 不是已经写了那几条表达式：** 官方把产出脚本和写了具名表达式写成两句。
- **两份或四份脚本 不是已经交差：** 官方把份数和账户策略写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 钱包策略 | 不是已经是一份钱包策略 | 不是已经是 388 那种策略（1160） |
| 具名表达式 | 不是已经写了那几条 | 不是已经带齐见证对（1164） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-384 one-combo not already wallet-policy / not already those-named-exprs / not already settled 正式三事（281 余量），必须分开是不是已经是一份钱包策略、是不是已经写了那几条表达式、是不是已经交差。可以跳过「看见一把钥就已经是一种输出脚本」。不要另写怎样拼那几份输出脚本。281 combo vs one-script bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样拼 P2PK / P2PKH / P2WPKH / P2SH-P2WPKH、怎样判断压缩、怎样嵌套。
