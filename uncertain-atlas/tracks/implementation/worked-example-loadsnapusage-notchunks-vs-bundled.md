# 例：看见 retrieve snapshot chunks is not already ApplySnapshotChunk chunk 栏 bundled（397） interchangeable / ACCEPT bundled（401） interchangeable / LoadSnapshotChunk 已经齐（375/483） interchangeable

**层次**：实现 / LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事（501 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事（501 余量）/ not 660 loadsnapusage-notchunks interchangeable / not 659 loadsnapusage-notdiscover interchangeable / not 658 loadsnapusage-notretrieve interchangeable / not 501 loadsnapusage retrieve bundled interchangeable」，不是 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501），也不是 ApplySnapshotChunk chunk 栏 bundled（397）。不要另写怎样做 LoadSnapshotChunk、怎样切块、怎样写 ApplySnapshotChunk。

## 官方三件事

规范把 LoadSnapshotChunk Usage 里 retrieve snapshot chunks 和「已经是 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 bundled（397） interchangeable / 已经是 ApplySnapshotChunk Result ACCEPT 是这块收下了（401） interchangeable / 已经齐 interchangeable / 已经是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 bundled（375 第一件事） interchangeable / 已经是 Only AppHash can be trusted（483） interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 retrieve snapshot chunks 就已经 ApplySnapshotChunk chunk 栏 interchangeable / 就已经 ACCEPT interchangeable / 就已经 LoadSnapshotChunk 已经齐 interchangeable / 就已经 Only AppHash interchangeable / 就已经齐 interchangeable」一件事：

1. **看见 retrieve snapshot chunks / 看见拉块 is not already 已经 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 bundled（397） interchangeable / 397 applysnap-chunk interchangeable / applychunk-sold-as-loadchunk interchangeable / 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 已经 ApplySnapshotChunk 请求 chunk 栏 interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage item 2 upon accepting retrieve and apply interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 660 loadsnapusage-notchunks interchangeable / 659 loadsnapusage-notdiscover interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve interchangeable / 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable，也不是已经 retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事 bundled（501 item 3 余量） interchangeable / 501 loadsnapusage retrieve item 3 interchangeable，也不是已经 retrieve from peers not ListSnapshots discover（501 item 2 余量 / 659） interchangeable / 659 loadsnapusage-notdiscover interchangeable / 500 listsnapusage-discover interchangeable。**  
   官方 Usage 写：retrieve snapshot chunks。看见 retrieve chunks，不是已经 ApplySnapshotChunk 请求 chunk 栏 bundled（397） interchangeable——397 钉 Request chunk 栏，本页从 501 item 3 侧钉 not ApplySnapshotChunk chunk 栏 单句。看见拉块，不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable——378 钉 refetch/reject_senders 应用指令，本页钉 Methods Usage retrieve 单句。看见 retrieve snapshot chunks，不是已经 retrieve from peers not ListSnapshots discover interchangeable——659 另钉 item 2，本页钉 item 3 第一件事。501 loadsnapusage retrieve unbundling 在本页 item 3 续。

2. **看见 retrieve snapshot chunks / retrieve chunks is not already 已经 ApplySnapshotChunk Result ACCEPT 是这块收下了（401） interchangeable / 401 offerafter interchangeable / ApplySnapshotChunk Result ACCEPT 已经齐 interchangeable / 398 applysnap-result interchangeable / 398 Result 枚举 interchangeable / 已经 Offer 收下之后 bundled（401） interchangeable / 648 offersnapusage-notrestored interchangeable / applyaccept-sold-as-restored interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 660 loadsnapusage-notchunks interchangeable / 659 loadsnapusage-notdiscover interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve item 3 retrieve snapshot chunks interchangeable / 378 applysnap interchangeable / 485 applysnapusage verify/Info/unable interchangeable，也不是已经 retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事 bundled（501 item 3 余量） interchangeable / 321 offerrestored interchangeable / 323 transition interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable，也不是已经 ApplySnapshotChunk chunk 栏 bundled（397） interchangeable / 397 applysnap-chunk interchangeable / 378 applysnap item 1 refetch_chunks interchangeable。**  
   官方把 Usage retrieve chunks 单句和 ApplySnapshotChunk Result ACCEPT 枚举分开——501 bundled 第三件事常与 401 混成「看见 retrieve snapshot chunks 就已经 ACCEPT interchangeable / 就已经 Offer 收下之后 bundled interchangeable / 就已经齐 interchangeable」，本页钉 not ACCEPT bundled 单句。看见 retrieve chunks，不是已经 ApplySnapshotChunk Result ACCEPT（401） interchangeable——401 钉 Accept 后装块，本页钉 Usage retrieve 单句。看见 retrieve snapshot chunks，不是已经 all chunks accepted 后 Info 对了就 Transition interchangeable——485/654 另钉 Info 路径，本页钉 item 3 第二件事。

