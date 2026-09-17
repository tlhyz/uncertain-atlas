# 例：看见 Used during state sync to retrieve snapshot chunks from peers 不是已经 LoadSnapshotChunk height/format/chunk bundled（375） interchangeable；看见 retrieve snapshot chunks from peers 不是已经 ListSnapshots discover on peers（500） interchangeable；看见 retrieve chunks from peers 不是已经 ApplySnapshotChunk chunk 是 LoadSnapshotChunk 回包（397） interchangeable

**层次**：实现 / LoadSnapshotChunk Usage retrieve 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Used during state sync to retrieve snapshot chunks from peers 不是 LoadSnapshotChunk bundled interchangeable / 不是 ListSnapshots discover interchangeable / 不是 ApplySnapshotChunk 已经在装 interchangeable」，不是 LoadSnapshotChunk height/format/chunk bundled（375），也不是 ListSnapshots Usage discover（500）。不要另写怎样写 LoadSnapshotChunk、怎样切块。

## 官方三件事

规范把 LoadSnapshotChunk Methods Usage 单句写成三件独立的实现事，不是「看见 LoadSnapshotChunk Usage 了就已经 height/format/chunk bundled interchangeable、已经 discover interchangeable、已经 Apply 了 interchangeable」一件事：

1. **看见 Used during state sync to retrieve snapshot chunks from peers / 看见在 state sync 时从邻居拉快照块 不是已经 LoadSnapshotChunk 请求用 height / format / chunk（从 0 起）认这块 bundled（375） interchangeable，也不是已经 LoadSnapshotChunk 回包块含元数据不能超过 16 MB bundled（375） interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable，也不是已经 Transition to Consensus 已经切进共识（323） interchangeable。**  
   官方 Usage 写：Used during state sync to retrieve snapshot chunks from peers。看见 during state sync retrieve，不是已经 LoadSnapshotChunk bundled（375） interchangeable——375 钉 Request/Response 栏和 Usage 拉块 bundled 三事，本页钉 Methods Usage retrieve 单句。看见 retrieve snapshot chunks from peers，不是已经 Offer 收下之后 bundled（401）第一件事 bundled 就代表已经齐 interchangeable——401 钉 Accept 后拉块装块，本页钉 Usage 侧 retrieve from peers 语义。看见 used during state sync，不是已经 Transition to Consensus 已经能出块 interchangeable——323 钉切进共识，本页钉 Usage state sync 语境。
2. **看见 retrieve snapshot chunks from peers / 看见从邻居拉块 不是已经 ListSnapshots Used during state sync to discover on peers（500） interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / 已经本地清单 interchangeable，也不是已经 Snapshot Discovery 问了邻居就已经齐（322） interchangeable，也不是已经 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 bundled（395 第三件事） interchangeable。**  
   官方 Usage 写：retrieve snapshot chunks from peers。看见 retrieve from peers，不是已经 ListSnapshots Usage discover on peers（500） interchangeable——500 钉 ListSnapshots Usage discover 单句，本页钉 LoadSnapshotChunk Usage retrieve 单句。看见拉块，不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable——395 钉本地清单栏，本页钉 Usage 侧 retrieve 语义。看见 from peers，不是已经 Snapshot Discovery 问了邻居就已经齐（322） interchangeable——322 钉 app requirements Snapshot Discovery，本页钉 Methods LoadSnapshotChunk Usage 单句。
3. **看见 retrieve snapshot chunks / 看见拉块 不是已经 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 bundled（397） interchangeable，也不是已经 ApplySnapshotChunk Result ACCEPT 是这块收下了（401） interchangeable / 已经齐 interchangeable，也不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 bundled（375 第一件事） interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable。**  
   官方 Usage 写：retrieve snapshot chunks。看见 retrieve chunks，不是已经 ApplySnapshotChunk 请求 chunk 栏 bundled（397） interchangeable——397 钉 Request chunk 栏，本页钉 Usage retrieve 单句。看见 retrieve，不是已经 ApplySnapshotChunk Result ACCEPT（401） interchangeable——401 钉 Accept 后装块，本页钉 Usage 侧 retrieve 语义。看见 snapshot chunks from peers，不是已经 LoadSnapshotChunk bundled（375） interchangeable——375 钉 bundled 三事，本页钉 Methods Usage retrieve 单句。

怎样做 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。LoadSnapshotChunk bundled（375）、ListSnapshots Usage discover（500）、ApplySnapshotChunk chunk 栏（397）、Offer 收下之后 bundled（401）是另外那套，本页不抄。

## 官方为什么这样拆

- **Used during state sync to retrieve ≠ LoadSnapshotChunk bundled interchangeable：** 官方把 Methods Usage retrieve 单句和 Request/Response bundled 分开。
- **retrieve from peers ≠ ListSnapshots discover interchangeable：** 官方把 LoadSnapshotChunk Usage retrieve 和 ListSnapshots Usage discover 分开。
- **retrieve chunks ≠ ApplySnapshotChunk chunk 栏 interchangeable：** 官方把 Usage retrieve 和 ApplySnapshotChunk Request 栏 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Used during state sync to retrieve | 不是 LoadSnapshotChunk bundled（375） | 不是 Offer 收下之后 bundled（401） |
| retrieve from peers | 不是 ListSnapshots discover（500） | 不是 ListSnapshots 空请求 bundled（395） |
| retrieve snapshot chunks | 不是 ApplySnapshotChunk chunk 栏（397） | 不是 LoadSnapshotChunk bundled 已经齐（375） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve 正式三事，必须分开 Used during state sync to retrieve 是不是 LoadSnapshotChunk bundled interchangeable / 已经装完 / 已经切进共识、retrieve from peers 是不是 ListSnapshots discover interchangeable / 已经本地清单 / 已经问了邻居就齐、retrieve snapshot chunks 是不是 ApplySnapshotChunk chunk 栏 interchangeable / 已经齐 / 已经 ACCEPT。可以跳过「看见 LoadSnapshotChunk Usage 了就已经 bundled interchangeable、已经 discover interchangeable、已经 Apply 了 interchangeable」。不要另写怎样写 LoadSnapshotChunk、怎样切块。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- LoadSnapshotChunk bundled。那是不变量 375。
- ListSnapshots Usage discover。那是不变量 500。
- ApplySnapshotChunk chunk 栏。那是不变量 397。
- Offer 收下之后 bundled。那是不变量 401。
