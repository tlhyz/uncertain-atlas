# 例：看见快照装完 is not already chainid interchangeable / not already block-ready interchangeable / not already settled interchangeable

**层次**：实现 / 装完 not already chainid / not already block-ready / not already settled 正式三事（323 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「装完 not already chainid / not already block-ready / not already settled 正式三事（323 余量）/ not 953 snapshot-switch-notchain interchangeable / not 323 snapshot-switch-vs-history bundled interchangeable」，不是切进 bundled（323），也不是只有 AppHash 可信任（38），也不是 Offer 收下已经装完（321）。不要另写怎样切到共识或怎样配扩展。

## 官方三件事

1. **看见快照已经装完 / 看见状态机已经恢复 这份恢复 is not already 已经有了 ChainID interchangeable，也不是已经切进 bundled（323） interchangeable / 953 snapshot-switch-notchain interchangeable / 954 snapshot-switch-notver interchangeable / 323 snapshot-switch item 2 AppHash 对上 interchangeable，也不是已经装完 not already chainid / not already block-ready / not already settled 正式三事 bundled（323 item 1 余量） interchangeable / 323 snapshot-switch item 1 interchangeable。**  
   官方写：快照都装完之后，CometBFT 还要从创世文件和轻客户端 RPC 再凑引导节点必要的信息（例如 ChainID、共识参数、验证者集合、块头）。看见装完，不是已经有了这些 interchangeable——本页从 323 item 1 侧钉 not already chainid 单句。323 snapshot-switch vs history bundled unbundling 在本页 item 1 启动。

2. **看见状态机在 / 看见装完 / 这份恢复 is not already 已经能出块 interchangeable，也不是已经切进 bundled（323） interchangeable / 953 snapshot-switch-notchain interchangeable / 323 snapshot-switch item 3 切进共识 interchangeable / 955 snapshot-switch-nothist interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-only interchangeable。**  
   官方把恢复状态机和已经能出块分开——323 bundled 第一件事常与 38 混成「看见装完就已经有了 ChainID 或已经可信任 interchangeable」，本页钉 not already block-ready 单句。

3. **看见有创世文件 / 看见装完 / 这份恢复 is not already 已经交差 interchangeable，也不是已经切进 bundled（323） interchangeable / 953 snapshot-switch-notchain interchangeable / 954 snapshot-switch-notver interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 snapshot-restore interchangeable。**  
   官方把有创世文件和已经和轻客户端那份对过分开。看见有创世文件，不是已经交差 interchangeable。323 snapshot-switch vs history bundled unbundling 在本页 item 1 启动。

怎样切到共识、怎样配 RFC-100、怎样写扩展高度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **装完 not already chainid ≠ 已经有了 ChainID interchangeable：** 官方把恢复状态机和再凑引导信息分开。
- **看见状态机在 not already block-ready ≠ 已经能出块 interchangeable：** 官方把状态机在和已经能出块分开。
- **看见有创世文件 not already settled ≠ 已经交差 interchangeable：** 官方把创世文件和已经和轻客户端对过分开；323 snapshot-switch vs history bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 装完 | 不是已经有了 ChainID | 不是只有 AppHash 可信任（38） |
| 看见状态机在 | 不是已经能出块 | 不是 Offer 收下已经装完（321） |
| 看见有创世文件 | 不是已经交差 | 不是 AppHash 对上就已经版本也对上（954） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完 not already chainid / not already block-ready / not already settled 正式三事（323 余量），必须分开是不是已经有了 ChainID、是不是已经能出块、是不是已经交差。可以跳过「看见装完就已经是全节点」。不要另写怎样切到共识或怎样配扩展。323 snapshot-switch vs history bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshot-switch-notver-vs-bundled.md`](worked-example-snapshot-switch-notver-vs-bundled.md)（不变量 954 item 2）。

## 本页不抄

- 怎样切到共识、怎样配 RFC-100、怎样写扩展高度。
- 切进 bundled。那是不变量 323。
- 只有 AppHash 可信任。那是不变量 38。
- Offer 收下已经装完。那是不变量 321。
