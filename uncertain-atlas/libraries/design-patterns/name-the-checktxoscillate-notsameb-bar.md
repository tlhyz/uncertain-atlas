# 模式：把本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事（328 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**例**：[本地不再振荡 not already same-b ≠ bundled（328）](../../tracks/implementation/worked-example-checktxoscillate-notsameb-vs-bundled.md)。

## 三个名字

1. **本地 h_p,stable 不是 already global-hstable：** 看见本地 h_p,stable / 本节点稳住了 / 只属于进程 p 的稳定高，不是已经是全局同一高度 interchangeable / 已经全网同一高交差 interchangeable，不是 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable。

2. **本节点不再振荡 不是 already same-b：** 看见本节点不再振荡 / 本地不再振荡 / 本进程 OK 稳住，不是已经各节点同一份 b interchangeable / 已经同一份 b 交差 interchangeable，不是 313 indexer interchangeable / 328 checktxoscillate item 1 interchangeable。

3. **可以把 h_stable 看成 h_p,stable 不是 already local-is-global：** 看见可以把 h_stable 看成 h_p,stable / 实现者本地化 / 一般性不丢，不是已经把本地当成全局 interchangeable / 已经本地即全局交差 interchangeable，不是 33 four gates interchangeable / 328 checktxoscillate item 2 interchangeable。

官方把本地 h_p,stable 单句、already global-hstable、already same-b、already local-is-global 写成三个名字。把它们叫成一个「看见本地不再振荡就已经全网同一高度 interchangeable / 就已经同一份 b interchangeable / 就已经把本地当成全局 interchangeable」，会把 not already global-hstable、not already same-b、not already local-is-global 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事（328 余量），先数清问的是本地 h_p,stable 是不是 already global-hstable / 328 / checktxcode-sold-as-stable，是不是本节点不再振荡 是不是 already same-b，还是可以把 h_stable 看成 h_p,stable 是不是 already local-is-global，再决定要不要同一次发布。328 checktxoscillate vs stable bundled unbundling 在本页 item 3 完成。
