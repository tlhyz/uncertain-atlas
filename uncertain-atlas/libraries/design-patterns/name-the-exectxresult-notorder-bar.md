# 模式：把结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事（316 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / Specifics of `ExecTxResult`。  
**例**：[回了列表 not already same order ≠ bundled（316）](../../tracks/implementation/worked-example-exectxresult-notorder-vs-bundled.md)。

## 三个名字

1. **回了列表 不是 already same order：** 看见结果列表 / FinalizeBlockResponse 有列表，不是已经和送来的交易同一顺序 interchangeable / 已经对上 interchangeable，不是 316 exectxresult bundled interchangeable / 33 four gates interchangeable / exectxresult-sold-as-consensus interchangeable。

2. **条数一样 不是 already count-implies-order：** 看见结果条数等于交易条数 / 列表长度对上，不是已经按送来的顺序 interchangeable / 已经长度等于顺序 interchangeable，不是 316 exectxresult item 2 interchangeable / 708 exectxresult-notexcluded interchangeable。

3. **Finalize 回了 不是 already engine-ordered：** 看见 FinalizeBlock 回了结果 / 引擎收下了回包，不是已经由引擎排好 interchangeable / 已经引擎替你排好 interchangeable，不是 316 exectxresult item 3 interchangeable / 709 exectxresult-notheader interchangeable。

官方把回了列表单句、already same order、already count-implies-order、already engine-ordered 写成三个名字。把它们叫成一个「看见回了就已经对上顺序 interchangeable / 就已经条数等于顺序 interchangeable / 就已经引擎排好 interchangeable」，会把 not already same order、not already count-implies-order、not already engine-ordered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事（316 余量），先数清问的是回了列表 是不是 already same order / 316 / exectxresult-sold-as-consensus，是不是条数一样 是不是 already count-implies-order，还是 Finalize 回了 是不是 already engine-ordered，再决定要不要同一次发布。316 exectxresult vs consensus bundled unbundling 在本页 item 1 完成。
