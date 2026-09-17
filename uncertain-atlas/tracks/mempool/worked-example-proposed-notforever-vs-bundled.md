# 例：看见 CheckTx 过了 is not already in-block interchangeable / not already settled interchangeable / not already forever-valid interchangeable

**层次**：共识 / CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事（301 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事（301 余量）/ not 994 proposed-notforever interchangeable / not 301 proposed-vs-removed bundled interchangeable」，不是内存池交接 bundled（301），也不是 CheckTx 振荡就已经是永远绿（328），也不是弱 CheckTx 就已经挡住拜占庭提案（339）。不要另写怎样加锁、怎样 flush、怎样再验。

## 官方三件事

1. **看见 CheckTx 过了 / 看见进了池 这份交接 is not already 已经进块 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 994 proposed-notforever interchangeable / 992 proposed-notdel interchangeable / 301 proposed item 1 提案收了 interchangeable，也不是已经 CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事 bundled（301 item 3 余量） interchangeable / 301 proposed item 3 interchangeable。**  
   官方写：进池前要先让应用验。有效性可以随应用状态变。某一状态绿了，后来可以变红。看见 CheckTx 过了，不是已经进块 interchangeable——本页从 301 item 3 侧钉 not already in-block 单句。301 proposed vs removed bundled unbundling 在本页 item 3 完成。

2. **看见进了池 / 看见曾经绿过 / 这份交接 is not already 已经结算 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 994 proposed-notforever interchangeable / 301 proposed item 2 commit 后再验 interchangeable / 993 proposed-notrecheck interchangeable，也不是已经 CheckTx 振荡就已经是永远绿 interchangeable / 328 oscillate interchangeable。**  
   官方把进了池和已经结算分开。看见进了池，不是已经结算 interchangeable。本页钉 not already settled 单句。

3. **看见曾经绿过 / 看见 CheckTx 过了 / 这份交接 is not already 已经永远有效 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 994 proposed-notforever interchangeable / 992 proposed-notdel interchangeable，也不是已经弱 CheckTx 就已经挡住拜占庭提案 interchangeable / 339 checktx-weak interchangeable，也不是已经策略拒绝就已经共识非法 interchangeable / 144 policy interchangeable。**  
   官方把曾经绿过和已经永远有效分开。看见曾经绿过，不是已经永远有效 interchangeable。301 proposed vs removed bundled unbundling 在本页 item 3 完成。

实现名单、加锁、flush、再验次数是规范里的做法或取值，本页不抄。

## 官方为什么这样拆

- **CheckTx 过了 not already in-block ≠ 已经进块 interchangeable：** 官方把进池前的验和已经进块分开。
- **看见进了池 not already settled ≠ 已经结算 interchangeable：** 官方把进了池和已经结算分开。
- **看见曾经绿过 not already forever-valid ≠ 已经永远有效 interchangeable：** 官方把曾经绿过和已经永远有效分开；301 proposed vs removed bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 过了 | 不是已经进块 | 不是 CheckTx 振荡就已经是永远绿（328） |
| 看见进了池 | 不是已经结算 | 不是弱 CheckTx 就已经挡住拜占庭提案（339） |
| 看见曾经绿过 | 不是已经永远有效 | 不是策略拒绝就已经共识非法（144） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事（301 余量），必须分开是不是已经进块、是不是已经结算、是不是已经永远有效。可以跳过「看见提案收了就已经从池里拿走」。不要另写怎样加锁、怎样 flush、怎样再验。301 proposed vs removed bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 实现名单、加锁、flush、再验次数。
- 内存池交接 bundled。那是不变量 301。
- CheckTx 振荡就已经是永远绿。那是不变量 328。
- 弱 CheckTx 就已经挡住拜占庭提案。那是不变量 339。
- 策略拒绝就已经共识非法。那是不变量 144。
