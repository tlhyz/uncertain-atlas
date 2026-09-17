# 例：看见 CheckTx every node runs CheckTx before letting into local mempool is not already broadcast_tx others run interchangeable / not already in-pool gossip interchangeable / not already forever valid interchangeable

**层次**：实现 / CheckTx Usage every node runs CheckTx before letting into local mempool not broadcast_tx others run / not in-pool gossip / not forever valid 正式三事（490 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage every node runs CheckTx before letting into local mempool not broadcast_tx others run / not in-pool gossip / not forever valid 正式三事（490 余量）/ not 690 chktxguardusage-notgates interchangeable / not 490 chktxguardusage-vs-optional bundled interchangeable」，不是 CheckTx Usage Guardian 正式三事 bundled（490），也不是四门已经结算（33）或 forever valid（301）。不要另写怎样写内存池守卫、怎样挑邻居。

## 官方三件事

规范把 CheckTx Usage 里 every node runs `CheckTx` before letting a transaction into its local mempool 和「已经 RPC `broadcast_tx` 回了就代表别的节点也会跑 CheckTx interchangeable / 已经进了本地池就开始 P2P 流言 interchangeable / 已经 CheckTx 过了就 forever valid（301） interchangeable / 已经 Check 通过就是已进提案（33） interchangeable」分开写成三件独立的实现事，不是「看见每条节点先跑 CheckTx 就已经别人也会跑 interchangeable / 就已经流言 interchangeable / 就已经 forever valid interchangeable」一件事：

1. **看见 every node runs `CheckTx` before letting a transaction into its local mempool / 看见每条节点先跑 CheckTx 才让交易进本地池 / every node is not already 已经 RPC `broadcast_tx` 回了就代表别的节点也会跑 CheckTx interchangeable / 已经单节点 optional 就等于全网可以不跑 interchangeable / 已经别的节点已经从邻居收到 interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 690 chktxguardusage-notgates interchangeable / 689 chktxguardusage-notoptional interchangeable / 490 chktxguardusage item 1 Guardian interchangeable，也不是已经 every node runs CheckTx not broadcast_tx others run / not in-pool gossip / not forever valid 正式三事 bundled（490 item 2 余量） interchangeable / 490 chktxguardusage item 2 interchangeable。**  
   官方 Usage 写：every node runs `CheckTx` before letting a transaction into its local mempool。看见 every node，不是已经 RPC 回了别人也会跑 interchangeable。490 chktxguardusage vs optional bundled unbundling 在本页 item 2 续。

2. **看见 every node runs CheckTx before letting into local mempool / 看见先跑了才让进本地池 / 看见每条节点 is not already 已经进了本地池就开始 P2P 流言 interchangeable / 已经流言出去 interchangeable / 已经 Check 通过就是已进提案（33） interchangeable / 33 four gates interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 690 chktxguardusage-notgates interchangeable / 490 chktxguardusage item 3 before letting interchangeable / 691 chktxguardusage-notsource interchangeable。**  
   官方把 Usage 本地池入口守卫和广播 / 四门结算路径分开——490 bundled 第二件事常与 33 混成「看见先跑了才让进本地池 就已经 Check 通过就是已进提案 interchangeable」，本页钉 not in-pool gossip / not Check passed is in proposal 单句。看见 runs CheckTx before letting in，不是已经别的节点已经从邻居收到 interchangeable。

3. **看见 before letting into its local mempool / 看见先跑了才让进本地池 / 看见 every node is not already 已经 CheckTx 过了就 forever valid（301） interchangeable / 301 forever valid interchangeable / 已经提案收了 interchangeable / 已经四门已经结算 interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 690 chktxguardusage-notgates interchangeable / 689 chktxguardusage-notoptional interchangeable。**  
   官方把 Usage 本地池入口和 forever valid 路径分开——490 bundled 第二件事常与 301 混成「看见先跑了才让进本地池 就已经 forever valid interchangeable」，本页钉 not forever valid 单句。看见 before letting into local mempool，不是已经 CheckTx 过了就永远有效 interchangeable——301 钉 mempool 交接，本页钉 Usage 本地池入口。490 chktxguardusage vs optional bundled unbundling 在本页 item 2 续。

怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx Usage Guardian 正式三事 bundled（490）、Guardian of the mempool（490 item 1 余量 / 689）、before letting into local mempool（490 item 3 余量 / 691）、四门已经结算（33）、forever valid（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **every node runs CheckTx not broadcast_tx others run ≠ RPC 回了别人也会跑 interchangeable：** 官方把 Usage 本地池入口和 broadcast_tx 别人也会跑路径分开。
- **every node runs CheckTx not in-pool gossip ≠ 33 / 已经流言 interchangeable：** 官方把 Usage 本地池入口和进池就开始流言 / Check 通过就是已进提案路径分开。
- **every node runs CheckTx not forever valid ≠ 301 interchangeable：** 官方把 Usage 本地池入口和 CheckTx 过了就永远有效路径分开；490 chktxguardusage vs optional bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| every node runs CheckTx | 不是 broadcast_tx 别人也会跑 | 不是 Guardian 单句（689/490 item 1） |
| 先跑了才让进本地池 | 不是已经流言 / Check 通过就是已进提案（33） | 不是 CheckTx Usage Code≠0（489） |
| 看见 every node | 不是 forever valid（301） | 不是 before letting in 来源边界（691/490 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage every node runs CheckTx before letting into local mempool not broadcast_tx others run / not in-pool gossip / not forever valid 正式三事（490 余量），必须分开 every node 是不是别人也会跑 interchangeable、是不是已经流言 / Check 通过就是已进提案 interchangeable / 33、是不是 forever valid interchangeable / 301。可以跳过「看见每条节点先跑 CheckTx 就已经四门已经结算」。不要另写怎样写内存池守卫。490 chktxguardusage vs optional bundled unbundling 在本页 item 2 续；续 [`worked-example-chktxguardusage-notsource-vs-bundled.md`](worked-example-chktxguardusage-notsource-vs-bundled.md)（不变量 691 item 3）。

## 本页不抄

- 怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx Usage Guardian 正式三事 bundled。那是不变量 490。
- Guardian of the mempool。那是不变量 490 item 1 余量 / 689。
- before letting into its local mempool 来源边界。那是不变量 490 item 3 余量 / 691。
- Check 通过就是已进提案。那是不变量 33。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
