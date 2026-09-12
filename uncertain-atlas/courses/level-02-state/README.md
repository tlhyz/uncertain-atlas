# Level 2 · 状态模型

优先级：必学  
先修：Level 0 + L1.1 + L1.2

本层回答：

> 账本上的「东西」是余额、是未花费输出，还是带所有权的对象？  
> 并行性是从哪里来的，不是执行器喊出来的。

| 课 | 文件 | 核心问题 |
|---|---|---|
| 2.1 | [L02-M01-utxo.md](L02-M01-utxo.md) | UTXO 为什么天然能并行 |
| 2.2 | [L02-M02-account.md](L02-M02-account.md) | 账户 + nonce 换来了什么；可花 ≠ 锁定已从写回排除；瞬时存储 ≠ 账户持久存储（不变量 159）；后来的 SELFDESTRUCT ≠ 账户已经删掉（不变量 160） |
| 2.3 | [L02-M03-object-resource.md](L02-M03-object-resource.md) | 对象/资源世界观差在哪；`store` ≠ 已经是顶层资源（不变量 151） |
| 2.4 | [L02-M04-design-map.md](L02-M04-design-map.md) | 《状态模型设计地图》 |
| 2.5 | [L02-M05-eutxo.md](L02-M05-eutxo.md) | eUTXO：输出带着数据；引用输入 ≠ 已经花费（不变量 150） |
| 2.6 | [L02-M06-state-occupancy.md](L02-M06-state-occupancy.md) | 谁为全节点磁盘付钱 |

对应横向专题副本：`tracks/state-models/`（本课 2.4 即第一版地图）。覆盖：L2.6 → 额外项 Nervos / M2.4 存储列。
