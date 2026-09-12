# 反模式：STM 跑完被写成已经最终

> 真值：[Block-STM 工作实例](../../tracks/parallelism/worked-example-block-stm.md)、[不变式 122](../invariants/README.md)。亲戚：[stm-replaces-consensus](stm-replaces-consensus.md)、[header-equals-settlement](header-equals-settlement.md)。

## 一句话

看见多核投机执行结束、或看见写集已经算出来，就写成顺序已经不重要，或该块已经最终。

## 正确写法

「提交写集必须等于既定序列 L 的串行执行。STM 跑完不是已经最终。未事先声明写集不是已经不需要 L。」
