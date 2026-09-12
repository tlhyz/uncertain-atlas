# 工作实例：blob gas 不是普通执行 gas，EVM 能读承诺不是已经读到袋里的字节

> **事实 / 推断 / 建议** 已分开。
> 对照：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)、[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)、[L7.1](../../courses/level-07-modular/L07-M01-four-layers.md)、[KZG ≠ DAS](worked-example-blob-vs-das.md)、[策略 ≠ 共识](../mempool/worked-example-policy-vs-consensus.md)、[提交 ≠ 兑付](../economic/worked-example.md)。
> 主文献：[EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（Final）。资料层级是 EIP。不另写 19 节。
> 本页钉 **blob gas ≠ 普通 gas**、**EVM 能访问承诺 ≠ 已经读到 blob 字节**、**付了 blob fee ≠ 数据已经永存**、**执行层不负责持久化 blob**。不抄每块上限、目标、`GAS_PER_BLOB`、兆字节、官网 rollup 倍数。

---

## 0. 先修

- [L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md) gas 是计量
- [L7.1](../../courses/level-07-modular/L07-M01-four-layers.md) 四层
- [不变量 23](../../libraries/invariants/README.md) 短时承诺 ≠ 永存 DA
- [不变量 145](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见「也付了 gas」或看见合约调用了 `BLOBHASH`，以为 blob 字节已经进 EVM，或以为付了 blob fee 数据就永远在，或以为执行 gas 涨了所以 DA 也贵了。

官方句（事实）：

- EIP-4844 Abstract：blob-carrying 交易含大量数据，**EVM 执行不能访问**这些数据，但**能访问其承诺**。
- Gas accounting：引入 blob gas，是**新的气种**。它**独立于普通 gas**，自己跟目标，类似 1559。目前**只有 blob 按 blob gas 计价**。
- `blob_fee` 在交易执行**之前**从发送者余额扣除并烧掉；交易失败**不退**。
- `BLOBHASH` 从栈上读下标，换成 `tx.blob_versioned_hashes[index]`（或零）。吐出的是 versioned hash，不是袋里的字节。
- Consensus layer validation：共识层负责为数据可用持久化 blob，**执行层不负责**。
- 规范**没有**把 blob gas 写成普通 `gas_used`，也没有把 `BLOBHASH` 写成已经读到 sidecar，也没有把付费写成永存。

执行气、blob 气、承诺、袋里的字节、过期窗，是不同对象。过期窗本身见不变量 23。

---

## 2. 直觉（ELI15）

教室有两种体力券。一种给演算纸（执行）。一种给走廊里那本会撕掉的附录（blob）。  
老师只许你看附录封面的编号，不许把整本附录抄进演算纸。  
付了附录费，不是图书馆已经永久收藏。演算失败，附录费也不退。

小朋友看见「都叫 gas」，以为是同一本账。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 普通 gas | 1559 路径上的执行计量 | blob 的价；DA 已永存 |
| blob gas | 独立气种，目前只给 blob 计价 | 普通 `gas_used`；EVM 算力 |
| versioned hash / `BLOBHASH` | 执行层能读的承诺引用 | 已经读到 sidecar 字节 |
| blob_fee | 执行前扣除并烧掉的 blob 费 | 失败会退；执行已经成功 |
| 执行层 | 验 versioned hash、扣两套费、跑 EVM | 负责持久化 blob |
| 共识层 sidecar | 为 DA 传播/暂存袋 | 执行正确；已经永存 |

---

## 4. 最小案例

一笔带 blob 的 4844 交易。

1. 发送者付普通 gas 上限，另付 `max_fee_per_blob_gas`。规范：两套费。不是「付了执行费就够贴附录」。
2. 合约调用 `BLOBHASH`。规范：栈上得到 versioned hash。不是已经把附录抄进存储。
3. 合约 revert。规范：blob_fee 已烧、不退。不是「失败所以附录费没花」。
4. 执行客户端出块。规范：执行层不负责把 sidecar 存下去。共识层才管 DA 持久化。
5. 有人把这听成「有 KZG 所以是 DAS / 永远可重建」。那是不变量 23。本页问的是气种和 EVM 看得见什么。
6. 有人把这听成 Bitcoin「费率高更正确」。不变量 144：费率不是正确性。本页再钉：两套气不是一套。

「都叫 gas 所以是同一本费用账」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | KZG 承诺 → versioned hash；本页不证伪造 |
| 协议 | 必须点名问的是普通 gas、blob gas、承诺还是袋里的字节 |
| 实现 | 头上 `blob_gas_used` / `excess_blob_gas` 与 `gas_used` 分开记 |
| 部署 | 谁在过期后存历史是部署对象（见 23） |
| 经济 | 两套 1559 式目标；执行堵了不是 DA 已经贵 |

**推断：** 产品句若只写「gas」或「付了 DA 费」，读者会把执行计量听成附录已入库。  
**建议：** 不确定第一版不要把短时 blob 当默认 DA。若对照，必须点名两套气和 EVM 看得见哪一层。不要抄上限或官网倍数。不要写怎样扣 sidecar。

---

## 6. 和另外几句不是同一句

1. **短时承诺 ≠ 永存 / KZG ≠ DAS**（不变量 23）：服务窗与抽样对象。本页是气种和 EVM 可见性。
2. **策略 ≠ 共识**（不变量 144）：Bitcoin 保安手册。本页是以太坊两套气。
3. **提交 ≠ 兑付**（不变量 9）：根进房东头不是桥能兑。本页不是桥。
4. **gas ≠ 墙钟**（不变量 101）：执行计量不是时间。本页再拆执行气与 blob 气。
5. **四层课文**（L7.1）：执行 / 结算 / 共识 / DA。本页给「执行费 ≠ DA 费」一句官方钉。
6. **calldata 地板 ≠ 已改执行气**（不变量 197）：执行气上的 calldata 下限。本页是另一套 blob 气。
7. **抬高日程 ≠ 已改气种 / 已经 PeerDAS**（不变量 200）：本页钉的是两套气和 EVM 看得见哪一层。那一页钉的是目标/上限数字和调价对称，不是已经并账，也不是已经抽样。
8. **blob 底价 ≠ 已并账**（不变量 201）：执行基础费托住的储备下限。本页仍是两套气。那一页钩的是两套价的下限，不是已经并成一本账。

不要把每块上限、目标、`GAS_PER_BLOB`、兆字节、官网 rollup 倍数抄进不确定常量。不要写怎样扣 sidecar。不编博物馆页。不另写 19 节。点评估预编译与 PeerDAS 列抽样标成另一对象（23）。

---

## 7. 「不确定」测试句（建议）

```text
blob gas ≠ 普通执行 gas
EVM 能读 versioned hash ≠ 已经读到 blob 字节
付了 blob fee ≠ 数据已经永存
blob fee 烧掉不退 ≠ 执行已经成功
执行层 ≠ 负责持久化 blob
```

语料：[C149](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「都叫 gas = 同一本账。」「`BLOBHASH` = 已经读到附录。」「付了 blob 费 = 永远可重建。」「执行堵了所以 DA 也贵。」  
**边界：** 不抄 EIP 参数表。不讲某一硬分叉的每块 blob 个数。不把官网 rollup 倍数当事实。不另写 19 节。不写怎样扣数据。过期窗与 DAS 对照见不变量 23。
