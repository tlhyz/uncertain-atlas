# 反模式：把结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事（316 余量）说成已经同一顺序 / 已经条数等于顺序 / 已经引擎排好

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了列表 not already same order ≠ bundled（316）](../../tracks/implementation/worked-example-exectxresult-notorder-vs-bundled.md)。

## 卖法

把回了列表 / 结果列表 / FinalizeBlockResponse 有列表 写成已经和送来的交易同一顺序 interchangeable / 已经 same order interchangeable / 已经对上 interchangeable / 316 exectxresult bundled interchangeable / 33 four gates interchangeable / exectxresult-sold-as-consensus interchangeable；把条数一样 / 结果条数等于交易条数 / 列表长度对上 写成已经按送来的顺序 interchangeable / 已经 count-implies-order interchangeable；把 Finalize 回了 / FinalizeBlock 回了结果 写成已经由引擎排好 interchangeable / 已经 engine-ordered interchangeable，或已经和 316 exectxresult bundled / exectxresult-sold-as-consensus interchangeable / 707 exectxresult-notorder interchangeable。

## 为什么错

官方把回了列表单句、already same order、already count-implies-order、already engine-ordered 写成三件独立的实现事。把它们卖成 already same order interchangeable / already count-implies-order interchangeable / already engine-ordered interchangeable，会把 not already same order、not already count-implies-order、not already engine-ordered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事（316 余量），必须分开 not already same order、not already count-implies-order、not already engine-ordered 三件事，不要和 316 / 33 / 708 / 709 / 147 糊成一句。

## 和相邻反模式

- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 ExecTxResult vs consensus bundled 全段，不是本页回了列表 item 1 单句边界。
- [maxgas-notcommitted-sold-as-bundled](maxgas-notcommitted-sold-as-bundled.md) 是已提交块 ≠ 按气验过（315），不是本页结果顺序边界。
- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTxResponse 另一对象，不是本页 Finalize 回包顺序边界。
