# 例：看见 signet 不是已经是 regtest；看见还能协调出块不是已经谁都能独占；看见本地无代价出块不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki)（Complete, Applications）。  
**对应课文**：[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、05b 当执行层测试网、M5.4、L5.4、03 共识。本页是「BIP-325 signet not already regtest / not already anyone-controls / not already settled 正式三事（265 余量）/ not 1194 sig325-notreg interchangeable / not 265 signet-vs-testnet bundled interchangeable」，不是 signet bundled（265），也不是 20 分钟例外就已经没有块风暴（1191），也不是跳脚本就已经全验证（25）。不要另写怎样拼挑战或造假签块。

## 官方三件事

1. **看见 signet / 看见还能协调出块 这份网 is not already 已经是 regtest interchangeable，也不是已经 signet bundled（265） interchangeable / 1194 sig325-notreg interchangeable / 1193 sig325-nottn interchangeable / 265 sig item 1 not-tn interchangeable，也不是已经 BIP-325 signet not already regtest / not already anyone-controls / not already settled 正式三事 bundled（265 item 2 余量） interchangeable / 265 sig item 2 interchangeable。**  
   官方写：regtest 不适合多家独立方做较长时间的场景，因为造块没有代价，任何一方都能完全控制测试网。看见 signet，不是已经是本地无代价出块。

2. **看见还能协调出块 / 看见 signet / 这份网 is not already 已经谁都能独占 interchangeable，也不是已经 signet bundled（265） interchangeable / 1194 sig325-notreg interchangeable / 265 sig item 3 work-not-sign interchangeable / 1195 sig325-notsign interchangeable，也不是已经 20 分钟例外就已经没有块风暴 interchangeable / 1191 tn94-notstorm interchangeable。**  
   官方把造块没有代价、任何一方都能完全控制写成 regtest 不适合多方长期测。看见还能协调出块，不是已经谁都能独占。

3. **看见本地无代价出块 / 看见 signet / 这份网 is not already 已经交差 interchangeable，也不是已经 signet bundled（265） interchangeable / 1194 sig325-notreg interchangeable / 1193 sig325-nottn interchangeable，也不是已经跳脚本就已经全验证 interchangeable / 25 skip interchangeable。**  
   官方把无代价控制和可预期不可靠写成两条路。看见本地无代价出块，不是已经交差。

挑战怎么承诺、虚拟交易怎么拼、最低难度数字是规范里的取值，本页不抄。

## 官方为什么这样拆

- **signet 不是已经是 regtest：** 官方把无代价出块写成不是本页。
- **还能协调出块 不是已经谁都能独占：** 官方把任何一方都能完全控制写成 regtest。
- **本地无代价出块 不是已经交差：** 官方把控制和可预期写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| regtest | 不是已经是 regtest | 不是已经没有风暴（1191） |
| 独占 | 不是已经谁都能独占 | 不是已经全验证（25） |
| 交差 | 不是已经交差 | 不是已经是 testnet（1193） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-325 signet not already regtest / not already anyone-controls / not already settled 正式三事（265 余量），必须分开是不是已经是 regtest、是不是已经谁都能独占、是不是已经交差。可以跳过「看见测试网就已经能当主网预演」。不要另写怎样拼挑战或造假签块。265 signet vs testnet bundled unbundling 在本页 item 2 续；续 [`worked-example-sig325-notsign-vs-bundled.md`](worked-example-sig325-notsign-vs-bundled.md)（不变量 1195 item 3）。

## 本页不抄

- 挑战头字节、最低难度、创世哈希、时间戳、例挑战脚本、虚拟交易字段。
- 怎样拼 to_spend / to_sign、怎样磨 nonce 还不重签、怎样让空解当挑战为真。
