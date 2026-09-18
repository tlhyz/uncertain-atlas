# 例：看见 20 分钟例外不是已经没有块风暴；看见最低难度不是已经拿掉了例外；看见留着例外不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-94](https://github.com/bitcoin/bips/blob/master/bip-0094.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-94 twenty-min not already no-storm / not already exception-removed / not already settled 正式三事（292 余量）/ not 1191 tn94-notstorm interchangeable / not 292 testnet4-vs-testnet3 bundled interchangeable」，不是 Testnet 4 bundled（292），也不是 signet 就已经是 testnet（265），也不是头上工作量就已经签过（265）。不要另写怎样挖最低难度或怎样造块风暴。

## 官方三件事

1. **看见 20 分钟例外 / 看见最低难度 这份网 is not already 已经没有块风暴 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1191 tn94-notstorm interchangeable / 1190 tn94-not3 interchangeable / 292 tn item 1 tn4-not-3 interchangeable，也不是已经 BIP-94 twenty-min not already no-storm / not already exception-removed / not already settled 正式三事 bundled（292 item 2 余量） interchangeable / 292 tn item 2 interchangeable。**  
   官方写：Testnet 3 那条 20 分钟例外本页还留着。块风暴的修法是：跨周期调难度时，基数必须取上一周期的第一块，不得再取上一周期的最后一块。看见还能出最低难度块，不是风暴已经没了。

2. **看见最低难度 / 看见 20 分钟例外 / 这份网 is not already 已经拿掉了例外 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1191 tn94-notstorm interchangeable / 292 tn item 3 old-not-follow interchangeable / 1192 tn94-notfollow interchangeable，也不是已经 signet 就已经是 testnet interchangeable / 265 signet interchangeable。**  
   官方另写：拿掉 20 分钟例外有人提过，评审认为它还让 CPU 能往前推链，所以没拿。看见留着例外，不是已经改成主网那套难度。

3. **看见留着例外 / 看见 20 分钟例外 / 这份网 is not already 已经交差 interchangeable，也不是已经 Testnet 4 bundled（292） interchangeable / 1191 tn94-notstorm interchangeable / 1190 tn94-not3 interchangeable，也不是已经头上工作量就已经签过 interchangeable / 265 signet interchangeable。**  
   官方把例外留下和改取上一周期第一块写成两件独立的事。看见留着例外，不是已经交差。

创世哈希、消息起始字节、端口、难度常数、时间窗数字是规范里的取值，本页不抄。

## 官方为什么这样拆

- **20 分钟例外 不是已经没有块风暴：** 官方把例外留下和改取第一块写成两件。
- **最低难度 不是已经拿掉了例外：** 官方把没拿例外写成还让 CPU 能往前推链。
- **留着例外 不是已经交差：** 官方把风暴修法和主网难度写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 风暴 | 不是已经没有块风暴 | 不是已经是 signet（265） |
| 例外 | 不是已经拿掉了例外 | 不是已经签过（265） |
| 交差 | 不是已经交差 | 不是已经换完（1190） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-94 twenty-min not already no-storm / not already exception-removed / not already settled 正式三事（292 余量），必须分开是不是已经没有块风暴、是不是已经拿掉了例外、是不是已经交差。可以跳过「看见又一条测试网就已经换完」。不要另写怎样挖最低难度或怎样造块风暴。292 testnet4 vs testnet3 bundled unbundling 在本页 item 2 续；续 [`worked-example-tn94-notfollow-vs-bundled.md`](worked-example-tn94-notfollow-vs-bundled.md)（不变量 1192 item 3）。

## 本页不抄

- 创世哈希、消息起始字节、端口、难度常数、时间窗数字、创世十六进制。
- 怎样挖最低难度、怎样按例外出块、怎样造块风暴、怎样做时间扭曲。
