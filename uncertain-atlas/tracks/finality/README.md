# 横向地图：最终性

学完各波后必须回这里改表。空单元格表示未写或不适用，禁止用营销句填。  
分区精读：[`../consensus/worked-example-partition.md`](../consensus/worked-example-partition.md)。  
弱主观性：[`worked-example-weak-subjectivity.md`](worked-example-weak-subjectivity.md)（finalized ≠ 从创世同步同样安全）。  
平行链阶段：[`worked-example-backed-vs-available.md`](worked-example-backed-vs-available.md)（backed ≠ 可用 ≠ 批准 ≠ GRANDPA）。

| 系统 | 协议对象 | 用户常误认 | 分区时 | 档案/课 |
|---|---|---|---|---|
| Bitcoin | 无「最终」；最重链 | k 确认 = 不可逆 | 两边可长 | L3.1 |
| CometBFT | 高度上的 commit | 投票中 = 已提交 | 倾向停 | L4.3 |
| Ethereum | head / justified / finalized | 出块 = finalized | 头可摆；最终有弱主观性 | L5.2 |
| Ethereum WS 同步 | 未过期的 `Checkpoint` + 路径命中 | finalized = 从创世一样安全 | 过期检查点；旧钥匙已解绑 | 精读 |
| Ethereum Altair LC | 512 抽样超多数签的信标头 | 抽样 2/3 = Casper finalized | 跟的是委员会视图，不是全集合最终 | L9.6 / 精读 |
| Avalanche | 抽样固化 | 参数 = BFT commit | 视参数 | 档案 |
| Algorand | 论文下快速最终（以规范为准） | 抽签 = 已结算 | 视同步假设 | 档案 |
| Solana | 确认深度 + Tower 锁 | 槽时间 = commit | 活性事故有记录待原文 | L6.1 |
| Sui | owned 快路径 vs shared 共识 | 所有交易同一「到了」 | 视路径 | L6.2 |
| Aptos | 共识给出的序 L 上的 commit | STM 跑完 = 最终 | 同 BFT 家族 | L6.3 |
| 乐观 rollup | L1 最终 + 窗口 + 根 | L2 UI = 兑付 | 排序者活性 | L7.4 |
| Celestia | 头 commit + DA 应可用 | 头最终 = 执行最终；NMT 齐 = 方阵已可用 | 同 CometBFT 倾向 | L7.2 / 精读 |
| Polkadot | 中继 GRANDPA 最终（平行块先可用） | collator RPC / backed = 共享安全最终 | 须读中继 | L7.3 / 精读 |
| Kaspa | DAG 上蓝序变深 | 进了一个块 = 最终 | 视图/传播分裂 | L3.8 |
| Zcash / Monero | 最重链家族 | 屏蔽/环 = 另一种最终 | 两边可长 | L8 |
| Mina | 最重链 + 递归证明（点名 SNARKed） | 22kB = 已结算状态；验 π = 最新 staged | 两边可长；DA 仍在；staged 另算 | L8.3 / 精读 |
| Nervos | Nakamoto 变体（Consensus RFC） | 占用不等式 = 最终 | 两边可长 | L2.6 / 档案 |
| Fuel | 取决于排序从哪来 | 并行执行完 = 最终 | 视部署 | 档案 |
| NEAR | `last_final_block`（BFT 谓词）≠ `last_ds_final_block` | 出块 / Doomslug = commit | 视 approvals 与缺 chunk | 思想级档案 |
| Monad（文档） | 共识最终的是**顺序**；状态根延迟 `D` 块 | 顺序最终 = 余额已到 | 视其 BFT；执行滞后是另一轴 | 仅过滤器页 |

「不确定」列空。若产品要说「到了」，先在 L10.1 选一行协议对象。
