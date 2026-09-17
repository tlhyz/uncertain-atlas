# 工作实例：排序者 unsafe 不是已经从 L1 推导，OP `safe` 不是 Gasper justified，桥等待窗不是 L2 已经 finalized

> **事实 / 推断 / 建议** 已分开。
> 对照：[乐观 Rollup 档案](../../protocols/optimistic-rollup/README.md)、[L7.4](../../courses/level-07-modular/L07-M04-rollup-tenant.md)、[提交 ≠ 兑付](../../libraries/invariants/README.md)（不变量 9）、[Gasper 三等](worked-example-head-vs-justified-vs-finalized.md)、[Starknet 四档](worked-example-l2-status-vs-l1.md)、[PoH 三档](../consensus/worked-example-poh-vs-tower.md)。
> 主文献：OP Stack 规范 [Derivation](https://specs.optimism.io/protocol/derivation.html)、[Glossary](https://specs.optimism.io/glossary.html)、[Execution Engine](https://specs.optimism.io/protocol/exec-engine.html)；官方文档 [Transaction finality](https://docs.optimism.io/op-stack/transactions/transaction-finality) 只用来钉「桥等待 ≠ 链 finalized」。资料层级是 rollup 规范 + 官方文档，不是信标规范。不另写 19 节（品类档案已有）。
> 本页钉 **`unsafe` ≠ `safe` ≠ `finalized`**、**RPC `latest` ≠ 已经从 L1 推导**、**OP `safe` ≠ Gasper `safe` / justified**、**L2 `finalized` ≠ 桥已经兑付**。不抄块秒、批次间隔、桥等待天数、epoch 个数。

---

## 0. 先修

- [L7.4](../../courses/level-07-modular/L07-M04-rollup-tenant.md) 租户
- [不变量 9](../../libraries/invariants/README.md) 提交 ≠ 兑付
- [不变量 127](../../libraries/invariants/README.md) head ≠ justified ≠ finalized
- [不变量 138](../../libraries/invariants/README.md) Starknet 四档
- [不变量 141](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见 OP Stack / Base 的 RPC 也有 `latest` / `safe` / `finalized`，以为和以太坊 Gasper 是同一把尺子；或看见排序者已经出块，以为已经从 L1 推导；或听见「提款要等很久」，以为 L2 交易还没 finalized。

官方句（事实）：

- 规范 Derivation：rollup 节点同时追三颗 L2 头。`finalized` L2 head：到这一块（含）都能从 L1 **已经 finalized**（规范写：canonical 且永远不可逆）的部分完整推导。`safe` L2 head：到这一块（含）都能从**当前 canonical** L1 完整推导。`unsafe` L2 head：safe 与 unsafe 之间的块**还没有**从 L1 推导；来自排序者出块（sequencer 模式）或向排序者做 unsafe sync（验证者模式）。规范把 unsafe head 也叫 `"latest"` head。
- Glossary：`safe` L2 块是 rollup 节点能**完全从 L1 推导**的块；不同节点可以因各自看见的 L1 而不同。`unsafe` L2 块是节点已经知道、但**不是**从 L1 推导出来的。Consolidation：节点试图把 safe head 往前挪一格，让最老的 unsafe 变成新的 safe；必须验证从 L1 推出的 payload attributes **恰好**等于那块最老的 unsafe。
- Derivation：consolidation 失败时，规范选 L1 推出来的属性，在当前 safe 之上做 L2 重组。`safe` head **只因为 L1 重组**才会被重组掉。
- Execution Engine：这三颗头映射到 Engine API 的 `headBlockHash` / `safeBlockHash` / `finalizedBlockHash`。`headBlockHash` 在用户 JSON-RPC 上标成 `"unsafe"`；节点可以先收下带外 L2 块，L1 数据冲突再重组。`safeBlockHash`：从 L1 数据推导、不太可能重组。`finalizedBlockHash`：不可逆，规范写它对准争议期的**下沿**，不是争议已经结束、桥已经兑付。
- 官方 Transaction finality 页（文档，不是规范）：协议三态就是 unsafe / safe / finalized。unsafe 是 soft finality：交易已在 L2 块里，数据**还没**贴到以太坊，信任的是排序者。safe：数据已经进了一个以太坊块，排序不再取决于排序者，但该以太坊块在 L1 finalized 之前仍可重组。finalized：含该数据的以太坊块已被以太坊共识 finalized。
- 同一页官方写常见误读：有人把 Standard Bridge 的提款等待听成「OP Stack 交易要等那么久才 finalized」。官方写这是错的。L2 交易 finalized 是「数据进了已 finalized 的以太坊块」。桥等待只影响经 Standard Bridge 提到以太坊的兑付，不改 L2 链上交易是否 finalized。官方另写：Fault Proof 挑战坏的是提款索赔，**不会**因此重组 OP Stack 链。
- 规范**没有**把 OP RPC `safe` 写成 Gasper justified，也没有把 `finalized` 写成争议窗已过、桥可提款。

`unsafe` / `latest`、`safe`（L1 当前 canonical 可推导）、`finalized`（L1 已不可逆部分可推导）、Gasper `safe` / justified、桥等待窗，是不同对象。

---

## 2. 直觉（ELI15）

厨房先把菜炒好递给邻桌看：`unsafe` / `latest`。总店菜单还没登记这桌。  
总店当天的菜单已经能反推出这道菜：`safe`。当天菜单若被换页，这道菜还可能被划掉。  
总店把那一页菜单锁进保险柜：`finalized`。  
保险柜上锁不是你已经能把押金从总店金库提走：桥还有自己的等待窗。  
邻店（以太坊）RPC 也有一盏叫 `safe` 的灯，那是另一栋楼的检查点，不是这间厨房的推导头。

小朋友看见三盏灯名字一样，以为和 Gasper 是同一句话。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| `unsafe` / RPC `latest` | 已知道、尚未从 L1 推导；排序者或 unsafe sync | 已经 `safe`；已经不可逆 |
| `safe` | 能从**当前 canonical L1** 完整推导 | Gasper justified；以太坊 RPC `safe`；已经 `finalized` |
| `finalized` | 能从 **L1 已 finalized** 的部分完整推导 | 桥已兑付；争议游戏已结束 |
| Consolidation | L1 推出的属性恰好等于最老 unsafe，才升 `safe` | 排序者口头「已经贴到 L1」 |
| 失败 consolidation | 规范选 L1 属性，在当前 `safe` 上重组 | 排序者可以坚持自己的 unsafe |
| Engine 三哈希 | `head` / `safe` / `finalized` BlockHash | 信标 forkchoice 的同一语义 |
| Standard Bridge 等待 | 官方写只挡经该桥提到 L1 的兑付 | L2 交易还没 finalized |
| 争议期下沿 | 规范把 `finalizedBlockHash` 写成对准这里 | 窗口结束 = 已经可提款 |
| Subblock / 跨链 local-safe | 产品另有的更快确认或互操作档 | 本页三颗推导头已经解释它们 |

---

## 4. 最小案例

用户在一条 OP Stack 链转一笔。

1. 排序者收入并出 L2 块。RPC `latest` 已经看见。规范：这是 `unsafe`，还没从 L1 推导。钱包可能已经绿。
2. 批次数据进了一个尚未 finalized 的以太坊块。规范：现在可以标 `safe`。官方文档：排序不再取决于排序者，但该 L1 块仍可重组。
3. 含该批次的以太坊块 finalized。规范：可以标 L2 `finalized`。这是 L2 推导头，不是桥已经放行。
4. 用户要经 Standard Bridge 提到以太坊。官方文档：还要过桥自己的等待。有人把这窗听成「交易还没 finalized」。官方写这是误读。
5. 有人把 RPC `safe` 听成以太坊 justified。不变量 127：信标页没有把 `safe` 写成 justified。本页的 `safe` 连信标检查点都不是，是「能从当前 L1 推导」。
6. 有人把这三档听成 Starknet `PRE_CONFIRMED` / `ACCEPTED_ON_L2` / `ACCEPTED_ON_L1`。不变量 138：那是有效性租户的执行/共识/L1 高度。本页是乐观租户的推导头。

「RPC 也叫 `safe`，所以和以太坊是同一盏灯」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 本页不证配对。批次可以是 blob 或 calldata，那是 DA 轴 |
| 协议 | 必须点名问的是 `unsafe`、L1 当前可推导的 `safe`、L1 已 finalized 可推导，还是桥兑付 |
| 实现 | 不同节点可以因 L1 视图而有不同 `safe`。Engine 标签会变 |
| 部署 | 谁当排序者、批次多久贴 L1，是部署事实 |
| 经济 | 桥等待是资金时间税；TVL 不是安全证明 |

**推断：** 产品句若只写「和以太坊一样有 `safe` / `finalized`」，读者会把排序者出块听成 L1 已推导，或把桥等待听成链还没 finalized。  
**建议：** 不确定第一版不要当别人的乐观租户。若对照，用户可见的「到了」必须点名推导头，不得复用 Gasper 三等当同一盏灯。不要抄秒数或桥等待天数。不要写怎样重组 unsafe 或怎样打争议。

---

## 6. 和另外几句不是同一句

1. **提交 ≠ 兑付**（不变量 9）：根被房东头包含 ≠ 桥可兑付。本页把「L2 `finalized`」从桥等待里再拆一刀。
2. **Gasper 三等**（不变量 127）：head / justified / finalized；官方没有把以太坊 `safe` 写成 justified。本页 RPC 标签碰巧同名，语义是推导。
3. **Starknet 四档**（不变量 138）：排序者回执 / L2 共识最终 / L1 高度。本页没有 `PRE_CONFIRMED`。
4. **PoH 三档**（不变量 133）：`processed` / `confirmed` / `finalized` 是票与 lockout。本页没有 Tower。
5. **平行链管道**（不变量 125）：Backed / 可用 / 批准 / GRANDPA。本页不是中继。
6. **Doomslug ≠ BFT**（不变量 135）：两枚头哈希。本页是三颗推导头。

不要把块秒、批次间隔、桥等待天数、epoch 个数、官网吞吐抄进不确定常量。不要写怎样让 consolidation 失败或怎样挑战 Fault Proof。不编博物馆页。不另写 19 节。Subblock / 跨链 `local-safe` / `cross-unsafe`、Arbitrum 自己的 assertion 管道，标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
unsafe / RPC latest ≠ 已经从 L1 推导
OP safe ≠ 已经 finalized
OP safe ≠ Gasper justified / 以太坊 RPC safe
L2 finalized ≠ 桥已经兑付 / 争议已经结束
consolidation 失败 ≠ 排序者可以坚持 unsafe
Standard Bridge 等待 ≠ L2 交易还没 finalized
Fault Proof 挑战 ≠ 已经重组 L2 链
```

语料：[C145](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「OP 的 `safe` = 以太坊的 `safe`。」「排序者出块 = 已经从 L1 推导。」「提款要等很久 = 交易还没 finalized。」「争议一开始 = 链会重组。」  
**边界：** 不讲某一版 Fault Proof / BoLD 逐步指令。不填秒数或等待天数。不把 OP 规范写成信标规范。不另写 19 节。不写怎样重组。Subblock 与跨链档另标。
