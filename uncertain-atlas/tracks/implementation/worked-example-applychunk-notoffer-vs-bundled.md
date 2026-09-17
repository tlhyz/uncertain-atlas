# 例：看见 ApplySnapshotChunk 回包 result 是装这块的结果 is not already Offer result interchangeable / not already restored interchangeable / not already Apply Result enum interchangeable

**层次**：实现 / ApplySnapshotChunk 回包 result not Offer result / not already restored / not Apply Result enum 正式三事（397 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk 回包 result not Offer result / not already restored / not Apply Result enum 正式三事（397 余量）/ not 742 applychunk-notoffer interchangeable / not 397 applychunk-vs-loadchunk bundled interchangeable」，不是 ApplySnapshotChunk 请求 bundled（397），也不是 OfferSnapshot 回包 result 就已经装完（396 / 738）或 Apply Result 枚举（398 / 719–721）。不要另写怎样写 ApplySnapshotChunk 请求。

## 官方三件事

1. **看见 ApplySnapshotChunk 回包 `result` 是装这块的结果 / 看见回了 result / 装这块的结果 is not already 已经是 OfferSnapshot 那份 Offer 的结果 interchangeable / 396 / 738 offersnapreq-notrestored interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 742 applychunk-notoffer interchangeable / 740 applychunk-notload interchangeable / 397 applychunk item 1 chunk interchangeable，也不是已经 result not Offer result / not already restored / not Apply Result enum 正式三事 bundled（397 item 3 余量） interchangeable / 397 applychunk item 3 interchangeable。**  
   官方写：`result` 是装这块的结果。看见回了 result，不是已经是 OfferSnapshot 那份 Offer 的结果 interchangeable——本页从 397 item 3 侧钉 not Offer result 单句。397 applychunk vs loadchunk bundled unbundling 在本页 item 3 完成。

2. **看见回了 result / 看见有结果 / 装这块的结果 is not already 已经 Offer 收下就已经装完 interchangeable / 321 offerrestored interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 742 applychunk-notoffer interchangeable / 397 applychunk item 2 sender interchangeable / 741 applychunk-notsenders interchangeable。**  
   官方把装这块的结果和已经装完分开——397 bundled 第三件事常与 321 混成「看见回了 result 就已经装完 interchangeable」，本页钉 not already restored 单句。

3. **看见回了 result / 看见能回 / 装这块的结果 is not already 已经 ApplySnapshotChunk Result 枚举 interchangeable / 398 / 719 applyretry-notrefetch interchangeable / 721 applyretry-notchunkresult interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 742 applychunk-notoffer interchangeable / 740 applychunk-notload interchangeable。**  
   官方把 397 侧装这块的结果和 398 Apply Result 枚举分开。看见能回，不是已经 719 / 721 interchangeable。397 applychunk vs loadchunk bundled unbundling 在本页 item 3 完成。

怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **result not Offer result ≠ 396 / 738 interchangeable：** 官方把装这块的结果和这次 Offer 的结果分开。
- **result not already restored ≠ 321 interchangeable：** 官方把有结果和已经装完分开。
- **result not Apply Result enum ≠ 398 / 719–721 interchangeable：** 官方把 397 侧装这块的结果和 398 枚举分开；397 applychunk vs loadchunk bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ApplySnapshotChunk 回包 result 是装这块的结果 | 不是已经是 Offer 的结果（396 / 738） | 不是 chunk（740/397 item 1） |
| 看见回了 result | 不是已经装完（321） | 不是 ApplySnapshotChunk 请求 bundled（397） |
| 看见能回 | 不是已经 Apply Result 枚举（398 / 719–721） | 不是 sender（741/397 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 回包 result not Offer result / not already restored / not Apply Result enum 正式三事（397 余量），必须分开 result 是不是已经是 Offer 的结果 interchangeable / 396 / 738、是不是已经装完 interchangeable / 321、是不是已经 Apply Result 枚举 interchangeable / 398。可以跳过「看见回了 result 就已经是 Offer 的结果」。不要另写怎样写 ApplySnapshotChunk 请求。397 applychunk vs loadchunk bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender。
- ApplySnapshotChunk 请求 bundled。那是不变量 397。
- ApplySnapshotChunk 请求 chunk。那是不变量 397 item 1 余量 / 740。
- ApplySnapshotChunk 请求 sender。那是不变量 397 item 2 余量 / 741。
- OfferSnapshot 回包 result 就已经装完。那是不变量 396 / 738。
- Offer 收下就已经装完。那是不变量 321。
- ApplySnapshotChunk Result 枚举。那是不变量 398 / 719–721。
