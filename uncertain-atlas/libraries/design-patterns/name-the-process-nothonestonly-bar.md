# 模式：把两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事（340 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5。  
**例**：[两边对任意块同一裁决 not already honest-only ≠ bundled（340）](../../tracks/implementation/worked-example-process-nothonestonly-vs-bundled.md)。

## 三个名字

1. **两边同判 不是 already honest-only：** 看见两边对任意块同一裁决 / 两边同判 / 所有正确进程对一份提案反应相同，不是已经只对诚实提案同一裁决 interchangeable / 已经只对诚实 *u_p* 同判交差 interchangeable，不是 340 processdet bundled interchangeable / 347 req3-coherence interchangeable / processdet-sold-as-prepare interchangeable。

2. **提议者坏了 不是 already may-diverge：** 看见提议者是拜占庭 / 提议者坏了 / 提议者可以不诚实，不是已经可以各判各的 interchangeable / 已经各判各的交差 interchangeable，不是 33 four gates interchangeable / 340 processdet item 1 interchangeable。

3. **任意块 不是 already req3-same：** 看见任意块 / 对任意块 *u* / 不是只对诚实准备好的提案，不是已经是 Req 3 诚实对诚实 interchangeable / 已经诚实对诚实交差 interchangeable，不是 347 req3-coherence interchangeable / 340 processdet item 3 interchangeable。

官方把两边同判单句、already honest-only、already may-diverge、already req3-same 写成三个名字。把它们叫成一个「看见两边同判就已经只对诚实提案 interchangeable / 就可以各判各的 interchangeable / 就已经是 Req 3 interchangeable」，会把 not already honest-only、not already may-diverge、not already req3-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事（340 余量），先数清问的是两边同判 是不是 already honest-only / 340 / processdet-sold-as-prepare，是不是提议者坏了 是不是 already may-diverge，还是任意块 是不是 already req3-same，再决定要不要同一次发布。340 processdet vs prepare bundled unbundling 在本页 item 2 续。
