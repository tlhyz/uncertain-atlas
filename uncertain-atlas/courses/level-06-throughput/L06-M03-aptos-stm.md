# L6.3 乐观并行，串行语义

优先级：重要  
先修：L6.1，L4.5（先有顺序再 Apply）

---

## A. 先修知识

CometBFT / 一般 BFT：先有字节的全序，再 `Apply`。  
Solana：你必须事先列账户。  
Sui：你必须把世界建成所有权。  
Aptos：程序员仍写普通 Move；运行时投机执行，再检查是否等于某个已共识的序列。

---

## B. 核心问题

**块内顺序还没在每个核上「先排死」时，为什么敢并行？错了怎么办？STM 能代替共识吗？**

---

## C. 直觉（ELI15）

老师已经写好了名单顺序 L：先批甲、再乙、再丙。  
三个助教同时批，但必须保证分数和「一个人按名单批」完全一样。  
乙偷看了甲还没改完的卷，发现对不上，乙的稿作废，重批。

助教再多，名单是谁定的，仍是老师的事。  
**没有名单 L，谈不上「批得对」。**

---

## D. 正式定义

**Block-STM（论文/系统描述，细节以论文与实现为准）**

1. 共识产出块内序列 `L = tx_0, tx_1, …`。
2. 多线程按推测顺序执行，记录读写版本。
3. 若某 `tx_i` 读到的版本 ≠ 「按 L 串行执行到 i 时应看见的」→ abort，再执行。
4. 全部通过后提交。结果必须等于单线程按 L 执行。

**invariant（事实，A25）：**

```text
并行是性能。串行语义是安全。
STM 不产生 L，也不提供最终性。
```

任何「为了更快而重排结果」都是 bug。

**最坏情况：** 每笔都冲突 → 接近串行 + 回滚税。热点资源会制造回滚风暴。

---

## E. 最小案例

L = [T0 写 X, T1 读 X 写 Y, T2 只写 Z]。  
T2 与前两笔无交，可先跑完。  
T1 若在 T0 提交前读了旧 X，验证失败，重做。  
最终根必须 = 先 T0 再 T1 再 T2 的单线程根。

若节点崩溃留下「T0 写了、T1 没写」：半提交。属实现/部署，见反模式 half-written-state。

---

## F. 真实项目

Aptos。档案第 3、6、7 节。  
其他链也有「并行 EVM / STM」工程，思想同类时才插入，不因有名而学。

---

## G. 源码入口

预告：块内序号如何喂给 STM；读写集校验；提交/崩溃边界。

---

## H. 攻击者模型

- 构造高冲突块，让并行广告变成 CPU 烧在回滚上。
- STM 实现不等价于 L → 两客户端同 L 不同根（实现保证）。
- 把「STM 跑完」展示成「已最终」（用户层，与 L5.2 同类错）。

---

## I. 代价

得到：低冲突时吃多核，程序员少声明锁。  
换：实现极难写对；多版本存储；最坏不比串行好；调试「哪笔被重做」变难。

---

## J. 对「不确定」的意义

**建议：** 先有确定的 L（BFT 或你们选的引擎），再谈要不要 STM。  
第一版规则少、冲突可预期，单线程 `Apply` 更可审计。  
反模式：[stm-replaces-consensus](../../libraries/anti-patterns/stm-replaces-consensus.md)。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | STM 不提供新的签名假设 |
| 协议 | 并行结果 ≡ 串行序 L；L 仍来自共识 |
| 实现 | 读写集与回滚必须确定 |
| 部署 | 高冲突时回滚吃 CPU |
| 经济 | 吞吐广告不能代替 L 的最终性 |

**禁止假学习：** 「STM 代替共识。」「并行结果可以重排。」
**边界：** 见反模式 [stm-replaces-consensus](../../libraries/anti-patterns/stm-replaces-consensus.md)、[stm-done-sold-as-final](../../libraries/anti-patterns/stm-done-sold-as-final.md)。工作实例：[`../../tracks/parallelism/worked-example-block-stm.md`](../../tracks/parallelism/worked-example-block-stm.md)（不变量 122）。模式：[optimistic-serial-equiv](../../libraries/design-patterns/optimistic-serial-equiv.md)。Quorum Store 批次传播 ≠ 已经写出 L：[`../../tracks/consensus/worked-example-quorum-store-vs-order.md`](../../tracks/consensus/worked-example-quorum-store-vs-order.md)（不变量 132）。不抄论文加速比 / 官网块时间。档案 §15 仍无官方主网七问，本课不编事故。
