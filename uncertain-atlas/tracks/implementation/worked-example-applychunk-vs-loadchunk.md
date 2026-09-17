# 例：看见 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容不是已经在拉块；看见 ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID 不是已经拒了人；看见 ApplySnapshotChunk 回包 result 是装这块的结果不是已经是 Offer 的结果

**层次**：实现 / ApplySnapshotChunk 请求。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容不是已经在拉块 / ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID 不是已经拒了人 / ApplySnapshotChunk 回包 result 是装这块的结果不是已经是 Offer 的结果」，不是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐，也不是 reject_senders 就已经能接着装。不要另写怎样写 ApplySnapshotChunk 请求。

## 官方三件事

规范把 ApplySnapshotChunk 请求 `chunk` 是 LoadSnapshotChunk 回的那块二进制内容、请求 `sender` 是送来这块的节点 P2P ID、回包 `result` 是装这块的结果写成三件独立的实现事，不是「看见填了 ApplySnapshotChunk 请求就已经在拉块、已经拒了人、已经是 Offer 的结果」一件事：

1. **看见 ApplySnapshotChunk 请求 `chunk` 是 LoadSnapshotChunk 回的那块二进制内容 / 看见填了 chunk 不是已经在拉块，也不是已经齐。**  
   官方写：`chunk` 是 `LoadSnapshotChunk` 回的那块二进制内容。看见填了 chunk，不是已经在从邻居拉快照块。看见有这块，不是已经齐。看见能填，不是已经交差。
2. **看见 ApplySnapshotChunk 请求 `sender` 是送来这块的节点 P2P ID / 看见填了 sender 不是已经拒了人，也不是已经封了。**  
   官方写：`sender` 是送来这块的节点 P2P ID。看见填了 sender，不是已经 `reject_senders` 不论 Result 都拒这些人。看见有人，不是已经封了。看见能填，不是已经交差。
3. **看见 ApplySnapshotChunk 回包 `result` 是装这块的结果 / 看见回了 result 不是已经是 Offer 的结果，也不是已经装完。**  
   官方写：`result` 是装这块的结果。看见回了 result，不是已经是 OfferSnapshot 那份 Offer 的结果。看见有结果，不是已经 Offer 收下就已经装完。看见能回，不是已经交差。

怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender 是规范里的做法，本页不抄。LoadSnapshotChunk 用来从邻居拉快照块就已经齐是不变量 375，本页不抄。

## 官方为什么这样拆

- **ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 ≠ 已经在拉块：** 官方把装回这块和拉这块分开。
- **ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID ≠ 已经拒了人：** 官方把送来这块的人和拒这些人分开。
- **ApplySnapshotChunk 回包 result 是装这块的结果 ≠ 已经是 Offer 的结果：** 官方把装这块的结果和这次 Offer 的结果分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 | 不是已经在拉块 | 不是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） |
| ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID | 不是已经拒了人 | 不是 reject_senders 不论 Result 都拒这些人就已经能接着装（378） |
| ApplySnapshotChunk 回包 result 是装这块的结果 | 不是已经是 Offer 的结果 | 不是 OfferSnapshot 回包 result 是这次 Offer 的结果就已经装完（396） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ApplySnapshotChunk 请求就已经在拉块、已经拒了人、已经是 Offer 的结果」，必须分开 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容是不是已经在拉块、ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID 是不是已经拒了人、ApplySnapshotChunk 回包 result 是装这块的结果是不是已经是 Offer 的结果。可以跳过「看见填了 ApplySnapshotChunk 请求就已经在拉块」。不要另写怎样写 ApplySnapshotChunk 请求。397 applychunk vs loadchunk bundled unbundling 完成（740 item 1 / 741 item 2 / 742 item 3）；精读 [`worked-example-applychunk-notload-vs-bundled.md`](worked-example-applychunk-notload-vs-bundled.md)（不变量 740 item 1）。

## 本页不抄

- 怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
- reject_senders 不论 Result 都拒这些人就已经能接着装。那是不变量 378。
- OfferSnapshot 回包 result 是这次 Offer 的结果就已经装完。那是不变量 396。
