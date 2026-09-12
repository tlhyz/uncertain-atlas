# 工作实例：KZG blob ≠ 纠删 DAS ≠ 永存档案

> **事实 / 推断 / 建议** 已分开。
> 对照：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)、[L7.2](../../courses/level-07-modular/L07-M02-data-availability.md)、[Celestia 档案](../../protocols/celestia/report.md)、[阿比放货](worked-example.md)、[EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)、[EIP-7594](https://eips.ethereum.org/EIPS/eip-7594)、[Fulu `das-core.md`](https://github.com/ethereum/consensus-specs/blob/master/specs/fulu/das-core.md)。
> 三层对象叠在「以太坊有 DA」四个字下面。分母不同。

---

## 0. 先修

- [L7.2 数据可用](../../courses/level-07-modular/L07-M02-data-availability.md)
- [L5.4 blob](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)
- [不变式 9](../../libraries/invariants/README.md)（提交 ≠ 兑付）
- [不变式 22](../../libraries/invariants/README.md#22-轻客户端必须点名信任对象)

---

## 1. 核心问题

老师在黑板上写了附录的指纹。三种完全不同的下一句：

1. 「走廊里贴着整本附录，过一段时间撕掉。」
2. 「附录撕成很多列，每人只保管几列，抽查过关就相信整本还拼得回来。」
3. 「附录按二维纠删码铺开，轻节点随机抽格子，统计上相信能重建。」

第 1 句是 EIP-4844 的 sidecar。第 2 句是 Fulu PeerDAS。第 3 句是 Celestia DAS。  
指纹对上 ≠ 十年后还能复印；抽到几列 ≠ 执行算对。

---

## 2. 直觉（ELI15）

rollup 把一大袋字节挂到以太坊，是为了让别人能复盘 L2，不是为了让 EVM 读这袋字节。  
EVM 只看见袋子的编号。袋子会过期。过期之后，信标链还可以继续走；想重放当年那条 L2 的人，必须另有档案。

---

## 3. 三层对象（规范事实）

### 3.1 EIP-4844：sidecar + KZG 承诺（Deneb）

来自 [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844) 与 `specs/deneb/`。

| 对象 | 规范怎么写 | 它不是 |
|------|------------|--------|
| Blob | `ByteVector[32 * 4096]`（`BYTES_PER_FIELD_ELEMENT × FIELD_ELEMENTS_PER_BLOB`） | 执行层账户存储、calldata |
| 传播 | 信标块 **引用** 承诺；字节走 **sidecar**，不嵌进 beacon body | 「有信标头就有 blob 体」 |
| 执行层看见的 | `kzg_to_versioned_hash`：`0x01 ‖ sha256(commitment)[1:]`；操作码 `BLOBHASH`；点评估预编译 | blob 字节本身（EVM **读不到** 袋里的数据） |
| 服务窗 | `specs/deneb/p2p-interface.md`：`MIN_EPOCHS_FOR_BLOB_SIDECARS_REQUESTS = Epoch(2**12)` = **4096 epoch** | 永存档案室。换算成「多少天」取决于 slot 秒数，**本页不把换算当规范常量** |
| 块内上限 | Deneb 表：`MAX_BLOBS_PER_BLOCK = 6` | **现行主网个数。** 后续分叉会改这个上限；禁止把 6（或你今天看见的任何个数）当永恒 |

EIP-4844 自己写：sidecar 设计是为了以后把 `is_data_available()` **换成** DAS，从而不必每个信标节点都下完所有 blob。  
**事实：** 4844 的作者把「全员下 sidecar」和「DAS」当成两句。有 KZG 承诺 ≠ 已经在做抽样。

### 3.2 Fulu PeerDAS：一维扩列 + 按 node-id 保管（规范层）

来自 [EIP-7594](https://eips.ethereum.org/EIPS/eip-7594)（要求 4844）与 `specs/fulu/das-core.md`。

| 对象 | 规范值 / 规则 | 它不是 |
|------|----------------|--------|
| 扩展 | 每个 blob 做 **一维** Reed-Solomon 扩展：`FIELD_ELEMENTS_PER_EXT_BLOB = 2 × FIELD_ELEMENTS_PER_BLOB` | Celestia 的二维纠删 |
| 列 | `NUMBER_OF_COLUMNS = 128`（`= CELLS_PER_EXT_BLOB`） | 「一行 = 一个完整 blob」那种抽样 |
| 保管组 | `NUMBER_OF_CUSTODY_GROUPS = 128`；诚实节点至少 `CUSTODY_REQUIREMENT = 4` 组 | 每个全节点默认存全部列 |
| 每槽抽样 | `SAMPLES_PER_SLOT = 8`；`sampling_size = max(SAMPLES_PER_SLOT, custody_group_count)` | EIP 动机段里的「1/8」——**以常量为准**（8/128 列，不是把动机数字抄进产品） |
| 重建 | 拿到 **50%+** 列可用 `recover_matrix` 重建（`recover_cells_and_kzg_proofs` 要求至少一半 cell） | 「抽到 8 列 = 我已经有整本 L2 历史」 |
| 承诺 | 仍是 4844 的 KZG；cell 另有 KZG proof | 换了一套与 4844 无关的根 |

**事实：** PeerDAS 是 **网络层如何确信 blob 此刻可重建**。它不改 EVM 仍只看见 versioned hash，也不把 blob 变成永存状态。

**边界：** 某条网络的 Fulu fork epoch、以及后来改 blob 上限的参数分叉，本页 **不填日期、不填现行个数**。看你检出的 `consensus-specs` 标签和该网配置。

### 3.3 Celestia DAS：二维纠删 + 命名空间

来自 Celestia 档案 / L7.2，不是 4844。

| 对象 | 它是 | 它不是 |
|------|------|--------|
| 主业 | 共识 + 数据可用；执行在别人那里 | 「和以太坊 blob 同一种 DA」 |
| 抽样 | 轻节点随机抽 **纠删份额**；安全是参数化概率 | KZG 点评估预编译 |
| 树 | NMT / 命名空间（完备性 ≠ DAS，见 [nmt-vs-das](worked-example-nmt-vs-das.md)） | `blob_kzg_commitments` |

---

## 4. 一张对照表

| | 4844 sidecar（Deneb） | PeerDAS（Fulu 规范） | Celestia DAS |
|--|----------------------|----------------------|--------------|
| 承诺 | KZG → versioned hash | 同一套 KZG + cell proof | 份额 / NMT 根 |
| 谁必须下多少 | 设计原意：信标节点下 sidecar（服务窗内） | 诚实节点抽固定列数，保管自己的组 | 轻节点抽份额 |
| 编码 | 多项式 / KZG | 一维扩展成 128 列 | 二维纠删 |
| EVM / 执行 | 只见 hash | 只见 hash | 无 EVM |
| 过期 | 4096 epoch 服务窗 | 规范仍有 pruning period | 以 Celestia 自己的存留规则为准 |
| 能得出的句子 | 「这个 hash 被信标块承诺过」 | 「按规范抽到了该抽的列」 | 「按参数抽到了份额」 |
| 得不出的句子 | 「L2 永远可重建」 | 「执行正确 / 和 Celestia 一种 DAS」 | 「头最终 = 执行最终」 |

---

## 5. 攻击者

| 攻击 | 机制 | 规范挡得住的 | 规范挡不住的 |
|------|------|--------------|--------------|
| 把 KZG 说成 DAS | 营销把 4844 叫「以太坊 DAS」 | 4844 正文把 DAS 写成以后的替换 | 用户以为已经在抽样 |
| 把抽样说成执行 | 抽到列 / 份额就显示「L2 已验证」 | 抽样只谈 **数据在** | 状态根、欺诈/有效性证明另走 |
| 窗过了当档案室 | finalized 头里还有 versioned hash | hash 还在；sidecar 服务义务有窗 | 新节点无法只靠 L1 重放当年 L2 |
| 扣留 | 出块者只喂抽样节点 | PeerDAS / Celestia 各有扣留模型 | 参数外的对手、只问 RPC 的钱包 |
| 量子 | KZG 依赖配对 | 4844 用 versioned hash **预留** 换承诺（文中举例 Merkle+STARK） | 现在这版承诺不是后量子 |

---

## 6. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | KZG / 配对 ≠ 纠删码；versioned hash 可换版本 | 「有承诺所以后量子」 |
| 协议 | sidecar、4096 epoch 窗、128 列、每槽至少 8 个抽样组、一半列可重建 | 现行每块几个 blob |
| 实现 | 客户端是否真抽列、是否过窗仍谎称可取 | 没读实现就写「全网都在 DAS」 |
| 部署 | 钱包必须点名：hash / 抽样 / 自己存档 | 官网「blob 扩容」 |
| 经济 | blob 费市场存在；个数会变 | 把某一周的 blob 费当规范 |

---

## 7. 对不确定的意义（建议）

- 第一版结算机 **不要** 抄 KZG blob 当默认 DA：配对不是后量子；4844 自己都给换承诺留了版本字节。
- 若提供短时 DA：规范必须写出 **服务窗（epoch）**、过窗后谁还存、产品句不得写「已上链所以永远可重建」。
- 若提供抽样 DA：写清编码维度、每槽抽多少、重建阈值；抽到 ≠ `Apply` 正确。
- 不要把 Celestia 的二维 DAS 和 PeerDAS 的列保管写成一个零件。

---

## 8. 禁句

- 「有 blob / 有 KZG 所以和 Celestia 一种 DAS」
- 「信标头 finalized = 这条 L2 永远能重放」
- 「PeerDAS 抽到了所以执行对」
- 「每块 6 个 / 21 个 blob」（把某一分叉的上限当永恒）
- 把 EIP-7594 动机段的「1/8」写成规范常量（规范是 `SAMPLES_PER_SLOT` 与 `NUMBER_OF_COLUMNS`）
- 未标注 fork epoch 的「PeerDAS 已于某日上主网」当本页事实（部署事实跟网走，本页只钉规范对象）
