# 反模式：体可变拒绝被写成头已经绑死

> 真值：[Zcash ZIP 256](../../tracks/failure-museum/zcash-2026-nu5-body-poison.md)、[不变式 106](../invariants/README.md)。亲戚：[mutated-clears-others-download](mutated-clears-others-download.md)、[local-error-as-consensus-invalid](local-error-as-consensus-invalid.md)、[announce-sold-as-received](announce-sold-as-received.md)。

## 一句话

看见块被拒、或看见 Merkle 根对得上，就写成授权数据已经绑在头上、诚实头被拉黑等于这块已经非法。

## 正确写法

「授权数据的承诺对象必须先于会随体变的拒绝。体失败不得写入头的永久非法表。Merkle 根不是授权根。」
