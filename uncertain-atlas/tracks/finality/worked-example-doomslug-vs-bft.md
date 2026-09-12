# 工作实例：Doomslug 标记不是已经 BFT 最终

> **事实 / 推断 / 建议** 已分开。
> 对照：[NEAR 档案](../../protocols/near/report.md)、[L7.3](../../courses/level-07-modular/L07-M03-shared-security.md)、[BABE ≠ GRANDPA](../consensus/worked-example-babe-vs-grandpa.md)、[Gasper 三等](worked-example-head-vs-justified-vs-finalized.md)、[PoH ≠ Tower](../consensus/worked-example-poh-vs-tower.md)、[反模式 two-finality-sold-as-one](../../libraries/anti-patterns/two-finality-sold-as-one.md)。
> 主文献：Nomicon [Consensus](https://nomicon.io/ChainSpec/Consensus.html)、nearcore 指南 [Block and Block Header](https://near.github.io/nearcore/DataStructures/Block.html)、官方 [Indexer 教程 · Finality](https://docs.near.org/data-infrastructure/tutorials/near-indexer)。
> 本页钉 **`last_ds_final_block` ≠ `last_final_block`**、**Doomslug / `near-final` ≠ Nomicon BFT 谓词 / `final`**、**`optimistic` ≠ 已经不可逆**、**head（最高合法块）≠ 已经最终**。不抄超时常数、epoch 长度、秒数。不写怎样出冲突 endorsement / skip。

---

## 0. 先修

- [L4.6](../../courses/level-04-bft/L04-M06-hotstuff-casper-contrast.md) 每高度 commit ≠ 检查点最终
- [不变量 126](../../libraries/invariants/README.md) 出块装置 ≠ 最终装置
- [不变量 127](../../libraries/invariants/README.md) head ≠ justified ≠ finalized
- [不变量 135](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见 NEAR 出了新块，或看见 RPC / 索引器写了 `near-final`，以为 Doomslug 标记已经等于 Nomicon 那条 BFT 最终谓词，或以为和 CometBFT 每高度 commit 是同一把尺子。

官方句（事实）：

- Nomicon：最终性不是块自己的属性。`final(B, T)` 的意思是：在以 `T` 为尖的那条链上，`B` 算最终。同一块在另一条链上可以不算。
- Nomicon 谓词：`B` 在 `chain(T)` 上最终，当且仅当 `B` 是创世，或存在 `X ≤ T` 使 `B = prev(prev(X))`，并且三个高度连续（`h(X) = h(prev(X))+1 = h(B)+2`）。口语：这条链在 `B` 后面至少连续盖了两块。
- Nomicon 非正式句：若 `B` 最终，以后的最终块只能盖在 `B` 上面；`B` 及更早的交易不会被倒回去。这是对 **这条谓词** 的解释，不是对头上另一枚哈希的解释。
- Nomicon 的 `head`：本节点见过的、高度最大的合法块。头在走不是已经最终。定时器看的是头里的 `last_final_block_hash`。
- Nomicon 共识页的头草图只点了 `last_final_block_hash`。活性证明指向 Doomslug 白皮书与 Nightshade；同页写：这一节和论文的差别是，这里要求**连续两块**都带着 endorsement。
- nearcore 数据结构指南把两枚哈希分开写：`last_final_block` 注释是 **full BFT finality**；`last_ds_final_block` 注释是 **doomslug finality**。两枚可以同时出现在同一个头里。
- 官方 Indexer 教程把流块的 finality 写成三档：`optimistic`（None）= 一块（虽不太可能）仍可能被跳过；`near-final`（DoomSlug）= 不可逆，除非至少一个出块者被 slash；`final` = 最终且不可逆。
- RPC / OpenAPI 把 `Finality` 枚举写成 `optimistic` / `near-final` / `final`。枚举在，不等于三档已经是 Gasper 的 head / justified / finalized。
- 交易生命周期另有 `wait_until`（收据执行轴 vs 块最终轴）。`ExecutedOptimistic` 与 `IncludedFinal` 不是同一轴。那是另一对象，本页不展开。

头上的 Doomslug 哈希、Nomicon 连续两高度谓词、RPC `near-final`、RPC `final`，是不同对象。

---

## 2. 直觉（ELI15）

同一张成绩单上印了两个章。  
一个章写「Doomslug / 快一点」：`last_ds_final_block`。  
一个章写「BFT / 满的」：`last_final_block`。  
老师改作业的规矩是：后面连续盖了两本，前面那本才算 BFT 最终。  
门卫还可以按三种灯放行：可能还改（`optimistic`）、Doomslug 灯（`near-final`）、满章（`final`）。

小朋友看见「也有最终两个字」或「near-final」，以为已经和 Tendermint commit 一样，或以为两枚哈希是一枚。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| Nomicon `head` | 本节点最高合法块 | 已经最终 |
| Nomicon `final(B,T)` | 在这条链上，B 后面连续两高度 | 块自己身上的永久属性；Doomslug 标记 |
| `last_final_block` | 头字段；注释写 full BFT finality | `last_ds_final_block` |
| `last_ds_final_block` | 头字段；注释写 doomslug finality | Nomicon 那条两高度谓词已经满足 |
| `optimistic` | 官方：仍可能被跳过 | 已经不可逆 |
| `near-final` | 官方 Indexer：DoomSlug 档 | 已经 `final`；已经 CometBFT commit |
| `final` | 官方 Indexer：最终且不可逆 | 只看见新头就已经到了这一档 |
| Doomslug 白皮书 | Nomicon 活性证明指向它 | 本页已经把论文步骤写成现行规范 |
| `wait_until` | 收据执行 vs 块最终两轴 | 本页两枚头字段 |

---

## 4. 最小案例

用户在 NEAR 转一笔。

1. 新头出来。`head` 升高。不是已经最终。
2. 头里带着 `last_ds_final_block`。这是 Doomslug 那枚。不是 `last_final_block`。
3. 索引器按 `near-final` 推流。官方写这一档是 DoomSlug，并且写了「除非至少一个出块者被 slash」。不是已经 `final`。
4. Nomicon 谓词要等这条链在某块后面连续盖两块。那才是 `final(B,T)`。
5. 有人把「两种最终」听成 BABE / GRANDPA：那边是两套服务。本页是**同一个头上的两枚哈希**。
6. 有人把三档听成 Gasper：那边是 head / justified / finalized。本页没有 justified 这个官方词。
7. 有人把三档听成 Solana RPC：那边是 Tower lockout。本页是 Doomslug 与两高度谓词。

「NEAR 秒最终所以已经 commit」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | approval 是对 `(inner, target_height)` 的签；本页不证 |
| 协议 | 必须点名问的是哪一枚头哈希、哪一条谓词、哪一档 RPC |
| 实现 | Nomicon 共识页草图没画 `last_ds_final_block`；数据结构页画了。两句都留 |
| 部署 | 缺 chunk 仍可以「有块」；那是分片件，不是已经最终 |
| 经济 | Indexer 写 `near-final` 可因出块者被 slash 而逆。不要把这句话发明成不确定的罚金表 |

**推断：** 产品句若只写「NEAR 是秒最终」，读者会把较快那枚哈希听成 Nomicon BFT 谓词。  
**建议：** 不确定第一版不要同时卖两枚头哈希当一盏「到了」。若对照，用户可见的绿勾必须点名是哪一枚、哪一档。不要抄超时或秒数。不要写怎样出冲突票。

---

## 6. 和另外几句不是同一句

1. **BABE ≠ GRANDPA**（不变量 126）：两套装置。本页是同一头上的两枚最终哈希。
2. **head ≠ justified ≠ finalized**（不变量 127）：Gasper 检查点三等。本页没有 justified。
3. **processed ≠ confirmed ≠ finalized**（不变量 133）：Tower lockout。本页没有 PoH。
4. **抽中 ≠ 已认证**（不变量 134）：Algorand 三步。本页没有 VRF 委员会。
5. **backed ≠ 可用 ≠ 批准 ≠ GRANDPA**（不变量 125）：平行链管道。本页是一条链上的 chunk + 两枚标记。
6. **leak ≠ slash**（不变量 130）：终局推迟与罚没。Indexer「除非被 slash」只用来把 `near-final` 和 `final` 分开，不是本页已经写罚金。

不要把超时常数、epoch 长度、秒数、Indexer 版本标签抄进不确定常量。不要写怎样出冲突 endorsement / skip，也不要写怎样 slash 来推翻 `near-final`。不编博物馆页。Doomslug 论文步骤不是本页现行规范。`wait_until` 不在本页展开。

---

## 7. 「不确定」测试句（建议）

```text
last_ds_final_block ≠ last_final_block
Doomslug / near-final ≠ Nomicon 连续两高度谓词 / final
optimistic ≠ 已经不可逆
head（最高合法块）≠ 已经最终
同一头上两枚哈希 ≠ BABE 与 GRANDPA 两套服务
near-final / final / optimistic ≠ Gasper 三等
near-final ≠ CometBFT 每高度 commit
活性指向 Doomslug 论文 ≠ 论文步骤已经写成现行规范
wait_until 的执行轴 ≠ 本页两枚头字段
```

语料：[C139](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「Doomslug 就是已经 BFT 最终。」「`near-final` 就是已经 `final`。」「出了新头就是已经 commit。」「两种最终就是 BABE + GRANDPA。」「三档就是 Gasper。」  
**边界：** 不证白皮书、不填超时 / epoch 长度 / 秒数。不把 Nomicon 共识草图写成头上只有一枚哈希。不写怎样出冲突票。`wait_until` 另标。
