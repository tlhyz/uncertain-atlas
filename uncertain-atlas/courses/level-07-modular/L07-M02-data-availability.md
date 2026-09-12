# L7.2 数据可用

优先级：必学  
先修：L1.3，L7.1，Celestia 档案

---

## A. 先修知识

Merkle 路径证明「T 被头承诺过」。  
它不证明你拿得到算出新状态所需的**全部字节**。

---

## B. 核心问题

**为什么验证了区块头，仍可能无法知道链上事情是不是真的？**

---

## C. 直觉

老师在黑板上写了「作业答案的指纹」，然后把作业本藏起来。  
你核对了指纹公式，但没看见作业。  
有人说「第 3 题你及格了」。你无法自己重算，也无法揭穿他。

数据扣留：出块者让大家看见头（指纹对齐），不让大家看见体。  
全节点若也没体，谁都不能重放。轻节点若只验头，会被骗去放货。

纠删码 + 抽样：作业本撕成很多编号碎片，多印几份。你随机要几片。若攻击者藏了太多，你高概率要不到；若抽样都成功，整本大概率能拼回。

---

## D. 正式定义

**Data Availability：** 被共识承诺的块体，诚实参与者能够下载并重建，以便：

- 重放执行  
- 构造欺诈证明 / 有效性证明的输入  
- 新全节点同步

**不是：** 头有签名、Merkle 根能对上一笔交易。

DAS：随机查询编码份额。安全是概率的，依赖参数与诚实应答节点。

**NMT 完备性（另一问）：** 证明「这一命名空间的份额都给了」，不是证明扩展方阵已经可用。官方把 DAS 与 NMT 写成两件套。精读：[`../../tracks/light-clients/worked-example-nmt-vs-das.md`](../../tracks/light-clients/worked-example-nmt-vs-das.md)（不变量 124）。

**事实：** 这是轻客户端安全的第三根柱子（另两根：共识证明、状态/包含证明）。
**事实：** 抽样过关不是编码已经诚实（还要错误扩展欺诈证明 + 诚实桥节点），也不是历史已经有人存。

---

## E. 最小案例

头 commit，Merkle 显示 T 在块里。  
体只有 miner 有。  
商家验了 T 的路径，放货。  
全网无法重放该块，也无法证明「还有一笔双花也在未公布的体里」。  
T 的路径只说明「若体是真的，T 在其中」。体不在，假设破产。

---

## F. 真实项目

Celestia DAS；Ethereum blobs（另一条承诺路线）；Bitcoin 全节点默认下载体（轻节点 SPV 弱在 DA+执行）。

---

## G. 源码

预告：份额索引、抽样客户端、失败时禁止显示最终。

---

## H. 攻击者视角

1. 只对抽样节点服务，对其余扣留。  
2. 让钱包把「头最终」当结算。  
3. 小参数欺骗「我们抽样过了」。

---

## I. Trade-off

全节点下载体：假设简单，家用带宽贵。  
抽样：手机可行，参数与概率。  
不提供 DA：轻节点假安全。

---

## J. 对「不确定」的意义

无论是否模块化，结算链的轻钱包规范必须写：

> 无体或不满足抽样 ⇒ 不得显示最终。

后量子块若因签名变大而裁体，先裁的可能是 DA。这是工程账，见 PQ 手册。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 纠删码与 KZG 是不同假设 |
| 协议 | 有头 ≠ 有体；抽样 ≠ 执行正确 |
| 实现 | NMT / 份额编码必须确定 |
| 部署 | 轻节点必须真抽样，不能只问 RPC |
| 经济 | 扣留数据的收益 vs 抽样抓住的概率（不填未核百分比） |

**禁止假学习：** 「有头就是有数据。」「抽到份额所以执行正确。」「有 KZG 所以和 Celestia 一种 DAS。」「验了 NMT 就是整块可用。」「抽样绿就是编码对 / 历史还在。」「DACert = 全文已经在以太坊。」「AnyTrust = Rollup DA。」
**边界：** Celestia 纠删码 ≠ Ethereum KZG sidecar ≠ Fulu PeerDAS 列抽样。NMT 完备性 ≠ DAS。DACert ≠ 全文已贴父链：[`../../tracks/light-clients/worked-example-dacert-vs-posted.md`](../../tracks/light-clients/worked-example-dacert-vs-posted.md)（不变量 142）。blob gas ≠ 普通执行 gas：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）。精读：[`../../tracks/light-clients/worked-example.md`](../../tracks/light-clients/worked-example.md)、[`../../tracks/light-clients/worked-example-blob-vs-das.md`](../../tracks/light-clients/worked-example-blob-vs-das.md)、[`../../tracks/light-clients/worked-example-nmt-vs-das.md`](../../tracks/light-clients/worked-example-nmt-vs-das.md)。不把某一分叉的每块 blob 个数当永恒。不抄方阵边长 / FAQ 百分比 / 委员会人数。档案 §15 仍不编事故。
