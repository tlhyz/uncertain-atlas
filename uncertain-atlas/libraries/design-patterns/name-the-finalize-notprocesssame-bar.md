# 模式：把两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事（342 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12。  
**例**：[两边状态机复制 not already process-same ≠ bundled（342）](../../tracks/implementation/worked-example-finalize-notprocesssame-vs-bundled.md)。

## 三个名字

1. **状态机复制 不是 already process-same：** 看见两边状态机复制 / 应用状态一起演化 / 各正确进程上的应用状态一起演化，不是已经是 Process 对任意块同一 Accept/Reject interchangeable / 已经 Process 同判交差 interchangeable，不是 342 finalizedet bundled interchangeable / 340 processdet interchangeable / finalizedet-sold-as-prepare interchangeable。

2. **状态一起演化 不是 already prepare-nondet：** 看见两边状态一起走 / 状态一起演化 / 不是只靠 Process 同判，不是已经是 Prepare 可以不确定 interchangeable / 已经和 Prepare 同一把尺交差 interchangeable，不是 338 preparenondet interchangeable / 342 finalizedet item 1 interchangeable。

3. **Agreement 不是 already settled：** 看见 Agreement / 共识 Agreement / 已经造出 *s_h* 和 *T_h*，不是已经交差 interchangeable / 已经交差同一句 interchangeable，不是 335 finalizepersist interchangeable / 342 finalizedet item 2 interchangeable。

官方把状态机复制单句、already process-same、already prepare-nondet、already settled 写成三个名字。把它们叫成一个「看见状态机复制就已经是 Process 同判 interchangeable / 就已经是 Prepare nondet interchangeable / 就已经交差 interchangeable」，会把 not already process-same、not already prepare-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事（342 余量），先数清问的是状态机复制 是不是 already process-same / 342 / finalizedet-sold-as-prepare，是不是状态一起演化 是不是 already prepare-nondet，还是 Agreement 是不是 already settled，再决定要不要同一次发布。342 finalizedet vs prepare bundled unbundling 在本页 item 3 完成。
