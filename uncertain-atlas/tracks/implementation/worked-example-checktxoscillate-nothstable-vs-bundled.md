# 例：看见还在振荡 / 看见还在池里 / 看见最终不再振荡 is not already already past-hstable interchangeable / already left-pool interchangeable / already in-block interchangeable

**层次**：实现 / 还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事（328 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事（328 余量）/ not 741 checktxoscillate-nothstable interchangeable / not 328 checktxoscillate bundled interchangeable」，不是 CheckTx 最终不再振荡 bundled（328），也不是同一高度回了不同码不是已经有了 CheckTxCode（740 item 1 余量）或本地不再振荡不是已经各节点同一份 b（742 item 3 余量）。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 官方三件事

规范把 Requirements 里存在 *h_stable* 之后不再振荡、池最终清掉、最终不再振荡不等于已经进块 和「已经是还在振荡就已经过了 h_stable interchangeable / 已经是还在池里就已经离池 interchangeable / 已经是最终不再振荡就已经进了块 interchangeable / 已经是 CheckTx 最终不再振荡 bundled interchangeable」分开写成三件独立的实现事，不是「看见还在振荡就已经过了 h_stable interchangeable / 就已经离池 interchangeable / 就已经进了块 interchangeable」一件事：

1. **看见还在振荡 / 看见还在成功和失败之间来回 / 看见此刻来回 is not already 已经过了 h_stable interchangeable / 已经 past-hstable interchangeable / 已经过了稳定高交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 741 checktxoscillate-nothstable interchangeable / 328 checktxoscillate item 2 interchangeable，也不是已经还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事 bundled（328 item 2 余量） interchangeable / 328 checktxoscillate item 2 interchangeable，也不是已经同一高度回了不同码不是已经有了 CheckTxCode（740） interchangeable / 742 checktxoscillate-notsameb interchangeable / 301 proposed interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：对任意 *tx*，存在高度 *h_stable*，使得任意正确进程在 *h ≥ h_stable* 上都有定义好的 *CheckTxCode*。看见还在振荡，不是已经 past-hstable interchangeable——328 钉 bundled 三事，本页从 item 2 侧钉 not already past-hstable 单句。看见还在成功和失败之间来回，不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable——328 钉 bundled，本页钉 item 2 第一件事。看见此刻来回，不是已经同一高度回了不同码不是已经有了 CheckTxCode（740） interchangeable——740 另钉 item 1。328 checktxoscillate vs stable bundled unbundling 在本页 item 2 续。

2. **看见还在池里 / 看见本节点池里还在 / 看见待得够久之前 is not already 已经离池 interchangeable / 已经 left-pool interchangeable / 已经清掉交差 interchangeable / 328 checktxoscillate bundled interchangeable / 301 proposed interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 741 checktxoscillate-nothstable interchangeable / 328 checktxoscillate item 1 有码 interchangeable / 328 checktxoscillate item 3 同一份 b interchangeable，也不是已经还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事 bundled（328 item 2 余量） interchangeable / 328 checktxoscillate item 2 interchangeable，也不是已经过了 h_stable（本页第一件事） interchangeable。**  
   官方写：这笔若在本节点池里待得够久，会**最终**不再振荡；于是各全节点的池最终会把它清掉。看见还在池里，不是已经 left-pool interchangeable——本页钉 not already left-pool 单句。看见本节点池里还在，不是已经提案收了已经从池里删掉（301） interchangeable——301 另钉提案离池。看见待得够久之前，不是已经过了 h_stable（本页第一件事） interchangeable——三件事分开钉。328 checktxoscillate vs stable bundled unbundling 在本页 item 2 续。

3. **看见最终不再振荡 / 看见不再来回 / 看见 Requirement 13 保证最终 is not already 已经进了块 interchangeable / 已经 in-block interchangeable / 已经进块交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 741 checktxoscillate-nothstable interchangeable / 328 checktxoscillate item 1 / 328 checktxoscillate item 3，也不是已经还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事 bundled（328 item 2 余量） interchangeable / 328 checktxoscillate item 2 interchangeable，也不是已经过了 h_stable（本页第一件事） interchangeable / 已经离池（本页第二件事） interchangeable。**  
   官方写：最终不再振荡之后，池会清掉——要么失败被扔掉，要么一直合法、够流言、够被提案、够被决定。看见最终不再振荡，不是已经 in-block interchangeable——本页钉 not already in-block 单句。看见不再来回，不是已经四门已经结算（33） interchangeable——33 另钉四门。看见 Requirement 13 保证最终，不是已经离池（本页第二件事） interchangeable——三件事分开钉。328 checktxoscillate vs stable bundled unbundling 在本页 item 2 完成。

怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔是规范里的取值或做法，本页不抄。CheckTx 最终不再振荡 bundled（328）、同一高度回了不同码不是已经有了 CheckTxCode（328 item 1 余量 / 740）、本地不再振荡不是已经各节点同一份 b（328 item 3 余量 / 742）、提案收了已经从池里删掉（301）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **还在振荡 not already past-hstable ≠ 328 / 33 interchangeable：** 官方把此刻来回和已经过了 *h_stable* 分开。
- **还在池里 not already left-pool ≠ 已经离池 interchangeable：** 官方把还在池里和最终清掉分开。
- **最终不再振荡 not already in-block ≠ 已经进了块 interchangeable：** 官方把最终不再振荡和已经进块分开；328 checktxoscillate vs stable bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 还在振荡 | 不是 already past-hstable | 不是有码 alone（740） |
| 还在池里 | 不是 already left-pool | 不是提案离池 alone（301） |
| 最终不再振荡 | 不是 already in-block | 不是四门 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事（328 余量），必须分开还在振荡 是不是 already past-hstable interchangeable / 328 checktxoscillate bundled interchangeable / checktxcode-sold-as-stable interchangeable、还在池里 是不是 already left-pool interchangeable、最终不再振荡 是不是 already in-block interchangeable。可以跳过「看见还在振荡就已经过了 h_stable interchangeable / 就已经离池 interchangeable / 就已经进了块 interchangeable」。不要另写怎样实现 CheckTx。328 checktxoscillate vs stable bundled unbundling 在本页 item 2 续（740 + 741）；续 [`worked-example-checktxoscillate-notsameb-vs-bundled.md`](worked-example-checktxoscillate-notsameb-vs-bundled.md)（不变量 742 item 3）已写；完成见 742。

## 本页不抄

- 怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔。
- CheckTx 最终不再振荡 bundled。那是不变量 328。
- 同一高度回了不同码不是已经有了 CheckTxCode。那是不变量 328 item 1 余量 / 740。
- 本地不再振荡不是已经各节点同一份 b。那是不变量 328 item 3 余量 / 742。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
