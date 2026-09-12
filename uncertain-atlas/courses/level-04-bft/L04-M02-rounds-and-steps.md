# L4.2 高度、轮、步

优先级：必学  
先修：L4.1，CometBFT 档案第 6 节

---

## A. 先修知识

一个高度只允许最终 commit 一个块。失败了不能「换个块偷偷当同一个高度的另一个最终」。

---

## B. 核心问题

**为什么要有 round？为什么一轮里还要拆 propose / prevote / precommit，而不是问一次？**

---

## C. 直觉

开会：先有人起草（propose），大家举「我看见这份稿了」（prevote），再举「我愿意把这份当决议」（precommit），秘书才盖章（commit）。

起草人掉线或稿子坏了：散会重开一轮，换起草人。  
高度是「第几号决议」，轮是「第几次尝试」，步是「这次尝试进行到举手的哪一段」。

只举一次手：你不知道别人是「随便看看」还是「已经签字入档」。骗子可以让一半人以为只是看看，另一半以为已经入档。

---

## D. 正式定义

**height h：** 链上第 h 个槽，最多一个 commit 值。  
**round r：** 在 h 上的第 r 次尝试，proposer 由确定性调度选出。  
**step：** 该轮内部状态：propose、prevote、precommit（及等待超时）。

两轮投票的原因（协议工程师）：

1. prevote 形成「我们是否在看同一个值」的证据。  
2. precommit 形成「我们可以锁定并准备 commit」的证据。  
一张 +2/3 prevote 和一张 +2/3 precommit 不是同一张纸。

超时：部分同步下，等不到票就 `r+1`。超时太短空转，太长卡死。

---

## E. 最小案例

h=9，r=0，proposer V1 掉线。  
众人超时 → r=1，proposer V2 提出块 B。  
prevote(B) 凑齐 → precommit(B) 凑齐 → commit(h=9, B)。  
h=10 开始。没有「再给 h=9 另一个 commit」。

---

## F. 真实项目

CometBFT / Tendermint 教科书状态机。  
HotStuff 把证书（QC）串起来，换轮更省，思想仍是「先形成可引用的多数证据」。对照，不深挖。

---

## G. 源码

预告：`enterPropose` / `enterPrevote` / `enterPrecommit` / `finalizeCommit` 一类。读转换表，不要读网络层。

---

## H. 攻击者视角

1. 拖延 proposer，逼不断换轮（活性）。  
2. 对同一轮发出两个 proposal（分裂）。  
3. 让节点的 round 时钟严重不同步。

---

## I. Trade-off

多一步投票：更清楚「看见」和「锁定」。  
代价：延迟、消息、后量子下每步都乘签名体积。

---

## J. 对「不确定」的意义

结算语义挂在 **height 的唯一 commit**，不是挂在「我看见一个 proposal」。  
产品只能把 commit 画成最终。prevote 是内部纸。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 每步消息仍要签 |
| 协议 | height / round / step；commit 才是结算对象 |
| 实现 | 步骤机必须确定；省略步骤会投出矛盾票 |
| 部署 | 超时触发依赖时钟，但超时数字是协议参数 |
| 经济 | 空轮有机会成本，不能用省略步骤省 |

**禁止假学习：** 「投票过 2/3 就可以省略步骤。」
**边界：** 超时与解锁谓词以规范为准，不在本课写死伪代码。Prevote / precommit 的被签字节见 [`../../tracks/consensus/worked-example-vote-signbytes.md`](../../tracks/consensus/worked-example-vote-signbytes.md)；两步不是同一哈希再签一次。块头时间不是「全网同意的现在」：PBTS timely 窗 ≠ BFT Time 中位数，见 [`../../tracks/consensus/worked-example-pbts.md`](../../tracks/consensus/worked-example-pbts.md)。
