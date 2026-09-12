# L1.2 数字签名

优先级：必学  
先修：L0.3，L0.4，L1.1

---

## A. 先修知识

哈希能绑定「这是哪份数据」。  
签名绑定「谁被授权对这份数据表态」。

---

## B. 核心问题

**验签通过究竟证明了什么？它没证明什么？算法被破时，哪一层救不了你？**

---

## C. 直觉（ELI15）

签名不是在信封上写名字。它是：

1. 用只有持钥者能做的计算，给**这一份精确消息**做了一个印。
2. 别人用公钥检查：这个印是配这把锁、配这张纸的。

验签通过只说明：

> 在算法假设还成立时，拥有对应私钥的人，对这串字节表示了同意。

它不说明：

- 这个人是不是被骗去签字
- 这串字节在另一条链会不会也被当成同意
- 钥匙是不是被偷了
- 十年后这套算法是不是还成立

所以签名消息必须把意图钉死：收款人、数量、哪条链、防重放、费用、算法域。漏一项，印还是真的，事情可以是假的。

---

## D. 正式定义（本科计算机）

一套签名方案：

```text
KeyGen() → (sk, pk)
Sign(sk, m) → σ
Verify(pk, m, σ) → true | false
```

工程不变量：

1. 诚实签名应验过。
2. 没有 `sk` 的人，不应能对**新消息**造出能过验的 `σ`（不可伪造）。
3. `m` 必须是规范化后的字节，不能「两种写法同一语义」。
4. 同一 `sk` 用在不同协议时，必须 **domain separation**：消息里写明「这是哪条链、哪类消息」。

常见算法族（先认脸）：

| 族 | 今天常见用途 | 工程特征 |
|---|---|---|
| ECDSA | Bitcoin 旧式、Ethereum EOA | 随机数泄漏会爆私钥；可 malleable |
| Schnorr | Bitcoin Taproot (BIP-340) | 线性，好做聚合/批量思路 |
| EdDSA | 不少新系统 | 确定性签名，实现仍可能泄漏 |
| BLS | 许多 PoS 投票聚合 | 聚合省带宽，假设和配对成本不同 |
| ML-DSA 等 PQ | 后量子候选 | 公钥/签名更大，验签账要重算 |

**事实：** Bitcoin 的 Taproot 路径使用 BIP-340 Schnorr。Ethereum 外部账户至今默认 secp256k1 ECDSA。  
**建议：** 「不确定」不要自创曲线或自创签名方程。

---

## E. 最小案例

消息（规范化后）：

```text
m = "chain=Uncertain | type=user-tx | from=A | to=B | amount=4 | nonce=7"
```

`σ = Sign(sk_A, m)`

节点：派生或读出 `pk_A` → 地址匹配 → `Verify(pk_A, m, σ)`。

攻击者把 amount 改成 9，仍拿旧 `σ`：应失败。  
攻击者把同一 `σ` 拿到另一条没写 chain 的测试链：若规范忘了域分离，可能成功。这不是数学被破，是工程没钉死。

---

## F. 真实项目

- **Bitcoin（事实）**：早期 ECDSA 有 transaction malleability（同一语义可对应不同 txid）。SegWit 把签名移出 txid 计算。Schnorr 在 BIP-340。
- **Ethereum（事实）**：EIP-155 把 `chainId` 编进签名，减少跨链重放。JSON 里写了 chainId 不是已经编进哈希；旧六字段签仍合法，不是已经防跨链。精读：[`../../tracks/crypto/worked-example-chainid-vs-signed.md`](../../tracks/crypto/worked-example-chainid-vs-signed.md)（不变量 161）。看见 P256 验签预编译不是已经在验默认 k1。验绿不是已经不可延展。空输出不是已经烧光剩余气。精读：[`../../tracks/crypto/worked-example-p256-vs-k1.md`](../../tracks/crypto/worked-example-p256-vs-k1.md)（不变量 204）。看见签过的自愿退出不是已经永远有效。域锁在某次分叉不是已经改了执行层。精读：[`../../tracks/consensus/worked-example-exit-domain-vs-fork.md`](../../tracks/consensus/worked-example-exit-domain-vs-fork.md)（不变量 213）。看见链号指令不是已经是签进哈希的链号。看见指令返回配置链号不是这笔交易已经带了 EIP-155 标识。看见编译期写死的链号不是已经在硬分叉后仍安全。精读：[`../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md`](../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md)（不变量 220）。
- **Cosmos / CometBFT（事实）**：验证者投票是另一类被签消息，必须和用户交易分域。
- **「不确定」（建议）**：用户交易签名和验证者投票从第一天就分开域。后量子换算法时，换的是 `Sign/Verify` 插件，不是整本账。若走 FIPS 204/205 外部 API，角色还要进 `ctx`（不变量 18）；空默认不算完成。见 [`../../tracks/post-quantum/fips-context.md`](../../tracks/post-quantum/fips-context.md)。

---

## G. 源码入口（预告）

1. `Verify` 的入口：失败是共识拒绝还是 mempool 策略？
2. 被签字节如何拼出来（规范编码）。
3. 随机数 / RFC6979 是否在 ECDSA 路径上。

