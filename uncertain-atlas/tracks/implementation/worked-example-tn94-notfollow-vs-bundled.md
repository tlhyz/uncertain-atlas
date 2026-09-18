# 例：看见会 Testnet 3 不是已经能安全跟 Testnet 4；看见补了参数不是已经在验新规则；看见和主网同一套软分叉不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-94](https://github.com/bitcoin/bips/blob/master/bip-0094.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-94 know-testnet3 not already safe-follow / not already new-rules / not already settled 正式三事（292 余量）/ not 1192 tn94-notfollow interchangeable / not 292 testnet4-vs-testnet3 bundled interchangeable」，不是 Testnet 4 bundled（292），也不是同一交易标识就已经唯一（257），也不是策略就已经是共识（144）。不要另写怎样挖最低难度或怎样造块风暴。

## 官方三件事

1. **看见会 Testnet 3 / 看见补了参数 这份网 is not already 已经能安全跟 Testnet 4 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1192 tn94-notfollow interchangeable / 1190 tn94-not3 interchangeable / 292 tn item 1 tn4-not-3 interchangeable，也不是已经 BIP-94 know-testnet3 not already safe-follow / not already new-rules / not already settled 正式三事 bundled（292 item 3 余量） interchangeable / 292 tn item 3 interchangeable。**  
   官方写：会 Testnet 3 的软件，理论上只要补网络参数就能跟 Testnet 4。可是只实现 Testnet 3 规则的节点，会收下违反 Testnet 4 的链，因而会被分叉甩开。看见补了参数，不是已经在验新规则。

2. **看见和主网同一套共识 / 看见会 Testnet 3 / 这份网 is not already 已经是同一条网 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1192 tn94-notfollow interchangeable / 292 tn item 2 exc-not-storm interchangeable / 1191 tn94-notstorm interchangeable，也不是已经策略就已经是共识 interchangeable / 144 policy interchangeable。**  
   官方写：Testnet 4 跟主网同一套共识，只加这三条例外；当时主网上已经激活的软分叉，从创世起就强制。看见和主网同一套软分叉，不是已经是同一条网。

3. **看见和主网同一套软分叉 / 看见会 Testnet 3 / 这份网 is not already 已经交差 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1192 tn94-notfollow interchangeable / 1190 tn94-not3 interchangeable，也不是已经同一交易标识就已经唯一 interchangeable / 257 txid interchangeable。**  
   官方把补参数就能连和只验旧规则会被甩开写成两道门。看见和主网同一套软分叉，不是已经交差。

创世哈希、消息起始字节、端口、难度常数、时间窗数字是规范里的取值，本页不抄。

## 官方为什么这样拆

- **会 Testnet 3 不是已经能安全跟 Testnet 4：** 官方把只验旧规则写成会被分叉甩开。
- **补了参数 不是已经在验新规则：** 官方把补参数和验新规则写成两步。
- **和主网同一套软分叉 不是已经交差：** 官方把同一套软分叉写成不是已经是同一条网。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 跟网 | 不是已经能安全跟 | 不是已经唯一（257） |
| 同一条 | 不是已经是同一条网 | 不是已经是共识（144） |
| 交差 | 不是已经交差 | 不是已经没有风暴（1191） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-94 know-testnet3 not already safe-follow / not already new-rules / not already settled 正式三事（292 余量），必须分开是不是已经能安全跟、是不是已经在验新规则、是不是已经交差。可以跳过「看见又一条测试网就已经换完」。不要另写怎样挖最低难度或怎样造块风暴。292 testnet4 vs testnet3 bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 创世哈希、消息起始字节、端口、难度常数、时间窗数字、创世十六进制。
- 怎样挖最低难度、怎样按例外出块、怎样造块风暴、怎样做时间扭曲。
