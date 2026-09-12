# 实例：跳过中间块，不是数一张新委员会的 2/3

目的 A/B。不是考试。  
先修：L4.5、L9.6、[`worked-example.md`](worked-example.md)、[`../consensus/worked-example-vote-signbytes.md`](../consensus/worked-example-vote-signbytes.md)。

规范原文：

- [CometBFT Light Client README](https://github.com/cometbft/cometbft/blob/main/spec/light-client/README.md)  
- [verification_001_published.md](https://github.com/cometbft/cometbft/blob/main/spec/light-client/verification/verification_001_published.md)（`CMBC-FM-2THIRDS.1`、`CMBC-VAL-CONTAINS-CORR.1`、`LCV-FUNC-VALID.1`）

规范目录自己写：英文与 TLA+ 仍有草稿页。本页只钉**已发布**验证文。实现正确 ≠ 模型过了（反模式 model-equals-implementation）。

---

## 故事

阿比的钱包说「BFT 轻客户端，有 +2/3 签名所以到了」。  
他拿到高度 10000 的头和一串新验证者的 commit，**没有**对照自己信任的那份旧集合。  
若攻击者自备一套新委员会，给自己投满 2/3，轻客户端会收下一条从未属于那条链的头。

规范要的不是「新集合看起来过门槛」，而是：**你已经信任的那份 `NextValidators` 里，要有足够重量的人在新 commit 上签字。**

---

## 事实：失败模型先于算法

`CMBC-FM-2THIRDS.1`：若头 `h` 在链上，则 `h.NextValidators` 里存在投票权 **> 2/3** 的子集，其中每个人在 `h.Time + trustingPeriod` 之前都遵守协议。

`CMBC-TIME-PARAMS.1`：`trustingPeriod` **小于** `unbondingPeriod`。验证 README 举例：二者同量级，例如 `TRUSTED_PERIOD = UNBONDING_PERIOD / 2`。这是数量级形状，不是「不确定已选一半」。

初始化：轻客户端从**可信来源**拿到一份 trusted header + 验证者集合。规范写：用户自己负责「这份 inithead 几乎不可能是伪造的」。社会共识 / 以前自己验过的全节点，都是部署假设，不是密码学免费午餐。

---

## 事实：邻接一块 vs 跳过许多块

`LCV-FUNC-VALID.1`（`ValidAndVerified`）：

**共同前置（形状）：** 未信任头形状合法；`untrusted.Time < now + clockDrift`；集合哈希对得上；**trusted 仍在信任期内**（`trusted.Header.Time > now - trustingPeriod`）；trusted 自己的 commit 是对该头的 +2/3；高度与时间都前进。

| 关系 | 规范要的重叠 | 失败返回 |
|---|---|---|
| **紧邻后继** | `trusted.NextValidators = untrusted.Validators`；commit 里 **> 2/3** 来自这份集合，且没有外人 | 前置不满足则错 |
| **跳过中间** | 新 commit 里，属于 `trusted.NextValidators` 的投票权 **> max(1/3, trustThreshold)** | `NOT_ENOUGH_TRUST` → 再取中间头做二分 |

`CMBC-VAL-CONTAINS-CORR.1` 说明为什么跳过时 1/3 够用：信任期内旧集合仍有 >2/3 正确；新 commit 若含旧集合 **>1/3** 的权重，则至少碰到一个当时仍正确的人。  
**不是事实：** 「轻客户端永远只验 1/3。」紧邻后继仍是 +2/3。阈值是参数，规范写 `trustThreshold` 在 1/3 与 2/3 之间。

重叠不够：不是「再信一次 RPC」，而是取介于中间的头，递归建立信任（bisection）。

---

## 它验的是头，不是余额

轻客户端同步的是 **signed header + 验证者集合变化**。  
`Apply` 有没有把阿安的 1 记对，本协议**不验**。状态证明仍要另信「根来自你已接受的头」。  
只信 primary 一台全节点：验证文只管「在失败模型下读操作安全」；**攻击检测**要第二台及以上（secondaries）。规范把验证与检测拆成两块。

攻击类型与上链对象：[`../economic/worked-example-evidence.md`](../economic/worked-example-evidence.md)。检测要 secondaries；问责算法后置。形式化过 ≠ 实现已对。

---

## 五层

| 层 | 本故事 |
|---|---|
| 密码 | 票上的 σ 可以真；域仍要是那条 chain 的 SignBytes |
| 协议 | 重叠的是 **trusted.NextValidators**，不是新委员会自嗨 |
| 实现 | 时钟漂移、集合哈希、二分取头必须按规范 |
| 部署 | inithead 从哪来；是否配置了 secondaries；信任期是否短于解绑期 |
| 经济 | 信任期过后，旧验证者可能已解绑，罚不到 |

---

## 对「不确定」（建议）

1. 默认结算角色仍是全节点。BFT 轻客户端是**显式第二配置**，产品句必须写：信任期、init 头来源、跳过时用的是旧集合的 1/3+。  
2. 不变量 20 / 语料 C22：跳过且旧集合重叠 ≤1/3 → 拒绝；紧邻但 `NextValidators` 对不上 → 拒绝。  
3. 后量子：跳过仍要验一批投票 σ。体积税在账本第 2 行，不在「轻」这个形容词里消失。  
4. 不填 CPU，不选自研轻客户端论文当规范。

---

## 精密检查

**禁止假学习：** 「有 +2/3 签名就是轻客户端。」「BFT 轻客户端验证了余额。」「信任期等于最终性。」「TLA+ 过了所以实现安全。」「ValidAndVerified 所以已经能交证据。」  
**边界：** 不写 IBC 反向高度的未完成问题；不抄某一链的解绑秒数；检测/问责算法后置。Ethereum 弱主观性是亲戚：[`../finality/worked-example-weak-subjectivity.md`](../finality/worked-example-weak-subjectivity.md)。朝前 lunatic 与「验过头 ≠ 能交证据」见 [Alderfly](../failure-museum/alderfly.md)。