Bitcoin Core：`src/pubkey.cpp` / secp256k1 库。go-ethereum：`crypto` 包。先记门，Level 3/5 再对路径。

---

## H. 攻击者视角

1. 偷 `sk`。链无法分辨。
2. 骗用户签错 `m`（盲签、钓鱼网站）。
3. 跨链/跨类型重放。
4. ECDSA 随机数重复或泄漏 → 私钥可解。这是实现/部署，不是协议口号。三种「nonce」的拆分见 L1.6。域分离精读：[`../../tracks/crypto/worked-example-domain.md`](../../tracks/crypto/worked-example-domain.md)。BIP-340 原文把「抄 nonce 派生却不换标签」写成漏钥：[`../../tracks/crypto/worked-example-tagged-hash.md`](../../tracks/crypto/worked-example-tagged-hash.md)。
5. 海量废签名打爆验签 CPU。后量子时代更狠。
6. 量子计算机对椭圆曲线的长期威胁。见 L1.5。

---

## I. Trade-off

| 选择 | 得到 | 失去 |
|---|---|---|
| 短签名（ECDSA/Schnorr） | 块小、传播快 | 量子假设下脆弱 |
| PQ 签名 | 抗已知量子算法（在其假设下） | 体积、验签、轻证明、投票流量 |
| 一种算法写死 | 实现简单 | 迁移会变成政治 |
| 多签 / 门限 | 单点失窃变难 | 协议与恢复流程变复杂 |

---

## J. 对「不确定」的意义

后量子主线的第一张工程表不是「选哪个论文」，而是：

- 一笔用户交易的签名多少字节
- 一个高度里验证者投票合计多少字节
- 节点每秒能验多少个
- 垃圾交易会不会先把 mempool 的 CPU 吃光

这些数字进 `tracks/post-quantum/`。本课先把「签名 = 授权，不是身份」钉死。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 验签过 = 持对应私钥者授权了这串字节；不证明姓名 |
| 协议 | 域分离：投票签 ≠ 用户签；FIPS `ctx` 是第二层，不是消息前缀的别名 |
| 实现 | 规范化消息、验签配额 |
| 部署 | 侧信道 / 坏 RNG 可漏钥 |
| 经济 | 验签过了不是经济安全；盗钥是保管失败 |

**禁止假学习：** 「签名证明你是谁。」「验签过了所以经济安全。」「Taproot 一个签名 = 脚本树已经公开。」「看见 chainId = 已经签进哈希。」「155 = 1559。」「库验过 = 共识已收。」「66 = 62。」「有了 BLS12-381 预编译 = 已经在验 BLS。」「加法不查子群 = MSM 也不查。」「2537 = 196。」「2537 = 116。」「有了 P256 预编译 = 已经在验 k1。」「验绿 = 已经不可延展。」「空输出 = 已经烧光。」「兼容 = 7212 洞已没。」「7951 = 2537。」「看见签过的自愿退出 = 已经永远有效。」「7044 = 7002。」「签过 = 已经能花。」「签过 = 已经付过。」「资金证明清单 = 已经齐。」
**边界：** 体积数字进账本，本课不填未测值。`ctx` 编码与 hedged 签见 PQ 轨，不在本课抄库文档当 FIPS。子群过了 ≠ 点已经在曲线上：[`../../tracks/failure-museum/cve-2025-30147.md`](../../tracks/failure-museum/cve-2025-30147.md)（不变量 116）。看见 BLS12-381 预编译 ≠ 已经在验 BLS 签：[`../../tracks/crypto/worked-example-bls-precompile-vs-verify.md`](../../tracks/crypto/worked-example-bls-precompile-vs-verify.md)（不变量 199）。看见 P256 验签预编译 ≠ 已经在验 k1：[`../../tracks/crypto/worked-example-p256-vs-k1.md`](../../tracks/crypto/worked-example-p256-vs-k1.md)（不变量 204）。看见签过的自愿退出 ≠ 已经永远有效：[`../../tracks/consensus/worked-example-exit-domain-vs-fork.md`](../../tracks/consensus/worked-example-exit-domain-vs-fork.md)（不变量 213）。看见链号指令 ≠ 已经是签进哈希的链号：[`../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md`](../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md)（不变量 220）。不要写怎样造可延展签。不要写怎样实现链号预言机或重放未绑链号的签。不要写怎样造点。钥匙路径 ≠ 已经揭开脚本树：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。JSON 里的 chainId ≠ 已经编进签名哈希：[`../../tracks/crypto/worked-example-chainid-vs-signed.md`](../../tracks/crypto/worked-example-chainid-vs-signed.md)（不变量 161）。ECDSA 验得过 ≠ 已经是严格 DER：[`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）。不抄链号表。不写怎样重放。不抄 DER 长度。不写怎样改编码。看见签过的消息 ≠ 已经证明能控制资金：[`../../tracks/lifecycle/worked-example-signed-message-vs-control.md`](../../tracks/lifecycle/worked-example-signed-message-vs-control.md)（不变量 258）。不要抄编码前缀或虚拟交易字段。不要写怎样拼能过验证器的签消息。
