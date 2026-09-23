# 工作实例：块上的时间，不是墙上的「现在」

> **事实 / 推断 / 建议** 已分开。
> 对照：[调整钟](../network/worked-example-adjusted-time.md)、[四门](worked-example-prepare-process.md)、[CVE-2024-52912](../failure-museum/cve-2024-52912.md)。
> 主文献：[PBTS](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-based-timestamp/README.md)、[BFT Time](https://github.com/cometbft/cometbft/blob/main/spec/consensus/bft-time.md)、[ABCI FeatureParams.PbtsEnableHeight](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。
> 本页钉 **块时间是哪一套算法**。不抄 PRECISION / MSGDELAY 默认毫秒、不抄 BFT Time 的 1 ms 增量当不确定常数。  
> 亲戚：能复算中位数 ≠ 故障者不能抬高 Time，见 [CSA-2026-001 Tachyon](../failure-museum/csa-2026-001.md)（不变量 61）。

---

## 0. 先修

- [L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)
- [L0.6](../../courses/level-00-machine/L00-M06-agreement-problem.md)
- [不变量 29](../../libraries/invariants/README.md#29-网络调整钟不得绕过上限)

---

## 1. 核心问题

阿比看见块头上有个时间，以为那是「全网同意的现在」，或以为那是 Bitcoin 的 MTP，或以为那是对等节点拧过的调整钟。

CometBFT 家族里至少两套**不同**的块时间算法。名字都带 BFT，对象不一样。

---

## 2. 直觉（ELI15）

值班班长在自己手表上盖「这节课开始」的时间戳。全班只问：我收到座位表的那一刻，这个戳是不是落在「略早 / 略晚」的窗子里。窗子太窄，大家都会弃权，课永远开不了。  
另一套旧规矩：不看班长的表，而看上一节课交卷时各人表上的中位数。

墙上的钟、邻居告诉你的偏移、Bitcoin「最近几块的中位」，都是别人家的尺子。

---

## 3. 正式对象（规范，事实）

### 3.1 PBTS

提议者用**自己的本地钟**给块打时间。验证者按 `timely` 决定收不收这份提案：

记收到 `Proposal` 的本地时刻为 `proposalReceiveTime`，块时间为 `ts`：

- `ts <= proposalReceiveTime + PRECISION`
- `ts >= proposalReceiveTime - MSGDELAY - PRECISION`

两条都成立才算 timely。不 timely → **prevote `nil`**（和 Process REJECT 一样伤活性）。

规范给共识加上同步假设：诚实节点同时读钟，相差不超过 `PRECISION`；诚实提议者的 `Proposal` 端到端延迟不超过 `MSGDELAY`。二者是共识参数。

**活性：** `MSGDELAY` 估小了，诚实提案也会被全体拒，可能卡在这一高度。实现里 `MSGDELAY` 按轮变大：`MSGDELAY(r+1) > MSGDELAY(r)`，规范里的原值是 `MSGDELAY(0)`。本页不抄现行毫秒。

**再提议：** 时间戳是确定的——同一块再被提议，保留原时间。已经在更早轮拿到 +2/3 prevote 再提出的块，**不再**验 timely。提议者可能要等到本地钟大于上一块时间，以保单调。

**开关：** `PbtsEnableHeight` 必须大于当前高度。PBTS **一旦启用不能关**。规范鼓励新链用 PBTS，并写 BFT Time **可能**在未来版本弃用——那是规范态度，不是「已经弃用」。

**未决：** 规范 issue 仍问「拜占庭提议者乱填时间能不能罚」。本页不发明罚没谓词。

### 3.2 BFT Time（旧算法）

块 `H` 的时间，由高度 `H-1` 提交轮的 `Precommit` 时间戳做**加权中位数**（权是投票权），输入是本块的 `LastCommit`。中位数一定是某张 precommit 上的时间戳。每个节点都能从同一份 `LastCommit` **确定复算**；算错则拒块。

验证者给自己的 precommit 填时间：默认本地钟；若已锁块或已有提案，则至少比该块时间大一个小增量（规范写了 1 ms，不当不确定常数）。规范声称：拜占庭权 < 1/3 时，中位数落在诚实者给出的值里。

### 3.3 都不是另外三把尺

| 算法 | 块时间从哪来 | 「太离谱」怎么判 |
|------|--------------|------------------|
| PBTS | 本块提议者本地钟 | 相对**本节点收到 Proposal** 的 timely 窗 |
| BFT Time | 上一高度 LastCommit 的加权中位 | 复算中位数对不上则拒 |
| Bitcoin MTP | 父块时间序列的中位（另见 [MTP 三把尺](worked-example-mtp.md)） | 太早：相对父 MTP；locktime：BIP113 后也看父 MTP；太新不是 MTP |
| 调整钟（52912） | 实现：系统钟 + 对等偏移 | 实现上限；绕过是实现事故 |

**事实：** 「块时间 = 墙上现在」在这四列里都不成立。  
**事实：** 把 PBTS 写成 MTP，或把调整钟拒块写成 PBTS / MTP，文献等级都错了。

---

## 4. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 把块时间当墙上现在 | 文案 | 两套算法都写了来源 | 用户按墙钟放货 |
| MSGDELAY 过小 | 参数 | 规范警告活性；实现按轮加大 | 已启用后不能关 PBTS |
| 乱填时间 | 拜占庭提议者 | timely → 别人 prevote nil | 罚没谓词规范仍开放 |
| 把 52912 当改了 MTP/PBTS | 文案 | 那是实现对等偏移 | 一台节点离开尖 |

---

## 5. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 时间戳在被签的提案/票里 | 「时间已经后量子」 |
| 协议 | 两套算法；timely；中位数可复算 | 「BFT 所以时间是真的」 |
| 实现 | MSGDELAY 可按轮加大 | 现行默认毫秒 |
| 部署 | 启用高度；钟同步假设 | 某机房 NTP 品牌 |
| 经济 | 乱填时间未必有罚 | 未决 issue 当已 slash |

---

## 6. 对不确定的意义（建议）

- 文档必须点名块时间算法。不要写「BFT 时间」四个字交差。
- 若抄 PBTS：写出 timely 两不等式、不 timely = prevote nil、再提议不再验、启用后不能关。`PRECISION` / `MSGDELAY` 先当空参数，测过再填；估小了会停。
- 若抄 BFT Time：时间从 LastCommit 复算，不是提议者当场说了算。
- 不要把对等调整钟掺进共识时间；52912 是实现尺子，不是第三套算法。
- 不要发明「时间乱填就 slash」，除非先写成客观谓词（不变量 26）。
- Bitcoin MTP 不要当 BFT 链的默认。

---

## 7. 禁句

- 「块时间就是墙上现在」
- 「PBTS = MTP = BFT Time」
- 「不 timely 所以块非法 / 该罚」
- 「调整钟拒块说明共识改了时间规则」
- 未标注版本的 PRECISION / MSGDELAY / 1 ms 当永恒共识
