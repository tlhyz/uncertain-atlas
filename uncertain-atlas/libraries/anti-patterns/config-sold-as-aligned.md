# 反模式：把分叉配置 RPC 对上写成已经同根

**标识：** `config-sold-as-aligned`
**等级：** 重要
**相关模式：** [`name-the-fork-config`](../design-patterns/name-the-fork-config.md)
**相关课文：** [L5.3](../../courses/level-05-ethereum/L05-M03-multi-client.md)
**相关不变量：** 210、149、209、207

## 错误句

「各家 eth_config 对上了，所以已经过多客户端同根。」「看见 current / next / last，所以共识已经改了。」「RPC 绿了，所以对等节点没有撒谎。」「EIP-7910 就是不变量 149 / 209 / 207。」

## 为什么错

官方页写：加一条 RPC，报告本节点当前、下一份、以及已知最后一份分叉配置。动机是分叉前核对，因为历史上有客户端没配好即将到来的硬分叉。本页不改以前的行为。官方写客户端可以谎报。官方不用配置哈希做快对。只改 blob 参数的专用分叉在本页里当成一份新分叉对象，看见本页不是已经是那套机制。规范没有把 RPC 对上写成已经同根，也没有把三份对象写成已经改了共识，也没有把 RPC 绿写成对等节点没有撒谎。

看见分叉配置 RPC 对上了不是已经过多客户端同根；看见 current / next / last 不是已经改了共识；RPC 绿不是对等节点没有撒谎；EIP-7910 不是不变量 149 也不是 209 也不是 207。

## 正确替代

[`name-the-fork-config`](../design-patterns/name-the-fork-config.md)。需要处理完一块是否改头时用[不变量 149](../invariants/README.md)。需要只改 blob 的专用分叉时用[不变量 209](../invariants/README.md)。需要线协议历史窗时用[不变量 207](../invariants/README.md)。

## 会在哪炸

把分叉前核对当成已经过了分叉，会把「清单对上了」写成「已经到了同一座城」。把三份对象当成共识已改，会把 RPC 听成硬分叉。把 RPC 绿当成没人撒谎，会漏掉官方写的谎报。把本页写成 149 / 209 / 207，会把改头、专用分叉、历史窗混进配置核对。

## 考试怎么挖

[`C214`](../../libraries/adversarial-corpus/README.md)。
