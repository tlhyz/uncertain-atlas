# 反模式：看见 Homestead 就当成已经改了 CREATE / 已经拒高 s / 已经限制代码 / 已经没有炸弹

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-2](https://eips.ethereum.org/EIPS/eip-2)。  
**例**：[Homestead ≠ 已经做完](../../tracks/implementation/worked-example-homestead-vs-already-done.md)。

## 塌法

1. 看见交易创建变贵，就当成 `CREATE` 操作码也变贵了。
2. 看见交易拒高 `s`，就当成 `ECRECOVER` 也拒了；或当成已经写了比特币 BIP-66，或当成已经写了链标识。
3. 看见创建失败不再留空合约，就当成已经限制返回代码长度、已经限制 initcode、已经区分 empty / dead。
4. 看见难度朝均值收敛，就当成指数炸弹已经取消。
5. 看见官方提到创建再自毁的便宜转账，就当成本页已经写了退款 / 自毁家族。

## 为什么会出事

四件事共享一次分叉，不共享一个对象。预编译仍接受高 `s` 是官方留下的旧接口。空合约失败是创建结果的语义，不是代码有多长。难度公式仍带着炸弹项。

## 和相邻反模式

- [create-size-sold-as-already-capped](create-size-sold-as-already-capped.md) 是 170，不是本页。
- [initcode-sold-as-already-bounded](initcode-sold-as-already-bounded.md) 是 3860，不是本页。
- [empty-sold-as-dead](empty-sold-as-dead.md) 是 161，不是本页。
- [der-sold-as-already-strict](der-sold-as-already-strict.md) 是比特币 BIP-66，不是本页。
- [chainid-sold-as-already-signed](chainid-sold-as-already-signed.md) 是 155，不是本页。
- [delegatecall-sold-as-callcode](delegatecall-sold-as-callcode.md) 是同一分叉的另一份规范。
