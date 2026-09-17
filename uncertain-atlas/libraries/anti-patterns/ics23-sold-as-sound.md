# 反模式：ICS-23 验通过被写成叶子已在原树

> 真值：[Dragonberry](../../tracks/failure-museum/dragonberry.md)、[不变式 79](../invariants/README.md)。亲戚：[timeout-hook-sold-as-atomic](timeout-hook-sold-as-atomic.md)、[ack-json-sold-as-deterministic](ack-json-sold-as-deterministic.md)、[proof-ok-equals-no-inflation](proof-ok-equals-no-inflation.md)。

## 一句话

看见跨链缺席证明验绿，就写成包真的没收到、超时已经结算；或只升 SDK 版本，把 ics23 replace 写成可省略。

## 正确写法

「ICS-23 必须先有 soundness。Verify 绿不是叶子已在原树。缺席证明被接受不是包真的没收到。伪造超时不是 ICS-20 已结算。升依赖不是证明库已经换。」
