# 例：看见冲突提案 is not already evidence interchangeable / not already object interchangeable / not already exists interchangeable

**层次**：共识 / 冲突提案 not already evidence / not already object / not already exists 正式三事（304 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应课文**：[L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「冲突提案 not already evidence / not already object / not already exists 正式三事（304 余量）/ not 999 votets-notevid interchangeable / not 304 vote-ts-vs-checked bundled interchangeable」，不是签字校验 bundled（304），也不是双签证据已经通知应用（21），也不是先装证据就已经装满交易（299/989）。不要另写怎样记上次签过的高度轮类型。本页不写 amnesia 分类。

## 官方三件事

1. **看见冲突提案 / 看见双签证据机制 这份校验 is not already 已经有提案证据 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 999 votets-notevid interchangeable / 998 votets-notcheck interchangeable / 304 vote item 1 Timestamp interchangeable，也不是已经冲突提案 not already evidence / not already object / not already exists 正式三事 bundled（304 item 2 余量） interchangeable / 304 vote item 2 interchangeable。**  
   官方写：引擎能公布冲突票的证据，好让应用罚。冲突提案目前没有证据，以后也许有。看见能交双签证据，不是提案冲突已经能交 interchangeable——本页从 304 item 2 侧钉 not already evidence 单句。304 vote-ts vs checked bundled unbundling 在本页 item 2 续。

2. **看见两份提案 / 看见冲突 / 这份校验 is not already 已经有对象 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 999 votets-notevid interchangeable / 304 vote item 3 断开 interchangeable / 1000 votets-notslash interchangeable，也不是已经双签证据已经通知应用 interchangeable / 21 evidence notify interchangeable。**  
   官方把两份提案和已经有对象分开。看见两份提案，不是已经有对象 interchangeable。本页钉 not already object 单句。

3. **看见「以后也许有」 / 看见冲突 / 这份校验 is not already 已经有 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 999 votets-notevid interchangeable / 998 votets-notcheck interchangeable，也不是已经先装证据就已经装满交易 interchangeable / 299/989 evidreap-notfull interchangeable。**  
   官方把「以后也许有」和已经有分开。看见「以后也许有」，不是已经有 interchangeable。304 vote-ts vs checked bundled unbundling 在本页 item 2 续。

类型字节、链号长度、可恢复签编码是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **冲突提案 not already evidence ≠ 已经有提案证据 interchangeable：** 官方把票的证据和提案的证据分开。
- **看见两份提案 not already object ≠ 已经有对象 interchangeable：** 官方把两份提案和已经有对象分开。
- **看见「以后也许有」 not already exists ≠ 已经有 interchangeable：** 官方把「以后也许有」和已经有分开；304 vote-ts vs checked bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 冲突提案 | 不是已经有证据 | 不是双签证据已经通知应用（21） |
| 看见两份提案 | 不是已经有对象 | 不是先装证据就已经装满交易（299/989） |
| 看见「以后也许有」 | 不是已经有 | 不是断开就已经罚了（1000） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看冲突提案 not already evidence / not already object / not already exists 正式三事（304 余量），必须分开是不是已经有提案证据、是不是已经有对象、是不是已经有。可以跳过「看见签过就已经验过时间」。不要另写怎样记上次签过的高度轮类型。不要写 amnesia 分类。304 vote-ts vs checked bundled unbundling 在本页 item 2 续；续 [`worked-example-votets-notslash-vs-bundled.md`](worked-example-votets-notslash-vs-bundled.md)（不变量 1000 item 3）。

## 本页不抄

- 类型字节、链号长度、可恢复签编码、1 ms 增量。
- 签字校验 bundled。那是不变量 304。
- 双签证据已经通知应用。那是不变量 21。
- 先装证据就已经装满交易。那是不变量 299/989。
- amnesia 分类、解锁谓词。
