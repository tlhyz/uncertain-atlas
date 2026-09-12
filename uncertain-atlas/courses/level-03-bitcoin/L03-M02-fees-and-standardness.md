# L3.2 费用与标准性

优先级：重要  
先修：L0.4，L0.7，Bitcoin 档案第 4、7 节

---

## A. 先修知识

块有权重上限。想进块的交易通常多于空间。

---

## B. 核心问题

**为什么「节点不肯转发」和「共识非法」不是一回事？费用市场在排的是什么？**

---

## C. 直觉

仓库只有一辆卡车。谁多付运费，谁的货先装。  
但门口保安还有另一本《我们今天看不顺眼的货不进院子》——这比法律更严。

共识是法律：脚本过、没双花、格式对，就能进合法块。  
standardness / mempool 策略是保安：最小费、脚本模板、数据包大小。保安拒绝 ≠ 法官判你死刑。

用户却常把保安拒绝看成「链拒绝了」，于是改参数乱重发。

---

## D. 正式定义

**费用：** 输入和 − 输出和。矿工收。市场是块空间拍卖。  
**policy：** 本地转发与 mempool 准入。各节点可不同。  
**consensus rule：** 全节点验证块时必须一致，否则分裂。

**事实：** 一笔非标准但共识合法的交易，仍可能被矿工直接打进块。轻钱包等不到转发，不代表永远无效。Bitcoin Core 官方：Policy 是共识之外、对未确认交易进 mempool 之前的本地可配置规则；**不作用于块内交易**。[精读](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。

---

## E. 最小案例

T 共识合法，但费低于你邻居的 minrelaytxfee。  
邻居不进池、不转发。你以为失败。矿工从别处看见 T，打进下一块。你的钱包又显示成功。  
同一字节，三种故事：策略、共识、用户层。

---

## F. 真实项目

Bitcoin Core 的 mempool / 标准脚本模板。RBF 是策略与社交的混合物。选择加入替换信号不是已经换掉。nSequence 示意不是已经是相对锁。精读：[`../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md`](../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)（不变量 166）。
Ethereum 的 mempool 替换更日常，但「策略 ≠ 共识」同一条。

---

## G. 源码

预告：`AcceptToMemoryPool` 一类 vs `ConnectBlock`。两个门。

---

## H. 攻击者视角

1. 用最低共识合法、最高验证成本的交易打节点（policy 存在的理由）。  
2. 替换商家看见的那笔（RBF）。  
3. 让用户以为「失败」而重复授权。

---

## I. Trade-off

严策略：节点活得下去。  
代价：网络碎片化、用户语义混乱。  
松策略：DoS。

---

## J. 对「不确定」的意义

后量子验签贵，policy 必须有验签配额（反模式：无上限验签）。  
产品文案必须三套：本地错、池拒绝、共识非法。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 标准性不验更多数学，只过滤继电器 |
| 协议 | consensus 与 policy 是两套门 |
| 实现 | policy 分叉不裂共识，只裂传播 |
| 部署 | 每个节点一份本地 mempool |
| 经济 | 费率买的是空间，不是正确性 |

**禁止假学习：** 「标准性 = 共识规则。」「费率高所以交易更正确。」「邻居不转发 = 链拒绝。」「进了 mempool = 已经进块。」「进了块的手续费 = 矿工已经能花。」「带了 RBF = 已经换掉。」「较低序列号 = 已经是相对锁。」「标准赎回类型 = 共识已经执行内层。」「跳过库存通告 = 已经拒进池。」「发了费率过滤器 = 对等节点已经照做。」「内存池查询回了一串库存 = 已经有那些交易。」「只肯给最近转发过的 = 已经支持整池查询。」「协议版本够了 = 已经在答内存池查询。」
**边界：** mempool 政策通论在 L9.2。策略 ≠ 共识精读：[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。进了块的 coinbase ≠ 已经能花：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。选择加入替换信号 ≠ 已经换掉：[`../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md`](../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)（不变量 166）。付给脚本哈希 ≠ 已经揭开赎回脚本：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。跳过库存通告 ≠ 已经拒进池；发了费率过滤器 ≠ 对等节点已经照做；布隆过了 ≠ 已经过了费率门：[`../../tracks/mempool/worked-example-feefilter-vs-rejected.md`](../../tracks/mempool/worked-example-feefilter-vs-rejected.md)（不变量 245）。不抄默认费率。不抄协议版本号。不写怎样绕策略或怎样替换。不写怎样按费率认出节点。不写怎样构造旧合法新非法的赎回。内存池查询回了一串库存 ≠ 已经有那些交易；只肯给最近转发过的 ≠ 已经支持整池查询；协议版本够了 ≠ 已经在答：[`../../tracks/mempool/worked-example-mempool-dump-vs-have.md`](../../tracks/mempool/worked-example-mempool-dump-vs-have.md)（不变量 253）。不要抄协议版本号 / 库存条数上限。不要写怎样把别人的内存池整包拉走或按内存池认人。
