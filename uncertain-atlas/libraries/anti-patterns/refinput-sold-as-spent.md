# 反模式：引用输入被写成已经花掉

> 真值：[引用 ≠ 花费](../../tracks/state-models/worked-example-refinput-vs-spent.md)、[不变式 150](../invariants/README.md)、[不变式 143](../invariants/README.md)。亲戚：[predicate-sold-as-script](predicate-sold-as-script.md)。

## 一句话

看见交易列了某枚输出或脚本读到 datum，就把引用写成已经花费，或把看见写成已经过锁，或把同一枚输出写成可以既花又引用。

## 正确写法

「引用输入不是已经花费。被引用输出仍在 UTXO，值不参与平衡，花费条件不被检查。同一枚不得既花又引用。」
