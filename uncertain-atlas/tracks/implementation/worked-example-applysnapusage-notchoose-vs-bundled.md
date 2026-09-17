# 例：看见 can choose refetch/ban is not already refetch_chunks bundled（378） interchangeable / reject_senders bundled（378） interchangeable / RETRY bundled（398） interchangeable

**层次**：实现 / ApplySnapshotChunk Usage can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事（502 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Usage can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事（502 余量）/ not 656 applysnapusage-notchoose interchangeable / not 657 applysnapusage-notunless interchangeable / not 502 applysnapusage refetch/ban bundled interchangeable」，不是 ApplySnapshotChunk Usage refetch/ban 正式二事 bundled（502），也不是 ApplySnapshotChunk 再拉 refetch/reject_senders（378）。不要另写怎样做增量验、怎样封邻居、怎样写 ApplySnapshotChunk。

## 官方三件事

规范把 ApplySnapshotChunk Usage 里 The application can choose to refetch chunks and/or ban P2P peers as appropriate 和「已经是 ApplySnapshotChunk 回包 refetch_chunks / reject_senders bundled（378） interchangeable / 已经是 ApplySnapshotChunk Result RETRY（398） bundled interchangeable / 已经是 Snapshot Verification 封邻居就没有快照 DoS（332） interchangeable / 已经是 unable to retrieve next chunk refetch 就齐（485） interchangeable」分开写成三件独立的实现事，不是「看见 can choose refetch/ban 就已经 refetch/ban bundled interchangeable / 就已经 RETRY interchangeable / 就已经封邻居就交差 interchangeable」一件事：

1. **看见 The application can choose to refetch chunks and/or ban P2P peers as appropriate / 看见应用可以按情况再拉块和/或封 P2P 邻居 is not already 已经 ApplySnapshotChunk 回包 `refetch_chunks` 不论 result 都再拉再装 bundled（378） interchangeable / 378 applysnap interchangeable / 397 ApplySnapshotChunk chunk 栏 interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable / 已经 ApplySnapshotChunk 再拉 bundled interchangeable / 已经 refetch 不论 result 都再拉 interchangeable，也不是已经 ApplySnapshotChunk Usage refetch/ban 正式二事 bundled（502） interchangeable / 656 applysnapusage-notchoose interchangeable / 502 applysnapusage refetch/ban interchangeable / 657 applysnapusage-notunless interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 655 applysnapusage-notunable interchangeable，也不是已经 can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事 bundled（502 item 1 余量） interchangeable / 502 applysnapusage refetch/ban item 1 interchangeable，也不是已经 unable to retrieve next chunk not refetch/reject_senders bundled（485 item 3 余量 / 655） interchangeable / 655 applysnapusage-notunable interchangeable / 649 offersnapusage-notreject interchangeable。**  
   官方 Usage 写：The application can choose to refetch chunks and/or ban P2P peers as appropriate。看见 can choose refetch and/or ban，不是已经 refetch_chunks 列了块号 bundled（378） interchangeable——378 钉 Response 栏 refetch_chunks，本页从 502 item 1 侧钉 not refetch_chunks bundled 单句。看见 choose refetch/ban，不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable——378 钉 refetch/reject_senders 应用指令，本页钉 Methods Usage can choose 单句。看见 as appropriate，不是已经 unable to retrieve next chunk refetch 就齐 interchangeable——655 另钉 not refetch/reject_senders on unable retrieve，本页钉 item 1 第一件事。502 applysnapusage refetch/ban unbundling 在本页 item 1 启动。

2. **看见 can choose refetch chunks and/or ban P2P peers / ban P2P peers as appropriate is not already 已经 ApplySnapshotChunk 回包 `reject_senders` 不论 Result 都拒这些人 bundled（378） interchangeable / 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 已经 ApplySnapshotChunk 回包 reject_senders 栏 interchangeable / 651 offersnaptrust-notverify item 3 avoid DoS interchangeable / 332 snapshotverify interchangeable / 已经 Snapshot Verification 封邻居就没有快照 DoS interchangeable，也不是已经 ApplySnapshotChunk Usage refetch/ban 正式二事 bundled（502） interchangeable / 656 applysnapusage-notchoose interchangeable / 657 applysnapusage-notunless interchangeable / 502 applysnapusage refetch/ban item 2 will not do unless instructed interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 655 applysnapusage-notunable interchangeable，也不是已经 can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事 bundled（502 item 1 余量） interchangeable / 483 offersnaptrust item 2 avoid DoS interchangeable / 649 offersnapusage-notreject interchangeable / 400 offerabort interchangeable，也不是已经 ApplySnapshotChunk Result REJECT_SENDER bundled（398） interchangeable / 398 applysnap-result interchangeable / 378 applysnap item 2 reject_senders interchangeable。**  
   官方把 Usage can choose ban P2P peers 单句和 Response 栏 reject_senders bundled 分开——502 bundled 第一件事常与 378 混成「看见 can choose refetch/ban 就已经 reject_senders 不论 Result 都拒这些人 interchangeable / 就已经封邻居就交差 interchangeable」，本页钉 not reject_senders bundled 单句。看见 ban P2P peers as appropriate，不是已经 reject_senders 拒了人 bundled（378） interchangeable——378 钉 Response 栏 reject_senders，本页钉 Usage 侧 can choose ban 语义。看见 choose refetch/ban，不是已经 Snapshot Verification 封邻居就没有快照 DoS（332） interchangeable——332 钉 app requirements 封邻居，本页钉 Methods Usage can choose 单句。

