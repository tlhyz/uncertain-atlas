# 反模式：nonce 顶到上限被写成已经还能加一

> 真值：[上限 ≠ 还能加](../../tracks/state-models/worked-example-max-nonce-vs-next.md)、[不变式 175](../invariants/README.md)、[不变式 161](../invariants/README.md)、[不变式 162](../invariants/README.md)。亲戚：[code-sender-sold-as-eoa](code-sender-sold-as-eoa.md)、[chainid-sold-as-signed](chainid-sold-as-signed.md)、[type-sold-as-payload](type-sold-as-payload.md)。

## 一句话

看见账户 nonce 很大或客户端已经用窄整数存，就把上限写成已经还能加一，或把 2681 写成 155，或把创建指令碰到上限写成已经创建。

## 正确写法

「nonce 顶到规范上限不是已经还能加一。交易 nonce 达到或超过上限不是已经合法。CREATE / CREATE2 碰到上限不是已经创建。客户端已经用窄整数存 nonce 不是共识已经写了这道上限。EIP-2681 不是 EIP-155。」
