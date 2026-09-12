# 工作实例：进了块的 coinbase 不是已经能花

> **事实 / 推断 / 建议** 已分开。
> 对照：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)、[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)、[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[策略 ≠ 共识](../mempool/worked-example-policy-vs-consensus.md)、[MTP 三把尺](../consensus/worked-example-mtp.md)。
> 主文献：[Bitcoin Developer Guide · Block Chain](https://developer.bitcoin.org/devguide/block_chain.html)。官方开发者文档。不另写 19 节。
> 本页钉 **进了块的 coinbase ≠ 已经能花**、**钱包看见奖励 ≠ 已经成熟**、**普通确认深度 ≠ coinbase 成熟窗**、**成熟规则 ≠ 本地策略**。不抄成熟块数进不确定常量。不写怎样花未成熟奖励或怎样用重组作废已花奖励。

---

## 0. 先修

- [L2.1](../../courses/level-02-state/L02-M01-utxo.md) UTXO 是未花费输出
- [L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md) 短分叉会扔掉 stale 块
- [不变量 144](../../libraries/invariants/README.md) 策略 ≠ 共识
- [不变量 41](../../libraries/invariants/README.md) locktime / 太早 / 太新
- [不变量 163](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见矿工奖励已经写进块，以为已经能当普通 UTXO 花；或看见钱包列出这笔奖励，以为已经成熟；或看见商家常用的确认数，以为成熟窗已经到。

官方句（事实）：

- 官方开发者文档：每个块的第一笔必须是 coinbase（也叫 generation），用来收取本块补贴和本块交易费。
- coinbase 的 UTXO 有特殊条件：**至少**再过一段块数，才能被当作输入花掉。
- 官方写明动机：暂时不让矿工花掉这笔补贴和手续费，因为这条块以后可能被判 stale，coinbase 会随块一起毁掉。
- 规范**没有**把「进了块」写成已经能花，也没有把钱包列表写成已经成熟，也没有把商家常用确认数写成这条成熟窗。

进块、看见、能花，是三件事。

---

## 2. 直觉（ELI15）

工钱先记在工单上，过了观察期才能取现。  
工单贴上墙，不等于钱已经在口袋里。  
咖啡店等几分钟出货，和工钱要等多久，不是同一只钟。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| coinbase UTXO | 本块补贴 + 本块费；未成熟不得当输入 | 已经能花的普通输出 |
| 成熟 | 官方要求再过一段块之后才准花 | 钱包列表里看见了；商家常用确认数到了 |
| stale 后毁掉 | 短分叉输掉，这笔奖励与费一起没了 | 已经进块所以已经安全 |
| 共识成熟规则 | 全节点验花费时必须挡 | 本地策略、费率、标准性 |

---

## 4. 最小案例

一条 Bitcoin 要对齐「这一口气奖励能不能花」。

1. 新块第一笔是 coinbase。规范：这笔 UTXO 现在还不能当输入。
2. 钱包列出奖励。规范：看见不是已经成熟。
3. 商家常用几个确认出货。本页：那是经济习惯，不是这条成熟窗。
4. 有人把这听成策略拒（不变量 144）。本页是共识：未成熟当输入，块必须非法。
5. 有人把这听成 locktime / MTP（不变量 41）。本页是 coinbase 输出自己的年龄，不是交易上的锁时字段。
6. 有人把这听成 Zcash coinbase 正余额崩（不变量 109）。本页是 Bitcoin 花不花得了，不是两本账对不上。
7. 短分叉把块判 stale。官方：这正是要等的原因。等过了仍可能被更深重组，那是 L3.1，不是本页已经最终。

「进了块所以已经能花 / 钱包看见所以已经成熟」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 无新原语；花的时候仍验脚本 |
| 协议 | 必须点名问的是这块奖励能不能当输入 |
| 实现 | `ConnectBlock` 花输入时查 coinbase 年龄；两实现必须同拒 |
| 部署 | 钱包「未成熟」标签是 RPC 分类，不是另一条共识 |
| 经济 | 等，是怕 stale 把补贴和费一起毁掉 |

**推断：** 产品句若只写「出块就发奖」，读者会把工单听成已经到账。  
**建议：** 第一版若有出块奖励，必须另写成熟窗。进块不得写成已经能花。不要把商家确认数抄成奖励成熟。不要抄 Bitcoin 的块数当不确定常量。

---

## 6. 和另外几句不是同一句

1. **策略 ≠ 共识**（不变量 144）：本页是共识非法，不是本地不转发。
2. **MTP 三把尺**（不变量 41）：太早 / locktime / 太新。本页是 coinbase 年龄。
3. **6 确认 ≠ 协议最终**（L3.1）：商家政策。本页是奖励能不能当输入。
4. **Zcash 正余额 ≠ 能重启**（不变量 109）：屏蔽池记账。本页是 Bitcoin 花不花。
5. **非 chain block 的 coinbase**（不变量 137）：Kaspa 稳定后无效。本页是 Bitcoin 最重链上的年龄。
6. **高度 ≠ 已在头上**（不变量 173）：coinbase 第一项写高度。本页是能不能花。
7. **Ethereum 出块者开跑已热 ≠ 本页成熟**（不变量 187）：那是执行热集合。本页是 Bitcoin 出块奖励年龄。

不要抄成熟块数 / 补贴表 / 钱包分类字符串进不确定常量。不要写怎样花未成熟奖励，或怎样重组作废已花奖励。不编博物馆页。不另写 19 节。BIP-65 CLTV、BIP-113 locktime、钱包 `immature` / `generate` 细则、减半表是另一对象。Ethereum 出块者开跑预填精读：[`../implementation/worked-example-coinbase-vs-prefill.md`](../implementation/worked-example-coinbase-vs-prefill.md)（不变量 187）。

---

## 7. 「不确定」测试句（建议）

```text
进了块的 coinbase ≠ 已经能花
钱包看见奖励 ≠ 已经成熟
普通确认深度 ≠ coinbase 成熟窗
成熟规则 ≠ 本地策略
```

语料：[C167](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「进了块 = 已经能花。」「钱包列出奖励 = 已经成熟。」「几个确认 = 已经过成熟窗。」「未成熟 = 只是钱包不让点。」  
**边界：** 不抄块数。不另写 19 节。不写怎样花未成熟奖励。策略见 **C148**。locktime 见不变量 41。
