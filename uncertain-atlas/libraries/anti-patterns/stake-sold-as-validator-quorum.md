# 反模式：质押加权被写成已经是共识超多数的单位

> 真值：[NPoS 等权工作实例](../../tracks/consensus/worked-example-npos-equal-weight.md)、[不变式 129](../invariants/README.md)。亲戚：[babe-sold-as-grandpa](babe-sold-as-grandpa.md)、[justified-sold-as-finalized](justified-sold-as-finalized.md)、[chill-sold-as-score-paired](chill-sold-as-score-paired.md)、[sample-sold-as-full-set](sample-sold-as-full-set.md)。

## 一句话

看见验证者是按质押选出来的、或某验证者背后质押特别多，就把 ⅔ 质押写成已经过了官方超多数，或把提名时的加权写成当选后共识也按币计票。

## 正确写法

「NPoS 选举按质押加权。当选之后，官方对照页写共识协议里每个验证者等权：一条链要过超多数，数的是验证者，不是质押。Cosmos 对照才是按质押凑 ⅔。BABE 抽槽官方另写按质押，不要把它听成 GRANDPA 也按质押。」
