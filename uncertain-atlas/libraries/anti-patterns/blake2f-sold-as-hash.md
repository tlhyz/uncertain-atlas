# 反模式：把 BLAKE2 压缩函数写成已经是哈希

**标识：** `blake2f-sold-as-hash`
**等级：** 重要
**相关模式：** [`name-the-blake2f`](../design-patterns/name-the-blake2f.md)
**相关课文：** [L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)
**相关不变量：** 230、199、228、221

## 错误句

「有了 BLAKE2 压缩函数，就已经是 BLAKE2b 哈希。」「能便宜跑更高轮，所以 Equihash 已经能验 / 中继已经上线 / 原子交换已经能做 / 隐私已经有了。」「EIP-152 就是 keccak / SHA3。」

## 为什么错

官方页写：加入的是 BLAKE2 里的压缩函数 F，返回更新后的状态向量，不是完整哈希。先做 F，是互操作当时严格必需的一块；完整 BLAKE2b 是加分项，当时不清楚能不能及时找到一套够用的完整哈希 API。Equihash 验证、跨链中继、原子交换、给公开账本补隐私，都是「可能」，不是已经上线。输入必须定长，最后一块旗标只有两档合法。本页不是 keccak，也不是 SHA3。

看见压缩函数 F 不是已经是 BLAKE2b 哈希；看见本页不是已经能验 Equihash，也不是中继、原子交换或隐私已经齐；看见定长输入不是已经是任意哈希 API；EIP-152 不是 keccak / SHA3。

## 正确替代

[`name-the-blake2f`](../design-patterns/name-the-blake2f.md)。需要曲线算术时用[不变量 199](../invariants/README.md)。需要 bn128 改价时用[不变量 228](../invariants/README.md)。需要读账户代码哈希时用[不变量 221](../invariants/README.md)。

## 会在哪炸

把压缩函数当成完整哈希，会把「压一轮」听成「已经得到摘要」。把动机当成产品，会把「可能做中继」听成跨链和隐私已经齐。把 152 当成 keccak，会把另一条哈希积木听成已经换了默认哈希。

## 考试怎么挖

[`C234`](../../adversarial-corpus/README.md)。
