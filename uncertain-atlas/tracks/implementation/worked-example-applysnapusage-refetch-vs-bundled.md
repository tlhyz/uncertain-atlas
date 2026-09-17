# 例：看见 application can choose to refetch chunks and/or ban P2P peers as appropriate 不是已经 ApplySnapshotChunk refetch/ban bundled（378） interchangeable；看见 CometBFT will not do this unless instructed by the application 不是已经引擎自动 refetch / 已经封邻居 interchangeable

**层次**：实现 / ApplySnapshotChunk Usage refetch/ban 正式二事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「can choose refetch/ban 不是 refetch/ban bundled interchangeable / will not do unless instructed 不是引擎自动 refetch interchangeable」，不是 ApplySnapshotChunk 再拉 bundled（378），也不是 ApplySnapshotChunk Usage verify/Info/unable（485）。不要另写怎样做增量验、怎样封邻居、怎样写 ApplySnapshotChunk。

## 官方两件事

规范把 ApplySnapshotChunk Methods Usage 第一段写成两件独立的实现事，不是「看见 Apply 了 chunk 回包 refetch_chunks / reject_senders 就已经 refetch/ban bundled interchangeable、已经引擎自动 refetch interchangeable」一件事：

1. **看见 The application can choose to refetch chunks and/or ban P2P peers as appropriate / 看见应用可以按情况再拉块和/或封 P2P 邻居 不是已经 ApplySnapshotChunk 回包 `refetch_chunks` 不论 result 都再拉再装 bundled（378） interchangeable，也不是已经 ApplySnapshotChunk 回包 `reject_senders` 不论 Result 都拒这些人 bundled（378） interchangeable，也不是已经 ApplySnapshotChunk Result `RETRY` 是再装这块 bundled（398） interchangeable，也不是已经 Snapshot Verification 封禁邻居就没有快照 DoS（332） interchangeable，也不是已经 unable to retrieve next chunk refetch 就齐（485） interchangeable。**  
   官方 Usage 写：The application can choose to refetch chunks and/or ban P2P peers as appropriate。看见 can choose refetch and/or ban，不是已经 refetch_chunks 列了块号 bundled（378） interchangeable——378 钉 Response 栏 refetch_chunks，本页钉 Methods Usage can choose 单句。看见 ban P2P peers as appropriate，不是已经 reject_senders 拒了人 bundled（378） interchangeable——378 钉 Response 栏 reject_senders，本页钉 Usage 侧 can choose ban 语义。看见 choose refetch/ban，不是已经 ApplySnapshotChunk Result RETRY（398） interchangeable——398 钉 Result 枚举，本页钉 Usage can choose 单句。
2. **看见 CometBFT will not do this unless instructed by the application / 看见引擎不会自己做，除非应用下指令 不是已经 refetch_chunks 不论 result 都再拉再装 bundled（378） interchangeable / 已经引擎自动 refetch interchangeable，也不是已经 reject_senders 不论 Result 都拒这些人 bundled（378） interchangeable / 已经引擎自动封邻居 interchangeable，也不是已经 unable to retrieve next chunk 引擎 reject via OfferSnapshot（485） interchangeable / 已经应用 reset and accept or abort interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 已经齐 interchangeable。**  
   官方 Usage 写：CometBFT will not do this unless instructed by the application。看见 will not do this unless instructed，不是已经 refetch_chunks 列了块号 bundled（378） interchangeable——378 钉 refetch_chunks 行为，本页钉 Methods Usage unless instructed 单句。看见不会自己做，不是已经引擎 unable to retrieve next chunk 就 reject via OfferSnapshot interchangeable——485 钉 unable retrieve 换快照，本页钉 Usage 侧 unless instructed 语义。看见 unless instructed by the application，不是已经 ApplySnapshotChunk Result RETRY 按需配合 RefetchChunks bundled（398） interchangeable——398 钉 RETRY 枚举，本页钉 Usage unless instructed 单句。

怎样做增量验、怎样封邻居、怎样写 ApplySnapshotChunk 是规范里的做法，本页不抄。ApplySnapshotChunk 再拉 bundled（378）、ApplySnapshotChunk Result RETRY/REJECT_SNAPSHOT（398）、ApplySnapshotChunk Usage verify/Info/unable（485）、Snapshot Verification 封邻居（332）是另外那套，本页不抄。

## 官方为什么这样拆

- **can choose refetch/ban ≠ refetch/ban bundled interchangeable：** 官方把 Methods Usage can choose 单句和 Response 栏 refetch_chunks / reject_senders bundled 分开。
- **will not do unless instructed ≠ 引擎自动 refetch interchangeable：** 官方把 unless instructed 单句和 refetch_chunks / unable retrieve 行为 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| can choose refetch/ban | 不是 refetch/ban bundled（378） | 不是 RETRY/REJECT_SNAPSHOT（398） |
| will not do unless instructed | 不是引擎自动 refetch | 不是 unable retrieve → OfferSnapshot（485） |
| ApplySnapshotChunk Usage refetch/ban | 不是 verify each chunk | 不是 ApplySnapshotChunk Usage verify/Info/unable（485） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage refetch/ban 正式二事，必须分开 can choose refetch chunks and/or ban P2P peers 是不是 refetch/ban bundled interchangeable / 已经 RETRY interchangeable / 已经封邻居就交差、CometBFT will not do this unless instructed 是不是引擎自动 refetch interchangeable / 已经 unable retrieve 换快照 interchangeable / 已经齐。可以跳过「看见 Apply 了 chunk 回包 refetch_chunks 就已经 refetch/ban bundled interchangeable、已经引擎自动 refetch interchangeable」。不要另写怎样做增量验、怎样封邻居。502 applysnapusage refetch/ban unbundling 在本页 item 1 启动；精读 [`worked-example-applysnapusage-notchoose-vs-bundled.md`](worked-example-applysnapusage-notchoose-vs-bundled.md)（不变量 656 item 1）；完成 [`worked-example-applysnapusage-notunless-vs-bundled.md`](worked-example-applysnapusage-notunless-vs-bundled.md)（不变量 657 item 2）。502 applysnapusage refetch/ban unbundling 完成（656→657）。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样写 ApplySnapshotChunk、怎样再拉。
- ApplySnapshotChunk 再拉 bundled。那是不变量 378。
- ApplySnapshotChunk Result RETRY/REJECT_SNAPSHOT。那是不变量 398。
- ApplySnapshotChunk Usage verify/Info/unable。那是不变量 485。
- Snapshot Verification 封邻居。那是不变量 332。
