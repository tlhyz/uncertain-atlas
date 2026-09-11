# 决策：共识

状态：未决定。  
强烈对照：`protocols/bitcoin/report.md`、`protocols/cometbft/report.md`

| 维度 | Nakamoto | CometBFT | Avalanche | Gasper | 不确定候选 |
|---|---|---|---|---|---|
| 最终性 | 概率 | 确定 | 概率固化 | 头可摆 + FFG 最终 | （空） |
| 分区 | 可两边长 | 倾向停 | 视参数 | 头摆 / 最终延迟 | |
| 委员会 | 无许可算力 | 验证者集合 | 抽样 | 质押验证者 | |
| 投票流量 | 无 BFT 票 | 每轮全员量级 | 每轮少量 | attestation + 聚合 | |
| 后量子 | 主要打用户签 | 用户签+投票签 | 视实现 | 用户签+投票签 | |
| 结算文案 | 需确认数 | commit 可当结算 | 要解释参数 | 须钉 finalized | |
| 罚没执行 | 无验证者罚没对象 | 引擎交证据，应用写公式 | 视实现 / 产品 | 信标 `slash_validator`（double / surround / 同 slot 双头） | |

分区时停还是两边长：见 [`../../tracks/consensus/worked-example-partition.md`](../../tracks/consensus/worked-example-partition.md)。  
「不确定」若承诺「到了就是到了」，表会偏向 BFT 一类。这仍是建议方向，不是决定。
