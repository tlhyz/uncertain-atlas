# 反模式：发送者已有代码被写成已经能当 EOA 发交易

> 真值：[有代码 ≠ 能发](../../tracks/state-models/worked-example-code-sender-vs-eoa.md)、[不变式 162](../invariants/README.md)、[不变式 160](../invariants/README.md)。亲戚：[selfdestruct-sold-as-deleted](selfdestruct-sold-as-deleted.md)、[chainid-sold-as-signed](chainid-sold-as-signed.md)。

## 一句话

看见地址能恢复出私钥或合约后来调过自毁，就把已有代码的发送者写成已经能当 EOA 发交易，或把 RPC 模拟放行写成共识已经放行。

## 正确写法

「发送者已有代码不是已经能当 EOA 发交易。从该地址发出的交易不是已经合法。块里收了它不是块已经合法。RPC 模拟放行不是共识已经放行。」
