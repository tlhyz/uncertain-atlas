# 工作实例：backed 了，不等于已经可用，更不等于已经最终

> **事实 / 推断 / 建议** 已分开。
> 对照：[L7.3](../../courses/level-07-modular/L07-M03-shared-security.md)、[Polkadot 档案](../../protocols/polkadot/report.md)、[最终性表](README.md)、[Active ≠ Confirmed](../failure-museum/kusama-2024-02-15-disabled-active-dispute.md)、[NMT ≠ DAS](../light-clients/worked-example-nmt-vs-das.md)。
> 主文献：Polkadot Wiki [ELVES / parachain protocol](https://wiki.polkadot.network/docs/learn-parachains-protocol)（官方写明是 Implementers' Guide + AnV 规范的摘要）、[Asynchronous Backing](https://wiki.polkadot.network/docs/learn-async-backing)、[Validator](https://wiki.polkadot.network/docs/learn-validator)；Implementers' Guide [Inclusion](https://paritytech.github.io/polkadot-sdk/book/runtime/inclusion.html)、[Bitfield Signing](https://paritytech.github.io/polkadot-sdk/book/node/availability/bitfield-signing.html)。
> 本页钉 **Candidate / Backable / Backed / Pending availability / Included / Pending approval / Approved / GRANDPA**。不抄槽秒数、吞吐倍数、PoV 兆字节、归档小时、wiki 与 pallet 各自点名的门槛数字。

---

## 0. 先修

- [L4.3](../../courses/level-04-bft/L04-M03-locks.md) 锁与最终不是一盏灯
- [L7.2](../../courses/level-07-modular/L07-M02-data-availability.md) 有头 ≠ 有体
- [L7.3](../../courses/level-07-modular/L07-M03-shared-security.md)
- [不变量 125](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比听见 collator 说「已经上链」，或看见中继头里有一条候选回执，以为平行块已经可用、已经审批、已经 GRANDPA 最终。

官方句（事实）：

- 平行链协议分两段。Inclusion Pipeline：从出块到进入**未最终**的中继分叉。Approval Process：二次检查，过了才批准。
- 状态会变：Candidate → Seconded → Backable → Backed → Pending availability → Included。**Backed 仍可能进不了平行链。**
- Backable：分配到该链的验证者里，多数签了有效性声明。官方立刻补一句：他们是**小子集**，多数不诚实仍然可能，所以此时只是「看起来像合法转移」。
- Backed：中继出块者把**候选回执**记进某条中继分叉。中继块**不含**平行块本身。
- Pending availability：已经 backed，**还不算可用**。必须另证可用，才能算平行链的一块。
- 可用：验证者对纠删片投票。Wiki 与 Inclusion pallet 点名的是两把尺——「有人报告自己持有一片」和「链上 `availability_votes` 过门槛才 enact」。不要糊成一个数字。纠删片在**验证者磁盘**上，不在中继块、也不在链状态里；进中继的是回执里的根。
- 可用**不保证**有效。官方：可用性检查只说明片被分出去了。
- 异步 backing 页另写：**backing 不保证平行块有效。**
- 已可用、已算进平行链之后，仍是 **pending approval**（暂收入）。审批失败会作废该块**及其子孙**；被罚的是这块的 backer，不是子孙的 backer。
- 坏块停在未批准、未被 GRANDPA 最终的分叉上，可以丢掉这条分叉。批准之后，验证者才把该中继块（及其祖先）拿去 GRANDPA。
- 官方还写：Polkadot 保证的是**合法状态转移**，不是「每个状态槽都验过」。验证者不读未被改动的值。
- Inclusion pallet 有 `force_enact`：把待可用的候选当成已经可用。官方写一般不该用，只给会立刻丢掉状态的 Runtime API。

collator 的 RPC、本机 unincluded segment、中继头上的回执，是三个对象。

---

## 2. 直觉（ELI15）

小区请市局来验一箱货。

- 门口三个人看了一眼、签了「像真的」：backed。箱子还可以被丢掉。
- 市局把**回执**钉在公告栏：中继头上有字。箱子不在公告栏里。
- 同事各自收一角碎片并举手：可用。举手不是已经拆开验过每一页。
- 随机抽人再拆箱：审批。过了才批准。
- 局长盖章：GRANDPA。盖章前，整条巷子都可以不要。

小朋友在巷口喊「货到了」，只是 collator 自己看见了自己的箱子。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| Candidate / PoV | collator 交给分配验证者的块 + 见证 | 已经共享安全 |
| Backable | 该组多数有效性声明 | 全验证者已验；已经最终 |
| Backed | 回执进了某条未最终中继分叉 | 平行块字节在中继里；已经可用 |
| Pending availability | backed，等待可用性票 | 已经是平行链的一块 |
| Included | backed 且被当成可用 | 已经审批；已经 GRANDPA |
| Pending approval | 暂收入，等二次检查 | 已经批准 |
| Approved | 二次检查无争议或争议赢了 | 已经最终 |
| GRANDPA 最终 | 中继头被最终性装置敲定 | collator 绿勾 |
| 纠删片 | 验证者磁盘上的份额 | 中继状态；Celestia 轻节点 DAS |
| `force_enact` | 测试/API 假装可用 | 正常可用性谓词 |
| Fishermen | 官方写不计划正式实现 | 还在的第三种角色 |

头里可以同时写回执根和可用性笔记。一个头，几盏不同的灯。

---

## 4. 最小案例

用户在平行链转 1。

1. Collator 打包，RPC 先绿。这是部署，不是 Inclusion Pipeline。
2. 分配组多数签字：Backable。官方：此时仍可能是不诚实小组。
3. 中继作者选中回执：Backed。回执进头。PoV 不在头里。超时不可用 ⇒ 从这条分叉丢掉。
4. 可用性票过链上门槛：Included，仍 pending approval。
5. 二次检查矛盾 ⇒ 争议。失败则这块和它的孩子作废。
6. 无争议或争议赢了：Approved。验证者才拿去 GRANDPA。
7. GRANDPA 过了：共享安全接到这笔上。之前任何一步的绿勾，都不是这一步。

「中继还在出块」不是这条平行候选已经最终。那是不变量 114 的亲戚，对象不同：那边是废弃 API 送不进去；这边是协议本来就分阶段。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 纠删根在回执里；片在磁盘上。批准用另一套 session 钥 |
| 协议 | 上表每一行都是独立谓词；backing / 可用 / 审批 / GRANDPA 不得并成「上链」 |
| 实现 | bitfield 签的是「我有没有自己那一片」，不是「我验完整个 PoV」 |
| 部署 | 只连 collator RPC 不是已经走完 Inclusion |
| 经济 | 审批失败罚的是这块的 backer；未最终的坏分叉可以丢掉 |

**推断：** 产品句若只写「平行链已出块」，读者会把回执、可用、审批、最终糊成一盏灯。  
**建议：** 不确定第一版不要做平行链 / 共享安全租户。若以后借用，用户可见的「到了」必须点名停在哪一行。

---

## 6. 和另外三句不是同一句

1. **Celestia DAS / NMT**（不变量 23 / 124）：轻节点抽样或命名空间齐了。这里是验证者集合内部的纠删片 + 链上 bitfield。
2. **争议 Active ≠ Confirmed**（不变量 99）：禁用状态机。本页是纳入管道的阶段名。
3. **废弃 `backing_state`**（不变量 114）：返回编码。本页是「backed 这个词本身不等于可用」。

不要把 wiki 的槽秒数、吞吐倍数、PoV 尺寸、归档小时、或「⅓ / ⅔」门槛抄进不确定常量。异步 backing 页自己写：生产网尚未充分测性能。也不要写怎样让候选缺席、怎样扣片。

---

## 7. 「不确定」测试句（建议）

```text
collator RPC 绿 ≠ Inclusion Pipeline 已开始
Backable ≠ 全验证者已验，≠ 已经有效
Backed ≠ 已经可用，≠ 回执所在分叉已经最终
Pending availability ≠ 已经是平行链的一块
Included ≠ 已经批准
Approved ≠ 已经 GRANDPA 最终
中继头有回执 ≠ PoV / 纠删片在链上
可用性票过了 ≠ 已经有效
backing 过了 ≠ 已经有效
force_enact ≠ 正常可用性
```

语料：[C129](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「collator 出块就是共享安全。」「中继头有回执就是平行块在链上。」「backed 就是可用。」「可用就是有效。」「审批过了就是已经最终。」「这和 Celestia DAS 是同一种可用。」  
**边界：** 不讲 BABE 抽签公式、GRANDPA 投票字节、怎样拼 PoV。不抄秒数 / 倍数 / 兆字节 / 门槛数字。不写 AncestryProof / BEEFY 论坛利用路径。People / 弹性扩容仍不当事故页。档案 §15 已有的复盘不在本页重编。
