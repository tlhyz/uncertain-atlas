# 工作实例：处理完一块不是已经改规范头

> **事实 / 推断 / 建议** 已分开。
> 对照：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)、[Ethereum 档案](../../protocols/ethereum/README.md)、[head ≠ justified ≠ finalized](worked-example-head-vs-justified-vs-finalized.md)、[Engine API 尺寸](../failure-museum/ethereum-2024-03-sepolia-engine-rpc.md)、[本头 AppHash](../consensus/worked-example-apphash-vs-this-block.md)。
> 主文献：[EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)（Final）。Engine API 的 `engine_newPayload` / `engine_forkchoiceUpdated` 是这些 PoS 事件的通道名，不是另一套语义。不另写 19 节。
> 本页钉 **处理完一块 ≠ 已经是规范头**、**没有 `POS_FORKCHOICE_UPDATED` ≠ 已经改 fork choice**、**事件里的 head ≠ 已经 finalized**。不抄过渡总难度。不写怎样发假 forkchoice 或扣 payload。

---

## 0. 先修

- [L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md) 执行层 / 共识层
- [不变量 127](../../libraries/invariants/README.md) head ≠ justified ≠ finalized
- [不变量 96](../../libraries/invariants/README.md) 出块通道尺寸
- [不变量 149](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见执行层刚跑完一块，或看见 Engine API 回了 `VALID`，以为规范头已经指过去；或看见 `forkchoiceUpdated` 也回 `VALID`，以为已经 finalized。

官方句（事实）：

- EIP-3675：`POS_FORKCHOICE_UPDATED` 发生时，才更新 proof-of-stake 的 fork choice 状态。该事件带**规范链的头**和**最近 finalized 块**两份引用。第一份 finalized 出现之前，finalized 哈希用全零占位。
- 每次（含第一次）该事件：必须把从创世到事件点名的头当成规范链；把头设成事件点名的那一块；从第一份真正的 finalized 起，把最近 finalized 设成事件点名的那一块。这些对块树存储的改动必须**原子**。
- 规范写：**必须严格执行。禁止对头做「乐观」更新。** 即便在当前头上又处理了一块，这块成为新头当且仅当伴随一次 `POS_FORKCHOICE_UPDATED`。
- 测试清单另写：头和 finalized 按最近一次该事件设；**没收到该事件，不得更新任何 fork choice 状态**。
- 草案里曾经还有 `POS_CONSENSUS_VALIDATED`。Final 文本删掉：它危险——同一块可被两条冲突的 PoS 枝同时指到，于是对同一块可能又 TRUE 又 FALSE。
- 规范**没有**把「处理完一块」写成已经改头，也没有把事件里的 head 写成已经 finalized，也没有允许执行层自己把下一块乐观推成头。

处理、点名头、点名 finalized，是三件事。

---

## 2. 直觉（ELI15）

厨房刚验收完一盘菜（处理 / `newPayload`），不是已经宣布「今晚主菜就是它」。  
司仪另喊一次「今晚主菜是这盘、不可撤的是那盘」（`POS_FORKCHOICE_UPDATED` / `forkchoiceUpdated`）。  
验收通过，不是已经上桌当头盘，更不是已经写进不可撤菜单。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 处理一块 / `newPayload` | 按执行规则验并跑这块 | 已经改规范头；已经 finalized |
| `POS_FORKCHOICE_UPDATED` | 共识层点名头和 finalized | 处理本身；头已经等于 finalized |
| 规范头 | 事件点名的 head | 刚处理的下一块；已经不可逆 |
| finalized 引用 | 同一事件里另一份哈希 | 头已经最终；占位全零已经是第一份 finalized |
| 乐观改头 | 规范禁止 | 「我刚跑完所以已经是头」 |

---

## 4. 最小案例

一条合并后的以太坊要对齐「这块已经是头」。

1. 执行层在当前头上处理了 B。规范：处理不是改头。没有伴随的 `POS_FORKCHOICE_UPDATED`，B 不得成为新头。
2. 共识层发出该事件，点名 head = B、finalized = 更早的 F。规范：现在规范链的头是 B；最近 finalized 是 F。不是 B 已经 finalized。
3. 有人把 Engine API `VALID` 听成头已经指过去。通道名是 `newPayload` / `forkchoiceUpdated`。`VALID` 说的是这次调用的结果，不是已经把两份哈希糊成一盏灯。
4. 有人把这听成 Gasper 的 head / justified / finalized 三等（不变量 127）。那是信标检查点。本页是执行层：处理 ≠ 事件改头。
5. 有人把这听成 Engine API 尺寸（不变量 96）。那是通道有多宽。本页是哪一次调用才改头。

「跑完所以已经是头」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 事件用块哈希点名；全零 finalized 是占位不是已最终 |
| 协议 | 必须点名问的是处理、点名头，还是点名 finalized |
| 实现 | Engine API 两扇门；`VALID` 不是已经改完两份哈希 |
| 部署 | CL 与 EL 各跑各的；没收到 forkchoice 事件，EL 不得自己改头 |
| 经济 | 提议者奖励看规范头，不看「我刚跑完」 |

**推断：** 产品句若只写「执行层收下了」，读者会把验收听成已经上桌。  
**建议：** 第一版可以保持投票前先跑完、提交和头同一条路径。若拆 EL/CL，必须写清处理不是改头。不要抄过渡总难度。不要发明执行层乐观改头。

---

## 6. 和另外几句不是同一句

1. **head ≠ justified ≠ finalized**（不变量 127）：信标三等。本页是执行层处理 ≠ 事件改头。
2. **Engine API 尺寸**（不变量 96）：通道有多宽。本页是哪一次调用才改头。
3. **OP `unsafe` ≠ 已推导**（不变量 141）：L2 推导档。本页不是 rollup。
4. **本头 AppHash ≠ 本块已交差**（不变量 147）：CometBFT 头字段滞后。本页是以太坊 fork choice 事件。
5. **多客户端同根**（不变量 3）：两家跑完同一列表根要一样。本页不是「VALID 已经同根」。
6. **请求承诺 ≠ 已处理**（不变量 192）：头上的请求总线。本页是哪一次调用才改头。承诺不是已经改头，也不是共识层已经处理请求。

不要抄过渡总难度。不要写怎样发假 forkchoice 或扣 payload。不编博物馆页。不另写 19 节。Engine API 的 `ACCEPTED` / `SYNCING` 细表、Builder 出块标成另一对象。EIP-7685 请求总线见不变量 192。

---

## 7. 「不确定」测试句（建议）

```text
处理完一块 ≠ 已经是规范头
没有 POS_FORKCHOICE_UPDATED ≠ 已经改 fork choice
事件里的 head ≠ 已经 finalized
禁止对头做乐观更新
VALID ≠ 已经把头和 finalized 糊成一盏灯
```

语料：[C153](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「跑完 = 已经是头。」「`VALID` = 已经 finalized。」「下一块叠在当前头上 = 已经改头。」  
**边界：** 不讲某一版 Engine API 的 `payloadId`。不抄过渡总难度。不另写 19 节。不写怎样发假事件。Gasper 三等、通道尺寸、`ACCEPTED`/`SYNCING` 细表另标。
