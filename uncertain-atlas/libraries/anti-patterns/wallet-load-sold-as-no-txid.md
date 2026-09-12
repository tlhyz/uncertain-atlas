# 反模式：从文件加载钱包被写成出站 TXID 已经不泄漏

> 真值：[Monero 2025-08-26](../../tracks/failure-museum/monero-2025-08-find-and-save-rings.md)、[不变式 111](../invariants/README.md)。亲戚：[uri-fetch-sold-as-verify](uri-fetch-sold-as-verify.md)、[rpc-as-verification](rpc-as-verification.md)、[proxy-sold-as-peer](proxy-sold-as-peer.md)。

## 一句话

看见钱包只是打开本地文件，或看见有 trusted 开关，就写成出站交易名单不会送给远程守护进程。

## 正确写法

「加载路径上每一条会交出站历史的 RPC 必须先看 trusted。回填函数还在不是只给旧钱包跑一次。」
