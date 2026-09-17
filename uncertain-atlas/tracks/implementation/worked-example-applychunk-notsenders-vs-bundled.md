# 例：看见 ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID is not already reject_senders interchangeable / not already banned interchangeable / not already REJECT_SENDER interchangeable

**层次**：实现 / ApplySnapshotChunk 请求 sender not reject_senders / not already banned / not REJECT_SENDER 正式三事（397 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk 请求 sender not reject_senders / not already banned / not REJECT_SENDER 正式三事（397 余量）/ not 741 applychunk-notsenders interchangeable / not 397 applychunk-vs-loadchunk bundled interchangeable」，不是 ApplySnapshotChunk 请求 bundled（397），也不是 reject_senders 不论 Result 都拒这些人（378）或 Offer REJECT_SENDER（400 / 723）。不要另写怎样写 ApplySnapshotChunk 请求。

## 官方三件事

1. **看见 ApplySnapshotChunk 请求 `sender` 是送来这块的节点 P2P ID / 看见填了 sender / 送来这块的人 is not already 已经 `reject_senders` 不论 Result 都拒这些人 interchangeable / 378 refetch interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 741 applychunk-notsenders interchangeable / 740 applychunk-notload interchangeable / 397 applychunk item 1 chunk interchangeable，也不是已经 sender not reject_senders / not already banned / not REJECT_SENDER 正式三事 bundled（397 item 2 余量） interchangeable / 397 applychunk item 2 interchangeable。**  
   官方写：`sender` 是送来这块的节点 P2P ID。看见填了 sender，不是已经 `reject_senders` 不论 Result 都拒这些人 interchangeable——本页从 397 item 2 侧钉 not reject_senders 单句。397 applychunk vs loadchunk bundled unbundling 在本页 item 2 续。

2. **看见填了 sender / 看见有人 / 送来这块的人 is not already 已经封了 interchangeable / 378 refetch interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 741 applychunk-notsenders interchangeable / 397 applychunk item 3 result interchangeable / 742 applychunk-notoffer interchangeable。**  
   官方把送来这块的人和已经封了分开——397 bundled 第二件事常与 378 混成「看见填了 sender 就已经封了 interchangeable」，本页钉 not already banned 单句。

3. **看见填了 sender / 看见能填 / 送来这块的人 is not already 已经 OfferSnapshot Result `REJECT_SENDER` interchangeable / 400 / 723 offerfmt-notsenders interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 741 applychunk-notsenders interchangeable / 740 applychunk-notload interchangeable。**  
   官方把 397 侧送来这块的人和 400 REJECT_SENDER 分开。看见能填，不是已经 723 interchangeable。397 applychunk vs loadchunk bundled unbundling 在本页 item 2 续。

怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **sender not reject_senders ≠ 378 interchangeable：** 官方把送来这块的人和不论 Result 都拒这些人分开。
- **sender not already banned ≠ 378 interchangeable：** 官方把有人和已经封了分开。
- **sender not REJECT_SENDER ≠ 400 / 723 interchangeable：** 官方把 397 侧 sender 和 400 REJECT_SENDER 分开；397 applychunk vs loadchunk bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID | 不是已经拒了人（378） | 不是 chunk（740/397 item 1） |
| 看见填了 sender | 不是已经封了（378） | 不是 ApplySnapshotChunk 请求 bundled（397） |
| 看见能填 | 不是已经 REJECT_SENDER（400 / 723） | 不是回包 result（742/397 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 请求 sender not reject_senders / not already banned / not REJECT_SENDER 正式三事（397 余量），必须分开 sender 是不是已经拒了人 interchangeable / 378、是不是已经封了 interchangeable / 378、是不是已经 REJECT_SENDER interchangeable / 400 / 723。可以跳过「看见填了 sender 就已经拒了人」。不要另写怎样写 ApplySnapshotChunk 请求。397 applychunk vs loadchunk bundled unbundling 在本页 item 2 续；完成 [`worked-example-applychunk-notoffer-vs-bundled.md`](worked-example-applychunk-notoffer-vs-bundled.md)（不变量 742 item 3）。

## 本页不抄

- 怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender。
- ApplySnapshotChunk 请求 bundled。那是不变量 397。
- ApplySnapshotChunk 请求 chunk。那是不变量 397 item 1 余量 / 740。
- ApplySnapshotChunk 回包 result。那是不变量 397 item 3 余量 / 742。
- reject_senders 不论 Result 都拒这些人。那是不变量 378。
- OfferSnapshot Result REJECT_SENDER。那是不变量 400 / 723。
