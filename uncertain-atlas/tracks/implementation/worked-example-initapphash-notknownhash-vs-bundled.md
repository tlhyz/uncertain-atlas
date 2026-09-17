# 例：看见 Finalize 请求 hash 是这块的哈希 is not already known header hash interchangeable / not already Process interchangeable / not already settled interchangeable

**层次**：实现 / Finalize 请求 hash not already known header hash / not already Process / not already settled 正式三事（392 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 请求 hash not already known header hash / not already Process / not already settled 正式三事（392 余量）/ not 756 initapphash-notknownhash interchangeable / not 392 initapphash-vs-header bundled interchangeable」，不是 InitChain 回包余栏 bundled（392），也不是 Prepare 没有头哈希就已经知道本头（311）。不要另写怎样写 InitChain 回包余栏。

## 官方三件事

1. **看见 Finalize 请求 `hash` 是这块的哈希 / 看见填了 hash / Finalize 这份块哈希 is not already 已经是 Prepare 那种还没有头哈希就已经知道本头 interchangeable / 311 knownhash interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 756 initapphash-notknownhash interchangeable / 755 initapphash-notheader interchangeable / 392 initapphash item 1 app_hash interchangeable，也不是已经 hash not already known header hash / not already Process / not already settled 正式三事 bundled（392 item 2 余量） interchangeable / 392 initapphash item 2 interchangeable。**  
   官方写：`hash` 是这块的哈希。看见填了 hash，不是已经是 Prepare 那种还没有头哈希就已经知道本头 interchangeable——本页从 392 item 2 侧钉 not already known header hash 单句。392 initapphash vs header bundled unbundling 在本页 item 2 续。

2. **看见填了 hash / 看见有块哈希 / Finalize 这份块哈希 is not already 已经是 height / time 对上拟议头那种已经知道本头哈希 interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 756 initapphash-notknownhash interchangeable / 392 initapphash item 3 CommitInfo.round interchangeable / 757 initapphash-notranked interchangeable。**  
   官方把这块的哈希和已经跑过 Process / 已经知道本头哈希分开——392 bundled 第二件事常与 311 混成「看见填了 hash 就已经知道本头 interchangeable」，本页钉 not already Process 单句。

3. **看见填了 hash / 看见能填 / Finalize 这份块哈希 is not already 已经交差 interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 756 initapphash-notknownhash interchangeable / 755 initapphash-notheader interchangeable。**  
   官方把能填 Finalize 请求 hash 和已经交差分开。看见能填，不是已经交差 interchangeable。392 initapphash vs header bundled unbundling 在本页 item 2 续。

怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮是规范里的做法，本页不抄。

## 官方为什么这样拆

- **hash not already known header hash ≠ 311 interchangeable：** 官方把这块的哈希和已经知道本头哈希分开。
- **hash not already Process ≠ 已经跑过 Process interchangeable：** 官方把有块哈希和 height / time 对上就已经知道本头分开。
- **hash not already settled ≠ 已经交差 interchangeable：** 官方把能填 hash 和已经交差分开；392 initapphash vs header bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 请求 hash 是这块的哈希 | 不是已经知道本头哈希（311） | 不是 InitChain 回包 app_hash（755/392 item 1） |
| 看见填了 hash | 不是已经跑过 Process | 不是 InitChain 回包余栏 bundled（392） |
| 看见能填 | 不是已经交差 | 不是 CommitInfo.round（757/392 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 请求 hash not already known header hash / not already Process / not already settled 正式三事（392 余量），必须分开 hash 是不是已经知道本头哈希 interchangeable / 311、是不是已经跑过 Process、是不是已经交差。可以跳过「看见填了 hash 就已经知道本头哈希」。不要另写怎样写 InitChain 回包余栏。392 initapphash vs header bundled unbundling 在本页 item 2 续；完成 [`worked-example-initapphash-notranked-vs-bundled.md`](worked-example-initapphash-notranked-vs-bundled.md)（不变量 757 item 3）。

## 本页不抄

- 怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮。
- InitChain 回包余栏 bundled。那是不变量 392。
- InitChain 回包 app_hash。那是不变量 392 item 1 余量 / 755。
- CommitInfo.round。那是不变量 392 item 3 余量 / 757。
- Prepare 没有头哈希就已经知道本头。那是不变量 311。
