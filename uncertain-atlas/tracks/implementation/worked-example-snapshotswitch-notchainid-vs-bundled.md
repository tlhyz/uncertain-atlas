# 例：看见装完 / 看见状态机在 / 看见有创世文件 is not already already has-ChainID interchangeable / already can-propose interchangeable / already genesis-RPC-checked interchangeable

**层次**：实现 / 装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事（323 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事（323 余量）/ not 725 snapshotswitch-notchainid interchangeable / not 323 snapshotswitch bundled interchangeable」，不是 Transition to Consensus bundled（323），也不是 AppHash 对上不是已经版本也对上（726 item 2 余量）或切进共识不是已经有完整历史（727 item 3 余量）。不要另写怎样切到共识或怎样配扩展。

## 官方三件事

规范把 Requirements 里快照都装完之后 CometBFT 还要从创世文件和轻客户端 RPC **再凑** 引导节点必要的信息（例如 ChainID、共识参数、验证者集合、块头） 和「已经是装完就已经有了 ChainID 参数集合和头 interchangeable / 已经是状态机在就已经能出块 interchangeable / 已经是有创世文件就已经和轻客户端那份对过 interchangeable / 已经是 Transition to Consensus bundled interchangeable」分开写成三件独立的实现事，不是「看见快照已经装完就已经有了这些 interchangeable / 就已经能出块 interchangeable / 就已经和轻客户端对过 interchangeable」一件事：

1. **看见装完 / 看见快照已经装完 / 看见状态机已经恢复 is not already 已经有了 ChainID、参数、集合和头 interchangeable / 已经 has-ChainID interchangeable / 已经引导信息交差 interchangeable / 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 725 snapshotswitch-notchainid interchangeable / 323 snapshotswitch item 1 interchangeable，也不是已经装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事 bundled（323 item 1 余量） interchangeable / 323 snapshotswitch item 1 interchangeable，也不是已经 AppHash 对上不是已经版本也对上（726） interchangeable / 727 snapshotswitch-nothistory interchangeable / 321 snapshotrestore interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：快照都装完之后，还要从创世文件和轻客户端 RPC **再凑** ChainID、共识参数、验证者集合、块头。看见装完，不是已经有了这些 interchangeable——323 钉 bundled 三事，本页从 item 1 侧钉 not already has-ChainID 单句。看见快照已经装完，不是已经 Transition to Consensus bundled（323） interchangeable——323 钉 bundled，本页钉 item 1 第一件事。看见状态机已经恢复，不是已经 Offer 收下就已经装完（321） interchangeable——321 另钉装回，本页钉切共识 item 1。323 snapshotswitch vs history bundled unbundling 在本页 item 1 启动。

2. **看见状态机在 / 看见状态机已经恢复 / 看见装完之后 is not already 已经能出块 interchangeable / 已经 can-propose interchangeable / 已经能当全节点出块 interchangeable / 323 snapshotswitch bundled interchangeable / 322 snapshotdiscover interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 725 snapshotswitch-notchainid interchangeable / 323 snapshotswitch item 2 AppHash interchangeable / 323 snapshotswitch item 3 切进共识 interchangeable，也不是已经装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事 bundled（323 item 1 余量） interchangeable / 323 snapshotswitch item 1 interchangeable，也不是已经有了这些（本页第一件事） interchangeable。**  
   官方把状态机恢复和已经能出块路径分开——状态机在，不等于已经能出块。看见状态机在，不是已经 can-propose interchangeable——本页钉 not already can-propose 单句。看见状态机已经恢复，不是已经切进共识不是已经有完整历史（727） interchangeable——727 另钉 item 3，本页钉 item 1 第二件事。看见装完之后，不是已经有了这些（本页第一件事） interchangeable——三件事分开钉。323 snapshotswitch vs history bundled unbundling 在本页 item 1 启动。

3. **看见有创世文件 / 看见要从创世文件再凑 / 看见还要轻客户端 RPC is not already 已经和轻客户端那份对过 interchangeable / 已经 genesis-RPC-checked interchangeable / 已经创世与 RPC 対上交差 interchangeable / 323 snapshotswitch bundled interchangeable / 38 apphash interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 725 snapshotswitch-notchainid interchangeable / 323 snapshotswitch item 2 / 323 snapshotswitch item 3，也不是已经装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事 bundled（323 item 1 余量） interchangeable / 323 snapshotswitch item 1 interchangeable，也不是已经有了这些（本页第一件事） interchangeable / 已经能出块（本页第二件事） interchangeable。**  
   官方把要从创世和轻客户端 RPC 再凑和已经对过路径分开——有创世文件，不等于已经和轻客户端那份对过。看见有创世文件，不是已经 genesis-RPC-checked interchangeable——本页钉 not already genesis-RPC-checked 单句。看见要从创世文件再凑，不是已经有了这些（本页第一件事） interchangeable——三件事分开钉。看见还要轻客户端 RPC，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉信任边界。323 snapshotswitch vs history bundled unbundling 在本页 item 1 完成。

怎样切到共识、怎样配 RFC-100、怎样写扩展高度是规范里的取值或做法，本页不抄。Transition to Consensus bundled（323）、AppHash 对上不是已经版本也对上（323 item 2 余量 / 726）、切进共识不是已经有完整历史（323 item 3 余量 / 727）、Offer 收下已经装完（321）、只有 AppHash 可信任（38）、启动对齐当快照重放（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **装完 not already has-ChainID ≠ 323 / 33 interchangeable：** 官方把恢复状态机和再凑引导信息分开。
- **状态机在 not already can-propose ≠ 已经能出块 interchangeable：** 官方把状态机恢复和已经能出块路径分开。
- **有创世文件 not already genesis-RPC-checked ≠ 已经和轻客户端对过 interchangeable：** 官方把再凑来源和已经对过路径分开；323 snapshotswitch vs history bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 装完 | 不是 already has-ChainID | 不是 Offer 装完 alone（321） |
| 状态机在 | 不是 already can-propose | 不是切进共识 alone（727） |
| 有创世文件 | 不是 already genesis-RPC-checked | 不是 Only AppHash alone（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事（323 余量），必须分开装完 是不是 already has-ChainID interchangeable / 323 snapshotswitch bundled interchangeable / snapshotswitch-sold-as-full-history interchangeable、状态机在 是不是 already can-propose interchangeable、有创世文件 是不是 already genesis-RPC-checked interchangeable。可以跳过「看见快照已经装完就已经有了这些 interchangeable / 就已经能出块 interchangeable / 就已经和轻客户端对过 interchangeable」。不要另写怎样切到共识。323 snapshotswitch vs history bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshotswitch-notversion-vs-bundled.md`](worked-example-snapshotswitch-notversion-vs-bundled.md)（不变量 726 item 2，待写）。

## 本页不抄

- 怎样切到共识、怎样配 RFC-100、怎样写扩展高度。
- Transition to Consensus bundled。那是不变量 323。
- AppHash 对上不是已经版本也对上。那是不变量 323 item 2 余量 / 726。
- 切进共识不是已经有完整历史。那是不变量 323 item 3 余量 / 727。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
