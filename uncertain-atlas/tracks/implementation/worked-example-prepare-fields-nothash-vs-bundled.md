# 例：看见 height / time / proposer_address 对上拟议头 is not already header hash interchangeable / not already ExecuteTxState interchangeable / not already settled interchangeable

**层次**：实现 / height / time / proposer_address 对上拟议头 not already header hash / not already ExecuteTxState / not already settled 正式三事（359 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「height / time / proposer_address 对上拟议头 not already header hash / not already ExecuteTxState / not already settled 正式三事（359 余量）/ not 847 prepare-fields-nothash interchangeable / not 359 prepare-fields-vs-same bundled interchangeable」，不是 Prepare 请求字段 bundled（359），也不是候选已经是 ExecuteTxState（311），也不是本头 AppHash 就已经是本高度交差（147）。不要另写怎样填 Prepare 请求字段。

## 官方三件事

1. **看见 `height` / `time` / `proposer_address` 对上拟议头 / 看见对得上 这份对上 is not already 已经知道本头哈希 interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 847 prepare-fields-nothash interchangeable / 845 prepare-fields-notrun interchangeable / 359 prepare-fields item 1 同一套 interchangeable，也不是已经 height / time / proposer_address 对上拟议头 not already header hash / not already ExecuteTxState / not already settled 正式三事 bundled（359 item 3 余量） interchangeable / 359 prepare-fields item 3 interchangeable。**  
   官方写：这三列对上拟议块头里的值。看见对得上，不是已经有本头哈希 interchangeable——本页从 359 item 3 侧钉 not already header hash 单句。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

2. **看见对得上 / 看见头上有这些 / 这份对上 is not already 已经是候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 847 prepare-fields-nothash interchangeable / 359 prepare-fields item 2 local_last_commit interchangeable / 846 prepare-fields-notlocal interchangeable，也不是已经本头 AppHash 就已经是本高度交差 interchangeable / 147 header AppHash interchangeable。**  
   官方把头上有这些和已经是 ExecuteTxState 分开——359 bundled 第三件事常与 311 / 147 混成「看见对得上就已经知道本头哈希或已经是 ExecuteTxState interchangeable」，本页钉 not already ExecuteTxState 单句。

3. **看见对得上 / 看见拟议头 / 这份对上 is not already 已经交差 interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 847 prepare-fields-nothash interchangeable / 845 prepare-fields-notrun interchangeable，也不是已经 Finalize height/time 对上就已经验过 interchangeable / 462 finht interchangeable。**  
   官方把拟议头和已经交差分开。看见拟议头，不是已经交差 interchangeable。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **height / time / proposer_address 对上拟议头 not already header hash ≠ 已经知道本头哈希 interchangeable：** 官方把这三列和对上本头哈希分开。
- **看见头上有这些 not already ExecuteTxState ≠ 311 interchangeable：** 官方把头上有这些和已经是 ExecuteTxState 分开。
- **看见拟议头 not already settled ≠ 已经交差 interchangeable：** 官方把拟议头和已经交差分开；359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| height / time / proposer_address 对上拟议头 | 不是已经知道本头哈希 | 不是候选已经是 ExecuteTxState（311） |
| 看见头上有这些 | 不是已经是 ExecuteTxState | 不是本头 AppHash 就已经是本高度交差（147） |
| 看见拟议头 | 不是已经交差 | 不是 Finalize height/time 对上就已经验过（462） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height / time / proposer_address 对上拟议头 not already header hash / not already ExecuteTxState / not already settled 正式三事（359 余量），必须分开是不是已经知道本头哈希、是不是已经是 ExecuteTxState interchangeable / 311、是不是已经交差。可以跳过「看见对得上就已经知道本头哈希」。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样填 Prepare 请求字段、怎样读 local_last_commit、怎样对头。
- Prepare 请求字段 bundled。那是不变量 359。
- Prepare 和 Process / Finalize 同一套字段。那是不变量 359 item 1 余量 / 845。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
