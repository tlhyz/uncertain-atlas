# 工作实例：排序者回执不是已经 ACCEPTED_ON_L2，L2 accepted 不是已经 ACCEPTED_ON_L1

> **事实 / 推断 / 建议** 已分开。
> 对照：[Starknet 滤网](../../protocols/starknet/README.md)、[L7.4](../../courses/level-07-modular/L07-M04-rollup-tenant.md)、[Gasper 三等](worked-example-head-vs-justified-vs-finalized.md)、[PoH 三档](../consensus/worked-example-poh-vs-tower.md)、[Doomslug ≠ BFT](worked-example-doomslug-vs-bft.md)、[Mina SNARKed ≠ staged](../light-clients/worked-example-snarked-vs-staged.md)。
> 主文献：Starknet 官方 [Transactions](https://docs.starknet.io/learn/protocol/transactions)、[SNOS](https://docs.starknet.io/learn/protocol/snos)、[Data availability](https://docs.starknet.io/learn/protocol/data-availability)。资料层级是官方文档，不是冻结规范。不写 19 节。
> 本页钉 **`CANDIDATE` ≠ `PRE_CONFIRMED` ≠ `ACCEPTED_ON_L2` ≠ `ACCEPTED_ON_L1`**、**验当前登记程序哈希 ≠ 物理定律**、**有证明 ≠ 状态差已够重建**。不抄 mempool TTL、nonce 窗口、费率加价、现行 program hash、官网吞吐。

---

## 0. 先修

- [L7.4](../../courses/level-07-modular/L07-M04-rollup-tenant.md) 租户
- [不变量 28](../../libraries/invariants/README.md) 程序哈希 + 两层 accepted
- [不变量 127](../../libraries/invariants/README.md) head ≠ justified ≠ finalized
- [不变量 138](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见 Starknet 回执已经绿，或看见「ZK 所以一出块就和以太坊一样」，以为已经 `ACCEPTED_ON_L1`，或以为验 STARK 已经能提款，或以为电路永不可改。

官方句（事实）：

- Transactions 页：每笔交易走同一生命周期，拿执行状态和最终性状态。官方文档 ≠ 信标规范。
- 自官方列出的最终性档（该页写自 0.14.0）：`NOT_RECEIVED` → `RECEIVED` → `CANDIDATE` → `PRE_CONFIRMED` → `ACCEPTED_ON_L2` → `ACCEPTED_ON_L1`。本页不把版本号抄进不确定常量，只钉这些名字不是同一对象。
- `CANDIDATE`：排序者把交易写进 feeder gateway 存储。**还没执行**。没有执行信息，只写了交易哈希。
- `PRE_CONFIRMED`：排序者已经成功执行，回执写进 feeder gateway。不是已经进共识最终块。
- `ACCEPTED_ON_L2`：交易进了**共识协议最终**的块。
- `ACCEPTED_ON_L1`：以太坊上的 Starknet 状态高度 **≥** 含这笔的块高度。
- `RECEIVED`：全节点已经交给某个排序者。官方写全节点之间没有同步「已收到」的 P2P；问另一节点可能找不到哈希。那是部署/查询轴，不是本页最终性钉子。
- 执行状态另算：`SUCCEEDED` / `REVERTED`。`REVERTED` 仍可进块。`DECLARE` / `DEPLOY_ACCOUNT` 没有执行阶段，官方写它们不能 revert。Nonce 仍加、费仍收、校验阶段改动不撤、执行阶段改动撤——那是另一对象，本页不展开公式。
- SNOS：在 Cairo 里，只能证「**某个点名的 Cairo 程序 + 特定输入 + 特定输出**」。「某 Starknet 块有效」必须先写成这种句子。SNOS 吃旧状态和交易列表，吐 Apply 后的状态。它是「交易怎样算对」的最终仲裁。
- 两种执行：排序者组块可以按自己的方式跑，甚至不用 Cairo VM；证明者对**已经定下的块**跑 SNOS。排序者可以多加 SNOS 不强制的限制。两边语义必须一致，否则出不了证明，只能再重组。排序者跳过 `__validate__` 出不了证明——本页不写怎样跳。
- 只交 SNOS 证明不够：官方写还要 applicative bootloader 的证明（SNOS 作基程序 B，aggregator 压状态差）。Core 合约存 `programHash` / `aggregatorProgramHash`。破坏性协议变更必须改登记的哈希。
- Core 仍自检 SNOS 证不了的：交给 SNOS 的旧状态必须是 L1 上当前 Starknet 状态；L1→L2 消息确实在以太坊上发过。验证明不是桥条件已满足。
- DA：有效性 rollup 在证明之外还发状态差，让盯着以太坊的人能重建。后继版本可以把状态差写成彼此依赖。有证明不是已经不需要数据。压缩算法与现行哈希不抄。
- 文档**没有**声称 Starknet 是后量子链。结算仍锚在以太坊。SHARP 是多个 Cairo 程序摊一次验证，不是用户已经能提款。

`CANDIDATE`、`PRE_CONFIRMED`、`ACCEPTED_ON_L2`、`ACCEPTED_ON_L1`、当前登记程序哈希、状态差，是不同对象。

---

## 2. 直觉（ELI15）

厨房先把菜单抄到备餐单：`CANDIDATE`。还没炒。  
菜炒完、小票打出来：`PRE_CONFIRMED`。还没送出厨房门。  
楼层经理盖章说这桌算本层已定：`ACCEPTED_ON_L2`。  
总店账本高度追上这桌：`ACCEPTED_ON_L1`。  
总店只认一份登记过的菜谱哈希。换菜谱是升级，不是物理定律。  
小票上的「算对了」不是你已经能把钱从总店金库提走。

小朋友看见「ZK」或看见回执绿了，以为已经在总店入账。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| `CANDIDATE` | 排序者已写下哈希，尚未执行 | 已经有回执；已经共识最终 |
| `PRE_CONFIRMED` | 排序者已执行并写回执 | 已经 `ACCEPTED_ON_L2`；已经不可逆 |
| `ACCEPTED_ON_L2` | 进了 L2 共识最终的块 | 已经 `ACCEPTED_ON_L1`；已经可提款 |
| `ACCEPTED_ON_L1` | L1 上 Starknet 高度追上该块 | 桥已放行；DA 已够自己重建 |
| SNOS | 点名 Cairo 程序：旧状态 + 交易 → 新状态 | 排序者口头「我执行了」 |
| 程序哈希 | Core 登记的 SNOS / aggregator 哈希 | 不可改的物理定律 |
| 两种执行 | 排序者组块 vs 证明者跑 SNOS | 跳过 `__validate__` 也能上 L1 |
| 状态差 DA | 证明之外用来重建的数据 | 有证明所以不需要数据 |
| `REVERTED` | 执行失败仍可进块 | 没进块；和最终性档是同一轴 |
| SHARP | 多程序摊一次验证 | 用户已经能提款 |

---

## 4. 最小案例

用户在 Starknet 转一笔。

1. 全节点交给排序者：`RECEIVED`。问另一节点可能找不到。不是已经最终。
2. 排序者先写下哈希：`CANDIDATE`。还没执行。
3. 排序者跑完、打回执：`PRE_CONFIRMED`。钱包可能已经绿。不是已经 `ACCEPTED_ON_L2`。
4. 进了 L2 共识最终块：`ACCEPTED_ON_L2`。不是已经在以太坊更新根。
5. L1 上 Starknet 高度追上：`ACCEPTED_ON_L1`。仍要问桥与状态差。
6. 有人把「验 STARK」写成电路永不可改：Core 登记的哈希随破坏性升级而改。
7. 有人把「有证明」写成不需要数据：官方仍发状态差。后继版本还可以让状态差互相依赖。

「回执绿了所以已经在以太坊最终」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | STARK/FRI 证的是点名程序；改哈希是升级。本页不证 FRI |
| 协议 | 必须点名问的是 `CANDIDATE` / `PRE_CONFIRMED` / `ACCEPTED_ON_L2` / `ACCEPTED_ON_L1`，以及当前登记的哪一个 program hash |
| 实现 | 排序者执行与 SNOS 执行必须同语义；官方文档会改档名 |
| 部署 | `RECEIVED` 黏在提交节点上；证明者 / 排序者中心化是部署事实 |
| 经济 | `REVERTED` 仍收费；L1 更新另耗房东资源。数字不抄 |

**推断：** 产品句若只写「ZK 所以秒最终」，读者会把排序者回执听成 L1 已更新。  
**建议：** 不确定第一版不要当别人的有效性租户。若对照，用户可见的「到了」必须点名停在哪一档，并且写出被锁的程序哈希。不要抄 TTL 或现行 hash。不要写 19 节。

---

## 6. 和另外几句不是同一句

1. **程序哈希 + 两层 accepted**（不变量 28）：本页把它展开到四档最终性，并钉 `CANDIDATE` / `PRE_CONFIRMED`。28 的钉子仍在。
2. **head ≠ justified ≠ finalized**（不变量 127）：Gasper 检查点。本页是 L2 租户档 + L1 高度。
3. **`processed` ≠ `finalized`**（不变量 133）：Tower / RPC。本页没有 PoH。
4. **Doomslug ≠ BFT**（不变量 135）：同一条链两枚头哈希。本页是 L2 档 vs 房东高度。
5. **SNARKed ≠ staged**（不变量 123）：Mina 递归账本。本页是有效性租户锚在以太坊。
6. **顺序 ≠ 状态根**（不变量 136）：先定序再揭开。本页是回执档 vs L1 根。

不要把 mempool TTL、nonce 窗口、费率加价、现行 program hash、官网吞吐抄进不确定常量。不要写怎样跳过 `__validate__` 或扣状态差。不编博物馆页。不写 19 节。有状态压缩后的状态差互相依赖、SHARP 摊销、`REVERTED` 部分回滚，标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
CANDIDATE ≠ 已经执行 / 已经有回执
PRE_CONFIRMED ≠ 已经 ACCEPTED_ON_L2
ACCEPTED_ON_L2 ≠ 已经 ACCEPTED_ON_L1
ACCEPTED_ON_L1 ≠ 桥已放行 / 状态差已够重建
验当前登记 program hash ≠ 电路物理定律
排序者执行 ≠ SNOS 已经同意
有证明 ≠ 不需要 DA
REVERTED ≠ 没进块（执行轴，不是最终性档）
```

语料：[C142](../../libraries/adversarial-corpus/README.md)。程序哈希旧句仍见 [C30](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「回执绿了就是已经在以太坊最终。」「ZK 所以无需 DA。」「SNOS 证明一过，桥就能放行。」「程序哈希不能改。」「Starknet 是后量子链。」  
**边界：** 不讲 FRI / 电路；不填 TTL / 现行 hash / 官网吞吐。不把官方文档写成冻结规范。不写 19 节。不写怎样重组或扣数据。`REVERTED` 公式与有状态压缩另标。
