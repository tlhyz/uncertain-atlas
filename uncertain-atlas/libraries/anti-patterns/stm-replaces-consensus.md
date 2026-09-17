# 反模式：STM 代替共识

把乐观并行执行说成「所以不需要全局顺序 / 最终性」。  
Block-STM 的正确性定义在序列 L 上。没有 L，对错无定义。  
见 L6.3、Aptos 档案第 3、6、7 节、[工作实例](../../tracks/parallelism/worked-example-block-stm.md)。亲戚：[stm-done-sold-as-final](stm-done-sold-as-final.md)（跑完 ≠ 已最终）。
