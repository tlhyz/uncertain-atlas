# 反模式：单笔低于入池上限被写成拼块已被所有客户端接受

> 真值：[Sepolia 2024-03](../../tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md)、[不变式 96](../invariants/README.md)。亲戚：[max-msg-sold-as-recv-quota](max-msg-sold-as-recv-quota.md)、[maxtxbytes-sold-as-nested-bound](maxtxbytes-sold-as-nested-bound.md)、[announce-sold-as-received](announce-sold-as-received.md)。

## 一句话

看见单笔小于入池上限、或看见各家 RPC 已经收到同一低值，就写成拼出来的块对所有客户端合法。

## 正确写法

「入池单笔、块计量、出块通道尺寸是三把尺。多数拒、少数收按分叉审。把门口改窄，必须再测许多小交易。」
