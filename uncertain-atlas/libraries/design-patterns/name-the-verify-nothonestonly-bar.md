# 模式：把两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事（341 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8。  
**例**：[两边对任意扩展同一裁决 not already honest-only ≠ bundled（341）](../../tracks/implementation/worked-example-verify-nothonestonly-vs-bundled.md)。

## 三个名字

1. **两边同判 不是 already honest-only：** 看见两边对任意扩展同一裁决 / 两边同判 / 所有正确进程对一份扩展反应相同，不是已经只对诚实扩展同一裁决 interchangeable / 已经只对诚实 *e_p* 同判交差 interchangeable，不是 341 verifydet bundled interchangeable / 348 req6-coherence interchangeable / verifydet-sold-as-extend interchangeable。

2. **扩展坏了 不是 already may-diverge：** 看见扩展来自拜占庭 / 扩展坏了 / 扩展可以不诚实，不是已经可以各判各的 interchangeable / 已经各判各的交差 interchangeable，不是 34 vote-extension interchangeable / 341 verifydet item 1 interchangeable。

3. **任意扩展 不是 already req6-same：** 看见任意扩展 / 对任意扩展 *e* / 不是只对诚实交出的扩展，不是已经是 Req 6 诚实对诚实 interchangeable / 已经诚实对诚实交差 interchangeable，不是 348 req6-coherence interchangeable / 341 verifydet item 3 interchangeable。

官方把两边同判单句、already honest-only、already may-diverge、already req6-same 写成三个名字。把它们叫成一个「看见两边同判就已经只对诚实扩展 interchangeable / 就可以各判各的 interchangeable / 就已经是 Req 6 interchangeable」，会把 not already honest-only、not already may-diverge、not already req6-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事（341 余量），先数清问的是两边同判 是不是 already honest-only / 341 / verifydet-sold-as-extend，是不是扩展坏了 是不是 already may-diverge，还是任意扩展 是不是 already req6-same，再决定要不要同一次发布。341 verifydet vs extend bundled unbundling 在本页 item 2 续。
