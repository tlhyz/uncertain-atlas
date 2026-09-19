# 工作实例：钥匙路径不是已经揭开脚本树

> **事实 / 推断 / 建议** 已分开。
> 对照：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)、[L1.2](../../courses/level-01-crypto/L01-M02-signatures.md)、[txid ≠ wtxid](worked-example-txid-vs-wtxid.md)。
> 主文献：[BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)（Taproot: SegWit version 1 spending rules）。官方 BIP，Status Deployed。不另写 19 节。
> 本页钉 **钥匙路径 ≠ 已经揭开有没有脚本树**、**脚本路径 ≠ 已经揭开全部脚本**、**看见 Taproot 输出 ≠ 已经知道它是付款给钥还是付款给脚本**。不抄控制块长度 / 叶子版本 / annex 字节。不写怎样藏一条脚本路径。

---

## 0. 先修

- [L1.2](../../courses/level-01-crypto/L01-M02-signatures.md) Schnorr / BIP-340
- [L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md) 软分叉
- [L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md) 见证另树
- [不变量 152](../../libraries/invariants/README.md) txid ≠ wtxid
- [不变量 153](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见一笔 Taproot 花费只有一个签名，以为脚本树已经公开；或看见一个 Taproot 输出，以为已经能分辨这是付款给钥还是付款给脚本；或把脚本路径听成已经把全部条件摊在链上。

官方句（事实）：

- BIP-341：新的 SegWit version 1 输出类型。花费规则基于 Taproot、Schnorr 签名和 Merkle 枝。
- Merkle 枝只把**实际执行的那一支**脚本揭到链上，不是把所有可能执行方式都揭开。
- Taproot 把传统上分开的 pay-to-pubkey 和 pay-to-scripthash 政策并成一种输出：都能用一把钥或（可选）一段脚本花，且彼此不可分辨。
- **只要走钥匙路径花费，就不揭开当时是否还允许脚本路径。** 这同时省空间、在花费时提高脚本隐私。
- 非正式设计：输出能直接用对输出钥 `Q` 的签名花掉，或间接揭开内部钥 `P`、脚本与叶子版本、满足脚本的输入、以及证明 `Q` 承诺了那片叶子的 Merkle 路径。
- Taproot 输出是原生 SegWit version 1、32 字节见证程序。规则**只在花费这种输出时**适用。别的输出——包括长度不是 32 的 version 1、或 P2SH 包起来的 version 1——仍按旧规则，不被本页规则绑住。
- 见证栈 0 个元素则失败。去掉可选 annex 之后：剩下恰好 1 个元素走钥匙路径，该元素当签名、必须对输出钥成立；剩下至少 2 个元素走脚本路径。
- annex 是给未来软分叉留的空位；在另一份软分叉定义它之前，用户不应放 annex，否则可能永久丢钱。annex（有或没有）被签名盖住、计入重量，但在 Taproot 验证里其余部分被忽略。
- 输出钥叫 taproot output key，内部控制块里揭开的是 taproot internal key。概念上每个 Taproot 输出对应「一把内部钥条件」加「零个或多个组织成树的脚本条件」。
- 规范**没有**把钥匙路径写成已经揭开有没有脚本树，也没有把脚本路径写成已经揭开全部脚本，也没有把看见一个 Taproot 输出写成已经知道它是付款给钥还是付款给脚本。

钥匙路径、脚本路径、链上那一个输出，是三件事。

---

## 2. 直觉（ELI15）

门牌只钉一把看起来普通的钥匙孔。  
大多数日子用那把钥匙开门，路人看不见门后还有几本备用规章。  
只有走备用规章那天，才拿出**正在用的那一本**，并证明这本早就订在门框里。  
看见钥匙孔绿了，不是规章目录已经贴在街上。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 钥匙路径 | 去掉 annex 后只剩一个见证元素：对输出钥的签名 | 已经揭开有没有脚本树；已经等于没有脚本 |
| 脚本路径 | 揭开执行的那片叶子 + 控制块 | 已经揭开全部脚本；已经等于钥匙路径失败 |
| Taproot 输出 | 一种输出，既能走钥也能（可选）走脚本 | 已经能从输出本身分辨 pay-to-pubkey / pay-to-scripthash |
| annex | 预留扩展位；被签名盖住 | 已经有定义；已经参与 Taproot 其余验证 |

---

## 4. 最小案例

一条 Bitcoin 要对齐「这笔 Taproot 怎么花」。

1. 合作各方用钥匙路径花掉。规范：不揭开当时是否还允许脚本路径。
2. 某次必须走脚本。规范：只揭开实际执行的那一支，不是整棵树。
3. 有人从输出字节读出「这一定是多签脚本」。规范：输出彼此不可分辨。
4. 有人把这听成 txid ≠ wtxid（不变量 152）。本页是花费路径揭开什么，不是两套交易 ID。
5. 有人把这听成 Babylon 三条质押路径（不变量 139）。那是租户脚本，不是 BIP-341 这句「钥路径不揭树」。

「看见一个签名所以脚本已经公开」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | Schnorr / 带标签哈希；输出钥由内部钥和树根拧在一起 |
| 协议 | 必须点名问的是钥匙路径、脚本路径，还是链上那个输出 |
| 实现 | 见证栈剩几个元素，决定走哪条路径 |
| 部署 | 旧节点少验；完整验证看谁升级 |
| 经济 | 空间与隐私来自「多数日子走钥匙路径」的假设，不是官网 TPS |

**推断：** 产品句若只写「Taproot 输出」，读者会把备用规章听成已经贴在门牌上。  
**建议：** 第一版若做「一个输出、多条条件」，必须写清平常那次花费揭不揭开树。可以不上 Taproot / MAST。不要抄控制块公式。可以跳过「看见一个签名所以脚本树已经公开」。153 keypath vs scriptpath bundled unbundling 完成（1554 item 1 / 1555 item 2 / 1556 item 3）；精读 [`worked-example-kpsp-notree-vs-bundled.md`](worked-example-kpsp-notree-vs-bundled.md)（不变量 1554 item 1）、[`worked-example-kpsp-notall-vs-bundled.md`](worked-example-kpsp-notall-vs-bundled.md)（不变量 1555 item 2）、[`worked-example-kpsp-notlook-vs-bundled.md`](worked-example-kpsp-notlook-vs-bundled.md)（不变量 1556 item 3）。不要发明「钥匙路径已经等于没有脚本」。

---

## 6. 和另外几句不是同一句

1. **txid ≠ wtxid**（不变量 152）：两套哈希。本页是两条花费路径揭开什么。
2. **策略 ≠ 共识**（不变量 144）：本地池规则。本页是共识花费规则。
3. **同根不同列表**（不变量 12）：同一 Merkle 根下两份交易列表。本页是脚本树只揭一支。
4. **assumevalid 跳脚本**（不变量 25）：同步加速。本页不是跳过，是钥匙路径结构上不揭树。
5. **BTC 锁 ≠ commit**（不变量 139）：Babylon 在 Bitcoin 上的三条质押路径。本页是 BIP-341 本身的钥 / 脚本。
6. **哈希 ≠ 已揭开赎回**（不变量 170）：更早的付给脚本哈希。本页是一种输出里钥与脚本不可分辨。
7. **脚本路径 ≠ 已是 tapscript**（不变量 189）：本页是 341 结构。脚本路径里怎样跑是另一页。

不要抄控制块长度 / 叶子版本 / annex 字节 / NUMS 点。不要写怎样藏一条别人看不见的脚本路径。不编博物馆页。不另写 19 节。BIP-342 Tapscript 叶子语义见不变量 189。BIP-340 标签公式、BIP-143 签名摘要、annex 当产品功能标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
钥匙路径 ≠ 已经揭开有没有脚本树
脚本路径 ≠ 已经揭开全部脚本
看见 Taproot 输出 ≠ 已经分辨付款给钥还是付款给脚本
一个见证元素 ≠ 已经是脚本路径
annex 在场 ≠ 已经有定义
```

语料：[C157](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「Taproot 输出 = 已经看见脚本。」「钥匙路径绿 = 树上没有脚本。」「脚本路径 = 全部条件已公开。」  
**边界：** 不抄控制块数字。不另写 19 节。不写怎样藏脚本。Tapscript 叶子语义见 **C193** / 不变量 **189**：[`worked-example-tapscript-vs-scriptpath.md`](worked-example-tapscript-vs-scriptpath.md)。annex 产品语义 / NUMS 另标。
