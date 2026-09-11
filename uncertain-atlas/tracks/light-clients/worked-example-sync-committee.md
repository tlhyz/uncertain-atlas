# 工作实例：Altair 同步委员会轻客户端（抽样 ≠ 全集合）

> **事实 / 推断 / 建议** 已分开。
> 对照：[CometBFT skip](worked-example-bft-skip.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)、[投票签名域](../consensus/worked-example-vote-signbytes.md)、[EIP-8390 草案](https://eips.ethereum.org/EIPS/eip-8390)。
> 本页只讲 **Altair 稳定规范里已经写进 `specs/` 的同步委员会轻客户端**。它验证的是 **信标头 + 委员会轮换**，不是执行层余额。

---

## 0. 先修

- [L5.2 三种「到了」](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)
- [L9.6 轻节点](../../courses/level-09-systems/L09-M06-light-clients.md)
- [CometBFT skip](worked-example-bft-skip.md)
- [不变式 19](../../libraries/invariants/README.md#19-投票步类型进被签字节)（Altair 给同步消息另开了域）
- [不变式 20](../../libraries/invariants/README.md#20-bft-轻客户端重叠旧集合)
- [不变式 22](../../libraries/invariants/README.md#22-轻客户端必须点名信任对象)

---

## 1. 核心问题

CometBFT 轻客户端问的是：「跳跃后的提交，是否与 **我已经信任的下一验证者集合** 重叠？」

Altair 轻客户端问的是另一句：「这一段信标头，是否被 **当前同步委员会这个固定大小的抽样** 里足够多人签过？」

两句都叫「轻」，信任对象不同。

---

## 2. 直觉（ELI15）

全班 100 万人投票太贵。老师每学期抽 512 个同学当「课代表」，课代表举手说「黑板上这行字是真的」。

你如果只数课代表的手，你验证的是 **这 512 个人**，不是全班。课代表里三分之二举手，不等于全班三分之二同意。

---

## 3. 正式对象（稳定规范，事实）

下列数字来自共识规范 **仍列在 Phase0→Fulu 稳定表** 的 Altair 文件，不是营销页。

| 对象 | 规范位置 | 值 / 规则 | 它不是 |
|------|----------|-----------|--------|
| 委员会大小 | `specs/altair/beacon-chain.md` `SYNC_COMMITTEE_SIZE` | `Uint64(2**9)` = **512** | 全体验证者人数 |
| 任期 | 同文件 `EPOCHS_PER_SYNC_COMMITTEE_PERIOD` | `Epoch(2**8)` = **256 epoch** | 每个 slot 换一班 |
| 处理下限 | `specs/altair/light-client/sync-protocol.md` `MIN_SYNC_COMMITTEE_PARTICIPANTS` | `Uint64(1)` | **安全阈值**。`validate_light_client_update` 用它当参与人数下限：1 人只够「这条更新能被处理」，不够「这条更新安全」 |
| 超多数（同步协议） | 同文件 `process_light_client_update` / `is_better_update` | `get_set_bit_count(sync_committee_bits) * 3 >= len(sync_committee_bits) * 2` | **抽样的 2/3**，不是全体验证者的 2/3 |
| 签名域 | `specs/altair/beacon-chain.md` `DOMAIN_SYNC_COMMITTEE` | `0x07000000`；`compute_domain(..., fork_version, genesis_validators_root)` | `DOMAIN_BEACON_ATTESTER` / `DOMAIN_BEACON_PROPOSER` |
| 乐观头安全阈值 | 同文件 `get_safety_threshold` | `max(previous_max_active_participants, current_max_active_participants) // 2` | Casper 最终确定门槛 |

**事实：** 轻客户端验证的更新，绑定的是 **当前同步委员会公钥集合** 上的聚合签名，以及委员会如何轮到下一班。

**事实：** 它不验证执行层账户余额、收据或 EVM 存储。要那些对象，还得另接执行证明或自己跑执行客户端。

---

## 4. 和 CometBFT skip 的对照表

| | CometBFT skip（[工作实例](worked-example-bft-skip.md)） | Altair 同步委员会 |
|--|-----------------------------------------------------------|-------------------|
| 信任起点 | 已验证的 header + `NextValidatorsHash` | 已验证的 bootstrap：当前委员会 + 信标头 |
| 「足够多人」的分母 | **当时的验证者集合**（加权） | **512 人抽样** |
| 跳跃时必须重叠的对象 | 受信任集合的 `NextValidators` | 委员会轮换证明（下一班也是抽样） |
| 签名域 | `CanonicalVote` 的 `Type` + chain-id | `DOMAIN_SYNC_COMMITTEE` + genesis / fork |
| 能证明的状态 | 应用哈希（若 header 带了） | **信标头**；执行层另说 |
| 全集合 2/3 最终性 | Tendermint 提交本身 | Casper FFG 在 **全体验证者** 上；同步委员会 **不替代** FFG |

**建议（不确定）：** 若默认角色是全节点，不要把 Altair 式抽样轻客户端写成「和全节点同一安全」。若提供轻客户端，标题必须写出 **抽样大小和域**。

---

## 5. 攻击者（协议工程师）

| 攻击 | 机制 | 规范能挡的 | 规范挡不住的 |
|------|------|------------|--------------|
| 把抽样 2/3 说成全集合 2/3 | 营销 / 钱包文案 | 规范自己写的是 `committee` 长度 | 用户以为「以太坊已最终确定」 |
| 1 人更新当安全 | `MIN_SYNC_COMMITTEE_PARTICIPANTS = 1` 只是处理下限 | 实现若把 1 当成安全阈值 | 轻客户端跟着一条几乎无人签名的更新走 |
| 乐观头当最终确定 | `get_safety_threshold` 是近期参与的一半 | 规范区分 optimistic / finality | 钱包把 optimistic head 当不可逆 |
| 同步消息无罚没 | 稳定规范 **没有** 给 sync 聚合签名写 attestation 那种 surround/double 罚没 | — | 抽样成员作恶的经济代价 **不是**「和提议/证明同一套罚没」。见下一节草案 |
| 只验证信标头就显示余额 | 轻客户端协议停在 beacon | — | 执行层数据被另一套桥或 RPC 塞进来 |

---

## 6. EIP-8390：草案，不是已激活分叉（事实边界）

[EIP-8390](https://eips.ethereum.org/EIPS/eip-8390)（2026-08-22 创建，状态 **Draft**）提议 **去掉同步委员会和 Altair 轻客户端**。

**事实（草案文本自己写的，不是主网已发生）：**

- 草案主张：同步委员会消息 **没有** attestation 那种可罚没条件。
- 草案主张：轻客户端安全是 **抽样** 安全，不是全验证者集合的 2/3。
- 稳定规范表（Phase0→Fulu）**仍然包含** Altair 轻客户端规范；草案 **没有** 分叉 epoch，**不得**写成「主网已经删掉同步委员会」。

**禁止：** 把草案里的发行量估算、验证者人数、罚没 ETH 估算抄进本页当永恒事实。那些数随信标状态变。

**推断：** 核心研发在重新讨论「抽样轻客户端值不值得付持续发行」。这是治理 / 经济层讨论，不是「Altair 数学被证伪」。

---

## 7. 源码入口（预告，路径以你检出的 `consensus-specs` 标签为准）

- `specs/altair/light-client/sync-protocol.md`（`MIN_SYNC_COMMITTEE_PARTICIPANTS`、`process_light_client_update`、`get_safety_threshold`）
- `specs/altair/beacon-chain.md`（`DOMAIN_SYNC_COMMITTEE = 0x07000000`、`SYNC_COMMITTEE_SIZE`、`EPOCHS_PER_SYNC_COMMITTEE_PERIOD`）

---

## 8. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | BLS 聚合 + 独立域 | 「有域就等于和 Casper 同一安全」 |
| 协议 | 512 抽样、256 epoch、处理下限 1、超多数按委员会长度 | 「轻客户端验证了以太坊状态」 |
| 实现 | 客户端是否把 MIN=1 当安全 | 没读实现就写「都安全」 |
| 部署 | 钱包展示 optimistic vs finalized | 官网「轻节点」四个字 |
| 经济 | 同步委员会有独立奖励；草案在讨论其成本 | 把 8390 的估算当已激活事实 |

---

## 9. 对不确定的意义（建议）

- 全节点默认。若做轻客户端，先写清信任对象是 **全集合重叠** 还是 **固定抽样**。
- 不要把 `MIN_PARTICIPANTS = 1` 这类处理下限抄成安全参数。
- 抽样委员会若存在，签名域必须独立（已经是不变式 19 的亲戚）；罚没条件若没有，就不要在文档里写「和验证者同一刀」。
- **不要**把 Altair 轻客户端当 v1 默认产品抄过去。

---

## 10. 禁句

- 「同步委员会 2/3 = 以太坊验证者 2/3」
- 「MIN_SYNC_COMMITTEE_PARTICIPANTS = 1 所以一条签名就安全」
- 「轻客户端已经验证了你的 ETH 余额」
- 「EIP-8390 已经上主网 / 已经删掉同步委员会」（草案）
- 任何未标注日期的验证者人数、发行量、TVL
