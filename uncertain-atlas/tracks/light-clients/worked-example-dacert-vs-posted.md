# 工作实例：DACert 不是数据已经贴上房东链，AnyTrust 不是已经 Rollup DA

> **事实 / 推断 / 建议** 已分开。
> 对照：[乐观 Rollup 档案](../../protocols/optimistic-rollup/README.md)、[L7.2](../../courses/level-07-modular/L07-M02-data-availability.md)、[L7.4](../../courses/level-07-modular/L07-M04-rollup-tenant.md)、[KZG ≠ DAS](worked-example-blob-vs-das.md)、[NMT ≠ DAS](worked-example-nmt-vs-das.md)、[OP 推导头](../finality/worked-example-unsafe-vs-derived.md)。
> 主文献：Arbitrum 官方 [AnyTrust Protocol](https://docs.arbitrum.io/how-arbitrum-works/deep-dives/anytrust-protocol)。资料层级是官方文档，不是冻结 Ethereum 规范。不另写 19 节（品类档案已有）。
> 本页钉 **DACert ≠ 全文已经在父链**、**AnyTrust ≠ Rollup DA**、**凑不齐签名回退贴全文 ≠ 已经只走委员会**、**证书未过期 ≠ 已经永存档案**。不抄委员会人数、诚实人数、过期天数、回退分钟。

---

## 0. 先修

- [L7.2](../../courses/level-07-modular/L07-M02-data-availability.md) 数据可用
- [不变量 9](../../libraries/invariants/README.md) 提交 ≠ 兑付
- [不变量 23](../../libraries/invariants/README.md) 短时 blob ≠ DAS
- [不变量 124](../../libraries/invariants/README.md) NMT ≠ DAS
- [不变量 142](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见「也是 Arbitrum」或看见父链 Inbox 里有一笔，以为批次全文已经在以太坊上，或以为 AnyTrust 和 Rollup 是同一句 DA，或以为委员会证书过了就和纠删抽样同一把尺子。

官方句（事实）：

- AnyTrust 是 Arbitrum Nitro 的变体。官方写它用「温和的信任假设」换更低费用。这是假设，不是已经和 Rollup 同一安全。
- 协议要求所有 Arbitrum 节点（含验证者）都能拿到子链 inbox 里每一笔的数据。**Rollup** 的办法：把压缩批次以 blob 或 calldata **贴到父链**。官方写这是用 Arbitrum 时费用最大的一块。
- **AnyTrust** 改走外部 Data Availability Committee（DAC）：委员会存数据、按需提供。不是已经把全文贴上父链。
- 中心对象是 Data Availability Certificate（DACert）。证书里有：数据块哈希、过期时间、以及「够数的委员会成员签了 (哈希, 过期时间)」的证明（Keyset 哈希 + 谁签了的位图 + 聚合签）。本页不抄「够数」的公式，也不抄曲线名当不确定常量。
- 官方把 DACert 写成：在委员会诚实假设下，证明该哈希的原文至少能从一名诚实委员那里拿到，**至少到过期时间**。不是已经永存在父链。
- 排序者贴父链有两条路：像普通 Nitro 那样贴**全文**，或只贴一张证明数据可用的 **DACert**。父链 Inbox **拒**使用无效 Keyset 的 DACert；证书其余合法性由**子链代码**检查。
- 子链读 inbox：看见全文就按普通 Nitro 读。看见 DACert 则先验 Keyset 有效（父链 Inbox 已经验过这份 Keyset），再验签名人数够、聚合签对、过期时间仍晚于子链当前时间一个官方命名窗。证书无效则丢掉，读下一块。证书有效则去读数据块——官方写因为证书有效，数据被保证可拿。
- 排序者若在官方写的一段时间内凑不齐签名，就放弃 DAC，**回退到 Rollup 模式**：把全文直接贴到父链。子链两种格式都能读。回退不是「已经只走委员会」，也不是「回退了所以和抽样 DA 是同一句」。
- Keyset：委员会成员的公钥集合 + 一张有效 DACert 需要多少签。用哈希标识。父链 `KeysetManager` 维护当前有效 Keyset；子链 `Owner` 可增删。本页不把 Owner 钥写成协议已经去中心。
- Data Availability Server：委员会跑的软件。给排序者的提交 API 与给世界的按哈希读取 API 是两扇门。存储后端是部署事实。

DACert、父链上的全文、委员会诚实假设、纠删抽样、短时 blob 服务窗，是不同对象。

---

## 2. 直觉（ELI15）

普通租客把整本练习册塞进学校储物柜：Rollup DA。谁有钥匙都能打开柜门抄作业。  
特价租客只往储物柜塞一张「委员们签字：练习册在我们抽屉里，过期之前来拿」：DACert。  
柜子里没有练习册，只有这张条。条过期了，官方也不再说委员还保证拿得到。  
委员凑不齐签字，房东就改回「把整本塞进储物柜」。  
走廊里随机抽碎片（Celestia DAS）是另一栋楼的办法。

小朋友看见「也是 Arbitrum」，以为储物柜里已经有整本。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| Rollup DA | 压缩批次以 blob / calldata 贴上父链 | 委员会证书；抽样 DAS |
| AnyTrust | 外部委员会存数据，父链常见只收证书 | 已经和 Rollup 同一 DA |
| DACert | 哈希 + 过期 + 够数委员签 | 全文已经在父链；已经永存 |
| Keyset | 委员公钥 + 有效证书要多少签 | 信标验证者集合；抽样委员会 |
| 无效证书 | 子链丢掉，读下一块 | 父链已经收下所以数据已齐 |
| 回退 Rollup | 凑不齐签则贴全文 | 已经只走委员会；已经是 DAS |
| 过期时间 | 官方保证拿到数据的下限 | 已经像以太坊 calldata 永在 |
| 4844 sidecar | 短时服务窗里的袋 | 委员会抽屉 |
| Celestia DAS | 扩展方阵随机抽样 | 委员签字 |

---

## 4. 最小案例

用户在一条 AnyTrust 链转一笔。

1. 排序者把批次送给委员会。委员存数据、签 (哈希, 过期)。不是已经贴上以太坊。
2. 排序者把 DACert 送进父链 Inbox。钱包或浏览器看见「上了 L1」。Inbox 里是证书，不是全文。
3. 子链验证书。过期窗不够或签不够，官方写丢掉这块，读下一块。不是父链有一笔就等于数据已齐。
4. 排序者一时凑不齐签，改贴全文。官方叫回退到 Rollup 模式。这是另一条路，不是 AnyTrust 已经变成抽样 DA。
5. 有人把「Arbitrum」听成和 OP 推导头同一句。不变量 141：那是 `unsafe` / `safe` / `finalized`。本页问的是数据在父链还是在委员抽屉。
6. 有人把 DACert 听成 Celestia 抽了几格。不变量 124：抽样问方阵能不能重建。本页问的是委员会签字。

「L1 上有一笔，所以数据已经在以太坊」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 聚合签验的是 (哈希, 过期)，不是全文已经在父链。本页不证伪造 |
| 协议 | 必须点名问的是全文贴父链、DACert，还是凑不齐签后的回退 |
| 实现 | 子链验证书；存储后端会变 |
| 部署 | 谁当委员、Keyset 谁改，是部署事实 |
| 经济 | 官方用信任假设换费用；TVL / 费率不是安全证明 |

**推断：** 产品句若只写「也是 Arbitrum，数据在以太坊」，读者会把证书听成全文，或把委员会听成纠删抽样。  
**建议：** 不确定第一版不要靠外部 DA 委员会。若对照，必须点名数据在父链还是在证书背后的抽屉；不要抄「温和信任」当优点。不要抄人数或过期天数。不要写怎样扣数据或伪造证书。

---

## 6. 和另外几句不是同一句

1. **提交 ≠ 兑付**（不变量 9）：根被房东头包含 ≠ 桥可兑付。本页是数据在哪，不是桥窗。
2. **短时 blob ≠ DAS**（不变量 23）：4844 sidecar 有服务窗。本页的过期是委员会证书，不是 blob 窗。
3. **NMT ≠ DAS**（不变量 124）：命名空间齐了 ≠ 方阵可用。本页没有抽样。
4. **OP 推导头**（不变量 141）：`unsafe` / `safe` / `finalized`。本页可以发生在同一条乐观家族链上，问的是另一轴。
5. **有效性四档**（不变量 138）：排序者回执 / L2 / L1 高度。本页不是 SNOS。
6. **平行链可用**（不变量 125）：纠删片在验证者磁盘。本页是许可委员会。

不要把委员会人数、诚实人数、过期天数、回退分钟、费率抄进不确定常量。不要写怎样让委员不给数据或怎样拼假证书。不编博物馆页。不另写 19 节。哪条产品链开 AnyTrust、Owner 怎么换 Keyset、DAS 存 S3 还是本地，标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
DACert ≠ 全文已经贴上父链
AnyTrust ≠ Rollup DA
Inbox 收下证书 ≠ 子链已经读到数据
证书过期窗还在 ≠ 已经永存档案
凑不齐签名回退贴全文 ≠ 已经只走委员会
委员会诚实假设 ≠ 纠删抽样 / Ethereum DA
「也是 Arbitrum」 ≠ 已经和 OP 推导头同一句
```

语料：[C146](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「AnyTrust = Rollup，只是更便宜。」「L1 上有一笔 = 数据在以太坊。」「委员会证书 = DAS。」「回退了所以没有信任假设。」  
**边界：** 不讲某一版 Nitro 的证书字节布局。不填人数或天数。不把官方文档写成信标规范。不另写 19 节。不写怎样扣数据。产品链选型与 Owner 钥另标。
