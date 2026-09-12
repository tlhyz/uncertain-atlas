# Fuel 协议档案（思想级）

优先级：进阶（独特思想：UTXO 上声明依赖再并行）  
完整报告：[`report.md`](report.md)

一句话：

> 状态原子仍是 UTXO，交易先声明要碰哪些输出/合约，调度器按不相交并行；冲突仍要一条 canonical 序。

精读：[`../../tracks/parallelism/worked-example-utxo-access-list.md`](../../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143）。谓词通过不是脚本已经跑完。只读访问集重叠不是写冲突。写集相交不是可以并行。并行验证不是已经不需要顺序副作用。不另写第二份 19 节。
