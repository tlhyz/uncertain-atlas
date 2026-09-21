# 模式：把不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事（339 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**例**：[不该验排序相关有效性 not already in-checktx ≠ bundled（339）](../../tracks/implementation/worked-example-checktx-notordering-vs-bundled.md)。

## 三个名字

1. **不该验所有 不是 already in-checktx：** 看见 CheckTx 不该验所有有效性 / 不该把影响有效性的每件事都验完 / 不该验排序相关，不是已经该在 CheckTx 里验排序 interchangeable / 已经该写进 CheckTx 交差 interchangeable，不是 339 checktxweak bundled interchangeable / 312 checktxstate interchangeable / checktxweak-sold-as-consensus interchangeable。

2. **排序会改有效性 不是 already exec-state：** 看见有效性依赖排序 / 排序会改有效性 / 有效性可能依赖交易排序，不是已经按将要执行的那份验过 interchangeable / 已经按执行态验过交差 interchangeable，不是 312 checktxstate interchangeable / 339 checktxweak item 2 interchangeable。

3. **过了 CheckTx 不是 already settled：** 看见过了 CheckTx / CheckTx 绿了 / 弱过滤器放过了，不是已经交差 interchangeable / 已经交差同一句 interchangeable，不是 33 four gates interchangeable / 339 checktxweak item 3 interchangeable。

官方把不该验所有单句、already in-checktx、already exec-state、already settled 写成三个名字。把它们叫成一个「看见不该验所有就已经该在 CheckTx 里验 interchangeable / 就已经按执行态验过 interchangeable / 就已经交差 interchangeable」，会把 not already in-checktx、not already exec-state、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事（339 余量），先数清问的是不该验所有 是不是 already in-checktx / 339 / checktxweak-sold-as-consensus，是不是排序会改有效性 是不是 already exec-state，还是过了 CheckTx 是不是 already settled，再决定要不要同一次发布。339 checktxweak vs process bundled unbundling 在本页 item 1 启动。
