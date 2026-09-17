# 例：看见 height 是过错发生的高度、time 是那一高已提交块的时间 is not already verified time interchangeable / not already settled interchangeable / not already +2/3 interchangeable

**层次**：实现 / height/time not already verified time / not already settled / not already +2/3 正式三事（372 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「height/time not already verified time / not already settled / not already +2/3 正式三事（372 余量）/ not 810 misbehavior-nottime interchangeable / not 372 misbehavior-vs-enum bundled interchangeable」，不是 Misbehavior bundled（372），也不是票上 Timestamp 就已经验过（304），也不是 InitChain time 就已经过了 genesis_time（387/767），也不是 ProcessProposal time 就已经验过票上时间（420）。不要另写怎样写 Misbehavior。

## 官方三件事

1. **看见 `height` 是过错发生的高度、`time` 是那一高已提交块的时间 / 看见有时间 / 这份时间 is not already 已经验过这个时间 interchangeable / 304 votetime interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 810 misbehavior-nottime interchangeable / 809 misbehavior-notslashed interchangeable / 372 misbehavior item 1 type interchangeable，也不是已经 height/time not already verified time / not already settled / not already +2/3 正式三事 bundled（372 item 2 余量） interchangeable / 372 misbehavior item 2 interchangeable。**  
   官方写：`height` 是过错发生的高度。`time` 是那一高已提交块的时间戳。看见有高度，不是已经验过票上的时间 interchangeable——本页从 372 item 2 侧钉 not already verified time 单句。372 misbehavior vs enum bundled unbundling 在本页 item 2 续。

2. **看见有时间 / 看见有高度 / 这份时间 is not already 已经交差 interchangeable / 304 votetime interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 810 misbehavior-nottime interchangeable / 372 misbehavior item 3 总权 interchangeable / 811 misbehavior-notreward interchangeable，也不是已经 InitChain time 就已经过了 genesis_time interchangeable / 387 inittime / 767 inittime-notgenesis interchangeable，也不是已经 ProcessProposal time 就已经验过票上时间 interchangeable / 420 procreqrest interchangeable。**  
   官方把有高度和已经交差分开——372 bundled 第二件事常与 304 / 387 / 420 混成「看见有时间就已经验过或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见有时间 / 看见对上了高度 / 这份时间 is not already 已经是本高 +2/3 interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 810 misbehavior-nottime interchangeable / 809 misbehavior-notslashed interchangeable。**  
   官方把对上了高度和已经是本高 +2/3 分开。看见对上了高度，不是已经是本高 +2/3 interchangeable。372 misbehavior vs enum bundled unbundling 在本页 item 2 续。

怎样编 Misbehavior、怎样填枚举、怎样算总权是规范里的做法，本页不抄。

## 官方为什么这样拆

- **height/time not already verified time ≠ 304 interchangeable：** 官方把过错高度 / 已提交块时间和票上时间已经验过分开。
- **看见有高度 not already settled ≠ 已经交差 interchangeable：** 官方把有高度和已经交差分开。
- **看见对上了高度 not already +2/3 ≠ 已经是本高 +2/3 interchangeable：** 官方把对上了高度和已经是本高 +2/3 分开；372 misbehavior vs enum bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| height 是过错发生的高度、time 是那一高已提交块的时间 | 不是已经验过这个时间（304） | 不是 type 枚举（809/372 item 1） |
| 看见有时间 | 不是已经交差 | 不是 InitChain time（387/767） |
| 看见对上了高度 | 不是已经是本高 +2/3 | 不是 ProcessProposal time（420） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height/time not already verified time / not already settled / not already +2/3 正式三事（372 余量），必须分开是不是已经验过这个时间 interchangeable / 304、是不是已经交差、是不是已经是本高 +2/3。可以跳过「看见有时间就已经验过」。不要另写怎样写 Misbehavior。372 misbehavior vs enum bundled unbundling 在本页 item 2 续；续 [`worked-example-misbehavior-notreward-vs-bundled.md`](worked-example-misbehavior-notreward-vs-bundled.md)（不变量 811 item 3）。

## 本页不抄

- 怎样编 Misbehavior、怎样填枚举、怎样算总权。
- Misbehavior bundled。那是不变量 372。
- type 枚举。那是不变量 372 item 1 余量 / 809。
- 票上 Timestamp 就已经验过。那是不变量 304。
- InitChain time 就已经过了 genesis_time。那是不变量 387 / 767。
