# 模式：把 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事（376 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[回了 UNKNOWN not already fourgates ≠ bundled（376）](../../tracks/implementation/worked-example-proposalstatus-notfourgates-vs-bundled.md)。

## 三个名字

1. **回了 UNKNOWN 不是 already fourgates：** 看见回了 UNKNOWN / UNKNOWN 一律是错、引擎当应用坏了会崩 / 回了 UNKNOWN 状态，不是已经是四门已经结算 interchangeable / 已经 fourgates interchangeable / 已经是四门已经结算交差 interchangeable，不是 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable。

2. **崩了 不是 already settled：** 看见崩了 / 引擎当应用坏了会崩 / 崩，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 33 four gates interchangeable / 376 proposalstatus item 2 interchangeable。

3. **有枚举 不是 already selected：** 看见有枚举 / ProposalStatus 枚举 / 有 UNKNOWN/ACCEPT/REJECT，不是已经选型 interchangeable / 已经 selected interchangeable / 已经选型交差 interchangeable，不是 354 processwhen interchangeable / 376 proposalstatus item 3 interchangeable。

官方把回了 UNKNOWN、不是已经交差、不是已经选型写成三个名字。把它们叫成一个「看见回了 UNKNOWN 就已经是四门已经结算 interchangeable / 就已经交差 interchangeable / 就已经选型 interchangeable」，会把 not already fourgates、not already settled、not already selected 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事（376 余量），先数清问的是回了 UNKNOWN 是不是 already fourgates / 376 / proposalstatus-sold-as-prevote，是不是崩了 是不是 already settled，还是有枚举 是不是 already selected，再决定要不要同一次发布。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 1 启动。
