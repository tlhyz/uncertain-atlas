# 工作实例：PoH 槽钟在走，不等于已经投了票，更不等于已经 root

> **事实 / 推断 / 建议** 已分开。
> 对照：[L6.1](../../courses/level-06-throughput/L06-M01-solana-declare.md)、[Solana 档案](../../protocols/solana/report.md)、[最终性表](../finality/README.md)、[共识表](README.md)、[Gasper 三等](../finality/worked-example-head-vs-justified-vs-finalized.md)、[BABE ≠ GRANDPA](worked-example-babe-vs-grandpa.md)。
> 主文献：Solana 官方 [术语](https://solana.com/docs/references/terminology)、[RPC commitment](https://solana.com/docs/rpc/http/getslot)。
> 本页钉 **PoH / 槽钟 ≠ 账本票**、**processed ≠ confirmed ≠ finalized**、**超多数票 ≠ 最大 lockout / root**。不抄槽秒数、锁深度公式、官网 TPS、Alpenglow 目标毫秒。

---

## 0. 先修

- [L4.6](../../courses/level-04-bft/L04-M06-hotstuff-casper-contrast.md) 每高度 commit ≠ 检查点最终
- [L6.1](../../courses/level-06-throughput/L06-M01-solana-declare.md) 声明锁；课文已写 PoH 不是单独的 BFT
- [不变量 94](../../libraries/invariants/README.md) 槽号 ≠ 块身份；乐观确认 ≠ 已 rooted
- [不变量 133](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见槽在往前走，或看见 RPC `confirmed`，以为 PoH 自己就是 BFT，或以为超多数票已经等于最大 lockout，或以为 `processed` 已经不可逆。

官方句（事实）：

- 术语：PoH 是一叠证明。每一证证明某数据在此证之前就存在，并且距上一证经过了一段确定时间。像 VDF，验比做快。这是时间 / 先后的证明，不是投票。
- 术语：槽是领袖收交易、出一块的时间段。槽合在一起是逻辑钟，按顺序、不重叠，按 PoH 大致对齐墙钟。槽在走不是已经有人投票。
- 术语：账本票是验证者在某个 tick 高度对状态的哈希。它同时做两件事：这块我验过了；在 lockout 这段时间里，我答应不投冲突分叉。
- 术语：lockout 是验证者不能改投另一条叉的时长。confirmed block 是拿到超多数账本票。root 是**本验证者**上达到最大 lockout 的块或槽；它是该验证者所有活跃分叉的最高共同祖先。交易 finalized，当它的块成为 root。
- RPC：`processed` 是本节点当前认为最好的叉上、自己处理到的最高槽；最新，但仍可因集群切叉改掉。`confirmed` 是至少三分之二活跃质押**直接投票**确认的最高槽；比 processed 稳，比 finalized 弱。`finalized` 是集群认作最终的最高槽；实务上是验证者 vote tower 达到最大 lockout，并且至少三分之二活跃质押承认。这是最强一档。
- 跳过的槽：领袖没出块，或那条叉被共识丢掉。它不会当后续祖先，也不加块高。能不能算跳过，要等它比最新 root 更老才能确定。

PoH 钟、账本票、超多数确认、最大 lockout / root，是不同对象。

官方另有 Alpenglow 替换计划。那是另一对象，不是本页现行 Tower。不要抄目标毫秒，也不要把计划写成已经切完。

---

## 2. 直觉（ELI15）

墙上的钟自己会走：PoH / 槽。  
班长举手说「跟这一页」，并答应一时半会不改口：账本票 + lockout。  
多数人举了手：confirmed。  
举到不能再改、这一页成了以后所有作业的共同祖先：root / finalized。

钟在走，不是已经举手。举手了，不是已经钉死。小朋友看见「也是 PoS」或槽号往前跳，以为已经 commit。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| PoH | 可验的先后 / 时长证明，像 VDF | 单独的 BFT；已经决定跟谁 |
| 槽 | 领袖出一块的时间段；合起来是逻辑钟 | 已经 confirmed；已经 root |
| 账本票 | 验过这块 + lockout 内不投冲突叉 | PoH 自己；已经最大 lockout |
| lockout | 不能改投另一叉的时长 | 已经 finalized |
| confirmed | 超多数账本票；RPC 里至少 ⅔ 活跃质押直接投票 | 已经 finalized / 已经 root |
| finalized / root | 最大 lockout + 集群承认；块成为 root | processed；只是槽在走 |
| processed | 本节点当前最好叉上最新处理槽 | 已经不可逆 |
| 跳过的槽 | 没出块或叉被丢掉 | 当时已经能确定；已经 root |

---

## 4. 最小案例

用户在 Solana 转一笔。

1. 某领袖槽里打包。PoH 把先后写下。槽走了不是已经投票。
2. RPC 若只回 `processed`：本节点觉得这条叉最好。官方写仍可因切叉改。
3. 至少三分之二活跃质押直接投了这块：`confirmed`。官方写比 processed 稳、比 finalized 弱。
4. vote tower 达到最大 lockout，且至少三分之二承认：`finalized`。术语：交易 finalized 当块成为 root。
5. 有人把「PoH 在走」写成已经 BFT：术语里 PoH 没有投票。
6. 有人把 `confirmed` 写成已经 `finalized`：RPC 明明写成两档。
7. 有人把跳过的槽写成当时已经知道：官方写要等它比最新 root 更老。

「槽时间到了所以已经 commit」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | PoH 是可验延迟序列；票仍是验证者签 |
| 协议 | 必须点名问的是钟、票、超多数确认还是最大 lockout |
| 实现 | 各验证者自己的 tower / root；RPC 三档不是同一标签 |
| 部署 | explorer 绿勾若只跟 `processed` 或槽号，不是已经 root |
| 经济 | 票进 tower 才有 lockout 代价；PoH 自己不罚改口 |

**推断：** 产品句若只写「PoH 所以秒最终」，读者会把槽钟听成 commit。  
**建议：** 不确定第一版不要同时卖槽钟、超多数票和最大 lockout 三套「到了」。若对照 Solana，用户可见的「到了」必须点名 RPC 三档中的哪一档。不要抄槽秒数或官网 TPS。

---

## 6. 和另外几句不是同一句

1. **head ≠ justified ≠ finalized**（不变量 127）：Gasper 检查点三等。本页是 PoH 钟 + Tower lockout，没有 justified 那一档。官方对照表把 Casper-FFG 写成 Tower+PoH，那是对照，不是已经同一对象。
2. **BABE ≠ GRANDPA**（不变量 126）：出块装置 vs 最终装置。本页钟和票缠在同一条 PoH 账本上，仍不是同一对象。
3. **槽号 ≠ 块身份；乐观确认 ≠ 已 rooted**（不变量 94）：身份与 DA / repair。本页是确认档，不是「槽号能不能当主键」。
4. **停机里的 Tower / PoH 已经一致**（不变量 85 / 86）：一边收一边拒、根不前进。本页是正常三档定义，不是那两起事故。
5. **抽样 α ≠ QC**（不变量 131）：Snow 样本多数。本页不是 Avalanche。
6. **本地超时 ≠ 最终性**（不变量 47）：CometBFT 本地等待。本页 lockout 是投票承诺，不是 `timeout_commit`。

不要把槽秒数、32 票、锁深度位移、官网 TPS、确认墙钟、Alpenglow 目标毫秒抄进不确定常量。不要写怎样改投或造并行 PoH。不编博物馆页。

---

## 7. 「不确定」测试句（建议）

```text
PoH 在走 ≠ 已经投票
槽往前跳 ≠ 已经 confirmed
processed ≠ confirmed ≠ finalized
超多数账本票 ≠ 已经最大 lockout / 已经 root
confirmed ≠ 交易已经 finalized
跳过的槽当时看见 ≠ 已经能确定跳过
Alpenglow 计划 ≠ 现行 Tower 已经切完
PoH 像 VDF ≠ 已经是单独的 BFT
```

语料：[C137](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「PoH 单独就是 BFT。」「槽时间到了就是 commit。」「`confirmed` 就是 `finalized`。」「`processed` 已经不可逆。」「超多数票就是已经 root。」  
**边界：** 不证 VDF 数学、不填锁深度公式、不抄 TPS / 槽秒数。不把 Alpenglow 写成已经替换。乐观确认 ≠ rooted 仍指不变量 94。不写怎样改投。
