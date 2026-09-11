# 决策：状态模型

状态：未决定。  
依据：`courses/level-02-state/L02-M04-design-map.md`

| 方案 | Bitcoin | Ethereum | Solana | Sui | Aptos | 不确定候选 |
|---|---|---|---|---|---|---|
| 模型 | UTXO | Account | Account+声明锁 | Object | Resource+Block-STM | （空） |
| 安全性 | | | | | | |
| 复杂度 | | | | | | |
| 并行 | 输入不交 | 热点串行 | 声明锁 | owned/shared | 乐观回滚 | |
| 后量子成本 | | | | | | |
| 测试难度 | | | | | | |
| 升级 | | | | | | |

在 L4–L6 档案补齐前，禁止把最后一列填成口号。
