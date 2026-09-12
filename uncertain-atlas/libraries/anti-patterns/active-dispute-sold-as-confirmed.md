# 反模式：Active 争议被写成已经 Confirmed

> 真值：[Kusama 2024-02-15](../../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md)、[不变式 99](../invariants/README.md)。亲戚：[evidence-equals-slash](evidence-equals-slash.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)、[group-index-sold-as-vote-index](group-index-sold-as-vote-index.md)。

## 一句话

看见争议被导入并标 Active，或看见 GRANDPA 跳过这条叉，就写成已经 Confirmed、最终性还在走。

## 正确写法

「只被已禁用者发起的争议可以导入，不得标 Active。Active 不是 Confirmed。最终性测试必须另做，不得只断言禁用发生了。」
