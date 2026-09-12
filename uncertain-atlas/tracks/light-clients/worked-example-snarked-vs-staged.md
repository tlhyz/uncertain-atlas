# 工作实例：验过递归 π，不等于最新账本已经被证明

> **事实 / 推断 / 建议** 已分开。
> 对照：[L8.3](../../courses/level-08-privacy/L08-M03-succinct-history.md)、[Mina 档案](../../protocols/mina/report.md)、[轻节点表](README.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)、[证明大小等于整条链](../../libraries/anti-patterns/proof-size-equals-chain.md)。
> 主文献：Mina 官方 [Glossary](https://docs.minaprotocol.com/glossary)、[What's in a Block](https://docs.minaprotocol.com/mina-protocol/whats-in-a-block)、[Scan State](https://docs.minaprotocol.com/mina-protocol/scan-state)；Mina Foundation [22kB technical reference](https://minaprotocol.com/blog/22kb-sized-blockchain-a-technical-reference)；o1Labs [Kimchi](https://minaprotocol.com/blog/kimchi-the-latest-update-to-minas-proof-system)；[zkApps FAQ](https://docs.minaprotocol.com/zkapps/faq)。
> 本页钉 **SNARKed ledger / staged ledger / staking ledger / Pickles / Kimchi**。不抄 22kB、实测字节、`k`、槽常数、scan-state 示例棵数、Kimchi 博客加速句。

---

## 0. 先修

- [L1.3](../../courses/level-01-crypto/L01-M03-merkle.md) 承诺
- [L7.2](../../courses/level-07-modular/L07-M02-data-availability.md) DA 仍在
- [L8.3](../../courses/level-08-privacy/L08-M03-succinct-history.md) 简短历史
- [不变量 123](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见「整条链被压成一个小证明」，以为验绿 π 就已经拿到最新余额，或者 Pickles 和 Kimchi 是同一个东西。

官方句（事实）：

- Glossary：Mina 有三种账本——**staged**、**staking**、**SNARKed**。SNARKed ledger 只含已经有证明的交易，在 scan state 吐出证明之后才更新。staged ledger 是当前账户态，外加一队还没被 SNARK 的交易（scan state）。staking ledger 只用来抽下一块出块者。
- What's in a Block：一块里同时有 **protocol state proof** 和 **staged ledger diff**。官方写：递归 SNARK 让这份协议状态证明可以谈「整条历史合法」。同一页又写：staged ledger 是已经 Apply、但还没有 SNARK 的待定账户库。
- Scan State：出块者把 scan state 吐出的 ledger proof 放进区块链 SNARK；这份 SNARK 证明链的当前状态合法，并证明 **SNARKed ledger 里的交易**合法。进块的新交易先变成 scan state 的底作业，不是立刻进 SNARKed ledger。
- 2021 技术文：验一块对应的证明，等于验到**当前块后面几块之前**的交易。区块链 SNARK 证明的账本（snarked ledger）落后最新账本。最新 staged-ledger 由出块者显式 Apply，**不被区块链证明保证**。
- 同一篇技术文：可用的「区块链」还要账户记录 + 通向该账户的 Merkle 路径；根必须对上区块链 SNARK 证明过的账本。只拿证明对象和一堆不透明哈希，按他们自己的定义不够用。
- Kimchi 博客：Pickles 是递归层（证明的证明的证明……）。Kimchi 是 Pickles 用来出证明的 plonkish 系统。官方 FAQ：可以只用 Kimchi、不用 Pickles。

验 π 是在问「这条递归章能不能过」。过了，问的仍是 SNARKed 那一本，不是手机上那条最新余额。

---

## 2. 直觉（ELI15）

老师每天改新作业，同时请人把更早的卷子做成「全对」盖章。

- 盖章很小。盖章说的是已经装订进册的旧卷。
- 今天刚交上去、还在桌上的卷，老师已经打了分，但还没进那枚章。
- 你若想知道自己第 37 页写了什么，仍要那一页，或一条通向目录的页码条。章本身不把第 37 页塞进口袋。
- 装订车间（Pickles）和盖章油墨（Kimchi）不是同一个车间。没有装订车间，油墨仍能给单张卷盖章。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| protocol state proof | 递归证明：新协议状态合法，并接上上一枚章 | 最新 staged 账户库已经在证明里 |
| SNARKed ledger | 已有交易证明、被区块链 SNARK 点名的账本 | 刚进块的账户态 |
| staged ledger | 已 Apply 的当前账户态 + 未 SNARK 队列 | 已经被区块链证明保证 |
| staking ledger | 抽下一个出块者用的质押快照 | 用户余额、SNARKed 最新尖 |
| scan state | 把交易 SNARK 从出块者手里拆出去的队列 | 「进块 = 已进 SNARKed」 |
| Pickles | 递归层：证明的证明 | Kimchi；单笔电路 |
| Kimchi | plonkish 证明系统 | 递归协议本身 |
| 账户 + Merkle 路径 | 自己的那一页是否对着已验根 | 验 π 自动带上的附件 |

头里可以同时写 `staged_ledger_hash` 和 `snarked_ledger_hash`。两个哈希同时出现，不是已经是同一个对象。

---

## 4. 最小案例

块 N 收下用户付款 T。

1. T 进 staged ledger：出块者已经 Apply。阿安的 staged 余额变了。
2. T 同时变成 scan state 底作业。此时 T **还没有**关联证明。
3. 若干块之后，scan state 吐出覆盖 T 的 ledger proof。SNARKed ledger 才更新。
4. 之后的区块链 SNARK 才能点名「T 已经在被证明的那一本」。
5. 阿比只验当前 protocol state proof：他得到的是对 SNARKed 尖的简短验证，不是 T 刚进块那一刻的 staged 余额。
6. 阿比还要另要账户记录和路径。路径对上的必须是区块链 SNARK 证明过的那一本，不是 RPC 随口给的另一根。

「进块了」和「已经被递归证明覆盖」是两步。官方把第二步拆给 SNARK worker，就是为了让出块时间不跟交易 SNARK 绑死。这是部署/经济角色分离，不是「证明数学已经覆盖桌上每一张卷」。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 递归假设叠在电路与证明系统上；Pickles 与 Kimchi 不是同一对象 |
| 协议 | 三种账本必须点名；区块链 SNARK 点名 SNARKed，不保证 staged |
| 实现 | 验证器必须对着正确的公开输入（哪一个 ledger hash） |
| 部署 | 证明者 / SNARK worker 中心化是角色问题，不是「π 废了」 |
| 经济 | 出块者要买齐对应的 SNARK 作业才能再塞新交易；买不到可以出空块 |

**推断：** 产品句若只写「固定大小证明」，读者会把 staged 尖、质押快照、自己的账户页糊成同一张图。  
**建议：** 不确定第一版不要上递归 L1。若以后做简短验证，必须先写「证明覆盖哪一本账、用户页从哪来、DA 谁管」。

---

## 6. 和另外两句容易糊的事实

1. **「protocol state proof 证明整条历史」** 不是最新 staged 已经在证明里。官方同一页同时写这两句。历史章接的是协议状态链；被 SNARK 点名的账本仍是 SNARKed 那一本。
2. **「整条链约 22kB」** 是他们自己的产品句。同一篇技术文把「区块链」定义成可用表示 + 可验证数据 + 能广播。按该定义，还要账户和路径，不是只抱一个证明对象。不要把 22kB、后来测到的更小数字、或验证钥字节抄进不确定常量。
3. **Pickles 能递归** 不是 Kimchi 已经会递归。FAQ：Kimchi 可以单独用。

不要把 Kimchi 博客里的「更快 / 更大电路 / 可能更短」写成安全，也不要当成不确定常量。

---

## 7. 「不确定」测试句（建议）

```text
验 protocol state proof ≠ staged ledger 已被该证明保证
SNARKed ledger ≠ staged ledger ≠ staking ledger
进块 Apply ≠ 已进入 SNARKed ledger
Pickles ≠ Kimchi
验 π ≠ 已经持有账户记录与 Merkle 路径
固定大小证明 ≠ 全账户库 / 历史体
路径对上的根必须是区块链 SNARK 点名的那一本
```

语料：[C127](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「整条链只有 22kB。」「验了 π 就是最新余额。」「进块就是已经被递归证明覆盖。」「Pickles 就是 Kimchi。」「有证明所以不需要账户路径 / DA。」  
**边界：** 不讲 Pickles 电路、Pasta 曲线算术、怎样写 Kimchi 门。不抄 22kB / 实测字节 / `k` / 槽常数 / scan-state 示例数字。Mina 档案 §15 仍无官方主网七问，本页不编事故。
