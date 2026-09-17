# 工作实例：装上应用快照，不等于从创世重放过

> **事实 / 推断 / 建议** 已分开。
> 对照：[assumevalid / assumeutxo](worked-example-assumevalid.md)、[弱主观](../finality/worked-example-weak-subjectivity.md)、[BFT 轻跳过](../light-clients/worked-example-bft-skip.md)、[崩溃原子](worked-example-crash.md)。
> 主文献：[ABCI++ 基本概念 · State-sync](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_basic_concepts.md)、[方法 OfferSnapshot / Snapshot](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)、[P2P state sync](https://github.com/cometbft/cometbft/blob/main/spec/p2p/legacy-docs/messages/state-sync.md)。
> 本页钉 **跳过历史块重放之后，信任的是哪一个哈希**。不抄分块字节上限、最近快照条数、频道号。  
> 亲戚：轻验集合对上 ≠ 提议者选择已对齐，见 [ASA-2024-009](../failure-museum/asa-2024-009.md)（不变量 56）。

---

## 0. 先修

- [L9.3](../../courses/level-09-systems/L09-M03-storage.md)
- [L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)
- [不变量 20](../../libraries/invariants/README.md#20-bft-轻客户端重叠旧集合)、[24](../../libraries/invariants/README.md#24-检查点同步必须落在弱主观或信任期内)、[25](../../libraries/invariants/README.md#25-跳过验证必须点名跳过了哪条规则)

---

## 1. 核心问题

阿比看见「节点开了 state sync，几分钟就跟上了」，以为已经从创世执行过每一块。

规范写的是另一条路：发现对等节点上的**应用快照**，按块（chunk）装回去，**不重放历史块**。装完之后，用轻客户端验过的链上头里的 `AppHash`，去对应用现在的根。对上快照自己的 `hash` 字段不够。

---

## 2. 直觉（ELI15）

新生不抄整学年作业，向学长要一份「学期末成绩单复印件」，一页一页订进自己的本子。封面印的「学校钢印总分」才是可以信的；学长自己用彩笔写的页码和备注，对手能仿。订完必须拿钢印总分对一下。对上了，你也**没有**把每一道旧题重做一遍。

---

## 3. 正式对象（ABCI++ / P2P，事实）

### 3.1 四步

| 步 | 方法 | 事实 |
|----|------|------|
| 发现 | 对等节点 `ListSnapshots` | 列表是**元数据**：高度、format、chunk 数、任意 `hash`、任意 `metadata`。不是快照本体。 |
| 出价 | `OfferSnapshot` | 引擎带上这份元数据，以及**轻客户端已验**的该高度 `app_hash`。应用 ACCEPT / REJECT / 拒这种 format / 拒这些发送者。 |
| 装块 | `LoadSnapshotChunk` → `ApplySnapshotChunk` | 按 index 顺序装。应用可要求重取某些块、拉黑发送者。超时装不到下一块则换快照。 |
| 收尾 | `Info` | 本地 `LastBlockAppHash` / `LastBlockHeight` 必须对上期望值，再转入 block sync 或共识。 |

**事实（OfferSnapshot 用法原文形状）：只有 `AppHash` 可信任**，因为它已经过轻客户端验证。其它数据可被对手伪造。应用应另做校验，以免 DoS。验过的 `AppHash` 会在恢复结束时自动对恢复后的应用。

**事实（P2P）：** 快照高度的 light block 用来验 `AppHash`。state sync 用轻客户端验证规程验这些 light block。共识参数另用 `ParamsRequest`，并用头去验。

### 3.2 哪些字段不是钢印

`Snapshot.hash`：任意快照哈希。引擎**不解释**，只比较「相不相等」。相同快照 = 所有字段都相等（含 `metadata`）。  
`metadata` / `format`：应用自定；P2P 文案写 format 与 metadata **可以不确定**。  
对上对等节点宣称的 `hash`，只表示「他们说是同一份快照」，不是轻验过的链上 `AppHash`。

### 3.3 跳过了什么

跳过的是：**历史块的逐高 `FinalizeBlock` 重放**。  
没有跳过：此后新块仍要执行；头上的 `AppHash` 仍要能对上。  
没有自动获得：从创世复算供给、脚本、每一笔历史交易。那些字节若不另存，你没有独立重放路径。

---

## 4. 对照（不要糊成一个开关）

| | ABCI state sync | assumeutxo | assumevalid | 弱主观检查点 | BFT 轻跳过 |
|--|-----------------|------------|-------------|--------------|------------|
| 跳过什么 | 历史块重放 | 暂时跳 UTXO 重放 | 祖先脚本 | 从创世执行 | 中间头 |
| 信任锚 | 轻验头里的 `AppHash` | 编译进二进制的 UTXO 哈希 + 背景全验 | 所选链上的哈希 | 检查点在期内且在路径上 | 旧 `NextValidators` 重叠 |
| 背景全验？ | 规范不要求再重放历史块 | **要**背景 chainstate | 不重放那些脚本 | 不 | 不 |
| 过期 | 轻客户端信任期 | 编译值仍在 | 用户可 `-assumevalid=0` | WS 期 | `trustingPeriod` |

**事实：** 把 state sync 写成 assumeutxo「装上快照、背景还会从创世验完」，文献等级错了。CometBFT 这条路径的设计就是**不**重放历史块。

**事实：** 把「AppHash 对上了」写成「和从创世复算同一安全」，少了轻客户端假设（信任期、重叠旧集合）。见不变量 20、24。

---

## 5. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 伪造快照元数据 | 任意 hash / metadata | 只有轻验 AppHash 可信 | DoS、骗应用先 ACCEPT |
| 装完不对 Info | 块被改过 | 收尾必须对 LastBlockAppHash / Height | 实现若跳过 Info 对根 |
| 用过期轻头 | 信任期外的快照高度 | 轻客户端应拒 | 文案仍写「已全验证」 |
| 把 chunk 当共识 | 分块传输 | 分块是传播 | 用户以为每 chunk 都是块 |

---

## 6. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 对的是头里的 AppHash，不是对等节点的 snapshot.hash | 「快照哈希已经后量子」 |
| 协议 | 跳过历史重放；收尾对 Info；轻验 light block | 「state sync = 从创世」 |
| 实现 | chunk 顺序、重取、换快照 | 某 SDK 快照格式版本 |
| 部署 | 快照从哪来、信任期是否还覆盖该高度 | 现行分块上限当共识 |
| 经济 | 全历史归档是另一份成本 | 某链快照 CDN 品牌 |

---

## 7. 对不确定的意义（建议）

- 第一版默认：从创世（或自己生成的、可重放的归档）同步。State sync 是加速，必须写进部署假设。
- 若提供：产品句必须写「跳过了历史块重放；锚是轻验 AppHash；信任期必须盖住快照高度」。
- 不要抄 assumeutxo 的「背景还会全验」来安慰用户——除非你**另外**实现了一条重放路径。
- 应用必须假定 snapshot.hash / metadata / chunk 内容可伪造，只把 Offer 里的 `app_hash` 当钢印。
- 后量子：轻验仍走投票签；快照很大则 chunk 超时与换对等节点必须先写（对照不变量 36）。

---

## 8. 禁句

- 「state sync 过了所以从创世验证过」
- 「快照 hash 对上了就是 AppHash 对上了」
- 「和 assumeutxo 一样，背景还会全验」
- 「Offer 里的 metadata 已经过共识」
- 未标注版本的 4 MB / 16 MB / 「最近 10 份」当共识常数
