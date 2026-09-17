# 例：看见 Used during state sync to retrieve is not already LoadSnapshotChunk bundled（375） interchangeable / Offer 装完（321/401） interchangeable / Transition to Consensus（323） interchangeable

**层次**：实现 / LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事（501 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事（501 余量）/ not 658 loadsnapusage-notretrieve interchangeable / not 501 loadsnapusage retrieve bundled interchangeable」，不是 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501），也不是 LoadSnapshotChunk height/format/chunk bundled（375）。不要另写怎样写 LoadSnapshotChunk、怎样切块。

## 官方三件事

规范把 LoadSnapshotChunk Usage 里 Used during state sync to retrieve snapshot chunks from peers 和「已经是 LoadSnapshotChunk height/format/chunk bundled（375） interchangeable / 已经是 Offer 收下就已经装完（321） interchangeable / 已经是 Transition to Consensus 已经切进共识（323） interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 Used during state sync to retrieve 就已经 LoadSnapshotChunk bundled interchangeable / 就已经 Offer 装完 interchangeable / 就已经 Transition interchangeable / 就已经齐 interchangeable」一件事：

1. **看见 Used during state sync to retrieve snapshot chunks from peers / 看见在 state sync 时从邻居拉快照块 is not already 已经 LoadSnapshotChunk 请求用 height / format / chunk（从 0 起）认这块 bundled（375） interchangeable / 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable / 已经 LoadSnapshotChunk 回包块含元数据不能超过 16 MB bundled（375） interchangeable / 378 applysnap interchangeable / 397 ApplySnapshotChunk chunk 栏 interchangeable / 已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 bundled（375 第一件事） interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable，也不是已经 Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事 bundled（501 item 1 余量） interchangeable / 501 loadsnapusage retrieve item 1 interchangeable，也不是已经 retrieve from peers not ListSnapshots discover bundled（501 item 2 余量） interchangeable / 500 listsnapusage-discover interchangeable / 395 listsnap bundled interchangeable。**  
   官方 Usage 写：Used during state sync to retrieve snapshot chunks from peers。看见 during state sync retrieve，不是已经 LoadSnapshotChunk bundled（375） interchangeable——375 钉 Request/Response 栏和 Usage 拉块 bundled 三事，本页从 501 item 1 侧钉 not LoadSnapshotChunk bundled 单句。看见 retrieve snapshot chunks from peers，不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 interchangeable——375 钉 bundled 第一件事，本页钉 Methods Usage retrieve 单句。看见 used during state sync，不是已经 ListSnapshots discover interchangeable——500 另钉 retrieve from peers not discover，本页钉 item 1 第一件事。501 loadsnapusage retrieve unbundling 在本页 item 1 启动。

2. **看见 Used during state sync to retrieve / during state sync retrieve snapshot chunks is not already 已经 Offer 收下就已经装完（321） interchangeable / 321 offerrestored interchangeable / Snapshot Restoration 装回 interchangeable / 已经 Offer 装完 interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage item 2 upon accepting retrieve and apply interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 401 offerafter interchangeable / 397 ApplySnapshotChunk chunk 栏 interchangeable / 398 Result 枚举 interchangeable / ApplySnapshotChunk Result ACCEPT 已经齐 interchangeable / 378 applysnap interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve item 1 Used during state sync to retrieve interchangeable / 647 offersnapusage-notlisted interchangeable / 649 offersnapusage-notreject interchangeable，也不是已经 Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事 bundled（501 item 1 余量） interchangeable / 483 offersnaptrust interchangeable / 652 offersnaptrust-nottransition interchangeable，也不是已经 Transition to Consensus 已经切进共识（323） interchangeable / 323 transition interchangeable / 370 infover interchangeable。**  
   官方把 Usage retrieve 单句和 Offer 装完路径分开——501 bundled 第一件事常与 321/401 混成「看见 Used during state sync to retrieve 就已经 Offer 装完 interchangeable / 就已经 Accept 后拉块并装 interchangeable」，本页钉 not Offer 装完 单句。看见 during state sync retrieve，不是已经 Offer 收下就已经装完 interchangeable——321 钉 Snapshot Restoration 装回，本页钉 Methods Usage retrieve 单句。看见 retrieve snapshot chunks from peers，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装，本页钉 item 1 第二件事。

