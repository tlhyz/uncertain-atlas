# 将形成的全部知识资产目录

这些是长期资产。正文按轨追加。  
每一份都必须能回溯到 [`../GOAL.md`](../GOAL.md)。

---

## 课程资产

| 编号 | 资产 | 路径 | 状态 | 优先级 |
|---|---|---|---|---|
| 01 | 《区块链基础课程》 | `courses/` | L0–L10 正文已写；L8.4 数学后置 | 必学 |
| 02 | 《全球公链架构图谱》 | `protocols/` 19 节 + `tracks/` 横表 | 主线 + 第 8 波择优（含 Nervos 思想级） | 必学 |
| 03 | 《共识协议图谱》 | `tracks/consensus/` + `tracks/finality/` | 对照表 + ABCI 四门 + 扩展 + 集合延迟 | 必学 |
| 04 | 《状态模型图谱》 | `tracks/state-models/` + `tracks/parallelism/` | 进行中 | 必学 |
| 05 | 《区块链密码学地图》 | `tracks/crypto/` | 对照表 + 域分离三层编码精读 | 必学 |
| 05b | 《实现保证精读》 | `tracks/implementation/` | 编码 + 崩溃 + assumevalid + 头工作量 + state sync | 必学 |

---

## 安全与失败资产

| 编号 | 资产 | 路径 | 状态 | 优先级 |
|---|---|---|---|---|
| 06 | 《区块链失败博物馆》 | `tracks/failure-museum/` | 十三案 + 17144 五层精读 | 必学 |
| 07 | 《Design Pattern Library》 | `libraries/design-patterns/` | 15 条 | 重要 |
| 08 | 《Anti-Pattern Library》 | `libraries/anti-patterns/` | 42 条 | 重要 |

---

## 「不确定」专用资产

| 编号 | 资产 | 路径 | 状态 | 优先级 |
|---|---|---|---|---|
| 09 | 《后量子区块链工程手册》 | `tracks/post-quantum/` | FIPS 名义长度 + 外部 ctx + 有状态 HBS 卡；CPU 空 | 研究级 |
| 10 | 《不确定协议设计决策库》 | `libraries/decision-matrix/` | 对照列已扩；候选列空 | 重要 |
| 11 | 《不确定威胁模型》 | `libraries/threat-model/` | 草稿 | 必学 |
| 12 | 《不确定 Invariant Library》 | `libraries/invariants/` | 39 条 | 必学 |
| 13 | 《不确定 Adversarial Test Corpus》 | `libraries/adversarial-corpus/` | 目录 C01–C41；runner 未建 | 重要 |
| 14 | 《不确定长期技术路线图》 | `courses/level-10-uncertain-studio/` | 建议清单，非选型 | 重要 |

---

## 过程资产

| 资产 | 路径 | 作用 |
|---|---|---|
| 最高准则 | [`../GOAL.md`](../GOAL.md) | 门禁 |
| 通读顺序 | [`04-study-path.md`](04-study-path.md) | 目的 A 的六通，不是浏览 |
| MASTER ROADMAP | [`00-master-roadmap.md`](00-master-roadmap.md) | 怎么走完 Level 0–10 |
| 知识树 | [`01-knowledge-tree.md`](01-knowledge-tree.md) | 硬依赖 |
| 研究顺序 | [`02-research-order.md`](02-research-order.md) | 为什么不按名气 |
| 审核日志 | [`../AUDIT_LOG.md`](../AUDIT_LOG.md) | 对自己写的东西负责 |

---

## 每条核心链档案

| 链 / 品类 | 波次 | 优先级 | 档案状态 |
|---|---|---|---|
| Bitcoin | 1 | 必学 | 第一版 |
| Cosmos / CometBFT | 2 | 必学 | 第一版 |
| Ethereum | 3 | 重要 | 第一版 |
| Avalanche | 4 | 重要（对照） | 第一版 |
| Solana / Sui / Aptos | 5 | 重要 | 第一版 |
| Celestia / Polkadot | 6 | 重要 | 第一版 |
| Zcash / Monero / Mina | 7 | 进阶 | 第一版 |
| 乐观 Rollup | 8 | 重要 | 品类第一版 |
| Algorand | 8 | 进阶 | 抽签第一版 |
| Kaspa | 8 | 进阶 | 块 DAG 第一版 |
| Fuel | 8 | 进阶 | 思想级 |
| Nervos CKB | 8 | 进阶 | 思想级（占用） |
| NEAR Nightshade | 8 | 进阶 | 思想级（一条链+chunk） |
| Babylon | 8 | 进阶 | 仅过滤器页，无 19 节 |
| QRL | 8 | 研究级 | 仅过滤器页（XMSS / OTS） |
| Monad | 8 | 进阶 | 仅过滤器页（先定序再 Apply） |
| EigenLayer | 8 | 进阶 | 仅过滤器页（restake + AVS 自定罚没） |
| Starknet | 8 | 研究级 | 仅过滤器页（SNOS 程序哈希 + 两层 accepted） |

额外项目只在通过独特思想过滤器后建档。

---

## 不算资产的东西

- 币价、市值、空投
- 官网首页口号
- 无出处的 TPS 对比表
- 没有假设、没有代价、没有攻击面的「优点列表」
- 只列目录没有课文的「知识树完成」假象
