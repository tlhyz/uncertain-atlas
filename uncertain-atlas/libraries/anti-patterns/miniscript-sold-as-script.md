# 把 Miniscript 写成已经是链上脚本（miniscript-sold-as-script）

> 类型：anti-pattern  
> 对读：不变量 191；C195；模式 [`../design-patterns/name-the-miniscript.md`](../design-patterns/name-the-miniscript.md)；[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)。

## 坏句

- 「钱包支持 Miniscript，链上就已经是这种脚本。」
- 「Miniscript 是另一门语言，不是描述符。」
- 「共识健全就是策略已经完备。」
- 「Miniscript 已经覆盖付给脚本哈希。」
- 「379 就是 380 / 342 / 16。」

## 为什么坏

[BIP-379](https://github.com/bitcoin/bips/blob/master/bip-0379.md) 官方页把分析语言、链上脚本、描述符扩张、共识健全和策略完备写成不同对象。本页只适用于隔离见证脚本哈希和 tapscript；付给脚本哈希和裸脚本被排除。从用户看不是另一门语言。

## 对照

| 卖成 | 实际 |
| --- | --- |
| 看见片段 | 结构化表示，不是已经上链 |
| 另一门语言 | 官方写成描述符的显著扩张 |
| 共识健全 | 条件不满足就没有共识合法见证 |
| 策略完备 | 另要资源界、且没有时间锁混用 |
| 379 | 不是 380，不是 342，不是 16 |

相关反模式：[`keys-sold-as-scripts.md`](keys-sold-as-scripts.md)、[`scriptpath-sold-as-tapscript.md`](scriptpath-sold-as-tapscript.md)、[`hash-sold-as-redeem.md`](hash-sold-as-redeem.md)、[`keypath-sold-as-tree.md`](keypath-sold-as-tree.md)。
