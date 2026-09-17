# 例：看见 Misbehavior.type 只是过错枚举 is not already slashed interchangeable / not already rewarded interchangeable / not already settled interchangeable

**层次**：实现 / Misbehavior.type not already slashed / not already rewarded / not already settled 正式三事（372 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Misbehavior.type not already slashed / not already rewarded / not already settled 正式三事（372 余量）/ not 809 misbehavior-notslashed interchangeable / not 372 misbehavior-vs-enum bundled interchangeable」，不是 Misbehavior bundled（372），也不是证据上链就已经罚没（21），也不是 Finalize misbehavior 就已经定奖惩（569），也不是 ProposalStatus UNKNOWN 就已经崩（376/713）。不要另写怎样写 Misbehavior。

## 官方三件事

1. **看见 `Misbehavior.type` 只是过错枚举 / 看见有类型 / 这份枚举 is not already 已经罚没 interchangeable / 21 evidence interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 809 misbehavior-notslashed interchangeable / 810 misbehavior-nottime interchangeable / 372 misbehavior item 2 height interchangeable，也不是已经 Misbehavior.type not already slashed / not already rewarded / not already settled 正式三事 bundled（372 item 1 余量） interchangeable / 372 misbehavior item 1 interchangeable。**  
   官方写：`type` 是可能过错的枚举。枚举里有 `UNKNOWN`、`DUPLICATE_VOTE`、`LIGHT_CLIENT_ATTACK`。看见有类型，不是已经罚没 interchangeable——本页从 372 item 1 侧钉 not already slashed 单句。372 misbehavior vs enum bundled unbundling 在本页 item 1 启动。

2. **看见有类型 / 看见写成双签 / 这份枚举 is not already 已经定了奖惩 interchangeable / 21 evidence interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 809 misbehavior-notslashed interchangeable / 372 misbehavior item 3 总权 interchangeable / 811 misbehavior-notreward interchangeable，也不是已经 Finalize misbehavior 就已经定奖惩 interchangeable / 569 finmisbeh-notvoteinfo interchangeable，也不是已经 ProposalStatus UNKNOWN 就已经崩 interchangeable / 376 propstatus / 713 propstatus-notunknown interchangeable。**  
   官方把写成双签和已经定了奖惩分开——372 bundled 第一件事常与 21 / 569 / 376 混成「看见有类型就已经罚没或已经定了奖惩 interchangeable」，本页钉 not already rewarded 单句。

3. **看见有类型 / 看见枚举在 / 这份枚举 is not already 已经交差 interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 809 misbehavior-notslashed interchangeable / 810 misbehavior-nottime interchangeable。**  
   官方把枚举在和已经交差分开。看见枚举在，不是已经交差 interchangeable。372 misbehavior vs enum bundled unbundling 在本页 item 1 启动。

怎样编 Misbehavior、怎样填枚举、怎样算总权是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Misbehavior.type not already slashed ≠ 21 interchangeable：** 官方把枚举种类和已经罚没分开。
- **看见写成双签 not already rewarded ≠ 已经定了奖惩 interchangeable：** 官方把写成双签和已经定了奖惩分开。
- **看见枚举在 not already settled ≠ 已经交差 interchangeable：** 官方把枚举在和已经交差分开；372 misbehavior vs enum bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Misbehavior.type 只是过错枚举 | 不是已经罚没（21） | 不是 height/time（810/372 item 2） |
| 看见有类型 | 不是已经定了奖惩 | 不是 Finalize misbehavior（569） |
| 看见枚举在 | 不是已经交差 | 不是 ProposalStatus UNKNOWN（376/713） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Misbehavior.type not already slashed / not already rewarded / not already settled 正式三事（372 余量），必须分开是不是已经罚没 interchangeable / 21、是不是已经定了奖惩、是不是已经交差。可以跳过「看见有类型就已经罚没」。不要另写怎样写 Misbehavior。372 misbehavior vs enum bundled unbundling 在本页 item 1 启动；续 [`worked-example-misbehavior-nottime-vs-bundled.md`](worked-example-misbehavior-nottime-vs-bundled.md)（不变量 810 item 2）。

## 本页不抄

- 怎样编 Misbehavior、怎样填枚举、怎样算总权。
- Misbehavior bundled。那是不变量 372。
- height / time。那是不变量 372 item 2 余量 / 810。
- 证据上链就已经罚没。那是不变量 21。
- Finalize misbehavior 就已经定奖惩。那是不变量 569。
