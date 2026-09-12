# L4.4 ABCI 与 WAL

优先级：必学 / 重要  
先修：L4.3，L0.2

---

## A. 先修知识

共识选出字节串的顺序。`Apply` 算状态。二者不是同一个进程职责。

---

## B. 核心问题

**为什么共识引擎不该懂余额？为什么投票前必须先写日志？**

---

## C. 直觉

两间房子。

前厅（引擎）：只负责「第 9 号决议是不是这份稿」。不懂钱。  
后厅（应用）：只负责「稿上的转账按规则改账」。不懂谁该在第 3 轮提议。

门上的条子叫 ABCI：高度、交易列表、状态哈希来回递。

另外：你要举手之前，先在自己日记本上写「我将对 A 预提交」。写完再举手。断电了，醒来先读日记，不许改口。这本日记叫 WAL。

---

## D. 正式定义

**ABCI（事实，Cosmos/CometBFT）：** 引擎与应用的字节契约。旧接口只在决定时碰应用。ABCI 2.0 在提案创建（`PrepareProposal`）、提案验收（`ProcessProposal`）、precommit 扩展（`ExtendVote` / `VerifyVoteExtension`）再插三处。`CheckTx` 是池预检，不是最终。`FinalizeBlock` / `Commit` 才把高度钉进应用状态。四门精读：[`../../tracks/consensus/worked-example-prepare-process.md`](../../tracks/consensus/worked-example-prepare-process.md)。

应用必须：

- 确定性  
- 对同一高度同一列表返回同一 `AppHash`  
- 崩溃后能恢复到与引擎相同的高度

**WAL：** 先记录将发出的共识消息与内部状态，再对外投票。  
invariant：重启不得发出与已持久化意图矛盾的票。

CheckTx 通过 + 未 Finalize：链上状态未变。Prepare 还可以把这笔从本块名单拿掉（池里未必删）。用户文案不得写成最终。

---

## E. 最小案例

高度 9 commit 块 B。引擎调用应用执行。应用写库写到一半断电。

正确：恢复后要么重放完整高度 9，要么回到高度 8，两端一致。  
错误：应用以为 9 成功，引擎以为 8，下一轮哈希对不上，看起来像「共识坏了」，其实是部署/实现。

投票：节点已 precommit A 并写入 WAL，重启后对 B precommit。这是安全事故，不是「网络抖了一下」。

---

## F. 真实项目

CometBFT + Cosmos SDK。  
Ethereum 的 EL/CL 拆分是亲戚：执行与共识分开，但边界不同，不要叫 ABCI。

---

## G. 源码

预告：ABCI 服务器、`FinalizeBlock`、WAL 的 write-ahead 点。测试里找 crash replay。

---

## H. 攻击者视角

1. 让应用使用时间/map 遍历 → 哈希分裂。  
2. 杀进程专打「票已发出、WAL 未 fsync」。  
3. 用 CheckTx 与 Finalize 的差异做用户欺诈。  
4. 诱使应用把 Process REJECT 或 Verify 扩展 REJECT 当免费过滤器，拖垮活性。

---

## I. Trade-off

分离：可换执行、可换用户签名、好测。  
代价：两套存储对齐；应用不确定则全裂。  
WAL：安全。代价：磁盘延迟；实现复杂。

---

## J. 对「不确定」的意义

**建议：** 第一版就按「引擎不懂钱、应用不懂票、WAL 先写后投」搭。  
后量子换的是应用里的用户 `Verify` 和引擎里的 vote `Verify` 两枚插件，不是推倒重来。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 应用验用户签，引擎验投票签；两插件可换 |
| 协议 | ABCI：共识不知余额，应用不知票 |
| 实现 | CheckTx ≠ Prepare ≠ Process ≠ Finalize；WAL 先写后投 |
| 部署 | 崩溃必须回到原子高度 |
| 经济 | 应用可收费；共识不该按余额改票权，除非经 V(h) |

**禁止假学习：** 「CheckTx 等于已执行。」「Process / Verify 扩展拒绝没有活性代价。」「Finalize 按本高度扩展改状态。」「应用和共识哪个先写磁盘无所谓。」
**边界：** 存储通论在 L9.3。不抄扩展启用高度。精读：[`../../tracks/implementation/worked-example-crash.md`](../../tracks/implementation/worked-example-crash.md)、[`../../tracks/consensus/worked-example-prepare-process.md`](../../tracks/consensus/worked-example-prepare-process.md)、[`../../tracks/consensus/worked-example-vote-extension.md`](../../tracks/consensus/worked-example-vote-extension.md)。
