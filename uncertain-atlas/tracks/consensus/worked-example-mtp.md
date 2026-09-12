# 工作实例：Bitcoin 的 MTP 不是一把钟

> **事实 / 推断 / 建议** 已分开。
> 对照：[PBTS 四尺](worked-example-pbts.md)、[调整钟](../network/worked-example-adjusted-time.md)、[CVE-2024-52912](../failure-museum/cve-2024-52912.md)。
> 主文献：[Bitcoin Core `GetMedianTimePast`](https://github.com/bitcoin/bitcoin/blob/master/src/chain.h)、[`ContextualCheckBlockHeader` / `ContextualCheckBlock`](https://github.com/bitcoin/bitcoin/blob/master/src/validation.cpp)、[`BlockValidationResult`](https://github.com/bitcoin/bitcoin/blob/master/src/consensus/validation.h)、[BIP 113](https://github.com/bitcoin/bips/blob/master/bip-0113.mediawiki)。
> 本页钉 **同一缩写 MTP 至少两份共识工作，太新是第三把尺**。不把 `nMedianTimeSpan` / `MAX_FUTURE_BLOCK_TIME` 抄成不确定常数。

---

## 0. 先修

- [L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)
- [L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)
- [不变量 40](../../libraries/invariants/README.md#40-块时间必须点名算法)

---

## 1. 核心问题

阿比看见头上有个 Unix 时间，以为那是「全网现在」，或以为 MTP、未来窗、对等调整钟、PBTS 是同一个词。

Bitcoin 里至少三把尺。MTP 自己还干两份活。

---

## 2. 直觉（ELI15）

班长在黑板上写「这节课几点开始」。规矩不是「必须等于墙上的钟」，而是：

1. **不能比前几节课黑板时间的中位还早或一样早**——否则这节课的时间戳算假。  
2. **锁门时间**（交易 locktime）看的是**上一节**黑板中位，不是这节班长刚写的那个数。  
3. **不能比你自己手表快太多**——这可能是班长瞎写，也可能是你手表慢了。

第三把尺用的是**你的表**，不是黑板中位。

---

## 3. 正式对象（源码 / BIP，事实）

### 3.1 怎么算 MTP

`CBlockIndex::GetMedianTimePast()`（`src/chain.h`）：从**本索引**往父走，最多取 `nMedianTimeSpan` 个块的 `nTime`，排序，取中间那个。本页不把该跨度抄成不确定默认。

对**新块**来说，太早检查读的是**父块**的 MTP，因此输入是父块及其祖先，不含新块自己的 `nTime`。

`BLOCK_VALID_TREE` 注释写 `timestamp >= median previous`；真正拒绝条件见下一节的 `<=`（必须**严格大于**父 MTP）。

### 3.2 工作 A：新块太早

`ContextualCheckBlockHeader`：

- `block.GetBlockTime() <= pindexPrev->GetMedianTimePast()` → `time-too-old`，结果 `BLOCK_INVALID_HEADER`

`validation.h` 注释：`BLOCK_INVALID_HEADER` = invalid proof of work **or time too old**。

这是头级共识拒绝：时间戳相对**已经上链的块时间序列**太旧。不读本节点墙上钟。

### 3.3 工作 B：交易 locktime（BIP 113）

CSV 部署之后，`ContextualCheckBlock` 写明 `Enforce BIP113 (Median Time Past)`：`IsFinalTx` 的时间截止用 `pindexPrev->GetMedianTimePast()`，不再用**本块** `nTime`。

BIP 113 动机（BIP 原文）：块时间戳没有严格单调；若 locktime 看本块 `nTime`，出块者可以把时间往未来写，提前收尚未到期的锁时交易费。改成看父 MTP 之后，这个截止随链单调前进。

**事实：** 工作 A 和工作 B 都叫 MTP，对象不同。A 管新块头。B 管块里交易是否 final。  
**事实：** BIP 113 激活前，locktime 用的是本块时间。不要把「Bitcoin 一直用 MTP 做 locktime」写成创世就有的规则。

### 3.4 工作 C：太新（不是 MTP）

同一函数里另一条：

- `block.Time() >` 本节点钟 `+ MAX_FUTURE_BLOCK_TIME` → `time-too-new`，结果 `BLOCK_TIME_FUTURE`

`validation.h` 注释：`BLOCK_TIME_FUTURE` = timestamp too far in the future **(or our clock is bad)**。

现行 `chain.h` 把宽限说成相对 **current time**。历史上同一宽限曾相对**网络调整时间**（52912 打的就是那条实现路径）。钟源是实现，不是 MTP 公式。

本页不抄宽限秒数当永恒共识，也不把「太新以后自动变合法」写成规范句——那要跟具体实现的重试路径，这里只钉：**太新 ≠ 太早，拒绝码都不同**。

### 3.5 四家族对照（补 PBTS 页）

| 尺子 | 读什么 | 失败码 / 动作（Bitcoin 列） |
|------|--------|-----------------------------|
| MTP 工作 A | 父块时间序列的中位 | `time-too-old` / `BLOCK_INVALID_HEADER` |
| MTP 工作 B | 同一父 MTP，给 locktime | `bad-txns-nonfinal` / `BLOCK_CONSENSUS` |
| 太新窗 | 本节点钟 + 命名宽限 | `time-too-new` / `BLOCK_TIME_FUTURE` |
| 调整钟（52912） | 系统钟 + 对等偏移 | 实现把真块当成太新 |
| PBTS | 提议者本地钟 vs 收到 Proposal | prevote `nil` |
| BFT Time | LastCommit 加权中位 | 复算不对则拒块 |

---

## 4. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 把本块 nTime 写成墙上现在 | 文案 | 头时间是矿工写的 | 用户按墙钟放货 |
| 把 locktime 当成「到了墙上点」 | 文案 | BIP 113 改用父 MTP | 激活前的旧语义 |
| 把太新写成 MTP 共识 | 文案 | 拒绝码不同；注释承认钟可能坏 | 一台节点离开尖 |
| 把 MTP 抄进 BFT 当默认 | 选型文案 | 四家族表 | 乱填时间的罚没 |

---

## 5. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 头时间进 PoW 承诺 | 「时间已经后量子」 |
| 协议 | 太早看父 MTP；BIP113 后 locktime 也看父 MTP | 「Bitcoin 时间 = MTP」一个词 |
| 实现 | 太新读哪一口钟；`nMedianTimeSpan` 是命名常数 | 把跨度/宽限秒数当不确定默认 |
| 部署 | 本节点钟坏了会误伤太新 | 某 NTP 品牌 |
| 经济 | locktime 曾给矿工抢费激励（BIP 113 动机） | 把 BIP 文「大约多一小时」当产品 SLA |

---

## 6. 对不确定的意义（建议）

- 若学 Bitcoin：文档必须分开「头太早 / locktime / 头太新」。不要写「我们用 MTP」。
- 不要把 MTP 窗口宽度或未来宽限抄进第一版，除非先当空参数并写清拒绝码。
- 不要把 MTP 当 BFT 链的块时间算法（见不变量 40）。
- 太新若读本节点钟，必须能把「本节点拒」从「链判定非法」里拆出来（不变量 29）。

---

## 7. 禁句

- 「MTP 就是 Bitcoin 的现在」
- 「太新和太早是同一条共识」
- 「locktime 一直看本块时间」 / 「locktime 一直看 MTP」（缺激活）
- 「MTP = PBTS = BFT Time」
- 未标注出处的 11 块 / 两小时当永恒共识
- 「填了 nLockTime = 输出已经锁住」（那是 BIP-65，见 [`../state-models/worked-example-cltv-vs-nlocktime.md`](../state-models/worked-example-cltv-vs-nlocktime.md)，不变量 164）
