# 工作实例：委员会下标被挪出签名不是已经没有委员会

> **事实 / 推断 / 建议** 已分开。
> 对照：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)、[head ≠ justified ≠ finalized](worked-example-head-vs-justified-vs-finalized.md)、[处理完一块 ≠ 改头](worked-example-processed-vs-forkchoice.md)、[同步委员会样本 ≠ 全集](../light-clients/worked-example-sync-committee.md)。
> 主文献：[EIP-7549](https://eips.ethereum.org/EIPS/eip-7549) Move committee index outside Attestation。官方 EIP。不另写 19 节。
> 本页钉 **委员会下标被挪出签名消息 ≠ 已经没有委员会**、**AttestationData.index 写成零 ≠ 已经删掉该字段**、**分叉后第一块可以没有证明 ≠ 已经没有 LMD 票**、**本页不改执行层**、**EIP-7549 ≠ 同步委员会抽样**。不抄委员会上限 / 最少验票数 / 块内证明条数 / 罚没条数 / 位图宽度。不写怎样改 gossip 上的下标、怎样拼聚合证明，也不写怎样污染先见缓存。

---

## 0. 先修

- [L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md) 执行层 / 共识层
- [不变量 127](../../libraries/invariants/README.md) head ≠ justified ≠ finalized
- [不变量 22](../../libraries/invariants/README.md) 同步委员会必须点名样本
- [不变量 149](../../libraries/invariants/README.md) 处理完一块 ≠ 已经改规范头
- [不变量 198](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见委员会下标被挪到签名外面，以为已经没有委员会；或看见 `AttestationData.index` 写成零，以为字段已经删掉；或看见分叉后第一块可以没有证明，以为 LMD 票已经没了；或看见规范编号 7549，以为已经改了执行层，或已经是同步委员会抽样。

官方句（事实）：

- EIP-7549：把委员会的 `index` 字段挪出已签名的 Attestation 消息，好让**相同共识票**能聚合。
- 本页**不改执行层**。
- 共识层：把 `AttestationData` 里的 `index` **固定写成零**；委员会下标改放到外层 `Attestation` 的 `committee_bits`；`aggregation_bits` 容量扩到本槽全部委员会。
- 退役策略选「保留字段、写成零」，不删字段，也不改成 Optional，以免把 `AttesterSlashing` 弄复杂。`AttesterSlashing` 仍带不委员会数据的 indexed attestation。
- 容器改了，分叉前的证明不能进分叉后的块。因此分叉后第一块**可以没有证明**。LMD 票仍可通过 `on_attestation` 进分叉选择，所以只会少掉一部分 FFG 票。分叉最后一槽的证明者会挨一个 epoch 的离线罚。本页选择**不**让新块同时收两个分叉的证明。
- 下标挪出签名之后，恶意改写只可能发生在一条 gossip 主题上；别处外层还有签名挡住。若先跑「证明者必须属于该委员会」再进先见缓存，官方写没有缓存污染风险。
- 规范**没有**把外层 `committee_bits` 写成已经签进 `AttestationData`，也没有把 `index=0` 写成已经没有委员会，也没有把分叉后第一块没有证明写成已经没有 LMD，也没有把本页写成执行层改动或同步委员会抽样。

签名根、委员会下标、链上证明名单，是三件事。

---

## 2. 直觉（ELI15）

投票纸上只写「赞成哪一块」，委员会号码写在信封外面。  
信封外面写了零，不是已经没有委员会。  
新规则第一天信箱可以是空的，不是街上的人已经不举手了。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 已签名的 AttestationData | LMD 票 + FFG 票；`index` 固定为零 | 已经含委员会下标 |
| 外层 committee_bits | 委员会下标现在住的地方 | 已经签进 Data |
| 分叉后第一块可以没有证明 | 旧容器进不了新块 | 已经没有 LMD 票 |
| 7549 | 只改共识层证明容器 | 已经改执行层；已经是同步委员会 |

---

## 4. 最小案例

一条 Ethereum 要对齐「这一口气证明卡在哪」。

1. 看见 `AttestationData.index` 是零。规范：保留字段、固定写成零。不是已经删掉委员会。
2. 看见外层 `committee_bits`。规范：委员会下标现在在签名外面。不是已经签进 Data。
3. 分叉后第一块没有证明。规范：旧容器进不了新块。不是已经没有 LMD 票。
4. LMD 仍走 `on_attestation`。规范：分叉选择还能吃票。不是已经只剩 FFG。
5. 有人把这听成同步委员会（不变量 22）。那是轻客户端抽样。本页是全验证者证明的委员会下标。
6. 有人把这听成 head / justified / finalized（不变量 127）。本页不改那三等。
7. 有人把这听成处理完一块（不变量 149）。本页不改执行层，更不改规范头。

「index=0 = 已经没有委员会 / 外层位图 = 已经签进去 / 第一块空 = 已经没有 LMD / 7549 = 执行层」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 签名根不再含委员会下标；别处外层签名仍挡改写 |
| 协议 | 必须点名问的是已签名 Data、外层位图，还是链上证明名单 |
| 实现 | 分叉后第一块可以空；先验委员会再进先见缓存 |
| 部署 | 硬分叉；选择不收跨分叉旧证明 |
| 经济 | 分叉最后一槽证明者会挨一个 epoch 离线罚；不抄条数 |

**推断：** 产品句若只写「证明更便宜了」，读者会把外层位图听成已经签进 Data，或把第一块空听成 LMD 已经停。  
**建议：** 第一版若做可聚合投票，必须分开已签名票、外层委员会下标、链上名单。不要发明「挪出签名就已经没有委员会」。不要抄条数。不要把 7549 写成执行层。

---

## 6. 和另外几句不是同一句

1. **head ≠ justified ≠ finalized**（不变量 127）：三等确认。本页是证明容器怎么签名。
2. **同步委员会必须点名样本**（不变量 22）：Altair 抽样。本页是全验证者证明的委员会下标。
3. **处理完一块 ≠ 改头**（不变量 149）：执行层刚跑完。本页不改执行层。
4. **leak ≠ slash**（不变量 130）：终局推迟时的离线罚。本页只点名分叉最后一槽会挨一个 epoch 离线罚，不是已经是 inactivity leak。
5. **可罚关系必须写成两票谓词**（不变量 26）：`AttesterSlashing` 仍带不委员会数据的 indexed attestation。本页选择保留 `index=0`，正是为了不把罚没容器一并改复杂。

不要抄委员会上限 / 最少验票数 / 块内证明条数 / 罚没条数 / 位图宽度 / 压缩前后体积。不要写怎样改 gossip 上的下标、怎样拼聚合证明、或怎样污染先见缓存。不编博物馆页。不另写 19 节。同步委员会抽样、Gasper 三等、执行层请求总线是另一对象。三等精读：[`worked-example-head-vs-justified-vs-finalized.md`](worked-example-head-vs-justified-vs-finalized.md)（不变量 127）。

---

## 7. 「不确定」测试句（建议）

```text
委员会下标被挪出签名消息 ≠ 已经没有委员会
AttestationData.index 写成零 ≠ 已经删掉该字段
分叉后第一块可以没有证明 ≠ 已经没有 LMD 票
EIP-7549 ≠ 已经改了执行层 ≠ 同步委员会抽样
```

语料：[C202](../../libraries/adversarial-corpus/README.md)。
