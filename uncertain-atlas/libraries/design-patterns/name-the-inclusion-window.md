# 先给证明纳入窗起名（name-the-inclusion-window）

> 类型：design pattern  
> 对读：不变量 214；C218；反模式 [`../anti-patterns/window-sold-as-confirm.md`](../anti-patterns/window-sold-as-confirm.md)；[`../../tracks/finality/worked-example-inclusion-window-vs-confirm.md`](../../tracks/finality/worked-example-inclusion-window-vs-confirm.md)。

设计或讲解「证明能多等所以已经能快确认」时，先分开四个名字：

1. **加长纳入窗** — 证明最晚能进到下一纪元最后一槽，不是已经有确认规则。
2. **下一纪元末** — 纳入范围的新上沿，不是已经改了选头。
3. **目标奖不看延迟** — 合法窗里正确目标仍有非零奖，不是已经改了目标票含义。
4. **7045** — 加长纳入与底线奖，不是 7549，也不是三种「到了」。

四句对照：

- 看见的是纳入窗，还是已经有确认规则？
- 看见的是下一纪元末，还是已经改了 LMD-GHOST？
- 看见的是目标奖不看延迟，还是目标票已经换了含义？
- 这是 7045，还是已经是 7549 / 127 / 198？

不要和委员会下标≠已没委员会（不变量 198）、head≠justified≠finalized（不变量 127）、处理完一块≠改头（不变量 149）糊成「证明已经确认」一句。
