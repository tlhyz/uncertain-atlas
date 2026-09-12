# Aptos 协议档案

优先级：重要  
完整报告：[`report.md`](report.md)

精读：[`../../tracks/state-models/worked-example-ability-vs-resource.md`](../../tracks/state-models/worked-example-ability-vs-resource.md)（不变量 151）。`store` 不是已经是顶层资源。结构体写了 `has copy` 不是这个实例能复制。

一句话：

> 先按某个顺序乐观并行执行，用读写集检测冲突再回滚，最后给出确定性的提交顺序。
