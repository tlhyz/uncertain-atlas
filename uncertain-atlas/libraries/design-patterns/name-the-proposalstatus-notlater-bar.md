# 模式：把 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事（376 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[回了 REJECT not already later ≠ bundled（376）](../../tracks/implementation/worked-example-proposalstatus-notlater-vs-bundled.md)。

## 三个名字

1. **回了 REJECT 不是 already later：** 看见回了 REJECT / REJECT 表示应用认为提案非法、共识会发 Prevote nil / 回了 REJECT 状态，不是已经能稍后改裁决 interchangeable / 已经 later interchangeable / 已经能稍后改裁决交差 interchangeable，不是 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable。

2. **发了 nil 不是 already outofblock：** 看见发了 nil / 共识会发 Prevote nil / 发了 Prevote nil，不是已经没进块 interchangeable / 已经 outofblock interchangeable / 已经没进块交差 interchangeable，不是 354 processwhen interchangeable / 876 proposalstatus-notsettled interchangeable。

3. **非法 不是 already settled：** 看见非法 / 应用认为提案非法 / 非法状态，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 875 proposalstatus-notfourgates interchangeable / 376 proposalstatus item 2 interchangeable。

官方把回了 REJECT、不是已经没进块、不是已经交差写成三个名字。把它们叫成一个「看见回了 REJECT 就已经能稍后改裁决 interchangeable / 就已经没进块 interchangeable / 就已经交差 interchangeable」，会把 not already later、not already outofblock、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事（376 余量），先数清问的是回了 REJECT 是不是 already later / 376 / proposalstatus-sold-as-prevote，是不是发了 nil 是不是 already outofblock，还是非法 是不是 already settled，再决定要不要同一次发布。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 3 完成。
