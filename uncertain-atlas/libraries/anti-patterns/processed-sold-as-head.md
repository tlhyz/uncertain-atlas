# 反模式：处理完一块被写成已经改规范头

> 真值：[处理 ≠ 改头](../../tracks/finality/worked-example-processed-vs-forkchoice.md)、[不变式 149](../invariants/README.md)、[不变式 127](../invariants/README.md)。亲戚：[unsafe-sold-as-derived](unsafe-sold-as-derived.md)、[apphash-sold-as-this-block](apphash-sold-as-this-block.md)。

## 一句话

看见执行层刚跑完一块或 Engine API 回 `VALID`，就把处理写成已经改规范头，或把 forkchoice 事件里的 head 写成已经 finalized。

## 正确写法

「处理一块不是已经改头。头只在 `POS_FORKCHOICE_UPDATED` 时按事件点名。同一事件里的 finalized 是另一份哈希。禁止乐观改头。」
