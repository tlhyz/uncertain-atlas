# 例：看见 ApplySnapshotChunk Result RETRY_SNAPSHOT is not already switched snapshot interchangeable / not already restored interchangeable / not already Offer accepted interchangeable

**层次**：实现 / ApplySnapshotChunk Result RETRY_SNAPSHOT not switched / not restored / not Offer accepted 正式三事（398 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Result RETRY_SNAPSHOT not switched / not restored / not Offer accepted 正式三事（398 余量）/ not 720 applyretry-notswitch interchangeable / not 398 applyretry-vs-refetch bundled interchangeable」，不是 ApplySnapshotChunk 结果枚举 bundled（398），也不是拉失败换一份就已经能接着装（321）或 Offer 收下就已经装完（401）。不要另写怎样写 ApplySnapshotChunk 结果枚举。

## 官方三件事

1. **看见 ApplySnapshotChunk Result `RETRY_SNAPSHOT` 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块 / 看见回了 RETRY_SNAPSHOT / RETRY_SNAPSHOT is not already 已经拉失败换一份就已经能接着装 interchangeable / 321 offerrestored interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 720 applyretry-notswitch interchangeable / 719 applyretry-notrefetch interchangeable / 398 applyretry item 1 RETRY interchangeable，也不是已经 RETRY_SNAPSHOT not switched / not restored / not Offer accepted 正式三事 bundled（398 item 2 余量） interchangeable / 398 applyretry item 2 interchangeable。**  
   官方 Data Types 写：RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份，除非另有指令否则复用已拉块。看见回了 RETRY_SNAPSHOT，不是已经换一份就能接着装 interchangeable——本页从 398 item 2 侧钉 not switched 单句。398 applyretry vs refetch bundled unbundling 在本页 item 2 续。

2. **看见回了 RETRY_SNAPSHOT / 看见能重来这份 / RETRY_SNAPSHOT is not already 已经装完 interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 720 applyretry-notswitch interchangeable / 398 applyretry item 3 REJECT_SNAPSHOT interchangeable / 721 applyretry-notchunkresult interchangeable。**  
   官方把重来这份和已经装完分开——398 bundled 第二件事常与「看见能重来就已经装完 interchangeable」糊成一句，本页钉 not restored 单句。

3. **看见回了 RETRY_SNAPSHOT / 看见 Usage 这句 / RETRY_SNAPSHOT is not already 已经 Offer 收下就已经装完（321 / 401） interchangeable / 401 offerafter interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 720 applyretry-notswitch interchangeable / 719 applyretry-notrefetch interchangeable。**  
   官方把 Result RETRY_SNAPSHOT 重来这份和 Offer 收下就已经装完分开。看见能重来这份，不是已经 321 / 401 交差 interchangeable。398 applyretry vs refetch bundled unbundling 在本页 item 2 续。

怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **RETRY_SNAPSHOT not switched ≠ 321 interchangeable：** 官方把重来这份和换一份就能接着装分开。
- **RETRY_SNAPSHOT not restored ≠ 已经装完 interchangeable：** 官方把能重来这份和已经装完分开。
- **RETRY_SNAPSHOT not Offer accepted ≠ 321 / 401 interchangeable：** 官方把 Result RETRY_SNAPSHOT 和 Offer 收下就已经装完分开；398 applyretry vs refetch bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块 | 不是已经换一份就能接着装（321） | 不是 RETRY 再装这块（719/398 item 1） |
| 看见回了 RETRY_SNAPSHOT | 不是已经装完 | 不是 ApplySnapshotChunk 结果枚举 bundled（398） |
| 看见能重来这份 | 不是 Offer 收下就已经装完（321 / 401） | 不是 REJECT_SNAPSHOT 拒掉这份（721/398 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result RETRY_SNAPSHOT not switched / not restored / not Offer accepted 正式三事（398 余量），必须分开 RETRY_SNAPSHOT 是不是已经换一份就能接着装 interchangeable / 321、是不是已经装完、是不是 Offer 收下就已经装完 interchangeable / 401。可以跳过「看见回了 RETRY_SNAPSHOT 就已经换一份」。不要另写怎样写 ApplySnapshotChunk 结果枚举。398 applyretry vs refetch bundled unbundling 在本页 item 2 续；完成 [`worked-example-applyretry-notchunkresult-vs-bundled.md`](worked-example-applyretry-notchunkresult-vs-bundled.md)（不变量 721 item 3）。

## 本页不抄

- 怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT。
- ApplySnapshotChunk 结果枚举 bundled。那是不变量 398。
- RETRY 再装这块。那是不变量 398 item 1 余量 / 719。
- REJECT_SNAPSHOT 拒掉这份、换一份。那是不变量 398 item 3 余量 / 721。
- 拉失败换一份就已经能接着装。那是不变量 321。
- Offer 收下就已经装完。那是不变量 401。
