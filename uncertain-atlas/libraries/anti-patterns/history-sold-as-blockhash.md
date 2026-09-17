# 把状态历史哈希写成已经是 BLOCKHASH（history-sold-as-blockhash）

> 类型：anti-pattern  
> 对读：不变量 195；C199；模式 [`../design-patterns/name-the-history-hash.md`](../design-patterns/name-the-history-hash.md)；[`../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md`](../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md)。

## 坏句

- 「状态里能读哈希，BLOCKHASH 就已经改了。」
- 「系统写入了父哈希，窗口就已经齐。」
- 「合约窗口更长，操作码就已经更长。」
- 「2935 就是 4788 / 4399。」
- 「开块写入已经预热过。」

## 为什么坏

[EIP-2935](https://eips.ethereum.org/EIPS/eip-2935) 官方页写本页对 `BLOCKHASH` 的解析机制没有影响。合约另开一条更长窗口，要等激活后一整窗才填满。开块系统更新不预热。4788 是父信标根。4399 是 `PREVRANDAO`。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 状态里有哈希 | 系统合约存储，不是操作码 |
| 系统写入了父哈希 | 环还没填满 |
| 合约能查更长 | `BLOCKHASH` 窗口和代价不动 |
| 2935 | 不是 4788，不是 4399 |

相关反模式：[`parent-root-sold-as-head.md`](parent-root-sold-as-head.md)、[`prevrandao-sold-as-fair.md`](prevrandao-sold-as-fair.md)、[`first-access-sold-as-warm.md`](first-access-sold-as-warm.md)。
