# 反模式：把 blob 基础费指令写成已经是执行层基础费指令

**标识：** `blobbasefee-sold-as-basefee`
**等级：** 重要
**相关模式：** [`name-the-blobbasefee`](../design-patterns/name-the-blobbasefee.md)
**相关课文：** [L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)、[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)
**相关不变量：** 219、218、145、201

## 错误句

「多了一条 blob 基础费指令，所以已经是执行层那条基础费指令。」「合约能读 blob 基础费，所以两套气已经并账。」「跑 EVM 前就有这个数，所以 4844 日程已经改了。」「EIP-7516 就是 EIP-3198 / 不变量 218。」

## 为什么错

官方页写：给 EVM 加一条读本块数据 blob 基础费的指令。它和 3198 一样，只是返回按 4844 算出来的 blob 基础费。意图是让合约按 blob 气价记账。处理带 blob 的交易本来就要用到这个数，所以跑 EVM 之前它已经在。blob 基础费不敏感，头上本来就公开。规范没有把本页写成已经是 3198，也没有把能读到写成已经并账，也没有把本页写成已经改了 4844 或已经是 blob 底价规则。

看见 blob 基础费指令不是已经是执行层基础费指令；看见能读本块 blob 基础费不是已经并成一套气；看见跑 EVM 前就已经有这个数不是已经改了 4844 日程；EIP-7516 不是 EIP-3198 也不是不变量 218，也不是 EIP-4844。

## 正确替代

[`name-the-blobbasefee`](../design-patterns/name-the-blobbasefee.md)。需要读执行层基础费时用[不变量 218](../invariants/README.md)。需要两套气时用[不变量 145](../invariants/README.md)。需要 blob 底价规则时用[不变量 201](../invariants/README.md)。

## 会在哪炸

把读 blob 价当成已经是 3198，会把「看行李费牌子」写成「入场费牌子已经够了」。把能读到当成已经并账，会把两套气听成一本账。把本页写成 4844 / 7918，会把日程和底价规则混进读数。

## 考试怎么挖

[`C223`](../adversarial-corpus/README.md)。
