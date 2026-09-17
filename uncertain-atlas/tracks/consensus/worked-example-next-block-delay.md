# 工作实例：谁决定 commit 后再等，仍不是最终性

> **事实 / 推断 / 建议** 已分开。
> 对照：[本地超时](worked-example-timeouts.md)、[ABCI 四门](worked-example-prepare-process.md)、[PBTS](worked-example-pbts.md)。
> 主文献：[abci++_methods.md · FinalizeBlock](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)（现行 `main`）、[ADR-115](https://github.com/cometbft/cometbft/blob/main/docs/references/architecture/adr-115-predictable-block-times.md)（Accepted）。
> 本页钉 **谁填 post-commit 等待**：本地 `timeout_commit` 还是应用的 `FinalizeBlockResponse.next_block_delay`。等待对象没变，填写人变了。不抄规范里的 1s / ADR 里的示例秒数。

---

## 0. 先修

- [超时精读](worked-example-timeouts.md)（不变量 47）
- [L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)

---

## 1. 核心问题

阿比看见 `next_block_delay`，以为应用终于能规定「全网每 N 秒一块」，或以为这是写进状态根的共识参数，或以为等这段时间才最终。

规范写的是：Commit 已经发生。这个字段只回答「再过多久开下一高度」。而且它被标成 **Deterministic = No**。

---

## 2. 直觉（ELI15）

章已经盖过了。以前是秘书自己看墙上的钟，再在门口站一会儿。  
现在秘书问柜台：「你忙完了吗？门口再站多久？」柜台可以每次答一个不同的数。  
柜台答的数，不写进大家共同的账本。有人答「立刻走」，有人答「再等一会儿」，章还是盖过的。

ADR 自己说：想要「每块刚好一样长」做不到。轮次变多、网络慢、钟不准、执行慢，都会把单块间隔拉开。最多是中长期平均往一个目标靠，而且是尽力而为。

---

## 3. 正式对象（规范 / ADR，事实）

### 3.1 现行 `main` 规范表

`FinalizeBlockResponse` 字段 6：`next_block_delay`（`google.protobuf.Duration`）。表上 **Deterministic = No**。  
同表里 `app_hash` / `validator_updates` / `consensus_param_updates` / `tx_results` 是 **Yes**。

规范原文语义：

- Commit **之后**、开下一高度 **之前**，引擎再等这么久。
- 这段包含应用和引擎处理已提交块花掉的时间。
- 目的仍是：提议者已经有 +2/3，再多收几张迟到的 precommit。
- 填 0：块已被应用处理完、票也齐了，立刻开下一高度。
- 以前这是配置里的 `timeout_commit`。规范写「若要保持旧行为，回一个常量」——本页不把那个常量抄进不确定。

各节点 **可以** 回不同的值，本意是看本机处理花了多久。规范说可变延迟若要好用，节点钟应大致同步（PBTS 也要钟）；这是部署假设，不是第三条最终性。

### 3.2 不是所有发布线都有

**事实：** 现行 `main` 的 `abci++_methods.md` 有这个字段。v0.38 / 部分 v1.0 发布线仍可能只有本地 `timeout_commit`。  
产品句必须点名：**这条发布线有没有 `next_block_delay`**。没有，就还是不变量 47。不要把 `main` 规范当成所有 CometBFT 节点已经换人填等待。

### 3.3 ADR-115（Accepted）在补哪一句

把等待从节点配置挪到应用回包，好让**每个高度**可以不同。语义「本质上还是 timeout_commit」。

ADR 明确丢掉的方案：

- 做成全局 `ConsensusParams`：解决不了多轮，而且参数更新还晚一高。
- 两个旋钮并存：同一件事两套控制，会糊。

升级路径（ADR）：`timeout_commit` 标过时；应用给了 `next_block_delay` 就忽略配置；没给就回退配置。

**事实（ADR）：** 「恒定出块间隔」做不到。能设计的是中长期平均往目标靠，单块仍是尽力而为。

### 3.4 对照表

| 对象 | 谁填写 | 是否复制状态 | 是不是最终性 |
|------|--------|--------------|--------------|
| `timeout_commit` | 本地配置 | 否 | 否。Commit 已发生 |
| `next_block_delay` | 本高度 `FinalizeBlock` 的应用 | 否（规范标非确定性） | 否。Commit 已发生 |
| `app_hash` | 应用 | 是 | 不是等待，是状态承诺 |
| PBTS timely | 提议者时间戳 vs 本机收到窗 | 头上的时间另算 | 不 timely → prevote nil |
| 锁 | 投票规则 | 是安全对象 | 安全，不是等待 |

---

## 4. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 把应用回的等待写成全网槽位 | 文案 | 规范：非确定性；ADR：恒定间隔做不到 | 用户按墙钟放货 |
| 把 delay 写进 app_hash / 参数更新 | 实现 | 规范表把 delay 标 No，参数更新标 Yes | 应用自己把秒数写进状态 |
| 一节点回 0、另一节点回很长 | 本地值不同 | 规范允许各回各的 | 出块机会不均（与 timeout_commit 不一致同类） |

---

## 5. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 等待不改被签字节 | 「delay 已经后量子」 |
| 协议 | Commit 先于等待；字段非确定性 | 「全网必须同一间隔」 |
| 实现 | 谁填：配置 vs Finalize 回包；发布线可能没有该字段 | 现行默认毫秒 |
| 部署 | 可变延迟若用墙钟，规范提到钟要大致同步 | 某机房 NTP 精度 |
| 经济 | ADR：平均间隔最多尽力而为 | 把某条应用链的槽位广告当事实 |

---

## 6. 对不确定的意义（建议）

- 先写不变量 47：等待不是最终性。再写本页：谁填等待。
- 第一版可以只保留本地 `timeout_commit`，测过再让应用回 delay。
- 若启用：必须标非确定性；禁止写进 `app_hash` 或当成 `consensus_param_updates`。
- 不要承诺「每块刚好 N 秒」。ADR 已经写做不到。
- 不要抄规范「保持旧行为」的那一个常量秒数。

---

## 7. 禁句

- 「next_block_delay 到了才最终」
- 「应用回了 delay，所以现在有全网槽位」
- 「delay 写进状态根，大家必须同一个数」
- 「所有 CometBFT 都已经没有 timeout_commit」
- 未标注出处的 1s / 6s / 12s 当永恒共识或结算 SLA

---

## 8. 边界

本页不写某条应用链如何算平均间隔。不把 ADR 里的产品名字当成那些链的规范保证。不把 PBTS 的 timely 窗和 delay 糊成一词。
