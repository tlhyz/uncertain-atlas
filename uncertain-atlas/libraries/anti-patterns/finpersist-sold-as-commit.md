# 反模式：把 FinalizeBlock When persist decision / synchronous call 正式三事卖成已经 executes block v / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[persist decision ≠ 已经 executes block v](../../tracks/implementation/worked-example-finpersist-vs-commit.md)。

## 卖法

- 「看见 persists _v_ as the decision 就已经 executes block _v_ / 已经交差。」
- 「看见 calls FinalizeBlock 就已经 persist tx outputs / AppHash / ResultsHash / 已经落盘应用状态。」
- 「看见 +2/3 precommit 决定，synchronous call 就已经是同一句，不用再分 persist decision。」

## 为什么错

官方把 persist decision、calls FinalizeBlock、synchronous call 和 executes block v、persist outputs、decides trigger 写成三件独立的实现事。把它们卖成已经 executes block v、已经 persist outputs、决定触发 interchangeable，会把 persist decision、sync call、outputs persist 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When steps 1–2，必须分开 persist decision、calls FinalizeBlock、synchronous call 三个名字，不要把它们卖成已经 executes block v / 已经交差。

## 和相邻反模式

- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页这种 persist decision 不是已经 executes block v。
- [finalizeafter-sold-as-commit](../../libraries/anti-patterns/finalizeafter-sold-as-commit.md) 是 Finalize 之后就已经交差，不是本页这种 calls FinalizeBlock 不是已经 persist outputs。
- [finexec-sold-as-decided](../../libraries/anti-patterns/finexec-sold-as-decided.md) 是 executes 就已经决定，不是本页 persist decision 三事。
