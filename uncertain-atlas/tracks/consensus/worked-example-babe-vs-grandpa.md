# 工作实例：BABE 出块了，不等于已经 GRANDPA 最终

> **事实 / 推断 / 建议** 已分开。
> 对照：[L4.6](../../courses/level-04-bft/L04-M06-hotstuff-casper-contrast.md)、[L7.3](../../courses/level-07-modular/L07-M03-shared-security.md)、[Polkadot 档案](../../protocols/polkadot/report.md)、[共识表](README.md)、[最终性表](../finality/README.md)、[backed ≠ 可用](../finality/worked-example-backed-vs-available.md)、[两种最终性](../../libraries/anti-patterns/two-finality-sold-as-one.md)。
> 主文献：Polkadot Wiki [Consensus](https://wiki.polkadot.network/learn/learn-consensus/)、[Cosmos 对照](https://wiki.polkadot.network/learn/learn-comparisons-cosmos/)、[Glossary](https://wiki.polkadot.network/docs/glossary)。
> 本页钉 **BABE 出块 ≠ GRANDPA 最终**。不抄槽秒数、期望终局秒数、「百万块」、「上千生产者」、异步 ⅕、wiki 超多数数字、EIP-1011。

---

## 0. 先修

- [L4.3](../../courses/level-04-bft/L04-M03-locks.md) 锁与最终不是一盏灯
- [L4.6](../../courses/level-04-bft/L04-M06-hotstuff-casper-contrast.md) 每高度 commit ≠ 检查点最终
- [L5.2](../../courses/level-05-ethereum/README.md) head / justified / finalized 是另一套三词
- [不变量 126](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见中继还在出新块，或 explorer 上刚出现一条 BABE 块，以为已经不可逆。

官方句（事实）：

- 中继是**混合共识**：最终性装置 GRANDPA + 出块装置 BABE。两者作为**独立服务并行**跑。
- 官方目标：概率活性（总能出新块）+ 可证明最终（规范链上没有回滚机会）。同时躲开两边的缺点——Nakamoto「也许跟错叉」、纯 BFT「卡住就什么都不出」。
- GRANDPA **对链达成协议，不对单个块**。超过官方超多数的验证者证明某条链含块 B，则 **B 及以前的祖先一次最终**。同一轮里，不同投票者可以投**不同高度**。
- BABE **必须建在已经 GRANDPA 最终的链上**。最终头之后，剩下的分叉选择是**最多主块**（primary），不是最长链。次块（secondary）用来填 VRF 抽空的槽；同槽已有主块则次块被忽略。
- 一槽多个 VRF 赢家：各自出块、赛跑，暂时分叉，直到 GRANDPA 砍掉一条。
- 词汇表：BABE 双签 = 同一槽出多块；GRANDPA 双签 = 同一轮签多条冲突链。Authority 在 BABE 里是出块者，在 GRANDPA 里是链投票者。不是同一对象。
- Cosmos 对照页：Tendermint **在同一条路径上**出一块、终一块。官方写拆开的理由：出块之后、终局之前，还可以做可用性与有效性检查。
- BEEFY 是挂在**已经 GRANDPA 最终**的块上的第二套桥协议（MMR + ECDSA）。BEEFY 绿不是已经解释了 GRANDPA。

出了块、explorer 绿了、桥客户端看见 BEEFY，是三盏灯。

---

## 2. 直觉（ELI15）

报社每天出号外，法院另开庭盖章。

- 记者抢到槽、印出一张号外：BABE。街上已经在传。
- 同一小时可能印出两张互相打架的号外：赛跑，不是已经定谳。
- 法官一次给整叠祖先盖章：GRANDPA。盖的是**这条卷宗**，不是单独一张纸。
- 记者下一张必须接在已盖章的卷宗后面。没盖章的那段，数的是「主块多」，不是「纸更长」。
- 桥对面的公证处再盖一次：BEEFY。那是给外人看的复印件，不是本院判决书。

小朋友看见报摊又出了新号外，以为法院已经判了。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| BABE 主块 | VRF 抽中的出块 | 已经最终；已经有效（平行块另算） |
| BABE 次块 | 空槽的保底出块 | 与主块同槽时仍算数 |
| 临时分叉 | 多赢家赛跑后的未最终枝 | 已经规范 |
| 最长链 | Nakamoto 尺子 | hybrid 最终头之后的尺子 |
| 最多主块 | 最终头之后 BABE 的尺子 | 已经 GRANDPA |
| GRANDPA 最终 | 对一条链的超多数证明；祖先一次敲定 | BABE 刚出的头 |
| BABE 双签 | 同槽多块 | GRANDPA 双签 |
| GRANDPA 双签 | 同轮签冲突链 | BABE 双签 |
| Authority（BABE） | 出块者 | 已经在投最终 |
| Authority（GRANDPA） | 链投票者 | 已经在出这块 |
| BEEFY | 已最终块上的桥gadget | GRANDPA 本身；本页新事故 |

头里可以同时写「刚出的块」和「上次最终的块」。一个头，两盏灯。

---

## 4. 最小案例

用户在中继上看见高度往前走。

1. BABE 抽中，出一块。explorer 先绿。这是出块服务。
2. 同槽另一人也可能出一块。两条枝都还活着。
3. 次块填了空槽。若后来看到主块，次块不算。
4. GRANDPA 这一轮有人投得更深、有人投得浅。超多数认定某条链含 B，则 B 和它的祖先一起最终。
5. 之后 BABE 只许接在这笔最终头上。未最终段比的是主块数，不是长度。
6. 桥客户端若再看见 BEEFY，那是第三盏灯。

「中继还在出块」不是「已经不可逆」。那和争议禁用后出块仍在、选举冻住但出块仍在、平行链送不进但中继仍最终，对象都不同：那些是事故或管道；本页是协议本来就把两套服务拆开。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | BABE 用 VRF 抽槽；GRANDPA / BEEFY 用另一套签。同一个人两套角色 |
| 协议 | 出块服务与最终服务并行；最终对链、一次敲定祖先；最终头之后比主块不是比长度 |
| 实现 | 两个独立服务；一个活着不等于另一个没停 |
| 部署 | explorer / RPC 先跟 BABE 头，不是已经最终 |
| 经济 | 两种双签不是同一种过错；不要写怎样造 |

**推断：** 产品句若只写「中继已出块」或「混合共识更快」，读者会把号外和判决糊成一盏灯。  
**建议：** 不确定第一版保持 CometBFT 式同路径出块+终局。若以后拆两套装置，用户可见的「到了」必须点名是出块还是最终。

---

## 6. 和另外几句不是同一句

1. **每高度 commit**（CometBFT / 不变量 40 的亲戚、L4.6）：出一块终一块，同一条路径。本页是拆成两条服务。
2. **head / justified / finalized**（L5.2）：Gasper 三词。Wiki 自己写 GRANDPA 与 Casper FFG 的差别：同轮可投不同高度；最终块才回写出块的分叉选择。
3. **两种最终性卖成一种**（不变量 135）：头上两枚最终哈希。本页是出块装置 vs 最终装置。精读：[`../finality/worked-example-doomslug-vs-bft.md`](../finality/worked-example-doomslug-vs-bft.md)。
4. **backed ≠ 可用 ≠ 批准 ≠ GRANDPA**（不变量 125）：平行链纳入管道。本页是中继自己的出块与终局。批准之后才拿去 GRANDPA，是管道接到本页的那一盏灯，不是本页把管道重讲一遍。
5. **出块还在 ≠ 纪元已转**（不变量 110）、**中继最终 ≠ 平行链已出**（不变量 114）、**Active ≠ Confirmed 时 GRANDPA 可跳**（不变量 99）：事故或治理。本页是正常协议对象。

不要把槽秒数、期望终局秒数、「百万块一次最终」、「上千出块者」、异步 ⅕、wiki 超多数、EIP-1011 抄进不确定常量。也不要写怎样双签 BABE 或 GRANDPA。BEEFY 只点名「已最终块上的另一套桥 gadget」，不展开 AncestryProof。

---

## 7. 「不确定」测试句（建议）

```text
BABE 出块 ≠ 已经 GRANDPA 最终
GRANDPA 对链投票 ≠ 对单个块 commit
同轮不同高度的票 ≠ 已经乱最终
最终头之后最长链 ≠ hybrid 的分叉选择
次块存在 ≠ 空槽已经没块；同槽有主块则次块不算
一槽多赢家 ≠ 已经分叉定谳
BABE 双签 ≠ GRANDPA 双签
Authority 出块 ≠ Authority 已经在投最终
BEEFY 绿 ≠ 已经解释了 GRANDPA
中继还在出块 ≠ 终局装置还在走
```

语料：[C130](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「混合共识所以出块就是最终。」「看见新块就是不可逆。」「最长链就是 Polkadot 的尺子。」「BEEFY 过了就是已经懂 GRANDPA。」「这和 Tendermint 每高一 commit 是同一句话。」「这和平行链 backed 是同一句话。」  
**边界：** 不讲 BABE 抽签公式、GRANDPA 投票字节、怎样拼双签。不抄秒数 / 百万 / ⅕ / 超多数数字。不写 AncestryProof / BEEFY 论坛利用路径。不编博物馆页。档案 §15 已有的复盘不在本页重编。
