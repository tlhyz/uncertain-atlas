# 反模式：看见难度把叔块算进去就当成已经按个数调 / 已经没有炸弹 / 已经改了奖励

**层次**：共识 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-100](https://eips.ethereum.org/EIPS/eip-100)。  
**例**：[含叔块的难度 ≠ 已经数清叔块](../../tracks/consensus/worked-example-uncle-diff-vs-header.md)。

## 塌法

1. 看见难度把叔块算进去，就当成已经按叔块个数调。
2. 看见头上叔块哈希不是空，就当成已经数清有几个叔块。
3. 看见发行可预期，就当成已经没有炸弹，或当成已经写了 Homestead 朝均值。
4. 看见不能靠叔块率往上抬发行，就当成已经改了出块奖励 / 叔块奖励。
5. 看见改了时间分母，就当成官网吞吐已经是事实。

## 为什么会出事

官方写：精确按个数调要看整块；本页只用头上的空 / 非空。均值目标里有叔块，不是炸弹项已经取消，也不是奖励表已经改。

## 和相邻反模式

- [homestead-sold-as-create](homestead-sold-as-create.md) 是 Homestead 四件事里的难度均值，不是本页。
- [coinbase-sold-as-spendable](coinbase-sold-as-spendable.md) 是奖励成熟，不是本页。
- [prevrandao-sold-as-fair](prevrandao-sold-as-fair.md) 是合并后难度字段，不是本页。
