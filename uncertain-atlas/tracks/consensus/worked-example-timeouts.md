# 工作实例：本地超时不是最终性，commit 后再等更不是锁

> **事实 / 推断 / 建议** 已分开。
> 对照：[轮与步](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)、[锁](../../courses/level-04-bft/L04-M03-locks.md)、[PBTS](worked-example-pbts.md)。
> 主文献：[consensus.md](https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md)、[configuration.md](https://github.com/cometbft/cometbft/blob/main/docs/core/configuration.md)。`skip_timeout_commit=true` 的官方语义是「像 `TimeoutCommit=0`」。[PR #2892](https://github.com/cometbft/cometbft/pull/2892) 在较新的线上删掉该键；现行 `main` 的 `config.go` 仍可能保留该字段（pkg.go.dev 标 Deprecated）。
> 本页钉 **超时是本地配置，不是块时间，也不是 commit 还没发生**。不抄文档示例秒数当不确定常数。

---

## 0. 先修

- [L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)
- [L4.3](../../courses/level-04-bft/L04-M03-locks.md)
- [不变量 40](../../libraries/invariants/README.md)（块时间须点名）

---

## 1. 核心问题

阿比看见 `timeout_commit`，以为那是「再等一会儿才最终」，或以为那是 PBTS 的 timely 窗，或以为全网必须填同一个秒数才算共识。

规范写的是：Commit 步已经决定这块。NewHeight 再等，是为了多收几张掉队的 precommit。

---

## 2. 直觉（ELI15）

开会已经盖章了。秘书还在门口多站一会儿，等人把迟到的签名塞进来，好让下一份名单更齐。  
门口多站的时间，不是「还没盖章」。有人把门一关立刻开下一场（`timeout_commit=0`），章还是盖过的。

另一把钟：起草人迟迟不交稿，大家举「弃权」继续。那是怕会开不完，不是改决议规则。

---

## 3. 正式对象（规范 / 官方文档，事实）

### 3.1 状态机里的等待（consensus.md）

| 步 | 超时做什么 |
|----|------------|
| Propose | `timeoutProposeR` 到了 → 进 Prevote（没收到合法提案就 prevote `nil`） |
| Prevote | 先等到任意 +2/3 prevote，再等 `timeoutPrevote` → 进 Precommit |
| Precommit | 先等到任意 +2/3 precommit，再等 `timeoutPrecommit` → 下一轮 Propose；或 +2/3 某块 → **Commit** |
| Commit | 记下 `CommitTime = now`，等到块到齐再进 NewHeight。这里等的是**块**，不是 timeout_commit |
| NewHeight | `StartTime = CommitTime + timeoutCommit`，等到点再 Propose 下一高度，为的是收掉队 commit |

规范：提案超时随轮加大（`timeoutProposeR`），为活性；提案体积有上限，轮数够了就能传完。

官方配置文：成功一轮里，**唯一不管怎样都等的**是 `timeout_commit`。其它超时可以因票先到而提前结束。

### 3.2 这些不是共识参数

`timeout_*` 是**本地配置**。各节点可以不同。官方文档写了不一致的代价：

- `timeout_propose` 过短：自己很快 prevote `nil`，别人的提案更难收齐。两人等权的玩具例子里，短的一方会连出块；文档接着写，人多时网络速度仍受「凑齐 +2/3」限制，不是最快提议者说了算。
- `timeout_commit` 过短：自己更早发下一高度提案，可能多拿出块机会；也可能因此错过别人的提案、prevote `nil`。文档用「可能被 inactivity 罚」当经济提醒，不是本页发明的 slash 谓词。

本页不把文档里的 0s / 示例秒数抄成不确定常数，也不把「十个验证者」玩具故事当成主网事实。

### 3.3 skip_timeout_commit

官方配置注释：`skip_timeout_commit=true` 等价于「像 `TimeoutCommit=0`」——已经 commit 之后立刻开下一高度。  
[PR #2892](https://github.com/cometbft/cometbft/pull/2892) 在较新的线上**删掉该键**，改成直接设 `timeout_commit=0`。现行 `github.com/cometbft/cometbft` `main` 的 `config.go` **仍可能有**该字段（Go 包注释标 Deprecated）。  
**事实：** 某条发布线还列不列这个键，不改变语义。零等待仍是「已经 commit 之后立刻开下一高度」，不是第三种最终性。本页不把「开关还在 / 已经删」写成另一套共识。

### 3.4 都不是另外几把尺

| 对象 | 何时发生 | 是不是最终性 |
|------|----------|--------------|
| timeout_commit | **已经** Commit 之后 | 不是。Commit 已发生 |
| PBTS timely | 验本轮提案时间戳 | 不 timely → prevote nil |
| BFT Time / MTP | 块头上的时间怎么算 | 另一页 |
| 锁 | 诚实者不得对两值乱承诺 | 安全，不是超时 |

---

## 4. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 把 timeout_commit 写成还没最终 | 文案 | 规范：Commit 在 NewHeight 等待之前 | 用户按墙钟放货 |
| 自己把 propose 超时拧到 0 | 本地配置 | 文档：人多时仍要凑 +2/3 | 两人玩具网里的出块不公平 |
| 把超时秒数写成共识 | 文案 | 配置文是本地 | 两实现各等各的 |

---

## 5. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 超时不改被签字节 | 「超时已经后量子」 |
| 协议 | Commit 先于 NewHeight 等待；propose 超时保活性 | 「全网必须同一秒数」 |
| 实现 | 本地配置；skip 已删 | 现行默认毫秒 |
| 部署 | 各节点可以不同；差太大会伤出块机会 | 某机房 RTT |
| 经济 | 文档提醒短 timeout_commit 的出块优势 / 漏提案 | 发明 inactivity slash 公式 |

---

## 6. 对不确定的意义（建议）

- 文档必须分开：锁、块时间、本地超时。不要写「BFT 超时」。
- `timeout_commit` 若保留，写明「已经 commit 之后等多收票」。想立刻开下一高度，写 `= 0`，不要发明第三种最终性。
- 第一版超时先当空参数，测过再填。不要抄文档示例秒数。
- 不要把 create_empty_blocks 的「大约每秒一块」写成结算 SLA。

---

## 7. 禁句

- 「timeout_commit 到了才最终」
- 「超时秒数是共识」
- 「skip_timeout_commit 还在 / 已删，所以更快就是另一种最终」
- 「PBTS = timeout_propose」
- 未标注出处的 3s / 1s / 500ms 当永恒共识

---

## 8. 边界

较新线上「谁填这段等待」见 [`worked-example-next-block-delay.md`](worked-example-next-block-delay.md)。不抄文档秒数。不把 `create_empty_blocks` 写成结算 SLA。
