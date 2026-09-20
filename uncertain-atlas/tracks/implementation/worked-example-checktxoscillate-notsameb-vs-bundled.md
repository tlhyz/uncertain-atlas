# 例：看见本地 h_p,stable / 看见本节点不再振荡 / 看见本节点稳住了 is not already already global-hstable interchangeable / already same-b interchangeable / already local-is-global interchangeable

**层次**：实现 / 本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事（328 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事（328 余量）/ not 742 checktxoscillate-notsameb interchangeable / not 328 checktxoscillate bundled interchangeable」，不是 CheckTx 最终不再振荡 bundled（328），也不是同一高度回了不同码不是已经有了 CheckTxCode（740 item 1 余量）或还在振荡不是已经过了 h_stable（741 item 2 余量）。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 官方三件事

规范把 Requirements 里全局 *h_stable*、可以本地的 *h_p,stable*、*b* 必须各正确进程相同 和「已经是本地 h_p,stable 就已经是全局同一高度 interchangeable / 已经是本节点不再振荡就已经同一份 b interchangeable / 已经是本节点稳住了就已经把本地当成全局 interchangeable / 已经是 CheckTx 最终不再振荡 bundled interchangeable」分开写成三件独立的实现事，不是「看见本地不再振荡就已经全网同一高度 interchangeable / 就已经同一份 b interchangeable / 就已经把本地当成全局 interchangeable」一件事：

1. **看见本地 h_p,stable / 看见本节点稳住了 / 看见只属于进程 p 的稳定高 is not already 已经是全局同一高度 interchangeable / 已经 global-hstable interchangeable / 已经全网同一高交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 742 checktxoscillate-notsameb interchangeable / 328 checktxoscillate item 3 interchangeable，也不是已经本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事 bundled（328 item 3 余量） interchangeable / 328 checktxoscillate item 3 interchangeable，也不是已经同一高度回了不同码不是已经有了 CheckTxCode（740） interchangeable / 741 checktxoscillate-nothstable interchangeable / 313 indexer interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：Requirement 13 写的是全局 *h_stable*；实现者也可以把它看成只属于进程 *p* 的 *h_p,stable*，一般性不丢。看见本地 *h_p,stable*，不是已经 global-hstable interchangeable——328 钉 bundled 三事，本页从 item 3 侧钉 not already global-hstable 单句。看见本节点稳住了，不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable——328 钉 bundled，本页钉 item 3 第一件事。看见只属于进程 *p* 的稳定高，不是已经还在振荡不是已经过了 *h_stable*（741） interchangeable——741 另钉 item 2。328 checktxoscillate vs stable bundled unbundling 在本页 item 3 完成。

2. **看见本节点不再振荡 / 看见本地不再振荡 / 看见本进程 OK 稳住 is not already 已经各节点同一份 b interchangeable / 已经 same-b interchangeable / 已经同一份 b 交差 interchangeable / 328 checktxoscillate bundled interchangeable / 313 indexer interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 742 checktxoscillate-notsameb interchangeable / 328 checktxoscillate item 1 有码 interchangeable / 328 checktxoscillate item 2 振荡 interchangeable，也不是已经本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事 bundled（328 item 3 余量） interchangeable / 328 checktxoscillate item 3 interchangeable，也不是已经是全局同一高度（本页第一件事） interchangeable。**  
   官方写：*b* **必须**各正确进程相同。看见本节点不再振荡，不是已经 same-b interchangeable——本页钉 not already same-b 单句。看见本地不再振荡，不是已经索引器已经保证不重放（313） interchangeable——313 另钉索引器。看见本进程 OK 稳住，不是已经是全局同一高度（本页第一件事） interchangeable——三件事分开钉。328 checktxoscillate vs stable bundled unbundling 在本页 item 3 完成。

3. **看见可以把 h_stable 看成 h_p,stable / 看见实现者本地化 / 看见一般性不丢 is not already 已经把本地当成全局 interchangeable / 已经 local-is-global interchangeable / 已经本地即全局交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable，也不是已经 CheckTx 最终不再振荡 bundled（328） interchangeable / 742 checktxoscillate-notsameb interchangeable / 328 checktxoscillate item 1 / 328 checktxoscillate item 2，也不是已经本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事 bundled（328 item 3 余量） interchangeable / 328 checktxoscillate item 3 interchangeable，也不是已经是全局同一高度（本页第一件事） interchangeable / 已经同一份 b（本页第二件事） interchangeable。**  
   官方把可以本地的稳定高度和必须全网同一份 *b* 分开——本地化 *h_p,stable* 一般性不丢，不等于已经把本地当成全局、也不等于 *b* 可以各进程不同。看见可以把 *h_stable* 看成 *h_p,stable*，不是已经 local-is-global interchangeable——本页钉 not already local-is-global 单句。看见实现者本地化，不是已经四门已经结算（33） interchangeable——33 另钉四门。看见一般性不丢，不是已经同一份 *b*（本页第二件事） interchangeable——三件事分开钉。328 checktxoscillate vs stable bundled unbundling 在本页 item 3 完成。

怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔是规范里的取值或做法，本页不抄。CheckTx 最终不再振荡 bundled（328）、同一高度回了不同码不是已经有了 CheckTxCode（328 item 1 余量 / 740）、还在振荡不是已经过了 h_stable（328 item 2 余量 / 741）、索引器已经保证不重放（313）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **本地 h_p,stable not already global-hstable ≠ 328 / 33 interchangeable：** 官方把可以本地的稳定高度和全局 *h_stable* 分开。
- **本节点不再振荡 not already same-b ≠ 已经各节点同一份 b interchangeable：** 官方把本地稳住和 *b* 必须各正确进程相同分开。
- **可以把 h_stable 看成 h_p,stable not already local-is-global ≠ 已经把本地当成全局 interchangeable：** 官方把本地化一般性不丢和已经把本地当成全局分开；328 checktxoscillate vs stable bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本地 h_p,stable | 不是 already global-hstable | 不是过了 h_stable alone（741） |
| 本节点不再振荡 | 不是 already same-b | 不是索引器 alone（313） |
| 可以把 h_stable 看成 h_p,stable | 不是 already local-is-global | 不是四门 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事（328 余量），必须分开本地 h_p,stable 是不是 already global-hstable interchangeable / 328 checktxoscillate bundled interchangeable / checktxcode-sold-as-stable interchangeable、本节点不再振荡 是不是 already same-b interchangeable、可以把 h_stable 看成 h_p,stable 是不是 already local-is-global interchangeable。可以跳过「看见本地不再振荡就已经全网同一高度 interchangeable / 就已经同一份 b interchangeable / 就已经把本地当成全局 interchangeable」。不要另写怎样实现 CheckTx。328 checktxoscillate vs stable bundled unbundling 在本页 item 3 完成（740 + 741 + 742）。

## 本页不抄

- 怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔。
- CheckTx 最终不再振荡 bundled。那是不变量 328。
- 同一高度回了不同码不是已经有了 CheckTxCode。那是不变量 328 item 1 余量 / 740。
- 还在振荡不是已经过了 h_stable。那是不变量 328 item 2 余量 / 741。
- 索引器已经保证不重放。那是不变量 313。
- 四门已经结算。那是不变量 33。
