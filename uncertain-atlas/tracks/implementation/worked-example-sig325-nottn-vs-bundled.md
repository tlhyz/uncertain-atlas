# 例：看见 signet 不是已经是 testnet；看见它比 testnet 稳不是已经和主网同一套结算；看见测试网不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki)（Complete, Applications）。  
**对应课文**：[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、05b 当执行层测试网、M5.4、L5.4、03 共识。本页是「BIP-325 signet not already testnet / not already same-unreliable / not already settled 正式三事（265 余量）/ not 1193 sig325-nottn interchangeable / not 265 signet-vs-testnet bundled interchangeable」，不是 signet bundled（265），也不是 Testnet 4 就已经是 Testnet 3（1190），也不是同一交易标识就已经唯一（257）。不要另写怎样拼挑战或造假签块。

## 官方三件事

1. **看见 signet / 看见它比 testnet 稳 这份网 is not already 已经是 testnet interchangeable，也不是已经 signet bundled（265） interchangeable / 1193 sig325-nottn interchangeable / 1194 sig325-notreg interchangeable / 265 sig item 2 not-reg interchangeable，也不是已经 BIP-325 signet not already testnet / not already same-unreliable / not already settled 正式三事 bundled（265 item 1 余量） interchangeable / 265 sig item 1 interchangeable。**  
   官方写：testnet 适合试新东西、不必拿真钱冒险，但出了名的不可靠。本页是一种新的测试网：出块除了工作量，还要签名。看见 signet，不是已经是 testnet。

2. **看见它比 testnet 稳 / 看见 signet / 这份网 is not already 已经和 testnet 一样不可靠 interchangeable，也不是已经 signet bundled（265） interchangeable / 1193 sig325-nottn interchangeable / 265 sig item 3 work-not-sign interchangeable / 1195 sig325-notsign interchangeable，也不是已经 Testnet 4 就已经是 Testnet 3 interchangeable / 1190 tn94-not3 interchangeable。**  
   官方写：目标不是完美可靠，而是不可靠的分量可预期。看见它比 testnet 稳，不是已经和主网同一套结算。

3. **看见测试网 / 看见 signet / 这份网 is not already 已经交差 interchangeable，也不是已经 signet bundled（265） interchangeable / 1193 sig325-nottn interchangeable / 1194 sig325-notreg interchangeable，也不是已经同一交易标识就已经唯一 interchangeable / 257 txid interchangeable。**  
   官方把 testnet 的巨大重组和出块风暴写成不可用，把本页写成可预期的不可靠。看见测试网，不是已经交差。

挑战怎么承诺、虚拟交易怎么拼、最低难度数字是规范里的取值，本页不抄。

## 官方为什么这样拆

- **signet 不是已经是 testnet：** 官方把本页写成工作量还要签名。
- **比 testnet 稳 不是已经和主网同一套结算：** 官方把可预期的不可靠写成不是主网结算。
- **测试网 不是已经交差：** 官方把不可靠和可预期写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| testnet | 不是已经是 testnet | 不是已经是 Testnet 4（1190） |
| 可靠 | 不是已经和 testnet 一样不可靠 | 不是已经唯一（257） |
| 交差 | 不是已经交差 | 不是已经是 regtest（1194） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-325 signet not already testnet / not already same-unreliable / not already settled 正式三事（265 余量），必须分开是不是已经是 testnet、是不是已经和 testnet 一样不可靠、是不是已经交差。可以跳过「看见测试网就已经能当主网预演」。不要另写怎样拼挑战或造假签块。265 signet vs testnet bundled unbundling 在本页 item 1 启动；续 [`worked-example-sig325-notreg-vs-bundled.md`](worked-example-sig325-notreg-vs-bundled.md)（不变量 1194 item 2）。

## 本页不抄

- 挑战头字节、最低难度、创世哈希、时间戳、例挑战脚本、虚拟交易字段。
- 怎样拼 to_spend / to_sign、怎样磨 nonce 还不重签、怎样让空解当挑战为真。
