# 工作实例：扩展被拒，丢掉的是整张 precommit，不是这块非法

> **事实 / 推断 / 建议** 已分开。
> 对照：[四门](worked-example-prepare-process.md)、[SignBytes](worked-example-vote-signbytes.md)、[证据](../economic/worked-example-evidence.md)。
> 主文献：[ABCI++ 基本概念](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_basic_concepts.md)、[应用要求](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)、[方法](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)、[数据结构 `CanonicalVoteExtension`](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md)。
> 本页钉 **precommit 上的应用字节**。不抄 `VoteExtensionsEnableHeight`、默认开关、某 SDK 预言机产品。  
> 亲戚：扩展快路径跳过普通票字段检查 → 接收节点 panic，见 [ASA-2024-011](../failure-museum/asa-2024-011.md)（不变量 57）。

---

## 0. 先修

- [L4.2 轮与步](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)
- [L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)
- [四门](worked-example-prepare-process.md)（Process REJECT = 自己 prevote nil）
- [不变量 19](../../libraries/invariants/README.md#19-投票步类型进被签字节)

---

## 1. 核心问题

阿比看见「验证者给块加了应用数据」，以为：

1. 这段数据和 prevote/precommit 是同一份签；或
2. 应用验扩展失败 = 这块共识非法；或
3. 本高度 `FinalizeBlock` 可以按收到的扩展改余额。

三句都假。扩展挂在 **非空 precommit** 上，是**另一份**被签对象。验失败丢掉的是**那张票**。本高度状态不得依赖本高度刚收到的扩展。

---

## 2. 直觉（ELI15）

全班对座位表先举手（prevote）。过了门槛，班长要盖「我认这张表」的章（precommit）。有人让班长在章旁边再夹一张自己写的小纸条。纸条内容共识引擎看不懂。邻座若说「纸条不行」，整枚章（连同「我认这张表」）都会被扔掉，不是把座位表改成非法。小纸条最早下节课值班班长组班报时才能拆。这节课改名册，不许偷看刚收到的纸条。

---

## 3. 正式对象（规范，事实）

### 3.1 何时才有扩展

引擎只在即将发出 **非空** precommit 时调 `ExtendVote`：已经锁住 *v*，且本轮对同一 `id(v)` 有 +2/3 prevote。  
要发 `precommit nil`（+2/3 prevote nil，或 `timeoutPrevote`）时 **不** 调 `ExtendVote`，nil 票也不带 `CanonicalVoteExtension`。

`ExtendVote` 可以不确定。可以返回 0 长度。对共识算法，字节不透明。

### 3.2 两份扩展、两份签

| 字段 | 被签形状 | 重放保护 |
|------|----------|----------|
| `vote_extension` | `CanonicalVoteExtension`：`Extension` + `Height` + `Round` + `ChainID` | 有（规范说与 chain-ID / 高度 / 轮绑在一起） |
| `non_rp_extension` | **按应用给的字节原样签** | 无；应用自己防重放 |

`CanonicalVote`（步类型 / 高度 / 轮 / BlockID / 时间 / chain_id）仍是**另一份**签。见 SignBytes 精读。  
扩展结构**没有** `SignedMsgType`，也没有 BlockID——它不替代 prevote/precommit 域分离。

启用扩展时，两类都会被签（即使应用给空）。关闭时两类与其签名皆空。本页不抄启用高度参数。

**事实：** 空扩展（0 长度）仍要有合法扩展签。引擎对空扩展**仍会**调 `VerifyVoteExtension`。

### 3.3 验收失败丢掉整张票

`VerifyVoteExtension` 必须确定；Accept/Reject **只**依赖本次请求与 `s_{h-1}`（Req 7–8）。  
不对本节点自己发出的 precommit 调用。  
请求里的 `hash` **不保证** 本应用已经对该块跑过 `ProcessProposal`。

`REJECT`：整张收到的 Precommit 视为无效并丢弃——包括「我认这块」的共识票，不只是纸条。  
规范通则：`SHOULD always ACCEPT`，除非你真的知道活性代价。  
+2/3 验证者已经发出对该块的 precommit，若扩展反复被诚实节点拒，仍可能**无法最终确定**这块。

高度已经结束后、还在攒更多 precommit 时，**不再**调 Verify。  
下一高度 round 0 收到上一高度的 precommit 时，规范允许写入 `ExtendedCommitInfo` 而**不**再 Verify。

### 3.4 最早下一次 Prepare 才用；本高度 Finalize 不许用

Accept 的扩展进入内部结构，供 **h+1** 轮到自己提议时的 `PrepareProposal`（`ExtendedCommitInfo` / `local_last_commit`）。  
Prepare 里用上一高度扩展时，规范提醒：过了 +2/3 之后才进来的扩展可能未经 Verify，建议按 Verify 同款逻辑再看一遍。

- **Req 6：** 诚实 *p* 做出的扩展，诚实 *q* 的 Verify 必须 Accept。
- **Req 9：** 高度 *h* 的 Extend / Verify **不得**改 `s_{h-1}`。
- **Req 10：** 正确进程在高度 *h* 算出的 `s_h`，**不得**依赖它在 *h* 收到的任何扩展 *e*。`FinalizeBlock` 的状态与交易结果只依赖 `s_{h-1}` 与已决定块 `v`（Req 11–12）。

**事实：** 把扩展写成「本块执行输入」或「又一层共识有效性」，文献等级错了。

### 3.5 和 Process REJECT 不是同一根钉子

| | `ProcessProposal` REJECT | `VerifyVoteExtension` REJECT |
|--|--------------------------|------------------------------|
| 你拒的是 | 这份提案 | 别人的一张 precommit |
| 你自己接下来 | prevote `nil` | 丢掉那张票，继续等别的票 |
| 块因此非法？ | 否；别人仍可能 commit | 否；票没了，块规则没变 |
| 本高度状态 | 不得因 Process 而改 `s_{h-1}` | 不得因扩展而算进 `s_h` |

---

## 4. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 把扩展当本块 `Apply` 输入 | 应用在 Finalize 读本高度收到的 *e* | Req 10 | 根因节点而异而裂 |
| 用 Verify REJECT 当免费过滤 | 纸条不行就丢整票 | SHOULD Accept；Req 6 | 有足够 precommit 仍停 |
| 把扩展签当 prevote | 复用扩展字节 | 另一套 Canonical 形状；无 Type | 实现若糊成一把签 |
| `non_rp` 重放 | 原样签、无高度轮 | 应用必须自防 | 规范不代劳 |
| 抄启用高度 / 预言机产品 | 配置与生态文案 | — | 数字过期；本页不填 |

---

## 5. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 票一份签、扩展一份签；`non_rp` 无包装 | 「扩展已经后量子」 |
| 协议 | 非空 precommit 才扩展；REJECT 丢票；Req 6–10 | 「扩展失败所以块非法」 |
| 实现 | 双状态：扩展只进下一高度 Prepare 的候选材料 | 某版本默认启用高度 |
| 部署 | 启用扩展 = 每张非空 precommit 多一次签与验 | 现行开关、预言机品牌 |
| 经济 | 扩展可被应用拿去排下一块；那是排序权，不是本块结算 | 某链用扩展做的 MEV |

---

## 6. 对不确定的意义（建议）

- 第一版可以**不启用**扩展。少一份热路径签，后量子更便宜（不变量 16 先按无扩展算）。
- 若启用：必须写清两套被签对象、空扩展仍验、Verify 默认 Accept、`s_h` 不读本高度 *e*。
- 不要用扩展承载本高度结算语义（余额、罚没公式）。罚没仍走证据 → 应用（不变量 21）。
- `non_rp` 不要当默认；要原样签就必须自己写防重放。
- 不要把扩展广告成 PBS 或「应用投票」。

---

## 7. 禁句

- 「扩展被拒所以这块非法」
- 「Finalize 按本高度收到的扩展改状态」
- 「扩展和 precommit 是同一份签」
- 「空扩展不用验」
- 「Verify 拒绝扩展没有活性代价」
- 未标注版本的启用高度、SDK 预言机口号
