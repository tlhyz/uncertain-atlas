# 反模式：看见收据状态码就当成已经能从剩余气推断 / 已经是中间根 / 已经有返回数据

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-658](https://eips.ethereum.org/EIPS/eip-658)。  
**例**：[收据状态码 ≠ 剩余气](../../tracks/implementation/worked-example-receipt-status-vs-gas.md)。

## 塌法

1. 看见还剩气，就当成已经成功；看见气烧光，就当成已经失败。
2. 看见收据里有状态码，就当成中间状态根还在，或当成已经能从收据复算中间根。
3. 看见 RPC 能重放告诉你成没成，就当成共识收据已经有状态码，或当成轻节点已经能验。
4. 看见状态码，就当成返回数据已经进了收据，或当成已经写了返回缓冲。
5. 看见本页依赖 140，就当成已经写了回滚留气那一页。

## 为什么会出事

官方写：故意回滚之后，不能再假定失败当且仅当气烧光。重放不是共识解，轻节点做不到。状态码替换的是中间根，不是返回数据。

## 和相邻反模式

- [revert-sold-as-invalid](revert-sold-as-invalid.md) 是回滚留气，不是本页。
- [returndata-sold-as-memory](returndata-sold-as-memory.md) 是返回缓冲，不是本页。
- [window-sold-as-consensus](window-sold-as-consensus.md) 是历史窗 / 线上收据无布隆，不是本页。
