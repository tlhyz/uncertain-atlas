# 例：看见 t1 没进块 / 看见 t2 进了块 / 看见改了 is not already already t1-lookup interchangeable / already origin-known interchangeable / already settled interchangeable

**层次**：实现 / 把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事（355 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事（355 余量）/ not 820 retarget-nottraceable interchangeable / not 355 preparedrop bundled interchangeable」，不是 Prepare 改列表 bundled（355），也不是从提案拿掉 tx 不是已经从内存池删掉（818 item 1 余量）或往提案加了一笔新的不是已经进了内存池（819 item 2 余量）。不要另写怎样改 Prepare 列表。

## 官方三件事

规范把 Methods 里拿掉再加可能丢掉可追踪性、客户端去查 t1 会发现 t1 没进已提交块、除非应用自己记没有组件知道 t2 来自 t1 和「已经是 t1 没进块就已经还能按 t1 查到 interchangeable / 已经是 t2 进了块就已经有人知道来源 interchangeable / 已经是改了就已经交差 interchangeable / 已经是 preparedrop bundled interchangeable」分开写成三件独立的实现事，不是「看见 t1 没进块就已经还能按 t1 查到 interchangeable / 就已经有人知道来源 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见把 t1 改成 t2 / 看见 t1 没进块 / 看见 t1 没进已提交块 is not already 已经还能按 t1 查到 interchangeable / 已经 t1-lookup interchangeable / 已经按 t1 查到交差 interchangeable / 355 preparedrop bundled interchangeable / 33 fourgates interchangeable / preparedrop-sold-as-evicted interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 820 retarget-nottraceable interchangeable / 355 preparedrop item 3 interchangeable，也不是已经把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事 bundled（355 item 3 余量） interchangeable / 355 preparedrop item 3 interchangeable，也不是已经出池（818） interchangeable / 819 add-notmempool interchangeable / 301 proposed-removed interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：拿掉再加可能丢掉可追踪性。客户端去查 t1，会发现 t1 没进已提交块（若再检又把它踢出池），误以为没上块。看见 t1 没进块，不是已经还能按 t1 查到。看见 t1 没进块，不是已经 t1-lookup interchangeable——355 钉 bundled 三事，本页从 item 3 侧钉 not already t1-lookup 单句。看见把 t1 改成 t2，不是已经 Prepare 改列表 bundled（355） interchangeable——355 钉 bundled，本页钉 item 3 第一件事。看见 t1 没进块，不是已经出池（818） interchangeable——818 另钉 item 1。看见 t1 没进块，不是已经进池（819） interchangeable——819 另钉 item 2。355 preparedrop vs mempool bundled unbundling 在本页 item 3 完成。

2. **看见 t2 进了块 / 看见 t2 在已提交块里 / 看见改成了 t2 is not already 已经有人知道 t2 来自 t1 interchangeable / 已经 origin-known interchangeable / 已经来源已知交差 interchangeable / 355 preparedrop bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 820 retarget-nottraceable interchangeable / 355 preparedrop item 1 拿掉 interchangeable / 355 preparedrop item 2 加新 interchangeable，也不是已经把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事 bundled（355 item 3 余量） interchangeable / 355 preparedrop item 3 interchangeable，也不是已经还能按 t1 查到（本页第一件事） interchangeable。**  
   官方写：t2 会在已提交块里，但除非应用自己记，没有组件知道 t2 来自 t1。看见 t2 进了块，不是已经有人知道来源。看见 t2 在已提交块里，不是已经 origin-known interchangeable——本页钉 not already origin-known 单句。看见改成了 t2，不是已经还能按 t1 查到（本页第一件事） interchangeable——三件事分开钉。355 preparedrop vs mempool bundled unbundling 在本页 item 3 完成。

3. **看见改了 / 看见拿掉再加 / 看见改了列表 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 355 preparedrop bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 820 retarget-nottraceable interchangeable / 355 preparedrop item 1 / 355 preparedrop item 2，也不是已经把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事 bundled（355 item 3 余量） interchangeable / 355 preparedrop item 3 interchangeable，也不是已经还能按 t1 查到（本页第一件事） interchangeable / 已经有人知道来源（本页第二件事） interchangeable。**  
   官方写：看见改了，不是已经交差。看见拿掉再加，不是已经 settled interchangeable——本页钉 not already settled 单句。看见改了列表，不是已经有人知道来源（本页第二件事） interchangeable——三件事分开钉。355 preparedrop vs mempool bundled unbundling 在本页 item 3 完成。

怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池是规范里的做法，本页不抄。Prepare 改列表 bundled（355）、从提案拿掉 tx 不是已经从内存池删掉（355 item 1 余量 / 818）、往提案加了一笔新的不是已经进了内存池（355 item 2 余量 / 819）、提案收了就已经从池里删掉（301）、整池可见就已经只能看见装得进一块的子集（345）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **t1 没进块 not already t1-lookup ≠ 355 / 33 interchangeable：** 官方把 t1 没进块和还能按 t1 查到分开。
- **t2 进了块 not already origin-known ≠ 已经有人知道来源 interchangeable：** 官方把 t2 进了块和已经有人知道来源分开。
- **改了 not already settled ≠ 已经交差 interchangeable：** 官方把改了和已经交差分开；355 preparedrop vs mempool bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| t1 没进块 | 不是 already t1-lookup | 不是四门已经结算 alone（33） |
| t2 进了块 | 不是 already origin-known | 不是往提案加新 already in-pool alone（819） |
| 改了 | 不是 already settled | 不是本块不提 already out-of-pool alone（818） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事（355 余量），必须分开 t1 没进块 是不是 already t1-lookup interchangeable / 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable、t2 进了块 是不是 already origin-known interchangeable、改了 是不是 already settled interchangeable。可以跳过「看见 t1 没进块就已经还能按 t1 查到 interchangeable / 就已经有人知道来源 interchangeable / 就已经交差 interchangeable」。不要另写怎样改 Prepare 列表。355 preparedrop vs mempool bundled unbundling 在本页 item 3 完成（818 + 819 + 820）。

## 本页不抄

- 怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池。
- Prepare 改列表 bundled。那是不变量 355。
- 从提案拿掉 tx 不是已经从内存池删掉。那是不变量 355 item 1 余量 / 818。
- 往提案加了一笔新的不是已经进了内存池。那是不变量 355 item 2 余量 / 819。
- 提案收了就已经从池里删掉。那是不变量 301。
- 整池可见就已经只能看见装得进一块的子集。那是不变量 345。
- 四门已经结算。那是不变量 33。
