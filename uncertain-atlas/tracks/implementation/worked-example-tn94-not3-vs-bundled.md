# 例：看见 Testnet 4 不是已经是 Testnet 3；看见测试币不是已经没价值；看见规则更近主网不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-94](https://github.com/bitcoin/bips/blob/master/bip-0094.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-94 testnet4 not already testnet3 / not already mainnet / not already settled 正式三事（292 余量）/ not 1190 tn94-not3 interchangeable / not 292 testnet4-vs-testnet3 bundled interchangeable」，不是 Testnet 4 bundled（292），也不是 signet 就已经是 testnet（265），也不是策略就已经是共识（144）。不要另写怎样挖最低难度或怎样造块风暴。

## 官方三件事

1. **看见 Testnet 4 / 看见测试币 这份网 is not already 已经是 Testnet 3 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1190 tn94-not3 interchangeable / 1191 tn94-notstorm interchangeable / 292 tn item 2 exc-not-storm interchangeable，也不是已经 BIP-94 testnet4 not already testnet3 / not already mainnet / not already settled 正式三事 bundled（292 item 1 余量） interchangeable / 292 tn item 1 interchangeable。**  
   官方写：本页是一条新的测试网，目标是替换 Testnet 3。共识规则有几处小而要紧的改动，好让只靠 CPU 挖矿去打这条网变得不实际。看见 Testnet 4，不是已经是 Testnet 3。

2. **看见测试币 / 看见 Testnet 4 / 这份网 is not already 已经没价值 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1190 tn94-not3 interchangeable / 292 tn item 3 old-not-follow interchangeable / 1192 tn94-notfollow interchangeable，也不是已经 signet 就已经是 testnet interchangeable / 265 signet interchangeable。**  
   官方另引：Testnet 3 跑了很多年，出块奖励已经薄到发测试币不再好用；测试币被拿去空投、被买卖，有人说测试币不该有价值这条底已经被破。看见测试币，不是已经没人当钱。看见规则更近主网，不是已经是主网结算。

3. **看见规则更近主网 / 看见 Testnet 4 / 这份网 is not already 已经交差 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1190 tn94-not3 interchangeable / 1191 tn94-notstorm interchangeable，也不是已经策略就已经是共识 interchangeable / 144 policy interchangeable。**  
   官方把替换、测试币被买卖、块风暴写成换网的理由，不是改个名字。看见规则更近主网，不是已经交差。

创世哈希、消息起始字节、端口、难度常数、时间窗数字是规范里的取值，本页不抄。

## 官方为什么这样拆

- **Testnet 4 不是已经是 Testnet 3：** 官方把本页写成一条新的测试网。
- **测试币 不是已经没价值：** 官方把测试币被买卖写成底已经被破。
- **规则更近主网 不是已经交差：** 官方把换网和主网结算写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 换网 | 不是已经是 Testnet 3 | 不是已经是 signet（265） |
| 价值 | 不是已经没价值 | 不是已经是共识（144） |
| 交差 | 不是已经交差 | 不是已经没有风暴（1191） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-94 testnet4 not already testnet3 / not already mainnet / not already settled 正式三事（292 余量），必须分开是不是已经是 Testnet 3、是不是已经没价值、是不是已经交差。可以跳过「看见又一条测试网就已经换完」。不要另写怎样挖最低难度或怎样造块风暴。292 testnet4 vs testnet3 bundled unbundling 在本页 item 1 启动；续 [`worked-example-tn94-notstorm-vs-bundled.md`](worked-example-tn94-notstorm-vs-bundled.md)（不变量 1191 item 2）。

## 本页不抄

- 创世哈希、消息起始字节、端口、难度常数、时间窗数字、创世十六进制。
- 怎样挖最低难度、怎样按例外出块、怎样造块风暴、怎样做时间扭曲。
