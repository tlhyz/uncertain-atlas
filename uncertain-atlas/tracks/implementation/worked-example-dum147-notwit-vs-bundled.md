# 例：看见隔离见证已经开不是已经没有 dummy 延展；看见 txid 没变不是 wtxid 已经没变；看见隔离见证不是已经交差

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-147](https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki)（Deployed, Consensus soft fork）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4。本页是「BIP-147 segwit not already no-dummy-malleation / not already wtxid-fixed / not already settled 正式三事（264 余量）/ not 1230 dum147-notwit interchangeable / not 264 dummy-vs-empty bundled interchangeable」，不是 dummy bundled（264），也不是策略就已经是共识（144），也不是紧凑块宣布就已经收到（36）。不要另写怎样改 dummy 撞身份。

## 官方三件事

1. **看见隔离见证已经开 / 看见隔离见证 这份开是 not already 已经没有 dummy 延展 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1230 dum147-notwit interchangeable / 1229 dum147-notany interchangeable / 264 dummy item 1 dum-not-any interchangeable，也不是已经 BIP-147 segwit not already no-dummy-malleation / not already wtxid-fixed / not already settled 正式三事 bundled（264 item 2 余量） interchangeable / 264 dummy item 2 interchangeable。**  
   官方写：没有隔离见证时，签名延展会改 txid，并让未确认的子交易作废。隔离见证之后，txid 不能被第三方改，但本页这条仍会改 wtxid，并可能降低紧凑块中继的效率。看见隔离见证已经开，不是已经没有 dummy 延展。

2. **看见 txid 没变 / 看见隔离见证已经开 / 这份开是 not already 已经 wtxid 没变 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1230 dum147-notwit interchangeable / 264 dummy item 3 pol-not-cons interchangeable / 1231 dum147-notpol interchangeable，也不是已经策略就已经是共识 interchangeable / 144 policy interchangeable。**  
   官方写：看见 txid 没变，不是 wtxid 已经没变，也不是紧凑块已经一样快。

3. **看见隔离见证 / 看见隔离见证已经开 / 这份开是 not already 已经交差 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1230 dum147-notwit interchangeable / 1229 dum147-notany interchangeable，也不是已经紧凑块宣布就已经收到 interchangeable / 36 compact interchangeable。**  
   官方把仍改 wtxid、仍伤紧凑块写成独立动机。看见隔离见证，不是已经交差。

激活日程、版本位编号是规范里的取值，本页不抄。不要另写怎样改 dummy 撞身份。

## 官方为什么这样拆

- **隔离见证已经开 不是已经没有 dummy 延展：** 官方把本页这条仍会改 wtxid 写成独立动机。
- **txid 没变 不是 wtxid 已经没变：** 官方把 txid 固定和 wtxid 固定写成两件。
- **隔离见证 不是已经交差：** 官方把开了隔离见证和已经交差写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没有延展 | 不是已经没有 dummy 延展 | 不是已经是共识（144） |
| wtxid 没变 | 不是 wtxid 已经没变 | 不是已经收到（36） |
| 交差 | 不是已经交差 | 不是已经随便填（1229） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-147 segwit not already no-dummy-malleation / not already wtxid-fixed / not already settled 正式三事（264 余量），必须分开是不是已经没有 dummy 延展、是不是 wtxid 已经没变、是不是已经交差。可以跳过「看见多重签验过就已经不可延展」。不要另写怎样改 dummy 撞身份。264 dummy vs empty bundled unbundling 在本页 item 2 续；续 [`worked-example-dum147-notpol-vs-bundled.md`](worked-example-dum147-notpol-vs-bundled.md)（不变量 1231 item 3）。

## 本页不抄

- 激活时间、版本位编号、部署名、参考客户端版本号。
- 怎样造非空 dummy、怎样把非兼容签改成兼容、怎样靠改 dummy 挡紧凑块。
