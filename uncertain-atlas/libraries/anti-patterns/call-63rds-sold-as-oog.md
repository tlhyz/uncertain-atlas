# 反模式：看见读树涨价就当成已经换成 63/64 / 已经问超了就 OOG / 已经没有深度

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-150](https://eips.ethereum.org/EIPS/eip-150)。  
**例**：[读树涨价 ≠ 已经换成 63/64](../../tracks/implementation/worked-example-call-63rds-vs-oog.md)。

## 塌法

1. 看见读树涨价，就当成已经写了后来的树依赖涨价，或当成已经是本笔冷热，或当成气已经等于墙钟。
2. 看见调用问的气比父帧还能给的还多，就当成已经耗尽气。
3. 看见去掉六十四分之一，就当成已经没有调用深度上限，或当成深度攻击已经消失。
4. 看见建议抬高气限，就当成已经是协议帽，或当成官网吞吐已经是事实。
5. 看见自毁现在要付钱，就当成本页已经写了自毁家族。

## 为什么会出事

官方把问超了改成仍开子调用，是为了不让当时按「剩下的再减一截」开调用的合约停掉。软深度替换的是硬栈上限，不是深度对象已经消失。建议气限不是共识帽。

## 和相邻反模式

- [selfbalance-sold-as-balance](selfbalance-sold-as-balance.md) 是 1884，不是本页。
- [first-access-sold-as-warm](first-access-sold-as-warm.md) 是 2929，不是本页。
- [gas-sold-as-wallclock](gas-sold-as-wallclock.md) 是气 ≠ 墙钟，不是本页。
- [default-sold-as-cap](default-sold-as-cap.md) 是客户端默认气限，不是本页。
- [selfdestruct-sold-as-deleted](selfdestruct-sold-as-deleted.md) 是自毁语义，不是本页。
