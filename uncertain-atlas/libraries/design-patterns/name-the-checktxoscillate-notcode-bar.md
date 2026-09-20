# 模式：把同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事（328 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**例**：[回了不同码 not already has-checktxcode ≠ bundled（328）](../../tracks/implementation/worked-example-checktxoscillate-notcode-vs-bundled.md)。

## 三个名字

1. **同一高度回了不同码 不是 already has-checktxcode：** 看见同一高度 CheckTx 回了不同码 / 同一高度回了不同码 / 码不一致，不是已经有了 CheckTxCode interchangeable / 已经有码交差 interchangeable，不是 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable。

2. **CheckTxCodes 是集合 不是 already ok-defined：** 看见 CheckTxCodes 是集合 / 集合在 / 码收成集合，不是已经能说 OK interchangeable / 已经 OK 交差 interchangeable，不是 317 checktxresponse interchangeable / 328 checktxoscillate item 2 interchangeable。

3. **回了两次 不是 already singleton-set：** 看见回了两次 / 集合可以有多个码 / 不是单元素，不是已经是单元素集合 interchangeable / 已经单元素交差 interchangeable，不是 313 indexer interchangeable / 328 checktxoscillate item 3 interchangeable。

官方把同一高度回了不同码单句、already has-checktxcode、already ok-defined、already singleton-set 写成三个名字。把它们叫成一个「看见同一高度回了不同码就已经有了 CheckTxCode interchangeable / 就已经能说 OK interchangeable / 就已经是单元素 interchangeable」，会把 not already has-checktxcode、not already ok-defined、not already singleton-set 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度回了不同码不是已经有了 CheckTxCode not already has-checktxcode / not already ok-defined / not already singleton-set 正式三事（328 余量），先数清问的是同一高度回了不同码 是不是 already has-checktxcode / 328 / checktxcode-sold-as-stable，是不是集合在 是不是 already ok-defined，还是回了两次 是不是 already singleton-set，再决定要不要同一次发布。328 checktxoscillate vs stable bundled unbundling 在本页 item 1 启动。
