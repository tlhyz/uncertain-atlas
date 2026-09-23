# 例：看见 Byzantine Validators 是过错名单不是已经成立；看见「Read Below」不是已经给出了定义；看见摘要说三种穷尽不是已经验完

**层次**：实现 / 证据指控栏。  
**分类**：事实（官方现状）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) LightClientAttackEvidence，与 [Light Client Accountability](https://github.com/cometbft/cometbft/blob/main/spec/light-client/accountability/README.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Byzantine Validators 是过错名单不是已经成立 / Read Below 不是已经给出了定义 / 摘要说三种穷尽不是已经验完」，不是证据里有 TotalVotingPower 就已经自证，也不是 LightBlock 两件都在就已经是同一高。不要另写怎样填指控名单。

**先说清一个不同的 phantom：** Kaspa 的 PHANTOM / GHOSTDAG 是另一套东西（见 [`../consensus/worked-example-dag-vs-selected-chain.md`](../consensus/worked-example-dag-vs-selected-chain.md)）。本页说的 phantom validator 是 CometBFT 轻客户端问责文里的那一类，两者无关。

## 官方三件事

规范把 `Byzantine Validators` 是一份「acted maliciously」的名单、它的校验栏写的是 `Read Below`、以及 `data_structures.md` 的摘要断言三种攻击**穷尽**，写成三件独立的事实，不是「看见名单上有谁就已经坐实、已经读完下文、已经验完」一件事：

1. **看见 `Byzantine Validators` / 看见名单 不是已经成立，也不是已经定奖惩。**  
   官方把它写成「acted maliciously 的验证者」。看见名单，不是已经证明这些人作恶。看见有名字，不是已经能罚。看见字段在，不是已经交差。名单是**指控**，成立与否要看下文那套。
2. **看见校验栏写 `Read Below` / 看见这四个字 不是已经给出了定义，也不是已经读到了。**  
   同一个表里有三个字段的说明或校验写成 `Read Below`（`ConflictingBlock`、`CommonHeight`、`Byzantine Validators`）。看见 `Read Below`，不是下文就有那套定义。看见指针，不是已经拿到被指的东西。
3. **看见摘要说三种穷尽 / 看见 exhaustive 不是已经验完，也不是已经拿到完整定义。**  
   `data_structures.md` 的摘要写：Lunatic、Equivocation、Amnesia 三种，并写 These attacks are exhaustive，同时把详情**指向**问责文。问责文里除了这三类，还写了 **phantom validators**（不在当前集合、但仍在解绑期内仍可签名的人），并且对「要不要把它当成单独一类」留了一个 **Q** 开放问题。看见摘要说穷尽，不是已经验完。看见三类，不是已经覆盖下文所有情形。

怎样构造 `LightClientAttackEvidence`、怎样算 `CommonHeight`、怎样挑指控名单是规范里的做法，本页不抄。证据字段的可信性是不变量 443，本页不抄。`LightBlock` 的绑定是不变量 445，本页不抄。三种攻击的分型见 [`../economic/worked-example-evidence.md`](../economic/worked-example-evidence.md)，本页不抄。

## 官方为什么这样拆

- **名单 ≠ 已成立：** 「acted maliciously」是主张，判定在别处。
- **`Read Below` ≠ 已经给出定义：** 它是「详情在别处」的指针，不是内容。
- **摘要说穷尽 ≠ 已经验完：** 摘要断言与问责文的开放问题不一致，实施者不能只看摘要。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Byzantine Validators 是过错名单 | 不是已经成立 | 不是证据里有 TotalVotingPower 就已经自证（443） |
| 校验栏写 Read Below | 不是已经给出了定义 | 不是 LightBlock 两件都在就已经是同一高（445） |
| 摘要说三种穷尽 | 不是已经验完 | 不是三种攻击的分型本身就够（见经济证据页） |
| 本页不涉及 | — | 不是朝前 lunatic 形不成证据（66） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见名单上有谁就已经坐实」，必须分开 Byzantine Validators 是过错名单是不是已经成立、Read Below 是不是已经给出了定义、摘要说三种穷尽是不是已经验完。**实现里不要只按 `data_structures.md` 的摘要写证据校验**，必须去问责文逐条读，并把 phantom validator 那一类当作待决问题处理。可以跳过「看见名单上有谁就已经坐实」。不要另写怎样填指控名单。

## 本页不抄

- 怎样构造 `LightClientAttackEvidence`、怎样算 `CommonHeight`、怎样挑指控名单。
- 证据字段的可信性。那是不变量 443。
- `LightBlock` 的绑定。那是不变量 445。
- 三种攻击的分型。见 [`../economic/worked-example-evidence.md`](../economic/worked-example-evidence.md)。
