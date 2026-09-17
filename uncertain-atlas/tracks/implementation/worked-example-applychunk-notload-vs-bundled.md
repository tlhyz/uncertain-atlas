# 例：看见 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 is not already loading chunks interchangeable / not already complete interchangeable / not already Usage retrieve interchangeable

**层次**：实现 / ApplySnapshotChunk 请求 chunk not already loading / not already complete / not Usage retrieve 正式三事（397 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk 请求 chunk not already loading / not already complete / not Usage retrieve 正式三事（397 余量）/ not 740 applychunk-notload interchangeable / not 397 applychunk-vs-loadchunk bundled interchangeable」，不是 ApplySnapshotChunk 请求 bundled（397），也不是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375）或 LoadSnapshotChunk Usage retrieve chunks（501 / 660）。不要另写怎样写 ApplySnapshotChunk 请求。

## 官方三件事

1. **看见 ApplySnapshotChunk 请求 `chunk` 是 LoadSnapshotChunk 回的那块二进制内容 / 看见填了 chunk / 装回这块 is not already 已经在从邻居拉快照块 interchangeable / 375 loadsnap interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 740 applychunk-notload interchangeable / 741 applychunk-notsenders interchangeable / 397 applychunk item 2 sender interchangeable，也不是已经 chunk not already loading / not already complete / not Usage retrieve 正式三事 bundled（397 item 1 余量） interchangeable / 397 applychunk item 1 interchangeable。**  
   官方写：`chunk` 是 `LoadSnapshotChunk` 回的那块二进制内容。看见填了 chunk，不是已经在从邻居拉快照块 interchangeable——本页从 397 item 1 侧钉 not already loading 单句。397 applychunk vs loadchunk bundled unbundling 在本页 item 1 启动。

2. **看见填了 chunk / 看见有这块 / 装回这块 is not already 已经齐 interchangeable / 375 loadsnap interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 740 applychunk-notload interchangeable / 397 applychunk item 3 result interchangeable / 742 applychunk-notoffer interchangeable。**  
   官方把装回这块和已经齐分开——397 bundled 第一件事常与 375 混成「看见填了 chunk 就已经齐 interchangeable」，本页钉 not already complete 单句。

3. **看见填了 chunk / 看见能填 / 装回这块 is not already 已经 LoadSnapshotChunk Usage retrieve chunks interchangeable / 501 / 660 loadsnapusage-notchunks interchangeable，也不是已经 ApplySnapshotChunk 请求 bundled（397） interchangeable / 740 applychunk-notload interchangeable / 741 applychunk-notsenders interchangeable。**  
   官方把 397 侧装回这块和 501 Usage retrieve chunks 分开。看见能填，不是已经 660 interchangeable。397 applychunk vs loadchunk bundled unbundling 在本页 item 1 启动。

怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **chunk not already loading ≠ 375 interchangeable：** 官方把装回这块和拉这块分开。
- **chunk not already complete ≠ 375 interchangeable：** 官方把有这块和已经齐分开。
- **chunk not Usage retrieve ≠ 501 / 660 interchangeable：** 官方把 397 侧装回这块和 501 Usage retrieve 分开；397 applychunk vs loadchunk bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 | 不是已经在拉块（375） | 不是 sender（741/397 item 2） |
| 看见填了 chunk | 不是已经齐（375） | 不是 ApplySnapshotChunk 请求 bundled（397） |
| 看见能填 | 不是已经 Usage retrieve（501 / 660） | 不是回包 result（742/397 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 请求 chunk not already loading / not already complete / not Usage retrieve 正式三事（397 余量），必须分开 chunk 是不是已经在拉块 interchangeable / 375、是不是已经齐 interchangeable / 375、是不是已经 Usage retrieve interchangeable / 501 / 660。可以跳过「看见填了 chunk 就已经在拉块」。不要另写怎样写 ApplySnapshotChunk 请求。397 applychunk vs loadchunk bundled unbundling 在本页 item 1 启动；续 [`worked-example-applychunk-notsenders-vs-bundled.md`](worked-example-applychunk-notsenders-vs-bundled.md)（不变量 741 item 2）。

## 本页不抄

- 怎样写 ApplySnapshotChunk 请求、怎样填 chunk、怎样填 sender。
- ApplySnapshotChunk 请求 bundled。那是不变量 397。
- ApplySnapshotChunk 请求 sender。那是不变量 397 item 2 余量 / 741。
- ApplySnapshotChunk 回包 result。那是不变量 397 item 3 余量 / 742。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
- LoadSnapshotChunk Usage retrieve chunks。那是不变量 501 / 660。
