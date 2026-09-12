# Level 1 · 工程密码学

优先级：必学  
先修：Level 0  
位置：课程轨。这里不讲币，不讲交易策略。

本层只回答一个问题：

> 这些密码零件各自挡住谁？挡住以后又会引入什么新成本？

先工程，后数学。公式和安全证明后置。

| 课 | 文件 | 覆盖 | 核心问题 |
|---|---|---|---|
| 1.1 | [L01-M01-hash.md](L01-M01-hash.md) | M1.1 | 哈希解决什么，撞了会怎样 |
| 1.2 | [L01-M02-signatures.md](L01-M02-signatures.md) | M1.2 | 签名如何把「授权」钉死 |
| 1.3 | [L01-M03-merkle.md](L01-M03-merkle.md) | M1.3 | 为什么轻节点能少下数据 |
| 1.4 | [L01-M04-canonical-encoding.md](L01-M04-canonical-encoding.md) | M1.4 | 同一对象两种写法如何分裂共识 |
| 1.5 | [L01-M05-pq-preview.md](L01-M05-pq-preview.md) | M1.6 | 后量子先改哪些工程账 |
| 1.6 | [L01-M06-randomness-and-determinism.md](L01-M06-randomness-and-determinism.md) | M1.5 | 三种 nonce 与 `Apply` 禁骰；PREVRANDAO ≠ 工作量 / 无偏骰子（不变量 157） |

试题后置，见 `exams/`。
