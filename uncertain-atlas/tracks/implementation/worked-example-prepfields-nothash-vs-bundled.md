# 例：看见对得上 / 看见头上有这些 / 看见拟议头 is not already already header-hash interchangeable / already execute interchangeable / already settled interchangeable

**层次**：实现 / height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事（359 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事（359 余量）/ not 832 prepfields-nothash interchangeable / not 359 preparefields bundled interchangeable」，不是 Prepare 请求字段 bundled（359），也不是 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process（830 item 1 余量）或 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展（831 item 2 余量）。不要另写怎样填 Prepare 请求字段。

## 官方三件事

规范把 Methods 里 `height`、`time`、`proposer_address` 对上拟议块头里的值 和「已经是对得上就已经知道本头哈希 interchangeable / 已经是头上有这些就已经是 ExecuteTxState interchangeable / 已经是拟议头就已经交差 interchangeable / 已经是 preparefields bundled interchangeable」分开写成三件独立的实现事，不是「看见对得上就已经知道本头哈希 interchangeable / 就已经是 ExecuteTxState interchangeable / 就已经交差 interchangeable」一件事：

1. **看见对得上 / 看见 `height` / `time` / `proposer_address` 对上拟议头 / 看见这三列对上 is not already 已经知道本头哈希 interchangeable / 已经 header-hash interchangeable / 已经有本头哈希交差 interchangeable / 359 preparefields bundled interchangeable / 311 candidate interchangeable / preparefields-sold-as-same interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 832 prepfields-nothash interchangeable / 359 preparefields item 3 interchangeable，也不是已经 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事 bundled（359 item 3 余量） interchangeable / 359 preparefields item 3 interchangeable，也不是已经跑过 Process（830） interchangeable / 831 prepfields-notthissigned interchangeable / 311 execute interchangeable，也不是已经候选已经是 ExecuteTxState 就已经知道本头哈希（311） interchangeable。**  
   官方写：这三列对上拟议块头里的值。看见对得上，不是已经有本头哈希。看见对得上，不是已经 header-hash interchangeable——359 钉 bundled 三事，本页从 item 3 侧钉 not already header-hash 单句。看见 `height` / `time` / `proposer_address` 对上拟议头，不是已经 Prepare 请求字段 bundled（359） interchangeable——359 钉 bundled，本页钉 item 3 第一件事。看见对得上，不是已经跑过 Process（830） interchangeable——830 另钉 item 1。看见对得上，不是已经是本高度刚签的扩展（831） interchangeable——831 另钉 item 2。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

2. **看见头上有这些 / 看见拟议头上有 height / time / proposer_address / 看见头上有这三列 is not already 已经是候选已经是 ExecuteTxState interchangeable / 已经 execute interchangeable / 已经是 ExecuteTxState 交差 interchangeable / 359 preparefields bundled interchangeable / 311 candidate interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 832 prepfields-nothash interchangeable / 359 preparefields item 1 同一套 interchangeable / 359 preparefields item 2 上一高 interchangeable，也不是已经 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事 bundled（359 item 3 余量） interchangeable / 359 preparefields item 3 interchangeable，也不是已经知道本头哈希（本页第一件事） interchangeable。**  
   官方写：看见头上有这些，不是已经是 ExecuteTxState。看见拟议头上有 height / time / proposer_address，不是已经 execute interchangeable——本页钉 not already execute 单句。看见头上有这三列，不是已经知道本头哈希（本页第一件事） interchangeable——三件事分开钉。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

3. **看见拟议头 / 看见有拟议块头 / 看见这三列进了请求 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 359 preparefields bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 832 prepfields-nothash interchangeable / 359 preparefields item 1 / 359 preparefields item 2，也不是已经 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事 bundled（359 item 3 余量） interchangeable / 359 preparefields item 3 interchangeable，也不是已经知道本头哈希（本页第一件事） interchangeable / 已经是 ExecuteTxState（本页第二件事） interchangeable。**  
   官方写：看见拟议头，不是已经交差。看见有拟议块头，不是已经 settled interchangeable——本页钉 not already settled 单句。看见这三列进了请求，不是已经是 ExecuteTxState（本页第二件事） interchangeable——三件事分开钉。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头是规范里的做法，本页不抄。Prepare 请求字段 bundled（359）、Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process（359 item 1 余量 / 830）、local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展（359 item 2 余量 / 831）、候选已经是 ExecuteTxState（311）、到了 H 就已经 Prepare 带了扩展（330）、Process 也会在提议者那边叫就已经不用再 Process（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **对得上 not already header-hash ≠ 359 / 311 interchangeable：** 官方把这三列和对上本头哈希分开。
- **头上有这些 not already execute ≠ 已经是 ExecuteTxState interchangeable：** 官方把头上有这些和已经是 ExecuteTxState 分开。
- **拟议头 not already settled ≠ 已经交差 interchangeable：** 官方把拟议头和已经交差分开；359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 对得上 | 不是 already header-hash | 不是候选已经是 ExecuteTxState alone（311） |
| 头上有这些 | 不是 already execute | 不是同一套 already ran-process alone（830） |
| 拟议头 | 不是 already settled | 不是上一高 already this-signed alone（831） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事（359 余量），必须分开对得上 是不是 already header-hash interchangeable / 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable、头上有这些 是不是 already execute interchangeable、拟议头 是不是 already settled interchangeable。可以跳过「看见对得上就已经知道本头哈希 interchangeable / 就已经是 ExecuteTxState interchangeable / 就已经交差 interchangeable」。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成（830 + 831 + 832）。

## 本页不抄

- 怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头。
- Prepare 请求字段 bundled。那是不变量 359。
- Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process。那是不变量 359 item 1 余量 / 830。
- local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展。那是不变量 359 item 2 余量 / 831。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
