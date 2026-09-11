# 将形成的全部知识资产目录

这些是长期资产。正文按轨追加。  
每一份都必须能回溯到 [`../GOAL.md`](../GOAL.md)。

状态栏：

- `目录已立`：现在只有地图
- `进行中`：已开始写
- `第一轮已交付`：本轮范围内写完
- `未开始`：等门禁打开

---

## 课程资产

| 编号 | 资产 | 路径 | 状态 | 优先级 |
|---|---|---|---|---|
| 01 | 《区块链基础课程》 | `courses/level-00-machine/` 起 | L0–L2 已写；L3+ 进行中 | 必学 |
| 02 | 《全球公链架构图谱》 | 各链 19 节模板报告，横排后汇总 | 目录已立 | 必学 |
| 03 | 《共识协议图谱》 | 以后 `tracks/consensus/` | 目录已立 | 必学 |
| 04 | 《状态模型图谱》 | 以后 `tracks/state-models/` | 目录已立 | 必学 |
| 05 | 《区块链密码学地图》 | 以后 `tracks/crypto/` | 目录已立 | 必学 |

---

## 安全与失败资产

| 编号 | 资产 | 路径 | 状态 | 优先级 |
|---|---|---|---|---|
| 06 | 《区块链失败博物馆》 | `tracks/failure-museum/` | 已开馆；CVE-2018-17144 已归档 | 必学 |
| 07 | 《Blockchain Design Pattern Library》 | `libraries/design-patterns/` | 已收 8 条 | 重要 |
| 08 | 《Blockchain Anti-Pattern Library》 | `libraries/anti-patterns/` | 已收 10 条 | 重要 |

---

## 「不确定」专用资产

| 编号 | 资产 | 路径 | 状态 | 优先级 |
|---|---|---|---|---|
| 09 | 《后量子区块链工程手册》 | `tracks/post-quantum/` | 工程账本第一版；未测数字保持空 | 研究级 |
| 10 | 《不确定协议设计决策库》 | `libraries/decision-matrix/` | 状态/共识表已立，候选列空 | 重要 |
| 11 | 《不确定威胁模型》 | `libraries/threat-model/` | 草稿 | 必学 |
| 12 | 《不确定 Invariant Library》 | `libraries/invariants/` | 已收 6 条 | 必学 |
| 13 | 《不确定 Adversarial Test Corpus》 | 以后实验与回归测试 | 未开始 | 重要 |
| 14 | 《不确定长期技术路线图》 | Level 10 产出 | 未开始 | 重要 |

---

## 过程资产（本轮就有）

| 资产 | 路径 | 作用 |
|---|---|---|
| 最高准则 | [`../GOAL.md`](../GOAL.md) | 一切写作的门禁 |
| MASTER ROADMAP | [`00-master-roadmap.md`](00-master-roadmap.md) | 怎么走完 Level 0–10 |
| 知识树 | [`01-knowledge-tree.md`](01-knowledge-tree.md) | 依赖关系，不是浏览目录 |
| 研究顺序 | [`02-research-order.md`](02-research-order.md) | 为什么不按名气学链 |
| 审核日志 | [`../AUDIT_LOG.md`](../AUDIT_LOG.md) | 对自己写的东西负责 |

---

## 每条核心链将来会留下的档案

模板固定 19 节，见 `protocols/_template.md`。

| 链 | 波次 | 优先级 | 档案状态 |
|---|---|---|---|
| Bitcoin | 1 | 必学 | 第一版已写 |
| Cosmos / CometBFT | 2 | 必学 | 第一版已写 |
| Ethereum | 3 | 重要 | 第一版已写 |
| Avalanche | 4 | 重要（对照） | 未开始 |
| Solana | 5 | 重要 | 未开始（Level 6） |
| Sui | 5 | 重要 | 未开始（Level 6） |
| Aptos | 5 | 重要 | 未开始（Level 6） |
| Celestia | 6 | 重要 | 未开始（Level 7） |
| Polkadot | 6 | 重要 | 未开始（Level 7） |
| Zcash | 7 | 进阶 / 对「不确定」重要 | 未开始（Level 8） |
| Monero | 7 | 进阶 | 未开始（Level 8） |
| Mina | 7 | 研究级 | 未开始（Level 8） |

额外项目只在通过「独特思想过滤器」后建档。

---

## 不算资产的东西

以下内容即使写得很长，也不算本项目的资产：

- 币价、市值、空投
- 官网首页口号
- 无出处的 TPS 对比表
- 没有假设、没有代价、没有攻击面的「优点列表」
- 用户还没答题就提前写的 Level 1+ 教材
