# 反模式：privatebroadcast 开关被写成 IP 已经不暴露

> 真值：[Bitcoin Core 2026-06-06](../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md)、[不变式 112](../invariants/README.md)。亲戚：[proxy-sold-as-peer](proxy-sold-as-peer.md)、[uri-fetch-sold-as-verify](uri-fetch-sold-as-verify.md)、[wallet-load-sold-as-no-txid](wallet-load-sold-as-no-txid.md)。

## 一句话

看见发行说明写「接收方永远不知道 IP」，或看见第一次连接走了 Tor，就写成握手失败后的 v1 重连仍然藏着源地址。

## 正确写法

「不暴露源 IP 的路径，每一次出站含降级重连必须仍走同一代理谓词。第一次走 Tor 不是降级已覆盖。」
