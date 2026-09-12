# Level 6 · 高吞吐：三种并行世界观

优先级：重要  
先修：L2 全部、L4 或 L5 其一、L3 网络直觉  
档案：[`../../protocols/solana/`](../../protocols/solana/README.md)、[`../../protocols/sui/`](../../protocols/sui/README.md)、[`../../protocols/aptos/`](../../protocols/aptos/README.md)

毕业：能拆开「高 TPS」的五个来源（状态 / 执行 / 网络 / 协议 / 硬件），并说出三种并行世界观各拿什么换。

禁止：把官网吞吐数字当事实；把 STM 说成可以代替共识。

覆盖：M6.1→L6.1 + 博物馆 2020-12-04、2022-04-30、2022-06-01、2022-09-30、2023-02-25、2024-02-06、2025-05-02；M6.2→L6.2 + 博物馆 2024-11-21、2026-01-14、2026-05 气费砸币、2026-05 DKG 未落盘；M6.3→L6.3 + Block-STM 工作实例（不变量 122）；M6.4+M6.5→L6.4（含 J 节；Avalanche 对照的是抽样，C-Chain 事故见不变量 119）。

| 课 | 文件 | 核心问题 |
|---|---|---|
| 6.1 | [L06-M01-solana-declare.md](L06-M01-solana-declare.md) | 为何先报读写集才能并行 |
| 6.2 | [L06-M02-sui-ownership.md](L06-M02-sui-ownership.md) | 所有权如何决定要不要全球排队 |
| 6.3 | [L06-M03-aptos-stm.md](L06-M03-aptos-stm.md) | 未排死时为何敢并行 |
| 6.4 | [L06-M04-three-worldviews.md](L06-M04-three-worldviews.md) | 三张地图怎么叠，不确定偷哪张 |