3. **看见 can choose refetch/ban / choose refetch chunks and/or ban P2P peers is not already 已经 ApplySnapshotChunk Result `RETRY` 是再装这块 bundled（398） interchangeable / 398 applysnap-result interchangeable / 397 chunk 栏 interchangeable / 已经 ApplySnapshotChunk Result 枚举 bundled interchangeable / 已经 RETRY 按需配合 RefetchChunks interchangeable / applyretry-sold-as-refetch interchangeable，也不是已经 ApplySnapshotChunk Usage refetch/ban 正式二事 bundled（502） interchangeable / 656 applysnapusage-notchoose interchangeable / 657 applysnapusage-notunless interchangeable / 502 applysnapusage refetch/ban item 2 will not do unless instructed interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 655 applysnapusage-notunable interchangeable，也不是已经 can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事 bundled（502 item 1 余量） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable，也不是已经 ApplySnapshotChunk Result REJECT_SNAPSHOT bundled（398） interchangeable / 649 offersnapusage-notreject interchangeable / 655 applysnapusage-notunable item 2 not REJECT_SNAPSHOT interchangeable。**  
   官方把 Usage can choose refetch/ban 单句和 ApplySnapshotChunk Result RETRY 枚举分开——502 bundled 第一件事常与 398 混成「看见 can choose refetch/ban 就已经 RETRY interchangeable / 就已经 ApplySnapshotChunk 回包 result 栏 interchangeable」，本页钉 not RETRY bundled 单句。看见 can choose refetch chunks，不是已经 ApplySnapshotChunk Result RETRY（398） interchangeable——398 钉 Result 枚举，本页钉 Usage can choose 单句。看见 choose refetch/ban，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装，本页钉 item 1 第三件事。

怎样做增量验、怎样封邻居、怎样写 ApplySnapshotChunk 是规范里的做法，本页不抄。ApplySnapshotChunk Usage refetch/ban 正式二事 bundled（502）、will not do unless instructed not engine auto refetch（502 item 2 余量 / 657）、ApplySnapshotChunk 再拉 refetch/reject_senders（378）、ApplySnapshotChunk Result RETRY/REJECT_SNAPSHOT（398）、ApplySnapshotChunk Usage verify/Info/unable（485）、unable to retrieve next chunk not refetch/reject_senders（485 item 3 余量 / 655）、Snapshot Verification 封邻居（332）是另外那套，本页不抄。

## 官方为什么这样拆

- **can choose refetch/ban not refetch_chunks bundled ≠ 378 applysnap interchangeable：** 官方把 Methods Usage can choose 单句和 Response 栏 refetch_chunks bundled 分开。
- **can choose refetch/ban not reject_senders bundled ≠ 378 applysnap reject_senders interchangeable：** 官方把 Usage can choose ban P2P peers 单句和 Response 栏 reject_senders bundled 分开。
- **can choose refetch/ban not RETRY bundled ≠ 398 applysnap-result interchangeable：** 官方把 Usage can choose refetch/ban 单句和 ApplySnapshotChunk Result RETRY 枚举分开；502 applysnapusage refetch/ban unbundling 启动（656 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| can choose refetch/ban | 不是 refetch_chunks bundled（378） | 不是 unable retrieve refetch（655） |
| can choose ban P2P peers | 不是 reject_senders bundled（378） | 不是 Snapshot Verification ban（332） |
| can choose refetch/ban | 不是 RETRY bundled（398） | 不是 REJECT_SNAPSHOT（649/655） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事（502 余量），必须分开 can choose refetch/ban 是不是 refetch_chunks bundled interchangeable / 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 375 LoadSnapshotChunk interchangeable、can choose ban P2P peers 是不是 reject_senders bundled interchangeable / 378 applysnap reject_senders interchangeable / 332 snapshotverify interchangeable / 651 offersnaptrust-notverify interchangeable、can choose refetch/ban 是不是 RETRY bundled interchangeable / 398 applysnap-result interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable。可以跳过「看见 can choose refetch/ban 就已经 refetch/ban bundled interchangeable / 就已经 RETRY interchangeable」。不要另写怎样做增量验、怎样封邻居。502 applysnapusage refetch/ban unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样写 ApplySnapshotChunk、怎样再拉。
- ApplySnapshotChunk Usage refetch/ban 正式二事 bundled。那是不变量 502。
- will not do unless instructed not engine auto refetch。那是不变量 502 item 2 余量 / 657。
- ApplySnapshotChunk 再拉 refetch/reject_senders。那是不变量 378。
- ApplySnapshotChunk Result RETRY/REJECT_SNAPSHOT。那是不变量 398。
- ApplySnapshotChunk Usage verify/Info/unable。那是不变量 485。
- unable to retrieve next chunk not refetch/reject_senders。那是不变量 485 item 3 余量 / 655。
- Snapshot Verification 封邻居。那是不变量 332。
