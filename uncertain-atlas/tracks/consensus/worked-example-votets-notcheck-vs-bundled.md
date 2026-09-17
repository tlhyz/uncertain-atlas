# 例：看见票或提案带了 Timestamp is not already checked interchangeable / not already enforced interchangeable / not already required interchangeable

**层次**：共识 / 带了 Timestamp not already checked / not already enforced / not already required 正式三事（304 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应课文**：[L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「带了 Timestamp not already checked / not already enforced / not already required 正式三事（304 余量）/ not 998 votets-notcheck interchangeable / not 304 vote-ts-vs-checked bundled interchangeable」，不是签字校验 bundled（304），也不是块时间必须点名算法（40），也不是同一高度换轮就已经换了集合（302/995）。不要另写怎样记上次签过的高度轮类型。本页不写 amnesia 分类。

## 官方三件事

1. **看见票或提案带了 Timestamp / 看见字段在 这份校验 is not already 已经验过这个时间 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 998 votets-notcheck interchangeable / 999 votets-notevid interchangeable / 304 vote item 2 冲突提案 interchangeable，也不是已经带了 Timestamp not already checked / not already enforced / not already required 正式三事 bundled（304 item 1 余量） interchangeable / 304 vote item 1 interchangeable。**  
   官方写：收到的 Proposal 或 Vote 上的时间戳，目前没有校验。一般期望验证者填自己的本地钟，也期望同一人严格单调，但这两句都没有强制。看见字段在，不是已经验过 interchangeable——本页从 304 item 1 侧钉 not already checked 单句。304 vote-ts vs checked bundled unbundling 在本页 item 1 启动。

2. **看见单调 / 看见字段在 / 这份校验 is not already 已经执行 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 998 votets-notcheck interchangeable / 304 vote item 3 断开 interchangeable / 1000 votets-notslash interchangeable，也不是已经块时间必须点名算法 interchangeable / 40 block-time interchangeable。**  
   官方把单调期望和已经执行分开。看见单调，不是已经执行 interchangeable。本页钉 not already enforced 单句。

3. **看见 BFT Time 会用 precommit 的时间去算下一块 / 看见 PBTS 要求提案时间对上块时间 / 这份校验 is not already 票上的时间已经有要求 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 998 votets-notcheck interchangeable / 999 votets-notevid interchangeable，也不是已经同一高度换轮就已经换了集合 interchangeable / 302/995 roundset-notset interchangeable。**  
   官方把 BFT Time / PBTS 用时间和收到时已经验过分开。看见会用来算下一块，不是收到时已经验过 interchangeable。304 vote-ts vs checked bundled unbundling 在本页 item 1 启动。

类型字节、链号长度、可恢复签编码是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **带了 Timestamp not already checked ≠ 已经验过这个时间 interchangeable：** 官方把字段在和收到时没有校验分开。
- **看见单调 not already enforced ≠ 已经执行 interchangeable：** 官方把单调期望和已经执行分开。
- **看见会用来算下一块 not already required ≠ 票上的时间已经有要求 interchangeable：** 官方把 BFT Time / PBTS 用时间和收到时已经验过分开；304 vote-ts vs checked bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收到的时间戳 | 不是已经验过 | 不是块时间必须点名算法（40） |
| 看见单调 | 不是已经执行 | 不是同一高度换轮就已经换了集合（302/995） |
| 看见会用来算下一块 | 不是票上的时间已经有要求 | 不是冲突提案就已经有证据（999） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看带了 Timestamp not already checked / not already enforced / not already required 正式三事（304 余量），必须分开是不是已经验过、是不是已经执行、是不是票上的时间已经有要求。可以跳过「看见签过就已经验过时间」。不要另写怎样记上次签过的高度轮类型。不要写 amnesia 分类。304 vote-ts vs checked bundled unbundling 在本页 item 1 启动；续 [`worked-example-votets-notevid-vs-bundled.md`](worked-example-votets-notevid-vs-bundled.md)（不变量 999 item 2）。

## 本页不抄

- 类型字节、链号长度、可恢复签编码、1 ms 增量。
- 签字校验 bundled。那是不变量 304。
- 块时间必须点名算法。那是不变量 40。
- 同一高度换轮就已经换了集合。那是不变量 302/995。
- amnesia 分类、解锁谓词。
