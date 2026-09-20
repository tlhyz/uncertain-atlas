# 例：看见同一高度回了不同码 / 看见 CheckTxCodes 是集合 / 看见回了两次 is not already already has-checktxcode interchangeable / already ok-defined interchangeable / already singleton-set interchangeable

**层次**：实现 / 同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事（328 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事（328 余量）/ not 740 checktxoscillate-notcode interchangeable / not 328 checktxoscillate bundled interchangeable」，不是 CheckTx 最终不再振荡 bundled（328），也不是还在振荡不是已经过了 h_stable（741 item 2 余量）或本地不再振荡不是已经各节点同一份 b（742 item 3 余量）。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 官方三件事

规范把 Requirements 里高度 *h* 上对同一笔 *tx* 的 `CheckTxResponse` 码收成集合 *CheckTxCodes*、只有单元素才定义 *CheckTxCode* 和「已经是回了不同码就已经有了 CheckTxCode interchangeable / 已经是集合在就已经能说 OK interchangeable / 已经是回了两次就已经是单元素集合 interchangeable / 已经是 CheckTx 最终不再振荡 bundled interchangeable」分开写成三件独立的实现事，不是「看见同一高度回了不同码就已经有了 CheckTxCode interchangeable / 就已经能说 OK interchangeable / 就已经是单元素 interchangeable」一件事：

1. **看见同一高度 CheckTx 回了不同码 / 看见同一高度回了不同码 / 看见码不一致 is not already 已经有了 CheckTxCode interchangeable / 已经 has-checktxcode interchangeable / 已经有码交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 740 checktxoscillate-notcode interchangeable / 328 checktxoscillate item 1 interchangeable，也不是已经同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事 bundled（328 item 1 余量） interchangeable / 328 checktxoscillate item 1 interchangeable，也不是已经还在振荡不是已经过了 h_stable（741） interchangeable / 742 checktxoscillate-notsameb interchangeable / 312 checktxstate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：高度 *h* 上对同一笔 *tx* 的码收成集合 *CheckTxCodes*；不是单元素，*CheckTxCode* **没有定义**。看见同一高度回了不同码，不是已经 has-checktxcode interchangeable——328 钉 bundled 三事，本页从 item 1 侧钉 not already has-checktxcode 单句。看见同一高度 CheckTx 回了不同码，不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable——328 钉 bundled，本页钉 item 1 第一件事。看见码不一致，不是已经 CheckTxState 已经是 ExecuteTxState（312） interchangeable——312 另钉 CheckTxState。328 checktxoscillate vs stable bundled unbundling 在本页 item 1 启动。

2. **看见 CheckTxCodes 是集合 / 看见集合在 / 看见码收成集合 is not already 已经能说 OK interchangeable / 已经 ok-defined interchangeable / 已经 OK 交差 interchangeable / 328 checktxoscillate bundled interchangeable / 317 checktxresponse interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 740 checktxoscillate-notcode interchangeable / 328 checktxoscillate item 2 振荡 interchangeable / 328 checktxoscillate item 3 同一份 b interchangeable，也不是已经同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事 bundled（328 item 1 余量） interchangeable / 328 checktxoscillate item 1 interchangeable，也不是已经有了 CheckTxCode（本页第一件事） interchangeable。**  
   官方写：不是单元素，*CheckTxCode* 没有定义，`OK(CheckTxCode)` 也就没有定义。看见集合在，不是已经 ok-defined interchangeable——本页钉 not already ok-defined 单句。看见 CheckTxCodes 是集合，不是已经 CheckTx 回包已经被引擎用了（317） interchangeable——317 另钉回包。看见码收成集合，不是已经有了 CheckTxCode（本页第一件事） interchangeable——三件事分开钉。328 checktxoscillate vs stable bundled unbundling 在本页 item 1 启动。

3. **看见回了两次 / 看见集合可以有多个码 / 看见不是单元素 is not already 已经是单元素集合 interchangeable / 已经 singleton-set interchangeable / 已经单元素交差 interchangeable / 328 checktxoscillate bundled interchangeable / 313 indexer interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 740 checktxoscillate-notcode interchangeable / 328 checktxoscillate item 2 / 328 checktxoscillate item 3，也不是已经同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事 bundled（328 item 1 余量） interchangeable / 328 checktxoscillate item 1 interchangeable，也不是已经有了 CheckTxCode（本页第一件事） interchangeable / 已经能说 OK（本页第二件事） interchangeable。**  
   官方写：集合可以有多个码；只有它是单元素时，才定义 *CheckTxCode*。看见回了两次，不是已经 singleton-set interchangeable——本页钉 not already singleton-set 单句。看见集合可以有多个码，不是已经索引器已经保证不重放（313） interchangeable——313 另钉索引器。看见不是单元素，不是已经能说 OK（本页第二件事） interchangeable——三件事分开钉。328 checktxoscillate vs stable bundled unbundling 在本页 item 1 完成。

怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔是规范里的取值或做法，本页不抄。CheckTx 最终不再振荡 bundled（328）、还在振荡不是已经过了 h_stable（328 item 2 余量 / 741）、本地不再振荡不是已经各节点同一份 b（328 item 3 余量 / 742）、CheckTxState 已经是 ExecuteTxState（312）、四门已经结算（33）、索引器已经保证不重放（313）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了不同码 not already has-checktxcode ≠ 328 / 33 interchangeable：** 官方把集合和单元素才定义的那个码分开。
- **集合在 not already ok-defined ≠ 已经能说 OK interchangeable：** 官方把集合在和 `OK(CheckTxCode)` 已经有定义分开。
- **回了两次 not already singleton-set ≠ 已经是单元素 interchangeable：** 官方把可以有多个码和已经是单元素分开；328 checktxoscillate vs stable bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一高度回了不同码 | 不是 already has-checktxcode | 不是 CheckTxState alone（312） |
| CheckTxCodes 是集合 | 不是 already ok-defined | 不是 CheckTx 回包 alone（317） |
| 回了两次 | 不是 already singleton-set | 不是索引器 alone（313） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事（328 余量），必须分开同一高度回了不同码 是不是 already has-checktxcode interchangeable / 328 checktxoscillate bundled interchangeable / checktxcode-sold-as-stable interchangeable、集合在 是不是 already ok-defined interchangeable、回了两次 是不是 already singleton-set interchangeable。可以跳过「看见同一高度回了不同码就已经有了 CheckTxCode interchangeable / 就已经能说 OK interchangeable / 就已经是单元素 interchangeable」。不要另写怎样实现 CheckTx。328 checktxoscillate vs stable bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktxoscillate-nothstable-vs-bundled.md`](worked-example-checktxoscillate-nothstable-vs-bundled.md)（不变量 741 item 2）已写；完成见 742。

## 本页不抄

- 怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔。
- CheckTx 最终不再振荡 bundled。那是不变量 328。
- 还在振荡不是已经过了 h_stable。那是不变量 328 item 2 余量 / 741。
- 本地不再振荡不是已经各节点同一份 b。那是不变量 328 item 3 余量 / 742。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- 索引器已经保证不重放。那是不变量 313。
- 四门已经结算。那是不变量 33。
