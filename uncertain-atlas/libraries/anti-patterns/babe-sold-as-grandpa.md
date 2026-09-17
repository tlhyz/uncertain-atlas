# 反模式：BABE 出块被写成已经 GRANDPA 最终

> 真值：[BABE ≠ GRANDPA 工作实例](../../tracks/consensus/worked-example-babe-vs-grandpa.md)、[不变式 126](../invariants/README.md)。亲戚：[two-finality-sold-as-one](two-finality-sold-as-one.md)、[header-equals-settlement](header-equals-settlement.md)、[backed-sold-as-available](backed-sold-as-available.md)、[chill-sold-as-score-paired](chill-sold-as-score-paired.md)。

## 一句话

看见中继还在出新块、explorer 跟上了 BABE 头、或文案写「混合共识」，就写成已经不可逆，或把最长链写成最终头之后的尺子。

## 正确写法

「BABE 是出块服务，GRANDPA 是并行的最终服务。最终对链、一次敲定祖先。最终头之后比主块，不比长度。BEEFY 是已最终块上的桥 gadget，不是 GRANDPA 本身。」
