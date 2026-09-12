# 实例：两张票进了块，不等于已经罚没

目的 A/B。不是考试。  
先修：L4.3、L4.4、L9.5、[`../consensus/worked-example-vote-signbytes.md`](../consensus/worked-example-vote-signbytes.md)、[`../light-clients/worked-example-bft-skip.md`](../light-clients/worked-example-bft-skip.md)。

规范原文：

- [CometBFT `spec/consensus/evidence.md`](https://github.com/cometbft/cometbft/blob/main/spec/consensus/evidence.md)  
- [CometBFT `spec/core/data_structures.md`](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md)（`DuplicateVoteEvidence` / `LightClientAttackEvidence`）  
- 攻击分型：[isolate-attackers_002_reviewed.md](https://github.com/cometbft/cometbft/blob/main/spec/light-client/attacks/isolate-attackers_002_reviewed.md)（lunatic / equivocation / amnesia）

---

## 故事

阿比看见链上收了一条「双签证据」，以为骗子已经被罚光。  
规范写得更窄：引擎负责**发现、流言、上链、通知应用**。罚不罚、罚多少，是 **ABCI 应用**的事。  
证据自己「不惩罚坏人」。

另一句假学习：证据进了块，经济安全就从「尽力」变成了物理定律。规范写：若 ≥1/3 仍是拜占庭，证据系统会被审查，只能当 **best effort** 的附加安全。

---

## 事实：两种证据对象

**`DuplicateVoteEvidence`：** 同一验证者在同一 height / round / **Type** 上，对两个不同 `BlockID` 投了票（`BlockID` 可以是空块）。两票按 `BlockID` 字典序排。  
验证规则（evidence.md）：

- 两票的 Address、Height、Round、Type 相同  
- `BlockID` 不同  
- 该高度上此人在验证者集合里  
- 两票签名都对，且用**本链** `ChainID`（接 SignBytes 精读）

**`LightClientAttackEvidence`：** 冲突的 `LightBlock` + `CommonHeight`。用来抓住对轻客户端的攻击，让全节点能在链上提交。数据结构文写三种攻击**穷尽**：lunatic、equivocation、amnesia。

问责文的分型（先分类，不抄完整算法）：

| 名 | 规范句形状 |
|---|---|
| lunatic | 签了**无效**块（乱造集合等） |
| equivocation | 同一轮对两个**有效**块双签 |
| amnesia | 不同轮签了冲突块，且没有足以解锁的法定人数理由 |

问责文还写：固定集合下，能破坏 agreement 的非 lunatic 情形，TLA+ / Ivy 分析只剩下 equivocation 与 amnesia。形式化过 ≠ 实现已对。

---

## 事实：过期、唯一、上链、交给应用

`EvidenceParams`：`MaxAgeNumBlocks`、`MaxAgeDuration`。规范的过期判定写成：

`CurrentHeight - MaxAgeNumBlocks > EvidenceHeight` **且** `CurrentTime - MaxAgeDuration > EvidenceTime` → 过期忽略。

（本页按原文的 **且** 抄。实现若改成「或」，那是实现分叉，语料必须红。）  
PoS 上证据年龄应**盖住**解绑期，否则人已走，罚不到——与轻客户端 `trustingPeriod < unbondingPeriod` 是同一根钉子的另一头。默认两参数可能短于解绑，见 [证据窗](worked-example-evidence-window.md) 与 [ASA-2024-004](../failure-museum/asa-2024-004.md)。

已上链的证据按哈希去重。块里证据优先于普通交易；体积用 `MaxBytes` 封顶，防已被罚的人刷证据。收块节点在 prevote/precommit **之前**验证据。

上链之后，`FinalizeBlock` 把 `[]abci.Misbehavior` 交给应用。类型枚举：`DUPLICATE_VOTE` / `LIGHT_CLIENT_ATTACK`。  
ABCI 附加字段（`TotalVotingPower`、`ValidatorPower`、时间戳等）**不影响证据本身是否成立**，但必须全网一致；错了节点会改成自己算出的值再共识。

---

## 五层

| 层 | 本故事 |
|---|---|
| 密码 | 两张票的 σ 必须各自对 SignBytes 为真 |
| 协议 | 同高同轮同 Type、不同 BlockID；轻客户端冲突另走 `verifySkipping` 等规则 |
| 实现 | 证据池去重、缓存验签、流言重发 |
| 部署 | 时钟与高度决定过期；分区时双签才容易成功（规范：>1/3 + 临时分区） |
| 经济 | 应用决定是否 slash；≥1/3 仍坏则证据可被审查 |

---

## 对「不确定」（建议）

1. 规范第一页写清：引擎提交 `Misbehavior`，应用写罚没公式。不要说「上链即罚光」。  
2. 不变量 21 / 语料 C23：合法双签形状必须能被验为证据；同 BlockID 或错 `ChainID` 必须拒。  
3. 后量子：一条 `DuplicateVoteEvidence` ≥ 两份投票 σ。`LightClientAttackEvidence` 还带整份 LightBlock。块预算与账本第 18 行先写公式，数字仍空。  
4. Ethereum CL 把部分罚没写进信标状态机，不是同一架构。谓词与执行人见 [`worked-example-casper-slashing.md`](worked-example-casper-slashing.md)。不要写成「所有 BFT 都会自动罚」。  
5. 不填 CPU，不选 CosmWasm 罚没百分比。

---

## 精密检查

**禁止假学习：** 「证据进块所以已经 slash。」「BFT 自动经济安全。」「轻客户端被骗等于全网双最终。」  
**边界：** 不写 IsolateAmnesiaAttacker 伪代码；不抄 10 秒流言间隔当永恒；不编无原文的 Cosmos 罚没事故。Casper 的 double / surround / 协议内 `slash_validator` 不在本页展开。