3. **看见 retrieve snapshot chunks / snapshot chunks from peers is not already 已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 bundled（375 第一件事） interchangeable / 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable / 已经 LoadSnapshotChunk height/format/chunk bundled（375） interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve item 1 Used during state sync to retrieve interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable / 483 offersnaptrust interchangeable / 651 offersnaptrust-notverify interchangeable / 650 offersnaptrust-notmetadata interchangeable / 38 apphash-trust interchangeable / 332 snapshotverify interchangeable / 653 applysnapusage-notverify interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 660 loadsnapusage-notchunks interchangeable / 659 loadsnapusage-notdiscover interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve item 3 retrieve snapshot chunks interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage bundled interchangeable，也不是已经 retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事 bundled（501 item 3 余量） interchangeable / 397 applysnap-chunk interchangeable / 401 offerafter interchangeable / 378 applysnap interchangeable，也不是已经 retrieve from peers not ListSnapshots discover（659） interchangeable / 659 loadsnapusage-notdiscover interchangeable / 500 listsnapusage-discover interchangeable。**  
   官方把 Usage retrieve chunks 单句和 LoadSnapshotChunk bundled / Only AppHash 路径分开——501 bundled 第三件事常与 375/483 混成「看见 retrieve snapshot chunks 就已经 LoadSnapshotChunk 已经齐 interchangeable / 就已经 Only AppHash 可信任就交差 interchangeable」，本页钉 not LoadSnapshotChunk 已经齐 单句。看见 snapshot chunks from peers，不是已经 LoadSnapshotChunk bundled（375） interchangeable——375 钉 bundled 三事，本页钉 Methods Usage retrieve 单句。看见 retrieve snapshot chunks，不是已经 Only AppHash can be trusted interchangeable——483 钉 OfferSnapshot Usage Only AppHash，本页钉 item 3 第三件事。501 loadsnapusage retrieve unbundling 在本页 item 3 完成。

怎样做 LoadSnapshotChunk、怎样切块、怎样写 ApplySnapshotChunk 是规范里的做法，本页不抄。LoadSnapshotChunk Usage retrieve 正式三事 bundled（501）、Used during state sync to retrieve not LoadSnapshotChunk bundled（501 item 1 余量 / 658）、retrieve from peers not ListSnapshots discover（501 item 2 余量 / 659）、ApplySnapshotChunk chunk 栏 bundled（397）、Offer 收下之后拉块并装（401）、LoadSnapshotChunk bundled（375）、Only AppHash can be trusted（483）是另外那套，本页不抄。

## 官方为什么这样拆

- **retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 ≠ 397 applysnap-chunk interchangeable：** 官方把 Methods Usage retrieve 单句和 ApplySnapshotChunk Request chunk 栏 bundled 分开。
- **retrieve snapshot chunks not ACCEPT bundled ≠ 401 offerafter interchangeable：** 官方把 Usage retrieve chunks 单句和 ApplySnapshotChunk Result ACCEPT 枚举分开。
- **retrieve snapshot chunks not LoadSnapshotChunk 已经齐 ≠ 375/483 loadsnap/offersnaptrust interchangeable：** 官方把 Usage retrieve chunks 单句和 LoadSnapshotChunk bundled / Only AppHash 路径分开；501 loadsnapusage retrieve unbundling 完成（660 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| retrieve snapshot chunks | 不是 ApplySnapshotChunk chunk 栏（397） | 不是 ApplySnapshotChunk 再拉（378） |
| retrieve chunks | 不是 ACCEPT bundled（401） | 不是 all chunks accepted 后 Info（485/654） |
| snapshot chunks from peers | 不是 LoadSnapshotChunk 已经齐（375） | 不是 Only AppHash can be trusted（483） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事（501 余量），必须分开 retrieve snapshot chunks 是不是 ApplySnapshotChunk chunk 栏 interchangeable / 397 applysnap-chunk interchangeable / applychunk-sold-as-loadchunk interchangeable / 378 applysnap interchangeable、retrieve chunks 是不是 ACCEPT bundled interchangeable / 401 offerafter interchangeable / 398 applysnap-result interchangeable / 648 offersnapusage-notrestored interchangeable、snapshot chunks from peers 是不是 LoadSnapshotChunk 已经齐 interchangeable / 375 loadsnap interchangeable / 483 offersnaptrust interchangeable / 653 applysnapusage-notverify interchangeable / 332 snapshotverify interchangeable。可以跳过「看见 retrieve snapshot chunks 就已经 ApplySnapshotChunk chunk 栏 interchangeable / 就已经 ACCEPT interchangeable / 就已经 LoadSnapshotChunk 已经齐 interchangeable」。不要另写怎样做 LoadSnapshotChunk、怎样写 ApplySnapshotChunk。501 loadsnapusage retrieve unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做 LoadSnapshotChunk、怎样切块、怎样写 ApplySnapshotChunk、怎样再拉。
- LoadSnapshotChunk Usage retrieve 正式三事 bundled。那是不变量 501。
- Used during state sync to retrieve not LoadSnapshotChunk bundled。那是不变量 501 item 1 余量 / 658。
- retrieve from peers not ListSnapshots discover。那是不变量 501 item 2 余量 / 659。
- ApplySnapshotChunk chunk 栏 bundled。那是不变量 397。
- Offer 收下之后拉块并装。那是不变量 401。
- LoadSnapshotChunk bundled。那是不变量 375。
- Only AppHash can be trusted。那是不变量 483。
