# 例：看见 CheckTx may come from another node is not already gossip verified interchangeable / not already removed from pool interchangeable / not already forever valid interchangeable

**层次**：实现 / CheckTx Usage may come from another node not gossip verified / not removed from pool / not forever valid 正式三事（488 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage may come from another node not gossip verified / not removed from pool / not forever valid 正式三事（488 余量）/ not 684 chktxsource-notremoved interchangeable / not 488 chktxsource-vs-recheck bundled interchangeable」，不是 CheckTx Usage tx source 正式三事 bundled（488），也不是提案收了 / CheckTx 过了就永远有效（301）或 CheckTx 守卫余量（405）。不要另写怎样挑邻居、怎样做索引器。

## 官方三件事

规范把 CheckTx Usage 里 The transaction may come from another node 和「已经流言广播就代表来源已经验过 interchangeable / 已经从池里删掉 / 提案收了（301） interchangeable / 已经 CheckTx 过了就永远有效（301） interchangeable」分开写成三件独立的实现事，不是「看见能来自另一节点 就已经 gossip verified interchangeable / 就已经 removed from pool interchangeable / 就已经 forever valid interchangeable」一件事：

1. **看见 The transaction may come from another node / 看见能来自另一节点 / another node is not already 已经 P2P 流言就代表全网已经验过 interchangeable / 已经流言广播就代表来源已经验过 interchangeable / 已经邻居送来就已经交差 interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 684 chktxsource-notremoved interchangeable / 683 chktxsource-notrecheck interchangeable / 488 chktxsource item 1 external user interchangeable，也不是已经 may come from another node not gossip verified / not removed from pool / not forever valid 正式三事 bundled（488 item 2 余量） interchangeable / 488 chktxsource item 2 interchangeable。**  
   官方 Usage 写：The transaction may come from an external user or another node。看见 may come from another node，不是已经 P2P 流言就代表全网已经验过 interchangeable。488 chktxsource vs recheck bundled unbundling 在本页 item 2 续。

2. **看见 may come from another node / 能来自邻居 / 看见邻居送来 is not already 已经从池里删掉 / 提案收了（301） interchangeable / 301 proposed-vs-removed interchangeable / 已经提案收了就从池里删掉 interchangeable / 已经 CheckTx 是内存池守卫（405） bundled 第一句就代表来源已经交差 interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 684 chktxsource-notremoved interchangeable / 488 chktxsource item 3 replay interchangeable / 685 chktxsource-notreplay interchangeable。**  
   官方把 Usage 邻居来源单句和 mempool 交接路径分开——488 bundled 第二件事常与 301 混成「看见能来自邻居 就已经从池里删掉 interchangeable」，本页钉 not removed from pool 单句。看见邻居送来，不是已经提案收了 interchangeable——301 钉 mempool 交接，本页钉 Usage 邻居来源。

3. **看见 may come from another node / 看见能来自另一节点 / 看见邻居送来 is not already 已经 CheckTx 过了就永远有效（301） interchangeable / 301 forever valid interchangeable / 已经 Check 通过就是已进提案（33） interchangeable / 已经四门已经结算 interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 684 chktxsource-notremoved interchangeable / 683 chktxsource-notrecheck interchangeable。**  
   官方把 Usage 邻居来源单句和 forever valid 路径分开——488 bundled 第二件事常与 301 混成「看见邻居送来 就已经 forever valid interchangeable」，本页钉 not forever valid 单句。看见另一节点，不是已经四门已经结算 interchangeable——33 钉四门，本页钉 Usage item 2。488 chktxsource vs recheck bundled unbundling 在本页 item 2 续。

怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx Usage tx source 正式三事 bundled（488）、may come from an external user（488 item 1 余量 / 683）、external user or another node not replay（488 item 3 余量 / 685）、提案收了 / forever valid（301）、CheckTx 守卫余量（405）是另外那套，本页不抄。

## 官方为什么这样拆

- **may come from another node not gossip verified ≠ 流言就已经验过 interchangeable：** 官方把 Methods Usage 邻居来源和 P2P 流言验完路径分开。
- **may come from another node not removed from pool ≠ 301 proposed-vs-removed interchangeable：** 官方把 Usage 邻居来源单句和提案收了就从池里删掉路径分开。
- **may come from another node not forever valid ≠ 301 forever valid interchangeable：** 官方把 Usage 邻居来源单句和 CheckTx 过了就永远有效路径分开；488 chktxsource vs recheck bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| may come from another node | 不是流言就已经验过 | 不是 external user（683/488 item 1） |
| 能来自邻居 | 不是已经从池里删掉（301） | 不是 CheckTx 守卫余量（405） |
| 看见邻居送来 | 不是 forever valid（301） | 不是 already 保证不重放（685/488 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from another node not gossip verified / not removed from pool / not forever valid 正式三事（488 余量），必须分开 another node 是不是流言就已经验过 interchangeable、是不是已经从池里删掉 interchangeable / 301、是不是 forever valid interchangeable / 301。可以跳过「看见邻居送来就已经从池里删掉」。不要另写怎样挑邻居。488 chktxsource vs recheck bundled unbundling 在本页 item 2 续；续 [`worked-example-chktxsource-notreplay-vs-bundled.md`](worked-example-chktxsource-notreplay-vs-bundled.md)（不变量 685 item 3）。

## 本页不抄

- 怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx Usage tx source 正式三事 bundled。那是不变量 488。
- may come from an external user。那是不变量 488 item 1 余量 / 683。
- external user or another node not replay。那是不变量 488 item 3 余量 / 685。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
- CheckTx 是内存池守卫。那是不变量 405。
