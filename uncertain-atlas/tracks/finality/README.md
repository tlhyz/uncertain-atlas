# 横向地图：最终性

学完各波后必须回这里改表。空单元格表示未写或不适用，禁止用营销句填。

| 系统 | 协议对象 | 用户常误认 | 分区时 | 档案/课 |
|---|---|---|---|---|
| Bitcoin | 无「最终」；最重链 | k 确认 = 不可逆 | 两边可长 | L3.1 |
| CometBFT | 高度上的 commit | 投票中 = 已提交 | 倾向停 | L4.3 |
| Ethereum | head / justified / finalized | 出块 = finalized | 头可摆；最终有弱主观性 | L5.2 |
| Avalanche | 抽样固化 | 参数 = BFT commit | 视参数 | 档案 |
| Solana | 确认深度 + Tower 锁 | 槽时间 = commit | 活性事故有记录待原文 | L6.1 |
| Sui | owned 快路径 vs shared 共识 | 所有交易同一「到了」 | 视路径 | L6.2 |
| 乐观 rollup | L1 最终 + 窗口 + 根 | L2 UI = 兑付 | 排序者活性 | L7.4 |

「不确定」列空。若产品要说「到了」，先在 L10.1 选一行协议对象。
