# 例：看见 Guardian of the mempool 不是已经 Technically optional；看见 every node runs CheckTx before letting into local mempool 不是已经四门已经结算；看见 before letting into its local mempool 不是已经保证不重放 / tx source bundled interchangeable

**层次**：实现 / CheckTx Usage Guardian 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Guardian of the mempool 不是 Technically optional / every node runs CheckTx before letting into local mempool 不是四门已经结算 / before letting into its local mempool 不是已经保证不重放 / validate-no-apply bundled interchangeable」，不是 CheckTx 守卫余量 bundled 第二三句（405），也不是 CheckTx Usage validate-no-apply bundled 第三件事（486）。不要另写怎样写内存池守卫、怎样挑邻居。

## 官方三件事

规范把 CheckTx Usage 里 Guardian of the mempool: every node runs `CheckTx` before letting a transaction into its local mempool，写成三件独立的实现事，不是「看见每条节点先跑 CheckTx 就已经是 optional、已经四门已经结算、已经保证不重放」一件事：

1. **看见 Guardian of the mempool / 看见内存池守卫 不是已经 Technically optional - not involved in processing blocks（373） interchangeable，也不是已经可以不跑 CheckTx / 已经四门已经结算（33），也不是已经 CheckTx Usage validate-no-apply（486） bundled 第三件事 interchangeable。**  
   官方 Usage 写：Guardian of the mempool。看见 Guardian，不是已经 Technically optional 那种 optional 就等于可以不跑 interchangeable——373 钉 optional vs block processing，本页钉 Methods CheckTx Usage Guardian 语义。看见内存池守卫，不是已经 Check 通过就是已进提案（33） interchangeable。看见 Usage 这句，不是已经 validate-no-apply bundled 第三件事 interchangeable——486 钉 validate-no-apply 全段，本页钉 Guardian 单句。
2. **看见 every node runs `CheckTx` before letting a transaction into its local mempool / 看见每条节点先跑 CheckTx 才让交易进本地池 不是已经 RPC `broadcast_tx` 回了就代表别的节点也会跑 CheckTx interchangeable，也不是已经进了本地池就开始 P2P 流言 interchangeable，也不是已经 CheckTx 过了就 forever valid（301）。**  
   官方 Usage 写：every node runs `CheckTx` before letting a transaction into its local mempool。看见 every node，不是已经单节点 optional 就等于全网可以不跑 interchangeable。看见 runs CheckTx before letting into its local mempool，不是已经别的节点已经从邻居收到 interchangeable。看见先跑了才让进本地池，不是已经 Check 通过就是已进提案（33） interchangeable——33 钉四门分开，本页钉 Usage 本地池入口守卫。看见 before letting into local mempool，不是已经 CheckTx 过了就 forever valid（301） interchangeable。
3. **看见 before letting a transaction into its local mempool / 看见才让进本地池 不是已经 may come from external user or another node（488） bundled 就代表来源已经验完 interchangeable，也不是已经内存池去重那种保证不重放（313），也不是已经 CheckTx Usage Code≠0 rejected（489） bundled 就代表 Guardian 已经交差 interchangeable。**  
   官方把 before letting into its local mempool 和 tx source、Replay Protection、Code 拒路径分开写。看见才让进本地池，不是已经 may come from external user or another node interchangeable——488 钉 tx source，本页钉本地池入口。看见 local mempool，不是已经提案收了就从池里删掉（301） interchangeable。看见 Guardian 语境下的 before letting in，不是已经 validate-no-apply bundled 或 Code≠0 bundled 就代表 Guardian 已经验完 interchangeable。

怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx 守卫余量 bundled（405）、CheckTx 技术上可选（373）、CheckTx Usage validate-no-apply（486）、CheckTx Usage tx source（488）、CheckTx Usage Code≠0 rejected（489）是另外那套，本页不抄。

## 官方为什么这样拆

- **Guardian of the mempool ≠ Technically optional / 四门已经结算：** 官方把 Methods Usage Guardian 和 optional / 四门结算分开。
- **every node runs CheckTx before letting into local mempool ≠ 已经流言 / Check 通过就是已进提案：** 官方把本地池入口守卫和广播 / 四门结算分开。
- **before letting into its local mempool ≠ 已经保证不重放 / tx source bundled interchangeable：** 官方把本地池入口和 tx source / Replay Protection 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Guardian of the mempool | 不是 Technically optional | 不是 validate-no-apply bundled（486） |
| every node runs CheckTx before letting into local mempool | 不是已经流言 / 四门已经结算 | 不是 Check 通过就是已进提案（33） |
| before letting into its local mempool | 不是已经保证不重放 | 不是 tx source bundled（488） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见每条节点先跑 CheckTx 就已经是 optional、已经四门已经结算、已经保证不重放」，必须分开 Guardian of the mempool 是不是 Technically optional / 四门已经结算、every node runs CheckTx before letting into local mempool 是不是已经流言 / Check 通过就是已进提案、before letting into its local mempool 是不是已经保证不重放 / tx source bundled interchangeable。可以跳过「看见每条节点先跑 CheckTx 就已经是 optional」。不要另写怎样写内存池守卫。

## 本页不抄

- 怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx 守卫余量 bundled 第二三句。那是不变量 405。
- CheckTx 技术上可选、不参与处理块。那是不变量 373。
- CheckTx Usage validate-no-apply / Technically optional bundled。那是不变量 486。
- CheckTx Usage tx source。那是不变量 488。
- CheckTx Usage Code≠0 rejected。那是不变量 489。
- 提案收了 / CheckTx 过了就 forever valid。那是不变量 301。
