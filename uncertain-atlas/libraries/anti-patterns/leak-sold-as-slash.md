# 反模式：inactivity leak 被写成已经 slash，或终局推迟被写成已经停链

> 真值：[leak ≠ slash 工作实例](../../tracks/finality/worked-example-inactivity-leak.md)、[不变式 130](../invariants/README.md)。亲戚：[justified-sold-as-finalized](justified-sold-as-finalized.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)、[two-votes-sold-as-slash](two-votes-sold-as-slash.md)、[stale-checkpoint-sold-as-genesis](stale-checkpoint-sold-as-genesis.md)。

## 一句话

看见好久没 finalized，就把链写成已经停，或不投票的人写成已经被 slash，或两边都 leak 到最终写成协议已经选出唯一规范链。

## 正确写法

「终局推迟不是高度已经停。Inactivity leak 抽的是不跟多数走的质押，官方写很贵但没有被 slash。Slash 要能指出双投 / 包围 / 同槽两块。两边都 finalized 时官方写只剩社会恢复。」
