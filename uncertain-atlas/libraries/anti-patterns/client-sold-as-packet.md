# 反模式：轻客户端被写成数据包已经送达

> 真值：[客户端 ≠ 数据包工作实例](../../tracks/economic/worked-example-ibc-client-vs-packet.md)、[不变式 146](../invariants/README.md)、[不变式 79](../invariants/README.md)。亲戚：[ics23-sold-as-sound](ics23-sold-as-sound.md)、[timeout-hook-sold-as-atomic](timeout-hook-sold-as-atomic.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)。

## 一句话

看见「开了 IBC」或看见链上有一个 client，就把轻客户端写成已经开连接，或把连接写成已经开通道，或把 `sendPacket` 写成对岸已经 recv。

## 正确写法

「客户端是对岸状态更新的验法，不是已经开连接。连接是授权，不是已经开通道。通道对载荷无所知，不是已经兑付。本链写下的是承诺，不是对岸已经 recv。」
