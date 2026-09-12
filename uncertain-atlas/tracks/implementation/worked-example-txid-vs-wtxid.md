# 工作实例：txid 不是 wtxid，改见证不是已经改交易身份

> **事实 / 推断 / 建议** 已分开。
> 对照：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L1.1](../../courses/level-01-crypto/L01-M01-hash.md)、[策略 ≠ 共识](../mempool/worked-example-policy-vs-consensus.md)、[同根不同列表](../../libraries/invariants/README.md)。
> 主文献：[BIP-141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)（Segregated Witness Consensus layer）。官方 BIP。不另写 19 节。
> 本页钉 **txid ≠ wtxid**、**改见证 ≠ 已经改 txid**、**coinbase 里的 wtxid 承诺 ≠ 已经在头上的 txid Merkle**。不抄承诺魔数 / 重量公式。不写怎样改见证编码。

---

## 0. 先修

- [L1.1](../../courses/level-01-crypto/L01-M01-hash.md) 哈希域
- [L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md) SegWit 软分叉
- [不变量 144](../../libraries/invariants/README.md) 策略 ≠ 共识
- [不变量 152](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见交易有一个哈希，以为签名已经进了这个身份；或看见块头 Merkle 绿了，以为见证也已经进头；或把 wtxid 听成已经等于 txid。

官方句（事实）：

- BIP-141：定义一种叫 witness 的新结构，**和交易 Merkle 树分开承诺进块**。它装检查有效性需要、但决定交易效果不需要的数据。脚本和签名被挪进这里。
- 每笔交易有 **2 个 ID**。txid 定义不变：传统序列化的 double SHA256。wtxid 是带见证的新序列化的 double SHA256：`[nVersion][marker][flag][txins][txouts][witness][nLockTime]`。
- 见证数据**不是脚本**。非见证程序的输入必须配空见证。若所有输入都不是见证程序，这笔的 wtxid **等于** txid。
- 新块规则要求承诺 wtxid。coinbase 的 wtxid 当作全零。用各笔 wtxid 当叶子算见证根，类似头上的 hashMerkleRoot。承诺记在 coinbase 的 scriptPubKey。块内若没有任何见证数据，这笔承诺可选。
- 动机句：签名数据不再是交易哈希的一部分，签名方式怎么变，都不再改交易身份。这是共识层，不是策略。
- 规范**没有**把 txid 写成已经含见证，也没有把头上的 txid Merkle 写成已经承诺了 wtxid，也没有把旧节点看见 txid 写成已经验过见证。

身份、见证、头上的交易 Merkle，是三件事。

---

## 2. 直觉（ELI15）

作业编号（txid）只看题目本身。  
答题过程订在另一本附件（witness / wtxid）。  
改笔迹不改编号。老师在成绩册封面只钉题目编号的目录；附件目录另订在班长的备注栏（coinbase 承诺）。  
看见封面目录绿了，不是已经核对过每一本附件。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| txid | 传统序列化的哈希；后续输入引用它 | 已经含见证；已经验过签名附件 |
| wtxid | 带见证序列化的哈希 | 已经等于 txid；已经印在头 Merkle |
| 见证 | 验有效性用、不算效果的数据 | 脚本本身；已经进 txid |
| coinbase wtxid 承诺 | 新节点要的见证根 | 头上那棵 txid Merkle；旧节点已经验过 |

---

## 4. 最小案例

一条 Bitcoin 要对齐「这笔交易的身份」。

1. 花费 SegWit 输出的交易 T。规范：txid 不含见证；wtxid 含。改见证不改 txid。
2. 后续输入引用 T 的 txid。规范：子交易钉的是编号，不是附件。
3. 块头 Merkle 用各笔 txid。新规则另要 coinbase 承诺 wtxid 根。头绿不是见证根已经在头里。
4. 有人把这听成策略 ≠ 共识（不变量 144）。本页是共识 BIP 的两套哈希，不是 mempool 策略。
5. 有人把这听成同根不同列表（不变量 12）。那是同一 Merkle 根下不同交易列表。本页是两棵不同的树。

「看见一个交易哈希所以签名已经进身份」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 两套哈希域；coinbase 的 wtxid 当作全零 |
| 协议 | 必须点名问的是 txid、wtxid，还是头上的 txid Merkle |
| 实现 | 算错哪一套即分裂 |
| 部署 | 旧节点少验见证；完整验证看谁升级 |
| 经济 | 重量折扣是另一对象，本页不抄公式 |

**推断：** 产品句若只写「交易 ID」，读者会把附件听成已经进编号。  
**建议：** 第一版若把大签名放进「旧节点不理解的附件」，必须写清哪一个 ID 承诺了它。不要抄重量公式。不要发明「旧节点也验了见证」。

---

## 6. 和另外几句不是同一句

1. **策略 ≠ 共识**（不变量 144）：本地池规则。本页是共识两套哈希。
2. **同根不同列表**（不变量 12）：同一棵 Merkle。本页是 txid 树 ≠ wtxid 树。
3. **多客户端同根**（不变量 3）：两家跑完同一列表。本页是哈希域。
4. **assumevalid 跳脚本**（不变量 25）：同步加速。本页不是跳过，是旧节点结构上少验。
5. **`BLOBHASH` ≠ sidecar 字节**（不变量 145）：以太坊承诺 ≠ 袋里的字节。本页是 Bitcoin 两套交易 ID。

不要抄承诺魔数 / 重量公式 / 版本 0 程序长度。不要写怎样改见证编码。不编博物馆页。不另写 19 节。BIP-341 钥匙路径 / 脚本路径、BIP-143 签名摘要、重量当费率标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
txid ≠ wtxid
改见证 ≠ 已经改 txid
头上的 txid Merkle ≠ 已经承诺 wtxid
旧节点看见 txid ≠ 已经验过见证
没有见证程序时 wtxid 才等于 txid
```

语料：[C156](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「交易哈希 = 已经含签名。」「块头 Merkle 绿 = 见证已进头。」「txid = wtxid。」「旧节点和以前一样验完。」  
**边界：** 不讲 Tapscript。不抄重量数字。不另写 19 节。不写怎样改见证。BIP-341 / BIP-143 另标。
