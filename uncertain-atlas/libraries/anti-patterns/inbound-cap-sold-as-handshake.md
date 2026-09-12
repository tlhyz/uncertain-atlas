# 反模式：入站邻居上限被写成握手请求已有界

> 真值：[CVE-2020-5303 / Lavender](../../tracks/failure-museum/cve-2020-5303.md)、[不变式 67](../invariants/README.md)。亲戚：[max-msg-sold-as-recv-quota](max-msg-sold-as-recv-quota.md)、[autoban-sold-as-bound](autoban-sold-as-bound.md)。

## 一句话

看见 `max_num_inbound_peers`，就写成入站握手已经有界；或让对等 ID 在连接启动之后才认领，失败路径只 Remove、不归还。

## 正确写法

「连接请求在变成 Peer 之前就必须有配额。ID 必须在连接启动前认领，并在所有退出路径归还。公开 RPC 另写配额。」
