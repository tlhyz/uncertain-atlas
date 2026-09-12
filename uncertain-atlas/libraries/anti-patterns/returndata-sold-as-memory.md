# 反模式：把返回数据缓冲写成已经是内存

**标识：** `returndata-sold-as-memory`
**等级：** 重要
**相关模式：** [`name-the-returndata`](../design-patterns/name-the-returndata.md)
**相关课文：** [L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)
**相关不变量：** 232、177、216、217

## 错误句

「返回数据已经在内存里。」「很像 calldata，所以就是 calldata。」「能再取失败数据，所以 140 已经齐了。」「缓冲会一直留到这笔交易结束。」

## 为什么错

官方页写：调用结束后，返回数据留在一份虚拟缓冲里，调用方再拷进内存。做法很像 calldata，下一次类调用会覆盖。不定长返回可以拆成两次调用先问长度，但更贵，不是已经是本页。本页让 140 更好用，不是已经是 140。创建成功视为空缓冲；没真正开出新帧时缓冲为空。越界读失败。

看见返回数据缓冲不是已经是内存；看见本页不是已经是 calldata，也不是已经用两次调用先问长度；看见失败数据能再取不是已经是 140；看见下一次类调用不是缓冲还在。

## 正确替代

[`name-the-returndata`](../design-patterns/name-the-returndata.md)。需要回滚语义时用[不变量 177](../invariants/README.md)。需要内存拷时用[不变量 216](../invariants/README.md)。需要压零时用[不变量 217](../invariants/README.md)。实现把缓冲和内存别名错了，见[不变量 3](../invariants/README.md)。

## 会在哪炸

把预留输出区当成缓冲，会把「当初开的窗口」听成「全部返回」。把缓冲当成 calldata，会把进门话筒和回音筒听成一支。把能再取失败数据当成 140，会把存放位置听成失败语义已经齐。把缓冲当下一次调用后还在，会把旧回音听成还在。

## 考试怎么挖

[`C236`](../../adversarial-corpus/README.md)。
