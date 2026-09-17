# 反模式：进了块的 coinbase 被写成已经能花

> 真值：[进块 ≠ 能花](../../tracks/economic/worked-example-coinbase-vs-mature.md)、[不变式 163](../invariants/README.md)、[不变式 144](../invariants/README.md)。亲戚：[policy-sold-as-consensus](policy-sold-as-consensus.md)、[coinbase-balance-sold-as-restart-safe](coinbase-balance-sold-as-restart-safe.md)。

## 一句话

看见奖励进了块或钱包列出了这笔，就把未成熟 coinbase 写成已经能当输入花，或把商家常用确认数写成已经过成熟窗。

## 正确写法

「进了块的 coinbase 不是已经能花。钱包看见奖励不是已经成熟。普通确认深度不是 coinbase 成熟窗。成熟规则不是本地策略。」
