# 反模式：把 calldata 降价写成已经没有上限

**标识：** `calldata-cut-sold-as-unlimited`
**等级：** 重要
**相关模式：** [`name-the-calldata-cut`](../design-patterns/name-the-calldata-cut.md)
**相关课文：** [L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)、[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)
**相关不变量：** 226、197、145、158

## 错误句

「非零 calldata 降价了，所以零字节也便宜了。」「降价了，所以块已经可以任意大。」「二层把数据贴在 calldata，所以 DA 已经齐了。」「EIP-2028 就是 EIP-7623 / 不变量 197 / EIP-4844。」

## 为什么错

官方页写：只降低非零 calldata 字节的气价，零字节不变。更高带宽一般能让一块多塞数据，不是已经没有上限。二层常把存储和计算挪到链下，但往往改成传数据；可选做法之一是把数据贴在主链 calldata，不是已经解决 DA，也不是已经是 blob。降低气价会导致潜在更大的块，加大传输延迟，从而降低攻击网络的成本。规范没有把非零降价写成零字节也降了，也没有把本页写成已经没有块上限，也没有把本页写成 7623 或 4844。

看见非零 calldata 降价不是已经给零字节也降价；看见降价不是已经没有块大小上限；看见降价不是已经不伤延迟 / 安全；EIP-2028 不是 EIP-7623 也不是不变量 197，也不是 EIP-4844。

## 正确替代

[`name-the-calldata-cut`](../design-patterns/name-the-calldata-cut.md)。需要后来的地板时用[不变量 197](../invariants/README.md)。需要 blob 气时用[不变量 145](../invariants/README.md)。需要费用市场时用[不变量 158](../invariants/README.md)。

## 会在哪炸

把非零降价当成零字节也降了，会把「空白填充」听成已经便宜。把便宜当成没有上限，会把潜在更大块听成已经无限。把 2028 当成 7623，会把降价听成已经加了数据为主的地板。

## 考试怎么挖

[`C230`](../../adversarial-corpus/README.md)。
