# 例：看见 collects txs from mempool in order of priority / creates header 不是已经 raw proposal bundled interchangeable；看见 PrepareProposal call is synchronous 不是已经能在返回后再改裁决 interchangeable；看见 Application can manipulate transactions 不是已经 Prepare 改列表 bundled interchangeable

**层次**：实现 / PrepareProposal When collect / synchronous / manipulate 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「collect priority / synchronous / manipulate 不是 raw proposal bundled interchangeable / 不是 Process 同步 interchangeable / 不是 Prepare 改列表 bundled interchangeable」，不是 validValue 跳过 Prepare（356），也不是 Prepare Usage raw proposal（503）。不要另写怎样从池子收交易、怎样造头、怎样改 Prepare 列表。

## 官方三件事

规范把 PrepareProposal When 里收池造头 / 同步调用 / 应用可改列表写成三件独立的实现事，不是「看见自己是提议者就已经 raw proposal bundled interchangeable、已经能在返回后再改裁决、已经 Prepare 改列表 bundled interchangeable」一件事：

1. **看见 CometBFT collects outstanding transactions from mempool in order of priority / creates a block header / calls PrepareProposal with the newly generated block / 看见从池子按优先级收未决交易、造头、再调 Prepare 不是已经 preliminary raw proposal bundled（503） interchangeable / 已经整池可见 interchangeable，也不是已经 validValue 非 nil 跳过 Prepare（356） interchangeable / 已经又从池子收了一遍 interchangeable，也不是已经 MaxBytes=-1 就没有上限（299） interchangeable。**  
   官方 When 写：CometBFT collects outstanding transactions from _p_'s mempool. The transactions will be collected in order of priority. _p_'s CometBFT creates a block header. _p_'s CometBFT calls `PrepareProposal` with the newly generated block...。看见 collects in order of priority，不是已经 PrepareProposalRequest.txs 是 preliminary raw proposal（503 Usage） interchangeable——503 钉 Usage raw proposal 单句，本页钉 When 侧收池按优先级造头。看见 newly generated block，不是已经 validValue 非 nil 直接当提案（356） interchangeable——356 钉 validValue 跳过，本页钉 When 侧 collect + header + call。看见从池子收交易，不是已经整池都给 Prepare 就没有上限（299） interchangeable。
2. **看见 The call is synchronous: CometBFT's execution will block until the Application returns from the call / 看见 PrepareProposal 调用是同步的、引擎会等到应用返回 不是已经能在返回之后再改裁决 interchangeable / 已经离开关键路径 interchangeable，也不是已经 Process 调用是同步的（354） interchangeable / 已经 async 了还能 Reject interchangeable，也不是已经 Prepare 没有确定性要求（338） interchangeable / 已经可以在返回后再改扩展 interchangeable。**  
   官方 When 写：The call is synchronous: CometBFT's execution will block until the Application returns from the call。看见 blocks until returns，不是已经 Process 调用是同步的（354） interchangeable——354 钉 Process When 同步，本页钉 Prepare When 同步单句。看见 synchronous Prepare call，不是已经能在返回之后再改 PrepareProposalResponse interchangeable。看见引擎在等回包，不是已经离开关键路径（327） interchangeable——327 钉 immediate execution 快路径，本页钉 When 侧 synchronous 语义。
3. **看见 The Application can manipulate transactions: leave untouched / add / remove / modify / reorder / MAY fully execute and produce candidate state / MAY use vote extensions in commit info / 看见应用可以改列表 不是已经 Prepare 改列表 consequences bundled（355） interchangeable / 已经从内存池删掉 interchangeable / 已经进了内存池 interchangeable，也不是已经候选已经是 ExecuteTxState（311） interchangeable / 已经交差 interchangeable，也不是已经 +2/3 之后才进来的扩展 bundled（352） interchangeable / 已经 Verify 过 interchangeable。**  
   官方 When 写：The Application can manipulate transactions: leave transactions untouched; add new transactions; remove transactions from the proposal (but not from the mempool); modify transactions; reorder transactions. The Application MAY fully execute the block and produce a candidate state. The Application MAY use the vote extensions in the commit info to modify the proposal。看见 can manipulate transactions，不是已经 Prepare 改列表 consequences bundled（355） interchangeable——355 钉拿掉/加入/改追踪性，本页钉 When 侧 manipulate 能力单句。看见 MAY fully execute candidate，不是已经候选已经是 ExecuteTxState（311） interchangeable——311 钉 Requirements 侧候选，本页钉 When 侧 MAY immediate execution 单句。看见 MAY use vote extensions in commit info，不是已经 +2/3 之后才进来的扩展 bundled（352） interchangeable——352 钉迟到扩展，本页钉 When 侧 MAY use extensions 单句。

怎样做从池子收交易、怎样造头、怎样改 Prepare 列表、怎样缓存候选是规范里的做法，本页不抄。validValue 跳过 Prepare（356）、Prepare Usage raw proposal（503）、Prepare 改列表 consequences（355）是另外那套，本页不抄。

## 官方为什么这样拆

- **collect priority / create header ≠ raw proposal bundled interchangeable：** 官方把 When 侧收池造头单句和 Usage raw proposal bundled 分开。
- **synchronous Prepare call ≠ 能在返回后再改裁决 interchangeable：** 官方把 Prepare When 同步单句和 Process 同步 / 离开关键路径 bundled 分开。
- **can manipulate transactions ≠ Prepare 改列表 bundled interchangeable：** 官方把 When 侧 manipulate 能力单句和改列表 consequences bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| collects in priority order / creates header | 不是 raw proposal bundled（503） | 不是 validValue 跳过 Prepare（356） |
| synchronous Prepare call | 不是能在返回后再改裁决 | 不是 Process 调用是同步的（354） |
| can manipulate transactions | 不是 Prepare 改列表 bundled（355） | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事，必须分开 collects priority / creates header 是不是 raw proposal bundled interchangeable、PrepareProposal synchronous call 是不是能在返回后再改裁决 interchangeable、can manipulate transactions 是不是 Prepare 改列表 bundled interchangeable / 已经候选交差 interchangeable。可以跳过「看见自己是提议者就已经 raw proposal bundled interchangeable、已经能在返回后再改裁决、已经 Prepare 改列表 bundled interchangeable」。505 PrepareProposal When collect bundled unbundling 完成（1310 item 1 / 1311 item 2 / 1312 item 3）；精读 [`worked-example-prepwhen-notprio-vs-bundled.md`](worked-example-prepwhen-notprio-vs-bundled.md)（不变量 1310 item 1）、[`worked-example-prepwhen-notsync-vs-bundled.md`](worked-example-prepwhen-notsync-vs-bundled.md)（不变量 1311 item 2）、[`worked-example-prepwhen-notmanip-vs-bundled.md`](worked-example-prepwhen-notmanip-vs-bundled.md)（不变量 1312 item 3）。不要另写怎样从池子收交易、怎样改 Prepare 列表。

## 本页不抄

- 怎样做从池子收交易、怎样造头、怎样改 Prepare 列表、怎样缓存候选。
- validValue 跳过 Prepare。那是不变量 356。
- Prepare Usage raw proposal / MUST remove。那是不变量 503。
- Prepare 改列表 consequences。那是不变量 355。
- +2/3 之后才进来的扩展。那是不变量 352。
