# 反模式：链下内存禁用被写成已确认争议已经不参与

> 真值：[Kusama 2025-05-09](../../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md)、[不变式 100](../invariants/README.md)。亲戚：[active-dispute-sold-as-confirmed](active-dispute-sold-as-confirmed.md)、[dkg-disabled-sold-as-persisted](dkg-disabled-sold-as-persisted.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)。

## 一句话

看见输了争议的人被写进链下名单，或看见训练轮已经触发，就写成垃圾争议已经没人参与、最终性还在走。

## 正确写法

「链下内存禁用只挡未确认。已确认仍要参与。重启清空名单不是已经禁用。训练轮触发不是最终性引擎还在走。」
