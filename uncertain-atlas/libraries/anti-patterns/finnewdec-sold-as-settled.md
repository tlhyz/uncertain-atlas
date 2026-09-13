# 反模式：把 FinalizeBlock Contains newly decided block fields 正式三事卖成已经四门已经结算

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Contains newly decided block fields ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finnewdec-vs-proposed.md)。

## 卖法

- 「看见 Finalize 含刚决定那块的字段就已经是四门已经结算 / 已经跑过 Process。」
- 「看见 newly decided block 就是 proposed block / ProcessProposal 含执行所需全部信息。」
- 「看见 height/time 对上了拟议块头，就代表 newly decided 和 proposed 已经分清。」

## 为什么错

官方把 Contains the fields of the newly decided block、newly decided block 对象、fields of the newly decided block 和 proposed / match header 的边界写成三件独立的实现事。把它们卖成已经四门已经结算、已经是 Process 含全部信息、height/time 对上就够，会把刚决定那块的字段、拟议块执行信息和 match header 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 含刚决定那块的字段，必须分开 Contains the fields of the newly decided block、newly decided block、fields of the newly decided block 三个名字，不要把它们卖成已经四门已经结算。
