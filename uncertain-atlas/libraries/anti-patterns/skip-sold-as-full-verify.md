# 反模式：跳过验签被写成「全节点已从创世验证」

> **事实 / 推断 / 建议** 已分开。
> 真值：[assumevalid 精读](../../tracks/implementation/worked-example-assumevalid.md)、[弱主观性](../../tracks/finality/worked-example-weak-subjectivity.md)、[不变式 25](../invariants/README.md#25-跳过验证必须点名跳过了哪条规则)。

---

## 一句话

实现跳过了脚本、签名或 UTXO 重放，产品句仍写「和从创世逐条验证一样」。

---

## 它看起来像什么

- 「Bitcoin 全节点没有弱主观性，所以默认同步等于验完所有脚本」
- 把 assumevalid 默认哈希说成共识指定的唯一历史
- assumeutxo 装上快照后、背景链未到基块，就显示「已完全验证」
- 把旧 checkpoint、assumevalid、WS 检查点写成一个开关

---

## 事实

- 0.14.0：assumevalid **不**强迫某条链；不在最佳链上则全验签名；`-assumevalid=0` 关闭默认。
- 旧 checkpoint **要求**标记块在链上。
- assumeutxo：快照哈希须对上编译值；背景 chainstate 应验到快照基块并核 UTXO 哈希。
- 这些都不是 Casper 弱主观周期。

---

## 正确写法

| 实际做了什么 | 能说的句子 |
|--------------|------------|
| `-assumevalid=0` 从创世验脚本 | 「本节点按配置验了历史脚本」 |
| 默认 assumevalid 且该块在链上 | 「祖先脚本按发行默认被跳过；之后的块仍验签名」 |
| 已 load 快照、背景未完成 | 「尖已可用；历史 UTXO 仍在背景验证」 |
| 背景已核过快照哈希 | 「快照基块的 UTXO 已与编译值对齐」 |

---

## 对不确定的意义（建议）

加速同步可以有。句子必须带跳过的规则和关闭方法。缺这两项还写「全验证」，这条就红。
