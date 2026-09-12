# 反模式：选择加入替换信号被写成已经换掉

> 真值：[信号 ≠ 已换](../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)、[不变式 166](../invariants/README.md)、[不变式 144](../invariants/README.md)、[不变式 165](../invariants/README.md)。亲戚：[policy-sold-as-consensus](policy-sold-as-consensus.md)、[csv-sold-as-absolute](csv-sold-as-absolute.md)。

## 一句话

看见交易带了 RBF 标记或输入序列号较低，就把选择加入信号写成已经换掉，或把 nSequence 示意写成已经是相对锁，或把未确认入账写成已经当付款。

## 正确写法

「选择加入替换信号不是已经换掉。nSequence 用来示意可替换不是已经是相对锁。子孙继承信号不是自己已经明示加入。钱包看见未确认不是已经当付款。」
