# 反模式：preserve_origin 被写成出站已经带了改 origin 的指令

> 真值：[Polkadot 2026-03](../../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md)、[不变式 113](../invariants/README.md)。亲戚：[authz-sold-as-validated](authz-sold-as-validated.md)、[tx-depth-sold-as-api-depth](tx-depth-sold-as-api-depth.md)。

## 一句话

看见旗标叫「保留 origin」，或看见修费绕过的热修已经合入，就写成出站消息已经带了别名或再清，目的地不会用运输发送者。

## 正确写法

「保留 origin 为真且当前 origin 已空必须失败关闭。静默跳过不是 BadOrigin。运输发送者不是用户 origin 已经清掉。」
