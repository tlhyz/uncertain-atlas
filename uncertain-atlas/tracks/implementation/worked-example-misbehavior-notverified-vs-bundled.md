# 例：看见有高度 / 看见有时间 / 看见对上了高度 is not already already verified interchangeable / already settled interchangeable / already plus23 interchangeable

**层次**：实现 / height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事（372 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事（372 余量）/ not 864 misbehavior-notverified interchangeable / not 372 misbehavior bundled interchangeable」，不是 misbehavior bundled（372），也不是 Misbehavior.type 只是过错枚举不是已经罚没（863 item 1 余量）或 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩（372 item 3 余量）。不要另写怎样写 Misbehavior。

## 官方三件事

规范把 Methods 里 `height` 是过错发生的高度、`time` 是那一高已提交块的时间 和「已经是有高度就已经验过票上的时间 interchangeable / 已经是有时间就已经交差 interchangeable / 已经是对上了高度就已经是本高 +2/3 interchangeable / 已经是 misbehavior bundled interchangeable」分开写成三件独立的实现事，不是「看见有高度就已经验过票上的时间 interchangeable / 就已经交差 interchangeable / 就已经是本高 +2/3 interchangeable」一件事：

1. **看见有高度 / 看见 `height` 是过错发生的高度 / 看见有高度 is not already 已经验过票上的时间 interchangeable / 已经 verified interchangeable / 已经验过票上的时间交差 interchangeable / 372 misbehavior bundled interchangeable / 304 Timestamp verified interchangeable / misbehavior-sold-as-enum interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 864 misbehavior-notverified interchangeable / 372 misbehavior item 2 interchangeable，也不是已经 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事 bundled（372 item 2 余量） interchangeable / 372 misbehavior item 2 interchangeable，也不是已经有类型就已经罚没（863） interchangeable / 21 evidence-slash interchangeable / 365 VoteInfo rewards interchangeable，也不是已经票上 Timestamp 就已经验过（304） interchangeable。**  
   官方写：`height` 是过错发生的高度。看见有高度，不是已经验过票上的时间。看见有高度，不是已经 verified interchangeable——372 钉 bundled 三事，本页从 item 2 侧钉 not already verified 单句。看见 `height` 是过错发生的高度，不是已经 misbehavior bundled（372） interchangeable——372 钉 bundled，本页钉 item 2 第一件事。看见有高度，不是已经有类型就已经罚没（863） interchangeable——863 另钉 item 1。372 misbehavior-vs-enum bundled unbundling 在本页 item 2 续。

2. **看见有时间 / 看见 `time` 是那一高已提交块的时间 / 看见有时间戳 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 372 misbehavior bundled interchangeable / 304 Timestamp verified interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 864 misbehavior-notverified interchangeable / 372 misbehavior item 1 罚没 interchangeable / 372 misbehavior item 3 按到场定奖惩 interchangeable，也不是已经 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事 bundled（372 item 2 余量） interchangeable / 372 misbehavior item 2 interchangeable，也不是已经验过票上的时间（本页第一件事） interchangeable。**  
   官方写：`time` 是那一高已提交块的时间戳。看见有时间，不是已经交差。看见有时间戳，不是已经 settled interchangeable——本页钉 not already settled 单句。看见有时间，不是已经验过票上的时间（本页第一件事） interchangeable——三件事分开钉。372 misbehavior-vs-enum bundled unbundling 在本页 item 2 续。

3. **看见对上了高度 / 看见高度对上 / 看见过错高度对上 is not already 已经是本高 +2/3 interchangeable / 已经 plus23 interchangeable / 已经是本高 +2/3 交差 interchangeable / 372 misbehavior bundled interchangeable / 148 LastCommit interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 864 misbehavior-notverified interchangeable / 372 misbehavior item 1 / 372 misbehavior item 3，也不是已经 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事 bundled（372 item 2 余量） interchangeable / 372 misbehavior item 2 interchangeable，也不是已经验过票上的时间（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见对上了高度，不是已经是本高 +2/3。看见高度对上，不是已经 plus23 interchangeable——本页钉 not already plus23 单句。看见过错高度对上，不是已经交差（本页第二件事） interchangeable——三件事分开钉。372 misbehavior-vs-enum bundled unbundling 在本页 item 2 续。

怎样编 Misbehavior、怎样填枚举、怎样算总权是规范里的做法，本页不抄。misbehavior bundled（372）、Misbehavior.type 只是过错枚举不是已经罚没（372 item 1 余量 / 863）、total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩（372 item 3 余量）、证据上链就已经罚没（21）、票上 Timestamp 就已经验过（304）、VoteInfo 能按到场定奖惩就已经罚没（365）、本头 LastCommit 就已经是本高 +2/3（148）是另外那套，本页不抄。

## 官方为什么这样拆

- **有高度 not already verified ≠ 372 / 304 interchangeable：** 官方把过错高度和已经验过票上的时间分开。
- **有时间 not already settled ≠ 已经交差 interchangeable：** 官方把已提交块时间和已经交差分开。
- **对上了高度 not already plus23 ≠ 已经是本高 +2/3 interchangeable：** 官方把过错高度对上和已经是本高 +2/3 分开；372 misbehavior-vs-enum bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有高度 | 不是 already verified | 不是票上 Timestamp 就已经验过 alone（304） |
| 有时间 | 不是 already settled | 不是有类型 already slashed alone（863） |
| 对上了高度 | 不是 already plus23 | 不是本头 LastCommit 就已经是本高 +2/3 alone（148） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事（372 余量），必须分开有高度 是不是 already verified interchangeable / 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable、有时间 是不是 already settled interchangeable、对上了高度 是不是 already plus23 interchangeable。可以跳过「看见有高度就已经验过票上的时间 interchangeable / 就已经交差 interchangeable / 就已经是本高 +2/3 interchangeable」。不要另写怎样写 Misbehavior。372 misbehavior-vs-enum bundled unbundling 在本页 item 2 续（863 + 864）。

## 本页不抄

- 怎样编 Misbehavior、怎样填枚举、怎样算总权。
- misbehavior bundled。那是不变量 372。
- Misbehavior.type 只是过错枚举不是已经罚没。那是不变量 372 item 1 余量 / 863。
- total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩。那是不变量 372 item 3 余量。
- 证据上链就已经罚没。那是不变量 21。
- 票上 Timestamp 就已经验过。那是不变量 304。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
- 本头 LastCommit 就已经是本高 +2/3。那是不变量 148。
