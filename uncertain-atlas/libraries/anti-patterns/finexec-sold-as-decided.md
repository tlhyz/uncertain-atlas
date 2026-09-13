# 反模式：把 FinalizeBlock When Application executes block v 正式三事说成已经把 v 落成这一高的决定

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Application executes block v ≠ 已经把 v 落成这一高的决定](../../tracks/implementation/worked-example-finexec-vs-decided.md)。

## 错在哪里

把 `_p_'s Application executes block _v_` 写成已经把 _v_ 落成这一高的决定，或已经交差；把 Application executes block v 写成已经每个验证者都跑过 Process，或已经是 ExecuteTxState；把 executes block v 写成已经套用 candidate 就不需要再在 Finalize 执行，或已经 Process 跑过就不执行，或已经和 362 / 360 / 460 / 452 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v 正式三事，必须分开 executes block v、Process 保证、apply candidate 三件事，不要和 362 / 360 / 460 / 452 糊成一句。
