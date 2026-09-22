# 模式：把 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事（342 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12。  
**例**：[Finalize 算出的结果必须只依赖上一份状态和决定块 not already printed ≠ bundled（342）](../../tracks/implementation/worked-example-finalize-notprinted-vs-bundled.md)。

## 三个名字

1. **结果必须确定 不是 already printed：** 看见 Finalize 算出的结果必须只依赖上一份状态和决定块 / *T_h* 必须确定 / 造出交易结果集合，不是已经是 Code/Data 印进本头 interchangeable / 已经印进本头交差 interchangeable，不是 342 finalizedet bundled interchangeable / 316 exectxresult interchangeable / finalizedet-sold-as-prepare interchangeable。

2. **只依赖这两份 不是 already same-order：** 看见只依赖这两份 / 只依赖 *s_{h-1}* 和 *v* / 结果内容只依赖这两份，不是已经是回执顺序对上 interchangeable / 已经顺序对上交差 interchangeable，不是 316 exectxresult interchangeable / 342 finalizedet item 1 interchangeable。

3. **造出了 *T* 不是 already persisted：** 看见造出了 *T* / 造出了交易结果集合 / *T_{p,h}* 回来了，不是已经落盘 interchangeable / 已经落盘交差 interchangeable，不是 335 finalizepersist interchangeable / 342 finalizedet item 3 interchangeable。

官方把结果必须确定单句、already printed、already same-order、already persisted 写成三个名字。把它们叫成一个「看见结果必须确定就已经印进本头 interchangeable / 就已经是回执顺序对上 interchangeable / 就已经落盘 interchangeable」，会把 not already printed、not already same-order、not already persisted 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事（342 余量），先数清问的是结果必须确定 是不是 already printed / 342 / finalizedet-sold-as-prepare，是不是只依赖这两份 是不是 already same-order，还是造出了 *T* 是不是 already persisted，再决定要不要同一次发布。342 finalizedet vs prepare bundled unbundling 在本页 item 2 续。
