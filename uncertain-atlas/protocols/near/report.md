# NEAR · Nightshade · 19 节档案（第一版，思想级）

独特思想过滤器：Bitcoin / CometBFT / Ethereum 一条未切执行的状态机；Polkadot 是**中继链 + 平行链候选**；Celestia 切 DA 不切执行。NEAR Nightshade 把系统建成**一条块链**：每个块逻辑上包含所有分片交易，物理上每分片最多一个 chunk。  
资料：Nightshade 论文（Near Protocol Sharding Design）；Nomicon `ChainSpec/Consensus`、`DataStructures/Block`、`ChainSpec/BlockProcessing`、`ChainSpec/SelectingBlockProducers`；nearcore `chain/chunks/README.md`。实现名、分片数、时代长度随版本变，以现行 Nomicon / 规范为准。不写官网 TPS。

---

## 1. 一句话定义

全网共享一个块哈希。块里挂各分片的 chunk 头（以及纠删后的分片件在网上走）；一个高度对某一分片要么有新 chunk、要么没有。头上同时记两种最终性标记，不能混成一句「秒最终」。

禁止的句子：「分片所以更快更安全」「和 Polkadot 一样是共享安全」。

---

## 2. 它解决的问题

旧问题（Nightshade 论文对「分片链 + 信标链」的批评）：每条分片自己跑分叉选择，信标与分片规则必须分开写、分开测。

它想：执行和状态可以按分片切开，**规范序仍只有一条**。

不解决：把「不确定」第一版变成高硬件世界计算机；也不自动等于 Polkadot 式「小链借用大验证者集」。

---

## 3. 架构图

```text
钱包 --tx--> 某分片的入口
                ↓
        chunk 生产者：本分片交易 + 跨分片收据
                ↓
        Reed–Solomon → PartialEncodedChunk（分给验证者子集）
                ↓
        出块者：本高度的块头 + 各分片 chunk 头 / chunk_mask
                ↓
        验证者：对自己跟踪的分片要有完整 chunk；
               对不跟踪的分片要有规定的收据/分片件（见 chunks README）
                ↓
        头字段：last_final_block（BFT）与 last_ds_final_block（Doomslug）
```

**事实：** nearcore `chain/chunks/README.md` 第一句：块由多个 chunk 组成，每分片最多一个。

---

## 4. 一笔交易完整生命周期

1. 用户按账户模型签名（细节以现行交易规范为准，本档不写操作码）。  
2. 交易进入**某一个分片**的 chunk，而不是「随便哪个块体」。  
3. chunk 被纠删、拆件、流言。  
4. 本高度的块若带上该 chunk，跟踪该分片的节点执行它，并检查与上一 chunk 的状态根等承诺（Nomicon BlockProcessing）。  
5. 「到了」必须点名：只是进了某个 chunk 头？块被 endorsements 接上？还是 `last_final_block` 已经盖过？  
6. 用户若只信分片 RPC，与别的链的 RPC 假验证相同。

---

## 5. 状态模型

账户 / 合约状态按分片切开。跨分片靠**收据**，不是共享内存。  
冲突：同一分片内仍会撞账户；跨分片延迟由收据路径决定。  
**推断：** 热账户若都挤在一个分片，并行广告帮不上——这是 L2.2 / L6 已经有的税，不是 Nightshade 独有。

---

## 6. 共识

Nomicon Consensus（事实，页上的定义）：

- 除创世外，块必须逻辑上带有超过 **2/3 权益加权**的 approvals（时代切换时可能还要下一时代的 2/3）。  
- 高度连续则 approval 是对 `prev` 哈希的 `Endorsement`；跳高度则是对 `prev` 高度的 `Skip`。两种条件**不能合并**（同页 Approval condition：Endorse 必须绑哈希，Skip 不得要求哈希一致，否则恶意两块会卡死出块）。  
- **Finality 谓词：** 在链 `T` 上，`B` 为最终，当且仅当 `B` 是创世，或存在 `X ≤ T` 使 `B = prev(prev(X))` 且三个块高度连续（`h(X) = h(prev(X))+1 = h(B)+2`）。  
- 诚实生产者不得签冲突的 endorsement / 冲突的 skip+endorsement；否则两个互不祖先的最终块会迫使 >1/3 作恶（同页定理）。