3. **看见 used during state sync / Used during state sync to retrieve is not already 已经 Transition to Consensus 已经切进共识（323） interchangeable / 323 transition interchangeable / 370 infover interchangeable / 652 offersnaptrust-nottransition interchangeable / 321 offerrestored interchangeable / 483 offersnaptrust item 4 verified AppHash at end interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve item 1 Used during state sync to retrieve interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage bundled interchangeable，也不是已经 Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事 bundled（501 item 1 余量） interchangeable / 501 loadsnapusage retrieve item 2 retrieve from peers interchangeable / 501 loadsnapusage retrieve item 3 retrieve chunks interchangeable，也不是已经 all chunks accepted 后 Info not Transition bundled（485） interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 654 applysnapusage-notinfo interchangeable / 653 applysnapusage-notverify interchangeable。**  
   官方把 Usage state sync retrieve 单句和 Transition to Consensus 路径分开——501 bundled 第一件事常与 323 混成「看见 Used during state sync to retrieve 就已经 Transition interchangeable / 就已经切进共识 interchangeable」，本页钉 not Transition to Consensus 单句。看见 used during state sync，不是已经 Transition to Consensus 已经能出块 interchangeable——323 钉切进共识，本页钉 Methods Usage retrieve 单句。看见 during state sync retrieve，不是已经 all chunks accepted 后 Info 对了就 Transition interchangeable——485/654 另钉 Info 路径，本页钉 item 1 第三件事。501 loadsnapusage retrieve unbundling 在本页 item 1 启动。

怎样做 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。LoadSnapshotChunk Usage retrieve 正式三事 bundled（501）、retrieve from peers not ListSnapshots discover（501 item 2 余量）、retrieve snapshot chunks not ApplySnapshotChunk chunk 栏（501 item 3 余量）、LoadSnapshotChunk bundled（375）、ListSnapshots Usage discover（500）、ApplySnapshotChunk chunk 栏（397）、Offer 收下之后拉块并装（401）、Transition to Consensus（323）是另外那套，本页不抄。

## 官方为什么这样拆

- **Used during state sync to retrieve not LoadSnapshotChunk bundled ≠ 375 loadsnap interchangeable：** 官方把 Methods Usage retrieve 单句和 Request/Response bundled 分开。
- **Used during state sync to retrieve not Offer 装完 ≠ 321/401 offerrestored/offerafter interchangeable：** 官方把 Usage retrieve 单句和 Offer 装完 / Accept 后拉块并装路径分开。
- **Used during state sync to retrieve not Transition to Consensus ≠ 323 transition interchangeable：** 官方把 Usage state sync 语境和 Transition to Consensus 路径分开；501 loadsnapusage retrieve unbundling 启动（658 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Used during state sync to retrieve | 不是 LoadSnapshotChunk bundled（375） | 不是 retrieve from peers / ListSnapshots discover（500） |
| during state sync retrieve | 不是 Offer 装完（321/401） | 不是 Offer 收下之后 bundled（401） |
| used during state sync | 不是 Transition to Consensus（323） | 不是 all chunks accepted 后 Info（485/654） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事（501 余量），必须分开 Used during state sync to retrieve 是不是 LoadSnapshotChunk bundled interchangeable / 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable / 378 applysnap interchangeable、during state sync retrieve 是不是 Offer 装完 interchangeable / 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable、used during state sync 是不是 Transition to Consensus interchangeable / 323 transition interchangeable / 370 infover interchangeable / 652 offersnaptrust-nottransition interchangeable。可以跳过「看见 Used during state sync to retrieve 就已经 LoadSnapshotChunk bundled interchangeable / 就已经 Offer 装完 interchangeable / 就已经 Transition interchangeable」。不要另写怎样写 LoadSnapshotChunk、怎样切块。501 loadsnapusage retrieve unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样做 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- LoadSnapshotChunk Usage retrieve 正式三事 bundled。那是不变量 501。
- retrieve from peers not ListSnapshots discover。那是不变量 501 item 2 余量。
- retrieve snapshot chunks not ApplySnapshotChunk chunk 栏。那是不变量 501 item 3 余量。
- LoadSnapshotChunk bundled。那是不变量 375。
- ListSnapshots Usage discover。那是不变量 500。
- ApplySnapshotChunk chunk 栏。那是不变量 397。
- Offer 收下之后拉块并装。那是不变量 401。
- Transition to Consensus。那是不变量 323。
