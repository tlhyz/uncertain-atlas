# 例：看见 CheckTx 不该验所有有效性 / 看见有效性依赖排序 / 看见过了 CheckTx is not already already in-checktx interchangeable / already exec-state interchangeable / already settled interchangeable

**层次**：实现 / 不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事（339 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 整池已经交差。本页是「不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事（339 余量）/ not 770 checktx-notordering interchangeable / not 339 checktxweak bundled interchangeable」，不是 CheckTx 弱过滤器 bundled（339），也不是拜占庭能提案一满块无效交易不是已经被池子挡住（771 item 2 余量）或 ProcessProposal 对付这种行为不是已经是 CheckTx（772 item 3 余量）。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。

## 官方三件事

规范把 Requirements 里 CheckTx 不该验所有有效性、有效性依赖排序 和「已经是不该验所有就已经该在 CheckTx 里验排序 interchangeable / 已经是排序会改有效性就已经按将要执行的那份验过 interchangeable / 已经是过了 CheckTx 就已经交差 interchangeable / 已经是 checktxweak bundled interchangeable」分开写成三件独立的实现事，不是「看见不该验所有就已经该在 CheckTx 里验 interchangeable / 就已经按执行态验过 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 CheckTx 不该验所有有效性 / 看见不该把影响有效性的每件事都验完 / 看见不该验排序相关 is not already 已经该在 CheckTx 里验排序 interchangeable / 已经 in-checktx interchangeable / 已经该写进 CheckTx 交差 interchangeable / 339 checktxweak bundled interchangeable / 312 checktxstate interchangeable / checktxweak-sold-as-consensus interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 770 checktx-notordering interchangeable / 339 checktxweak item 1 interchangeable，也不是已经不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事 bundled（339 item 1 余量） interchangeable / 339 checktxweak item 1 interchangeable，也不是已经拜占庭能提案一满块无效交易不是已经被池子挡住（771） interchangeable / 772 checktx-notprocess interchangeable / 33 four gates interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState（312） interchangeable。**  
   官方写：CheckTx 只是弱过滤器。交易不能保证按以后作为（可能的）决定块去执行时那一份状态来验，因此 CheckTx **不该**把影响有效性的每件事都验完，尤其是那些有效性可能依赖交易排序的检查。看见不该验所有，不是已经 in-checktx interchangeable——339 钉 bundled 三事，本页从 item 1 侧钉 not already in-checktx 单句。看见不该验排序相关，不是已经 CheckTx 弱过滤器 bundled（339） interchangeable——339 钉 bundled，本页钉 item 1 第一件事。看见不该验所有，不是已经 CheckTxState 已经是 ExecuteTxState（312） interchangeable——312 另钉。339 checktxweak vs process bundled unbundling 在本页 item 1 启动。

2. **看见有效性依赖排序 / 看见排序会改有效性 / 看见有效性可能依赖交易排序 is not already 已经按将要执行的那份验过 interchangeable / 已经 exec-state interchangeable / 已经按执行态验过交差 interchangeable / 339 checktxweak bundled interchangeable / 312 checktxstate interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 770 checktx-notordering interchangeable / 339 checktxweak item 2 池子挡住 interchangeable / 339 checktxweak item 3 ProcessProposal interchangeable，也不是已经不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事 bundled（339 item 1 余量） interchangeable / 339 checktxweak item 1 interchangeable，也不是已经该在 CheckTx 里验（本页第一件事） interchangeable。**  
   官方写：看见排序会改有效性，不是已经按将要执行的那份验过。看见有效性依赖排序，不是已经 exec-state interchangeable——本页钉 not already exec-state 单句。看见有效性可能依赖交易排序，不是已经该在 CheckTx 里验（本页第一件事） interchangeable——三件事分开钉。339 checktxweak vs process bundled unbundling 在本页 item 1 启动。

3. **看见过了 CheckTx / 看见 CheckTx 绿了 / 看见弱过滤器放过了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差同一句 interchangeable / 339 checktxweak bundled interchangeable / 33 four gates interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 770 checktx-notordering interchangeable / 339 checktxweak item 2 / 339 checktxweak item 3，也不是已经不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事 bundled（339 item 1 余量） interchangeable / 339 checktxweak item 1 interchangeable，也不是已经该在 CheckTx 里验（本页第一件事） interchangeable / 已经按执行态验过（本页第二件事） interchangeable。**  
   官方写：看见过了 CheckTx，不是已经交差。看见 CheckTx 绿了，不是已经 settled interchangeable——本页钉 not already settled 单句。看见弱过滤器放过了，不是已经按执行态验过（本页第二件事） interchangeable——三件事分开钉。339 checktxweak vs process bundled unbundling 在本页 item 1 启动。

怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal` 是规范里的做法，本页不抄。CheckTx 弱过滤器 bundled（339）、拜占庭能提案一满块无效交易不是已经被池子挡住（339 item 2 余量 / 771）、ProcessProposal 对付这种行为不是已经是 CheckTx（339 item 3 余量 / 772）、CheckTxState 已经是 ExecuteTxState（312）、四门已经结算（33）、索引器已经保证不重放（313）是另外那套，本页不抄。

## 官方为什么这样拆

- **不该验所有 not already in-checktx ≠ 339 / 312 interchangeable：** 官方把「不该验所有、尤其是排序相关」和「已经该写进 CheckTx」分开。
- **排序会改有效性 not already exec-state ≠ 已经按执行态验过 interchangeable：** 官方把排序依赖和按将要执行的那份验过分开。
- **过了 CheckTx not already settled ≠ 已经交差 interchangeable：** 官方把过了 CheckTx 和已经交差分开；339 checktxweak vs process bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 不该验所有 | 不是 already in-checktx | 不是 CheckTxState 已经是 ExecuteTxState alone（312） |
| 排序会改有效性 | 不是 already exec-state | 不是四门已经结算 alone（33） |
| 过了 CheckTx | 不是 already settled | 不是拜占庭已经被池子挡住 alone（771） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事（339 余量），必须分开不该验所有 是不是 already in-checktx interchangeable / 339 checktxweak bundled interchangeable / checktxweak-sold-as-consensus interchangeable、排序会改有效性 是不是 already exec-state interchangeable、过了 CheckTx 是不是 already settled interchangeable。可以跳过「看见不该验所有就已经该在 CheckTx 里验 interchangeable / 就已经按执行态验过 interchangeable / 就已经交差 interchangeable」。不要把「不验排序」当不确定已经验完。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。339 checktxweak vs process bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktx-notblocked-vs-bundled.md`](worked-example-checktx-notblocked-vs-bundled.md)（不变量 771 item 2）已写；完成见 772。

## 本页不抄

- 怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal`。
- CheckTx 弱过滤器 bundled。那是不变量 339。
- 拜占庭能提案一满块无效交易不是已经被池子挡住。那是不变量 339 item 2 余量 / 771。
- ProcessProposal 对付这种行为不是已经是 CheckTx。那是不变量 339 item 3 余量 / 772。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- 四门已经结算。那是不变量 33。
- 索引器已经保证不重放。那是不变量 313。