头上另有 `last_ds_final_block`（Doomslug 最终，数据结构注释）。活性证明 Nomicon 指向 Doomslug 论文与 Nightshade。  
`last_ds_final_block` 不是已经 `last_final_block`。`near-final` 不是已经 `final`。精读：[`../../tracks/finality/worked-example-doomslug-vs-bft.md`](../../tracks/finality/worked-example-doomslug-vs-bft.md)（不变量 135）。  
**禁止：** 把 Doomslug 标记写成 CometBFT 每高度 commit。见反模式 two-finality-sold-as-one。不抄超时 / 秒数。不写怎样出冲突票。

与 Polkadot：那里最终的是中继 GRANDPA 下的平行候选，不是「同一块内的 chunk 列表」。  
与 Celestia：那里块承诺的是 DA 数据，不是各分片账户执行。

---

## 7. 执行

跟踪某分片的节点：对纳入本块的新 chunk 跑该分片的 `Apply`，并用上一 chunk 的状态根、outcome 根、gas、烧毁余额、出站收据根等交叉检查（Nomicon BlockProcessing 列出这些 assert）。  
缺 chunk：该分片本高度没有新执行（论文写 0 或 1 个 chunk / 分片 / 块）。  
**确定性：** 同一 chunk 字节必须同状态；这是实现保证，不是「分片了所以自动同」。

---

## 8. 网络

chunk 体不都塞进块广播。`chain/chunks`：纠删后每个验证者拿一部分 PartialEncodedChunk；诚实验证者只在对块内**每个** chunk 都 `has_all_parts()` 时才批准该块。  
跟踪该分片的节点要能重建完整 chunk；不跟踪的节点仍要满足收据/分片件条件（README 原文）。  
攻击面：扣留分片件、对当前出块者/chunk 生产者做短时 DoS。这是部署 + 经济，不是签名被破。

---

## 9. 存储

跟踪分片 ⇒ 该分片状态在本地。时代轮换时 Nomicon 写：节点要在下时代开始前把新分片状态下载并补齐本时代 chunk。  
崩溃原子性以 nearcore 实现为准，本档不杜撰 WAL 文件名。原则与 L9.3 相同：半 chunk 不得变成「已执行」。

---

## 10. 密码学 primitive

常见积木：哈希、生产者/账户签名、Merkle 根（chunk 头、收据、纠删件）。  
纠删是编码，不是 Celestia 的抽样证明，也不是 Ethereum blob 的 KZG。  
本档不把某一曲线写成「不确定已定」。后量子税首先打在：**每块 approvals 的签名字节**（不变量 16）以及 chunk 件流言。

---

## 11. 安全假设（失效则什么作废）

| 假设 | 失效时用户哪句作废 |
|---|---|
| <1/3 权益签冲突 endorsement/skip | Nomicon 定理下的「两个最终块不可分叉」 |
| 纠删阈值：够多诚实持件 | 「块头在 ⇒ 该 chunk 能被重建」 |
| 你跟踪的分片你真有全体 | 「我验证了该分片执行」 |
| 出块者/块生产者按现行阶段跟踪足够分片 | 只信 chunk-only 节点时，安全模型变窄 |
| 用户连的是跟踪正确分片的全节点 | RPC 绿勾 |

Nomicon `SelectingBlockProducers` 有一则 **2021-03** 脚注：当时写 Simple Nightshade 阶段挑战未完全实现、出块者跟踪全分片。这是**该页当时的阶段描述**，不是 2026 的永恒事实。现行阶段必须回现行 Nomicon，禁止把脚注抄进产品句。

