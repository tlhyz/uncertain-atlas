# 例：看见往提案加了一笔新的 is not already in mempool interchangeable / not already passed CheckTx interchangeable / not already settled interchangeable

**层次**：实现 / 往提案加了一笔新的 not already in mempool / not already passed CheckTx / not already settled 正式三事（355 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「往提案加了一笔新的 not already in mempool / not already passed CheckTx / not already settled 正式三事（355 余量）/ not 855 prepare-drop-notinpool interchangeable / not 355 prepare-drop-vs-mempool bundled interchangeable」，不是 Prepare 改列表 bundled（355），也不是整池可见就已经只能看见装得进一块的子集（345），也不是 CheckTx 绿就已经进块（317）。不要另写怎样改 Prepare 列表。

## 官方三件事

1. **看见往提案加了一笔新的 / 看见回包里有它 这份加新的 is not already 已经进了内存池 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 855 prepare-drop-notinpool interchangeable / 854 prepare-drop-notdeleted interchangeable / 355 prepare-drop item 1 拿掉 interchangeable，也不是已经往提案加了一笔新的 not already in mempool / not already passed CheckTx / not already settled 正式三事 bundled（355 item 2 余量） interchangeable / 355 prepare-drop item 2 interchangeable。**  
   官方写：应用若要加一笔新的，就写进 `PrepareProposalResponse.txs`。引擎不会把它加进内存池。看见回包里有它，不是已经进池 interchangeable——本页从 355 item 2 侧钉 not already in mempool 单句。355 prepare-drop vs mempool bundled unbundling 在本页 item 2 续。

2. **看见回包里有它 / 看见能提 / 这份加新的 is not already 已经过了 CheckTx interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 855 prepare-drop-notinpool interchangeable / 355 prepare-drop item 3 改成 t2 interchangeable / 856 prepare-drop-nottrace interchangeable，也不是已经整池可见就已经只能看见装得进一块的子集 interchangeable / 345 poolvis interchangeable。**  
   官方把能提和已经过了 CheckTx 分开——355 bundled 第二件事常与 345 混成「看见回包里有它就已经进了内存池或已经过了 CheckTx interchangeable」，本页钉 not already passed CheckTx 单句。

3. **看见回包里有它 / 看见加进去了 / 这份加新的 is not already 已经交差 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 855 prepare-drop-notinpool interchangeable / 854 prepare-drop-notdeleted interchangeable，也不是已经 CheckTx 绿就已经进块 interchangeable / 317 prioritized interchangeable。**  
   官方把加进去了和已经交差分开。看见加进去了，不是已经交差 interchangeable。355 prepare-drop vs mempool bundled unbundling 在本页 item 2 续。

怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池是规范里的做法，本页不抄。

## 官方为什么这样拆

- **往提案加了一笔新的 not already in mempool ≠ 已经进了内存池 interchangeable：** 官方把回包里有它和进池分开。
- **看见能提 not already passed CheckTx ≠ 已经过了 CheckTx interchangeable：** 官方把能提和已经过了 CheckTx 分开。
- **看见加进去了 not already settled ≠ 已经交差 interchangeable：** 官方把加进去了和已经交差分开；355 prepare-drop vs mempool bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 往提案加了一笔新的 | 不是已经进了内存池 | 不是整池可见就已经只能看见装得进一块的子集（345） |
| 看见能提 | 不是已经过了 CheckTx | 不是 CheckTx 绿就已经进块（317） |
| 看见加进去了 | 不是已经交差 | 不是从提案拿掉就已经出池（854） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看往提案加了一笔新的 not already in mempool / not already passed CheckTx / not already settled 正式三事（355 余量），必须分开是不是已经进了内存池、是不是已经过了 CheckTx、是不是已经交差。可以跳过「看见回包里有它就已经进了内存池」。不要另写怎样改 Prepare 列表。355 prepare-drop vs mempool bundled unbundling 在本页 item 2 续；续 [`worked-example-prepare-drop-nottrace-vs-bundled.md`](worked-example-prepare-drop-nottrace-vs-bundled.md)（不变量 856 item 3）。

## 本页不抄

- 怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池。
- Prepare 改列表 bundled。那是不变量 355。
- 从提案拿掉 tx。那是不变量 355 item 1 余量 / 854。
- 整池可见就已经只能看见装得进一块的子集。那是不变量 345。
- CheckTx 绿就已经进块。那是不变量 317。
