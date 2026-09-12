# Starknet — 滤网页（不是 19 节档案）

> **事实 / 推断 / 建议** 已分开。
> 树节点：[M7.3 租户](../../index/01-knowledge-tree.md)、额外表「Starknet / zkSync」。
> 对照：[L7.4](../../courses/level-07-modular/L07-M04-rollup-tenant.md)、[乐观 rollup 19 节](../optimistic-rollup/report.md)、[Zcash 验证明≠供给](../../tracks/failure-museum/cve-2019-7167.md)、[Mina 证明大小≠链](../mina/report.md)。
> **不是** 主研究链，**不做** 19 节。官方文档 ≠ 信标规范。禁止抄「thousands of transactions」、TVL、现行 program hash。

---

## 为什么只开滤网

[额外表](../../index/01-knowledge-tree.md) 要的独特对象不是「又一条 ZK L2」，而是：

**L1 更新根之前，必须对一个被点名的 Cairo 程序（SNOS / 后来的 applicative bootloader）给出有效性证明；该程序的哈希登记在 L1 合约里。**

同时产品有两个「accepted」词。这和乐观窗、Zcash 屏蔽池、Mina 递归链都不是同一对象。

主文献：[SNOS](https://docs.starknet.io/learn/protocol/snos)、[Transactions · statuses](https://docs.starknet.io/learn/protocol/transactions)、[SHARP](https://docs.starknet.io/learn/protocol/sharp)、[Data availability](https://docs.starknet.io/learn/protocol/data-availability)。版本句会变，本页只钉对象，不钉某次升级数字。

---

## 独特对象（官方文档，事实）

| 对象 | 文档怎么说 | 它不是 |
|------|------------|--------|
| SNOS | 把「某 Starknet 块有效」写成：**特定 Cairo 程序 + 特定输入 + 特定输出**。输入旧状态与交易列表，输出 Apply 后的状态。它是「交易怎样算对」的最终仲裁 | 排序者口头说「我执行了」 |
| 程序哈希 | v0.13.2 起：只交 SNOS 证明不够，要 applicative bootloader 的证明（SNOS 作基程序 B，aggregator 压状态差）。Core 合约存 `programHash` / `aggregatorProgramHash`。破坏性协议变更必须改登记的哈希 | 「电路物理定律，升级改不了含义」 |
| 两种执行 | 排序者组块可以按自己的方式跑（甚至不用 Cairo VM）；证明者对**已经定下的块**跑 SNOS。排序者可以多加 SNOS 不强制的限制（如防 DoS 的 validate 上限）。两边语义必须一致，否则出不了证明，只能再重组 | 「排序者跳过 `__validate__` 也能上 L1」——文档写明这样出不了证明 |
| 两个 accepted | `ACCEPTED_ON_L2`：进了 L2 共识最终的块。`ACCEPTED_ON_L1`：以太坊上的 Starknet 状态高度 ≥ 该块 | 一个绿勾 |
| 更细的档 | 官方 Transactions 另列 `CANDIDATE`（已写哈希、尚未执行）和 `PRE_CONFIRMED`（排序者已执行并写回执）。精读：[`../../tracks/finality/worked-example-l2-status-vs-l1.md`](../../tracks/finality/worked-example-l2-status-vs-l1.md)（不变量 138） | `PRE_CONFIRMED` = 已经 `ACCEPTED_ON_L2` |
| Core 仍自检 | SNOS 证不了的：交给 SNOS 的旧状态必须是 L1 上当前 Starknet 状态；L1→L2 消息确实在以太坊上发过 | 「验 STARK = 桥条件已满足」 |
| DA | 有效性 rollup：证明之外还发状态差，让盯着以太坊的人能重建状态。后继版本可以把状态差写成彼此依赖 | 有证明所以不需要数据；也不是乐观那种「下载批次重放每一笔」的唯一形状 |

**事实：** 文档把 SHARP 写成多个 Cairo 程序共享一次 STARK 验证。那是证明聚合/摊销，不是「用户已经在 L1 提款」。

**事实：** 文档**没有**声称 Starknet 是后量子链。STARK/FRI 用哈希，和配对 SNARK 的 PQ 故事不同；结算仍锚在以太坊。

---

## 三句对照（建议你记这一张表）

| 产品 | 「执行正确」押在哪 | 升级改的是什么 | 「到了」至少几个词 |
|------|-------------------|----------------|-------------------|
| 乐观 rollup | 窗内无人有效揭穿 | 争议合约 / 证明机 | 排序者头 / L1 根 / 窗结束 |
| Starknet（本页） | 对**当前登记程序哈希**的证明 + Core 自检 | `programHash` 等 | L2 accepted / L1 accepted |
| Zcash 屏蔽 | 电路 + 公开输入；可靠性破可通胀 | 电路升级（见博物馆） | 进最重链（另加 nullifier） |

zkSync 仍停在额外表：只靠「另一种证明系统」不够开第二页。有独立于本页对象的规范级思想再写。

---

## 滤网结论

| 问题 | 答案 |
|------|------|
| 有没有独特协议对象？ | **有**：点名程序哈希 + 两种 accepted + 状态差 DA。够对照 L7.4，不够开 19 节 |
| 有没有共识规范级文献？ | **没有**（官方文档 + 合约 + cairo-lang；版本在走） |
| 应不应该抄进不确定 v1？ | **建议：不。** 第一版是可验证结算机，不要当别人的有效性租户 |
| 数字 | **禁止** 抄吞吐口号、TVL、现行 program hash、某版 mempool TTL |

---

## 对不确定的意义（建议）

- 若将来用有效性证明：先写 **哪段程序/电路的哈希被结算合约锁住**，改它等于改「什么叫对」。
- 产品必须有两个词：租户共识已收 ≠ 房东合约已更新。见 [生命周期](../../tracks/lifecycle/README.md)。
- 验证明 ≠ 供给守恒（不变量 13），≠ 用户可提款（仍要 DA 与桥）。
- 不要把 STARK 写成「已经后量子的以太坊」。

---

## 禁句

- 「ZK 所以无需信任 / 无需 DA」
- 「PRE_CONFIRMED = 已经 ACCEPTED_ON_L2」
- 「ACCEPTED_ON_L2 = 已经在以太坊最终」
- 「SNOS 证明一过，桥就能放行」
- 「Starknet 是后量子链」
- 官网「thousands of transactions」、未标注日期的 TVL / program hash
- 把本页升级成 19 节（文献等级不够）
