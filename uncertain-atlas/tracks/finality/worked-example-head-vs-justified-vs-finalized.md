# 工作实例：出块了，不是已经 justified，更不是已经 finalized

> **事实 / 推断 / 建议** 已分开。
> 对照：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)、[弱主观性](worked-example-weak-subjectivity.md)、[BABE ≠ GRANDPA](../consensus/worked-example-babe-vs-grandpa.md)、[Casper 两票](../economic/worked-example-casper-slashing.md)、[抽样委员会](../light-clients/worked-example-sync-committee.md)、[两种最终性](../../libraries/anti-patterns/two-finality-sold-as-one.md)。
> 主文献：ethereum.org [Gasper](https://ethereum.org/developers/docs/consensus-mechanisms/pos/gasper/)、[Proof-of-stake](https://ethereum.org/developers/docs/consensus-mechanisms/pos/)、[Attestations](https://ethereum.org/developers/docs/consensus-mechanisms/pos/attestations/)、[JSON-RPC 块参数](https://ethereum.org/developers/docs/apis/json-rpc/)。
> 本页钉 **head ≠ justified ≠ finalized**，以及 **latest ≠ safe ≠ finalized**。不抄槽秒数、epoch 长度、押金、美元、罚没天数、inactivity 连续个数。

---

## 0. 先修

- [L4.3](../../courses/level-04-bft/L04-M03-locks.md) 锁与最终不是一盏灯
- [L4.6](../../courses/level-04-bft/L04-M06-hotstuff-casper-contrast.md) 每高度 commit ≠ 检查点最终
- [L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)
- [不变量 127](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见钱包绿了，或 RPC 回了 `latest`，以为已经不可逆。有人更细一点，看见 `safe` 或「已经 justified」，仍当成 finalized。

官方句（事实）：

- Gasper 是两套装置：LMD-GHOST 选头，Casper-FFG 给某些块升级成最终。
- 最终要走**两步**。总质押的三分之二投票赞成该检查点进入规范链 → 升成 **justified**。官方立刻补一句：justified **不太可能**回滚，但**在某些条件下可以**。
- 再有一个检查点在它上面被 justified，并且两检查点之间存在 **supermajority link**（三分之二总质押认定 B 是 A 的正确后代）→ 较旧的升成 **finalized**，较新的升成 justified。
- 这两步**不是每个 slot 都发生**。只有 epoch 边界块（checkpoint）能被 justified / finalized。一槽只有一部分人投票，一整 epoch 才凑齐全员，所以超多数链接只能在检查点之间证明。
- 一张 attestation 的 `data` 里同时有三票：`beacon_block_root` 是此刻 fork-choice 的**头**；`source` 是看见的最近 **justified**；`target` 是本 epoch 第一块。奖励旗标也是 source / target / head 三面分开算。
- JSON-RPC 块参数官方写成三个标签：`latest` = 最新提出的块；`safe` = 最新 **safe head**；`finalized` = 最新 finalized。官方**没有**把 `safe` 写成 justified。
- 回滚 finalized 需要关键共识失败，并且毁掉至少三分之一总质押。不要把页上的美元 / 「数百万 ETH」抄进产品。
- 链一段时间不能最终时，另有 inactivity leak：不跟多数链投票的人质押被慢慢抽走，直到多数重新够三分之二。这是活性恢复，不是高度已经停，也不是已经 slash。精读：[`worked-example-inactivity-leak.md`](worked-example-inactivity-leak.md)（不变量 130）。

钱包绿勾、`latest`、`safe`、justified、finalized，是不同对象。

---

## 2. 直觉（ELI15）

学校门口每天换一张课表（头）。  
教务处先盖「本周草拟已锁定」（justified）：多半不会换，但仍可能换。  
再盖「上一周已经归档」（finalized）：再改要按破坏规则罚人。

小朋友看见门口课表，或听见「已经锁定」，以为档案室已经收了。  
班委一张纸条上同时写了：我跟哪张门口课表、我认哪份草拟、我认哪份本周首页。三句话印在同一张纸上，不是已经盖完两种章。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| head / `latest` | LMD-GHOST 此刻跟随的块；RPC「最新提出」 | 不可逆；已经 justified |
| justified | 检查点过了三分之二总质押的第一步升级 | 已经 finalized；与 CometBFT 每高 commit 同一语义 |
| finalized | 再过一档检查点 + supermajority link 之后的第二步 | 「用户已经看见余额」；从创世同步一样安全 |
| checkpoint | epoch 边界块 | 每一个 slot 的提议块 |
| supermajority link | 两检查点之间的三分之二总质押链接 | 单槽委员会自己的多数 |
| `beacon_block_root` | 头票 | 已经投了最终 |
| `source` / `target` | FFG 最终票的两端 | 已经 finalized |
| `safe` | RPC「最新 safe head」 | 官方页没有写成 justified；不是 finalized |
| inactivity leak | 终局卡住时抽少数质押，好让多数再凑够 | 高度已经停；已经最终 |

一个 JSON-RPC 调用可以选 `latest`、`safe` 或 `finalized`。选错标签，读到的不是同一盏灯。

---

## 4. 最小案例

用户转 1，钱包立刻绿。

1. 当前 slot 有人出块。这是提议。RPC `latest` 可能已经指到它。头还可以摆。
2. 验证者发 attestation：头根、source、target 写在同一份 `data` 里。头票绿不是 source/target 已经升级。
3. epoch 边界检查点凑齐三分之二总质押：该检查点 justified。官方：仍可能在某些条件下回滚。
4. 下一档检查点也被 justified，并且两档之间有 supermajority link：较旧的那档 finalized。
5. 若有人用 `safe` 当结算：官方只保证这是 safe head，没有把它写成 finalized，也没有写成 justified。
6. 若终局迟迟不来：出块与头票仍可能继续；inactivity leak 是另一条活性路径，不是「已经停链」。

「PoS 所以秒到」把出块、justified、finalized 糊成一盏灯。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | attestation 聚合 BLS；三旗标仍是三句 |
| 协议 | 头由 LMD-GHOST 选；justified / finalized 由 FFG 两步升级；只发生在检查点 |
| 实现 | 客户端把 head 事件和 finalized 事件分成两条流；RPC 三个标签 |
| 部署 | 钱包默认跟 `latest` 是部署选择，不是协议已经最终 |
| 经济 | 回滚 finalized 要烧掉至少三分之一总质押；justified 没有这句 |

**推断：** 产品若只写「已经确认」或「safe 了」，读者会把草拟章和归档章听成一句。  
**建议：** 不确定第一版不要同时卖三等确认。结算句钉一种协议对象。不要把 `safe` 写成已经 justified 或已经 finalized。

---

## 6. 和另外几句不是同一句

1. **BABE ≠ GRANDPA**（不变量 126）：中继出块服务 vs 最终服务。本页是同一条 Gasper 里的三等：头、中间检查点、最终检查点。以太坊没有「justified」的 Polkadot 同义词。
2. **finalized ≠ 从创世一样安全**（不变量 24）：弱主观性。本页是确认等级本身。
3. **抽样 2/3 ≠ 全集最终**（不变量 22）：Altair 同步委员会。本页是全质押的 FFG 升级。
4. **两票谓词 ≠ 已 slash**（不变量 26）：怎样才可罚。本页是用户看见的三等灯。
5. **NEAR 两枚最终标记**（two-finality-sold-as-one）：Doomslug vs BFT。本页是 head / justified / finalized。
6. **每高度 commit**（L4.6）：CometBFT 同路径。本页官方写：升级不在每个 slot 发生。

不要把槽秒数、epoch 长度、押金、美元、罚没日程、inactivity 连续个数、聚合人数抄进不确定常量。也不要写怎样让 justified 回滚。不编博物馆页。

---

## 7. 「不确定」测试句（建议）

```text
出块 / head / latest ≠ 已经 justified
justified ≠ 已经 finalized
justified 不太可能回滚 ≠ 已经不能回滚
supermajority link 是检查点对，不是每个 slot
一张 attestation 的头票 ≠ 已经投了最终
source / target 旗标绿 ≠ 已经 finalized
JSON-RPC latest ≠ safe ≠ finalized
safe ≠ 官方已经写成 justified
终局推迟 / inactivity leak ≠ 高度已经停
PoS ≠ 每个槽都 commit
```

语料：[C131](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「PoS 所以秒最终。」「出块了就是 finalized。」「justified 就是不可逆。」「`safe` 就是 justified。」「`safe` 就是 finalized。」「和 Tendermint 一样一槽一 commit。」「这和 BABE / GRANDPA 是同一句三等。」  
**边界：** 不证 Gasper 论文、不填现行 epoch 秒数、不抄罚金与美元。弱主观性见专页。slash 谓词见 Casper 精读。同步委员会见轻客户端专页。不写怎样重组 justified。Solana RPC 三档是另一句：[`../consensus/worked-example-poh-vs-tower.md`](../consensus/worked-example-poh-vs-tower.md)（不变量 133）。
