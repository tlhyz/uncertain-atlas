# 例：看见能出块 / 看见和其他节点一样跑 / 看见透明 is not already already full-history interchangeable / already genesis-replay interchangeable / already no-extension-care interchangeable

**层次**：实现 / 切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事（323 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事（323 余量）/ not 727 snapshotswitch-nothistory interchangeable / not 323 snapshotswitch bundled interchangeable」，不是 Transition to Consensus bundled（323），也不是装完不是已经有了 ChainID（725 item 1 余量）或 AppHash 对上不是已经版本也对上（726 item 2 余量）。不要另写怎样切到共识或怎样配扩展。

## 官方三件事

规范把 Requirements 里切过去之后这个节点和其他节点一样跑、只是块历史在恢复快照的那个高度被**截断**、对应用来说这些操作是透明的除非刚升到 ABCI 2.0 才要另写扩展何时必须带 和「已经是能出块就已经有从创世的完整历史 interchangeable / 已经是和其他节点一样跑就已经从创世重放 interchangeable / 已经是透明就已经不用管扩展高度 interchangeable / 已经是 Transition to Consensus bundled interchangeable」分开写成三件独立的实现事，不是「看见切进共识 / 看见能出块就已经有完整历史 interchangeable / 就已经从创世重放 interchangeable / 就已经不用管扩展高度 interchangeable」一件事：

1. **看见能出块 / 看见切进共识 / 看见能给新高度 is not already 已经有从创世的完整历史 interchangeable / 已经 full-history interchangeable / 已经能给任意旧高度 interchangeable / 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 727 snapshotswitch-nothistory interchangeable / 323 snapshotswitch item 3 interchangeable，也不是已经切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事 bundled（323 item 3 余量） interchangeable / 323 snapshotswitch item 3 interchangeable，也不是已经装完不是已经有了 ChainID（725） interchangeable / 726 snapshotswitch-notversion interchangeable / 321 snapshotrestore interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：块历史在恢复快照的那个高度被**截断**。看见能出块，不是已经有从创世的完整历史 interchangeable——323 钉 bundled 三事，本页从 item 3 侧钉 not already full-history 单句。看见切进共识，不是已经 Transition to Consensus bundled（323） interchangeable——323 钉 bundled，本页钉 item 3 第一件事。看见能给新高度，不是已经装完不是已经有了 ChainID（725） interchangeable——725 另钉 item 1，本页钉 item 3 第一件事。323 snapshotswitch vs history bundled unbundling 在本页 item 3 启动。

2. **看见和其他节点一样跑 / 看见切过去之后一样跑 / 看见能出块之后 is not already 已经从创世重放 interchangeable / 已经 genesis-replay interchangeable / 已经从创世重放交差 interchangeable / 323 snapshotswitch bundled interchangeable / 314 querystate interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 727 snapshotswitch-nothistory interchangeable / 323 snapshotswitch item 1 装完 interchangeable / 323 snapshotswitch item 2 AppHash interchangeable，也不是已经切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事 bundled（323 item 3 余量） interchangeable / 323 snapshotswitch item 3 interchangeable，也不是已经有完整历史（本页第一件事） interchangeable。**  
   官方把和其他节点一样跑和已经从创世重放路径分开——一样跑，不等于已经从创世重放。看见和其他节点一样跑，不是已经 genesis-replay interchangeable——本页钉 not already genesis-replay 单句。看见切过去之后一样跑，不是已经 AppHash 对上不是已经版本也对上（726） interchangeable——726 另钉 item 2，本页钉 item 3 第二件事。看见能出块之后，不是已经启动对齐已经是快照重放（314） interchangeable——314 另钉，本页钉 item 3 第二件事。323 snapshotswitch vs history bundled unbundling 在本页 item 3 启动。

3. **看见透明 / 看见对应用透明 / 看见操作透明 is not already 已经不用管扩展高度 interchangeable / 已经 no-extension-care interchangeable / 已经扩展高度交差 interchangeable / 323 snapshotswitch bundled interchangeable / 726 snapshotswitch-notversion interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 727 snapshotswitch-nothistory interchangeable / 323 snapshotswitch item 1 / 323 snapshotswitch item 2，也不是已经切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事 bundled（323 item 3 余量） interchangeable / 323 snapshotswitch item 3 interchangeable，也不是已经有完整历史（本页第一件事） interchangeable / 已经从创世重放（本页第二件事） interchangeable。**  
   官方写：对应用来说这些操作是透明的，除非刚升到 ABCI 2.0，才要另写扩展何时必须带。看见透明，不是已经不用管扩展高度 interchangeable——本页钉 not already no-extension-care 单句。看见对应用透明，不是已经有完整历史（本页第一件事） interchangeable——三件事分开钉。看见操作透明，不是已经没有截断 interchangeable——截断仍在。323 snapshotswitch vs history bundled unbundling 在本页 item 3 完成。

怎样切到共识、怎样配 RFC-100、怎样写扩展高度是规范里的取值或做法，本页不抄。Transition to Consensus bundled（323）、装完不是已经有了 ChainID（323 item 1 余量 / 725）、AppHash 对上不是已经版本也对上（323 item 2 余量 / 726）、Offer 收下已经装完（321）、只有 AppHash 可信任（38）、启动对齐当快照重放（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **能出块 not already full-history ≠ 323 / 33 interchangeable：** 官方把能出块和历史被截断分开。
- **和其他节点一样跑 not already genesis-replay ≠ 已经从创世重放 interchangeable：** 官方把一样跑和从创世重放路径分开。
- **透明 not already no-extension-care ≠ 已经不用管扩展高度 interchangeable：** 官方把对应用透明和 ABCI 2.0 扩展例外分开；323 snapshotswitch vs history bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能出块 | 不是 already full-history | 不是装完 ChainID alone（725） |
| 和其他节点一样跑 | 不是 already genesis-replay | 不是 AppHash 核对 alone（726） |
| 透明 | 不是 already no-extension-care | 不是启动对齐 alone（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事（323 余量），必须分开能出块 是不是 already full-history interchangeable / 323 snapshotswitch bundled interchangeable / snapshotswitch-sold-as-full-history interchangeable、和其他节点一样跑 是不是 already genesis-replay interchangeable、透明 是不是 already no-extension-care interchangeable。可以跳过「看见切进共识就已经有完整历史 interchangeable / 就已经从创世重放 interchangeable / 就已经不用管扩展高度 interchangeable」。不要另写怎样切到共识。323 snapshotswitch vs history bundled unbundling 在本页 item 3 完成（725 + 726 + 727）。

## 本页不抄

- 怎样切到共识、怎样配 RFC-100、怎样写扩展高度。
- Transition to Consensus bundled。那是不变量 323。
- 装完不是已经有了 ChainID。那是不变量 323 item 1 余量 / 725。
- AppHash 对上不是已经版本也对上。那是不变量 323 item 2 余量 / 726。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
