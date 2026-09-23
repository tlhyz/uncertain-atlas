# 例：看见本块不提 / 看见拿掉了 / 看见回包没有它 is not already already out-of-pool interchangeable / already never-propose interchangeable / already settled interchangeable

**层次**：实现 / 从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事（355 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事（355 余量）/ not 818 drop-notmempool interchangeable / not 355 preparedrop bundled interchangeable」，不是 Prepare 改列表 bundled（355），也不是往提案加了一笔新的不是已经进了内存池（819 item 2 余量）或把 t1 改成 t2 不是已经还能按 t1 查到（820 item 3 余量）。不要另写怎样改 Prepare 列表。

## 官方三件事

规范把 Methods 里应用若认为这笔不该进本块就不要写进 `PrepareProposalResponse.txs`、这不会把它从内存池删掉、只是推迟 和「已经是本块不提就已经出池 interchangeable / 已经是拿掉了就已经永远不提 interchangeable / 已经是回包没有它就已经交差 interchangeable / 已经是 preparedrop bundled interchangeable」分开写成三件独立的实现事，不是「看见本块不提就已经从池里删掉 interchangeable / 就已经永远不提 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见从提案拿掉 tx / 看见本块不提 / 看见回包没有它 is not already 已经从内存池删掉 interchangeable / 已经 out-of-pool interchangeable / 已经出池交差 interchangeable / 355 preparedrop bundled interchangeable / 301 proposed-removed interchangeable / preparedrop-sold-as-evicted interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 818 drop-notmempool interchangeable / 355 preparedrop item 1 interchangeable，也不是已经从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事 bundled（355 item 1 余量） interchangeable / 355 preparedrop item 1 interchangeable，也不是已经进了内存池（819） interchangeable / 820 retarget-nottraceable interchangeable / 33 fourgates interchangeable，也不是已经提案收了就已经从池里删掉（301） interchangeable。**  
   官方写：应用若认为这笔不该进本块，就不要写进 `PrepareProposalResponse.txs`。这**不会**把它从内存池删掉，只是推迟。看见本块不提，不是已经出池。看见本块不提，不是已经 out-of-pool interchangeable——355 钉 bundled 三事，本页从 item 1 侧钉 not already out-of-pool 单句。看见从提案拿掉 tx，不是已经 Prepare 改列表 bundled（355） interchangeable——355 钉 bundled，本页钉 item 1 第一件事。看见本块不提，不是已经进了内存池（819） interchangeable——819 另钉 item 2。看见本块不提，不是已经提案收了就已经从池里删掉（301） interchangeable——301 另钉。355 preparedrop vs mempool bundled unbundling 在本页 item 1 启动。

2. **看见拿掉了 / 看见本块不提这笔 / 看见没写进回包 is not already 已经永远不提 interchangeable / 已经 never-propose interchangeable / 已经永远不提交差 interchangeable / 355 preparedrop bundled interchangeable / 301 proposed-removed interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 818 drop-notmempool interchangeable / 355 preparedrop item 2 加新 interchangeable / 355 preparedrop item 3 改笔 interchangeable，也不是已经从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事 bundled（355 item 1 余量） interchangeable / 355 preparedrop item 1 interchangeable，也不是已经出池（本页第一件事） interchangeable。**  
   官方写：看见拿掉了，不是已经永远不提。看见本块不提这笔，不是已经 never-propose interchangeable——本页钉 not already never-propose 单句。看见没写进回包，不是已经出池（本页第一件事） interchangeable——三件事分开钉。355 preparedrop vs mempool bundled unbundling 在本页 item 1 启动。

3. **看见回包没有它 / 看见回包里没这笔 / 看见没写进 txs is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 355 preparedrop bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 818 drop-notmempool interchangeable / 355 preparedrop item 2 / 355 preparedrop item 3，也不是已经从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事 bundled（355 item 1 余量） interchangeable / 355 preparedrop item 1 interchangeable，也不是已经出池（本页第一件事） interchangeable / 已经永远不提（本页第二件事） interchangeable。**  
   官方写：看见回包没有它，不是已经交差。看见回包里没这笔，不是已经 settled interchangeable——本页钉 not already settled 单句。看见没写进 txs，不是已经永远不提（本页第二件事） interchangeable——三件事分开钉。355 preparedrop vs mempool bundled unbundling 在本页 item 1 启动。

怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池是规范里的做法，本页不抄。Prepare 改列表 bundled（355）、往提案加了一笔新的不是已经进了内存池（355 item 2 余量 / 819）、把 t1 改成 t2 不是已经还能按 t1 查到（355 item 3 余量 / 820）、提案收了就已经从池里删掉（301）、整池可见就已经只能看见装得进一块的子集（345）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **本块不提 not already out-of-pool ≠ 355 / 301 interchangeable：** 官方把本块不提和出池分开。
- **拿掉了 not already never-propose ≠ 已经永远不提 interchangeable：** 官方把拿掉了和已经永远不提分开。
- **回包没有它 not already settled ≠ 已经交差 interchangeable：** 官方把回包没有它和已经交差分开；355 preparedrop vs mempool bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本块不提 | 不是 already out-of-pool | 不是提案收了就已经从池里删掉 alone（301） |
| 拿掉了 | 不是 already never-propose | 不是往提案加新 already in-pool alone（819） |
| 回包没有它 | 不是 already settled | 不是改笔 already t1-lookup alone（820） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事（355 余量），必须分开本块不提 是不是 already out-of-pool interchangeable / 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable、拿掉了 是不是 already never-propose interchangeable、回包没有它 是不是 already settled interchangeable。可以跳过「看见本块不提就已经出池 interchangeable / 就已经永远不提 interchangeable / 就已经交差 interchangeable」。不要另写怎样改 Prepare 列表。355 preparedrop vs mempool bundled unbundling 在本页 item 1 启动；续 [`worked-example-add-notmempool-vs-bundled.md`](worked-example-add-notmempool-vs-bundled.md)（不变量 819 item 2）；完成见 820。

## 本页不抄

- 怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池。
- Prepare 改列表 bundled。那是不变量 355。
- 往提案加了一笔新的不是已经进了内存池。那是不变量 355 item 2 余量 / 819。
- 把 t1 改成 t2 不是已经还能按 t1 查到。那是不变量 355 item 3 余量 / 820。
- 提案收了就已经从池里删掉。那是不变量 301。
- 整池可见就已经只能看见装得进一块的子集。那是不变量 345。
- 四门已经结算。那是不变量 33。
