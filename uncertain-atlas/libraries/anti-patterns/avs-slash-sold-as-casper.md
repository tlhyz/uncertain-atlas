# 反模式：AVS 自定罚没被写成已经 Casper / 协议罚没

> 真值：[AVS 罚没 ≠ Casper 工作实例](../../tracks/economic/worked-example-avs-slash-vs-casper.md)、[不变式 140](../invariants/README.md)、[EigenLayer 滤网](../../protocols/eigenlayer/README.md)。亲戚：[leak-sold-as-slash](leak-sold-as-slash.md)、[btc-lock-sold-as-commit](btc-lock-sold-as-commit.md)、[backed-sold-as-available](backed-sold-as-available.md)。

## 一句话

看见「restake」或看见「也被罚了」，就把 AVS 按任何理由罚的产品函数写成 Casper surround / CometBFT 证据，或写成 restake 已经变成另一个信标最终，或写成协议会否决乱罚。

## 正确写法

「restake 是已有以太坊质押上的第二份可罚声明，不是另一条信标。AVS 罚没由产品定义，官方写不必链上可证；EigenLayer 协议不提供否决。这和 Casper 两票谓词不是同一句。」