---

## 12. 最大结构性优势

**一条分叉选择。** 分片切的是执行与状态，不是再养 N 条需要各自最终的链。产品若诚实，可以指着**一个块哈希**问「规范序到哪」。

---

## 13. 最大具体缺陷

1. 两种最终性标记并存，文案极易撒谎。  
2. DA / 分片件与执行分开：有头 ≠ 你验证了该分片。  
3. 跨分片收据把「一笔支付」拆成多步；生命周期表必须加列。  
4. 出块者与 chunk-only 的假设不同；部署上可能收敛成少数机房跑全跟踪。  
5. 思想级档案：本页不写未核的停机根因。有官方 postmortem 再进博物馆。

---

## 14. Trade-off

| 得到 | 换 |
|---|---|
| 执行可按分片切开 | 收据延迟、分片路由、缺 chunk 的空洞高度 |
| 块头可保持相对轻 | 另建 chunk 网与纠删；验证者要拿齐自己的件才敢批块 |
| 较快的 Doomslug 标记 | 用户会把它听成 BFT 最终 |
| 更多参与者只跑一分片 | 全跟踪节点的硬件/同步税仍在某处 |

吞吐必须拆五笔账：协议（一块一序）、执行（分片 Apply）、网络（分片件）、状态（收据）、硬件（谁跟踪全分片）。禁止写官网 TPS 代替这五笔。

---

## 15. 历史事故

本档不编。NEAR 主网停机/重组若无 CVE 或官方 postmortem，不进博物馆。  
方法见 L9.9。Ethereum 实现裂根的对照案：CVE-2021-39137（另一条链，但「一家客户端错根」的形状可借用）。

---

## 16. 源码入口（已核文件名者）

1. `chain/chunks/README.md`：chunk、纠删、批准条件。  
2. Nomicon `ChainSpec/Consensus`：approval / skip / 最终性谓词。  
3. Nomicon `ChainSpec/BlockProcessing`：何时算「块可应用」、chunk 交叉检查。  

其它路径标预告，深挖时对照当前 nearcore 树，不把博客文件名当规范。

---

## 17. 关键函数（逻辑级）

**Accept-block-parts（chunks README）**  
输入：块内各 chunk 的分片件。输出：验证者是否可批准该块。  
invariant：每个 chunk 都 `has_all_parts()` 才批准。

**Apply-chunk（BlockProcessing）**  
输入：上一 chunk extra、本 chunk。输出：新状态 / 拒绝。  
invariant：上一状态根、outcome 根、gas、烧毁、出站收据根必须对上。

**Final(B, T)（Consensus）**  
输入：链尖 T、块 B。输出：是否最终。  
invariant：连续两高度盖在 B 上；与 `last_ds_final_block` 不是同一谓词。

---

## 18. 如何测试

- 缺一个分片件：诚实验证者不得批该块。  
- 缺跟踪分片的完整 chunk：不得应用该块（Nomicon 条件）。  
- 同一 chunk 两实现同根。  
- 头上两个最终字段：测试产品句不得把 ds 标记当成 BFT 谓词。  
差分：若只有 nearcore 一家，skip 须写明，不得当 PASS。

---

## 19. 「不确定」适用性

| 档 | 内容 |
|---|---|
| 强烈建议研究 | 暂无。第一版结算不必分片。 |
| 可以参考 | 「一块一序、chunk 可缺」；头上两种最终性必须分开写 |
| 暂时不需要 | 收据路由、chunk-only 经济、纠删参数 |
| 不建议采用 | 第一版就上执行分片；把分片 RPC 写成无需信任；把 Doomslug 当 commit |

决策列仍空。模式：[single-chain-chunks](../../libraries/design-patterns/single-chain-chunks.md)。反模式：[two-finality-sold-as-one](../../libraries/anti-patterns/two-finality-sold-as-one.md)。
