# 看见 Miniscript 不是已经是链上脚本

> 类型：worked example（脚本分析语言 / 描述符扩张）  
> 范围：只写 [BIP-379](https://github.com/bitcoin/bips/blob/master/bip-0379.md) 官方页已经写明的对象。不写怎样拼片段、怎样编译花费策略、怎样凑见证。  
> 五层：协议（本页只覆盖隔离见证脚本哈希与 tapscript；付给脚本哈希和裸脚本被排除） / 实现（片段可组合不是已经是链上脚本） / 钱包（从用户看不是另一门语言，是描述符的扩张） / 应用（共识健全不是已经是策略完备） / 威胁（把看见片段写成已经上链）。  
> 分类标签：事实 / 推断 / 建议 已分开。  
> 对读：[`../../libraries/invariants/README.md`](../../libraries/invariants/README.md) 不变量 191；[`../../libraries/adversarial-corpus/README.md`](../../libraries/adversarial-corpus/README.md) C195；[`../../libraries/anti-patterns/miniscript-sold-as-script.md`](../../libraries/anti-patterns/miniscript-sold-as-script.md)；[`../../libraries/design-patterns/name-the-miniscript.md`](../../libraries/design-patterns/name-the-miniscript.md)；课 [`../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md`](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[`../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md`](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)；档案 [`../../protocols/bitcoin/README.md`](../../protocols/bitcoin/README.md)。

## 事实（官方页能指回去）

1. [BIP-379](https://github.com/bitcoin/bips/blob/master/bip-0379.md) 题目是 Miniscript。官方 BIP。应用层。信息 BIP。草案。依赖 BIP-380。不另写 19 节。
2. 官方页写：本页指定一种语言，用来结构化地写**一部分** Bitcoin 脚本，好做分析、组合和通用签名。
3. 官方页写：这些规定只适用于隔离见证脚本哈希（BIP-141）和 tapscript（BIP-342）。付给脚本哈希和裸脚本被本页排除。
4. 官方页写：Miniscript 由一套设计成可安全、正确组合的脚本片段组成。片段可组合不是已经是链上脚本。
5. 官方页写：这些片段预期用在后续描述符的脚本表达式里；钥表达式按 BIP-380。从用户看，Miniscript **不是另一门语言**，而是描述符语言的显著扩张。看见描述符里的脚本表达式不是已经换了一门语言。
6. 官方页写：本页首先要保证脚本正确性，也就是**共识健全**和**策略完备**。共识健全：除非本页写的花费条件满足，否则构造不出共识合法的见证。策略完备：在尊重资源界、并且没有时间锁混用的前提下，每条花费路径都能造出策略合法的见证。共识健全不是已经是策略完备。
7. 官方页写：兼容的脚本可以转回 Miniscript 形式。能转回去不是已经上链，也不是已经能花。
8. 因此：BIP-379 ≠ BIP-380 ≠ BIP-342 ≠ BIP-16。看见 Miniscript 不是已经是链上脚本。本页不是已经覆盖付给脚本哈希。

## 推断（从官方句推出，不是另一条共识规则）

- 把「脚本」一句用完，会把 170 的哈希赎回、189 的 tapscript 叶子、184 的描述符总语法和本页糊成同一对象。
- 把「描述符的扩张」读成「已经是另一套地址方案」，会把官方「不是另一门语言」那一句丢掉。
- 把共识健全读成策略完备，会把「能进块」和「能进本地池」两套见证条件糊成一句。

## 建议（对「不确定」）

第一版结算机若出现「结构化脚本 / 可分析花费条件」，先问四句：看见的是分析语言，还是已经是链上脚本？这是描述符的扩张，还是已经换了一门语言？问的是共识健全，还是策略完备？本页覆盖的是哪一种脚本封装，付给脚本哈希算不算？四句各指各的对象。不要发明片段表或策略编译配方。

## 五层（只展开本对象）

| 层 | 本对象要看见的 |
| --- | --- |
| 协议 | 只覆盖隔离见证脚本哈希与 tapscript；付给脚本哈希和裸脚本被排除。 |
| 实现 | 片段可组合不是已经编成链上脚本。 |
| 钱包 | 从用户看不是另一门语言，是描述符扩张。 |
| 应用 | 共识健全不是已经是策略完备。 |
| 威胁 | 文案把看见片段写成已经上链，或把本页写成已经覆盖赎回脚本。 |

## 禁句

- 「看见 Miniscript 就是已经是链上脚本。」
- 「Miniscript 已经是另一门语言，不是描述符。」
- 「共识健全就是已经策略完备。」
- 「本页已经覆盖付给脚本哈希 / 裸脚本。」
- 「BIP-379 就是 BIP-380 / BIP-342 / BIP-16。」
- 「脚本就是 170、189、184 里的同一种脚本。」

## 边界（本页不写）

- 不写片段表、包装器、类型字母、见证凑法、 malleability 分类。
- 不写怎样编译花费策略或怎样从脚本反推 Miniscript。
- 不写 184 描述符总语法、189 tapscript 叶子、170 赎回本身（只说本页不是它们）。
- 不写闪电网络路由。

## 和相邻对象的唯一性

1. **不是 184 / BIP-380** — 380 是描述符总语法；本页是描述符里那一套脚本表达式扩张。看见描述符不是已经是本页。
2. **不是 189 / BIP-342** — 342 是 tapscript 叶子怎么验；本页是分析语言，不是已经换了叶子语义。
3. **不是 170 / BIP-16** — 付给脚本哈希被本页排除。
4. **不是 153 / BIP-341** — 341 是钥匙路径和脚本路径的结构。本页不写怎么藏路径。
5. **不是 152 / BIP-141** — 141 是见证怎么进旧验证。本页只借用「适用于隔离见证脚本哈希」这一句。
