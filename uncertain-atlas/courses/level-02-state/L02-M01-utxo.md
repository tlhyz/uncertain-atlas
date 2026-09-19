# L2.1 UTXO

优先级：必学  
先修：L0.4，L1.2

---

## A. 先修知识

交易是签名过的状态请求。  
UTXO 把「钱」看成一张张还没被撕掉的支票，而不是账户里的一个数字。

---

## B. 核心问题

**为什么 Bitcoin 不记「阿安有 10」，却记「这几张输出还没花」？这给并行和重放各带来什么？**

---

## C. 直觉（ELI15）

阿安有三张支票：3、5、2。要付 6，他交出 5 和 2，找回 1 给自己，6 给阿比。  
被交出的那两张，盖「已花」作废。新的两张出生。

没有「阿安这个人的余额字段」必须被所有转账排队改写。  
只要两笔交易花的不是同一张支票，出块者可以并行检查。

重放也变简单：同一张支票不能撕两次。不必给阿安发一个全局序号。

代价：找零、找币、钱包体验、复杂应用更别扭。

---

## D. 正式定义（本科计算机）

**UTXO（Unspent Transaction Output）**：某笔交易的某个输出，尚未成为另一笔交易的输入。

状态 ≈ 当前所有 UTXO 的集合。  
`Apply`：删除被引用的输入（必须现为未花费），新增输出。

花费条件写在输出脚本 / 锁定条件上。授权是「满足这张支票的解锁」，不是「我是阿安」。

进了块的 coinbase 不是已经能花。钱包看见奖励不是已经成熟。精读：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。
脚本里的 CLTV 不是交易 nLockTime 已经把输出锁住。精读：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。
脚本里的 CSV 不是绝对锁，也不是「CSV 部署」四个字。精读：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md) BIP-112 script-csv not already nsequence-locked / not already 164 / not already 165-bundled 正式三事（165 余量）：[`../../tracks/state-models/worked-example-csvd-notseq-vs-bundled.md`](../../tracks/state-models/worked-example-csvd-notseq-vs-bundled.md)（不变量 1527）。 BIP-112 relative-lock not already absolute-lock / not already 164 / not already 163 正式三事（165 余量）：[`../../tracks/state-models/worked-example-csvd-notabs-vs-bundled.md`](../../tracks/state-models/worked-example-csvd-notabs-vs-bundled.md)（不变量 1528）。 BIP-112 csv-deploy not already opcode / not already 41 / not already 164 正式三事（165 余量）：[`../../tracks/state-models/worked-example-csvd-notdep-vs-bundled.md`](../../tracks/state-models/worked-example-csvd-notdep-vs-bundled.md)（不变量 1529）。（不变量 165）。
付给脚本哈希不是已经揭开赎回脚本。旧节点 HASH160 EQUAL 通过不是新节点已经再跑。精读：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。

**事实：** Bitcoin 状态机可以这样理解。完整脚本与隔离见证细节在 `protocols/bitcoin/`。  
**事实：** 两笔交易若输入集合不相交，其有效性在 UTXO 集上互不依赖（费用、块上限仍是块级约束）。Bitcoin 规范没有把这句话写成按访问集并行验证。Fuel 访问集：谓词通过 ≠ 脚本已经跑完；只读重叠 ≠ 写冲突：[`../../tracks/parallelism/worked-example-utxo-access-list.md`](../../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143）。

---

## E. 最小案例

```text
UTXO 集:
  U1: 5 → 锁给 pkA
  U2: 5 → 锁给 pkA
  U3: 2 → 锁给 pkB

T1 花 U1，产出 5 给 B
T2 花 U2，产出 5 给 C
```

T1 与 T2 可并行验证。  
T3 也花 U1：与 T1 冲突，块内只能活一个。

---

## F. 真实项目

- **Bitcoin（事实）**：经典 UTXO。  
- **Cardano（事实）**：eUTXO，输出带数据，校验更强，另一套编程模型。  
- **Fuel 等（进阶）**：在 UTXO 上做声明访问集再并行的实验。谓词通过不是脚本已经跑完。只读重叠不是写冲突。思想级档案 + [精读](../../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143）。未学完前不当结论。

---

## G. 源码入口

Bitcoin Core：UTXO 集（Chainstate / `CCoinsView` 一类）+ `ConnectBlock` 花与造。Level 3 档案给具体文件名并核路径。

---

## H. 攻击者视角

1. 双花同一 UTXO 给两个商家看不同未确认交易。  
2. 粉尘/大量微小 UTXO 膨胀状态。  
3. 利用脚本复杂度和签名哈希种类打 CPU。  
4. 未确认交易依赖链（子付母）让用户以为「已经花出去」。

---

## I. Trade-off

| 得到 | 失去 |
|---|---|
| 冲突可见、易并行、重放自然 | 找零、币选择、合约表达力、隐私（图谱分析） |
| 轻节点可对单笔做包含证明 | 证明「余额是多少」要汇总很多输出 |

---

## J. 对「不确定」的意义

结算链如果交易主要是「花确定的券」，UTXO 很贴。  
若要通用程序和热账户，账户模型更省事，但并行和热点会回来咬你。  
**建议：** 先别选。读完 2.4 地图再进决策矩阵。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 花费条件仍是签名 / 脚本；UTXO 不自动隐私 |
| 协议 | 一输出一花费；天然冲突 = 同一输出 |
| 实现 | 币选择、找零编码必须确定 |
| 部署 | UTXO 集磁盘；剪枝后仍须能验新块 |
| 经济 | 粉尘 / 占用谁付钱（L2.6） |

**禁止假学习：** 「UTXO 不能编程。」「UTXO 自动隐私。」「UTXO 并行 = 已经不需要顺序 / 已经和账户锁同一句。」「进了块的 coinbase = 已经能花。」「填了 nLockTime = 输出已经锁住。」「CSV = CLTV。」「CSV 之后 = 已经在讲操作码。」「付给哈希 = 赎回已经揭开。」「旧节点 EQUAL 通过 = 新节点已经再跑。」「看见地址 = 已经有 UTXO。」「校验过 = 程序已经上链。」
**边界：** 脚本细节在 L3.7 只触及软分叉结构，不教语言。Fuel 访问集主键与谓词/脚本拆分见 [`../../tracks/parallelism/worked-example-utxo-access-list.md`](../../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143）。进了块的 coinbase ≠ 已经能花：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。脚本里的 CLTV ≠ 交易 nLockTime 已经把输出锁住：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CSV ≠ 绝对锁 / ≠ 部署名：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。付给脚本哈希 ≠ 已经揭开赎回脚本：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。看见 Bech32 地址串 ≠ 链上已经有这笔输出：[`../../tracks/implementation/worked-example-address-vs-utxo.md`](../../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。不抄上限或官网 TPS。不抄字符表 / 例地址。不写怎样构造旧合法新非法的赎回。不写怎样增删字符撞合法地址。
