# 决策：共识

状态：**建议档已填**（2026-09-17）；仍非最终选型。推翻须走 L10.1 决策记录。  
强烈对照：`protocols/bitcoin/report.md`、`protocols/cometbft/report.md`、`courses/level-10-uncertain-studio/L10-M03-v1-settlement-machine.md`

| 维度 | Nakamoto | CometBFT | Avalanche | Gasper | 不确定候选（建议，非选型） |
|---|---|---|---|---|---|
| 最终性 | 概率 | 确定 | 概率固化 | 头可摆 + FFG 最终 | **BFT commit 对象**；产品只认一种 Y（见 [`settlement-copy.md`](../settlement-copy.md)） |
| 分区 | 可两边长 | 倾向停 | 视参数 | 头摆 / 最终延迟 | **倾向停**；不抄 Nakamoto 分区两边长 |
| 委员会 | 无许可算力 | 验证者集合 | 抽样 | 质押验证者 | **小验证者集合** + 明确 `V(h)` 延迟规则（不变量 8、35） |
| 投票流量 | 无 BFT 票 | 每轮全员量级 | 每轮少量 | attestation + 聚合 | **须先算** `每高度 × |σ_vote|`（不变量 16）；未测不得写「已后量子」 |
| 后量子 | 主要打用户签 | 用户签+投票签 | 视实现 | 用户签+投票签 | **用户签 + 投票签分域**；FIPS `ctx` 按角色（不变量 18、19） |
| 结算文案 | 需确认数 | commit 可当结算 | 要解释参数 | 须钉 finalized | **只写 commit 高度 + AppHash**；禁止「秒到 / 不可逆」未填空 |
| 罚没执行 | 无验证者罚没对象 | 引擎交证据，应用写公式 | 视实现 / 产品 | 信标 `slash_validator`（double / surround / 同 slot 双头） | **抄 CometBFT 证据 + 应用裁量**；不抄 Casper surround 当 v1 默认 |
| 排序权 | 矿工写列表并出块 | 本高度 proposer 写整块 | 视实现 | 本 slot 提议者可只签盲头，列表由域外 builder 写 | **本高度 proposer 写整块**；不抄域外 Builder API（不变量 27） |

分区时停还是两边长：见 [`../../tracks/consensus/worked-example-partition.md`](../../tracks/consensus/worked-example-partition.md)。  
块时间不是第四种最终性：CometBFT 须点名 PBTS 或 BFT Time，见 [`../../tracks/consensus/worked-example-pbts.md`](../../tracks/consensus/worked-example-pbts.md)。本地超时也不是最终性：`timeout_commit` 是 commit 之后再等，见 [`../../tracks/consensus/worked-example-timeouts.md`](../../tracks/consensus/worked-example-timeouts.md)。应用回的 `next_block_delay` 仍不是槽位，见 [`../../tracks/consensus/worked-example-next-block-delay.md`](../../tracks/consensus/worked-example-next-block-delay.md)。不确定列仍空。  
「不确定」若承诺「到了就是到了」，表会偏向 BFT 一类。上表「不确定候选」列是 **建议**，不是决定。  
路线图：[`../../ROADMAP.md`](../../ROADMAP.md) Phase 1 P1-2。
