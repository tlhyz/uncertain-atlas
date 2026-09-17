# 反模式：已确认的重复槽赢家被写成下一父块

> 真值：[Solana 2022-09-30](../../tracks/failure-museum/solana-2022-09-30-duplicate-fork.md)、[不变式 86](../invariants/README.md)。亲戚：[durable-nonce-sold-as-consumed](durable-nonce-sold-as-consumed.md)、[announce-sold-as-received](announce-sold-as-received.md)、[majority-vote-is-enough](majority-vote-is-enough.md)。

## 一句话

看见同槽两份块里正确版本已被确认，或看见票还在飞，就写成下一领导者会往上建、根已经前进、Tower / PoH 已经一致。

## 正确写法

「确认 ≠ 可当父块。投票还在、根不前进，是停链前兆，不是共识还在结算。同一身份两台同时出块不是高可用。关掉重复出块者不是边角已消失。」
