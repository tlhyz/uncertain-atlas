# 反模式：结构未验完被写成可以先流言

> 真值：[ASA-2025-003](../../tracks/failure-museum/asa-2025-003.md)、[不变式 60](../invariants/README.md)。亲戚：[part-index-sold-as-proof-index](part-index-sold-as-proof-index.md)。

## 一句话

看见对等消息里有位图 / 长度字段，就先转发给邻居、回头再处理；或把单点崩溃写成最坏情况，其实官方最坏是全网停。

## 正确写法

「带内部长度的结构必须在流言之前验完。对不上丢弃。先传后验会把单点事故变成停网。」
