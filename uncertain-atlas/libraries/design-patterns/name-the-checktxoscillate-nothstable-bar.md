# 模式：把还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事（328 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**例**：[还在振荡 not already past-hstable ≠ bundled（328）](../../tracks/implementation/worked-example-checktxoscillate-nothstable-vs-bundled.md)。

## 三个名字

1. **还在振荡 不是 already past-hstable：** 看见还在振荡 / 还在成功和失败之间来回 / 此刻来回，不是已经过了 h_stable interchangeable / 已经过了稳定高交差 interchangeable，不是 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable。

2. **还在池里 不是 already left-pool：** 看见还在池里 / 本节点池里还在 / 待得够久之前，不是已经离池 interchangeable / 已经清掉交差 interchangeable，不是 301 proposed interchangeable / 328 checktxoscillate item 1 interchangeable。

3. **最终不再振荡 不是 already in-block：** 看见最终不再振荡 / 不再来回 / Requirement 13 保证最终，不是已经进了块 interchangeable / 已经进块交差 interchangeable，不是 33 four gates interchangeable / 328 checktxoscillate item 3 interchangeable。

官方把还在振荡单句、already past-hstable、already left-pool、already in-block 写成三个名字。把它们叫成一个「看见还在振荡就已经过了 h_stable interchangeable / 就已经离池 interchangeable / 就已经进了块 interchangeable」，会把 not already past-hstable、not already left-pool、not already in-block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事（328 余量），先数清问的是还在振荡 是不是 already past-hstable / 328 / checktxcode-sold-as-stable，是不是还在池里 是不是 already left-pool，还是最终不再振荡 是不是 already in-block，再决定要不要同一次发布。328 checktxoscillate vs stable bundled unbundling 在本页 item 2 续。
