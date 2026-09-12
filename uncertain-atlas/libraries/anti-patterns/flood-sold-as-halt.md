# 反模式：入站洪水被写成已经停链

> 真值：[Solana 2022-04-30](../../tracks/failure-museum/solana-2022-04-30-fork-cleanup-oom.md)、[不变式 89](../invariants/README.md)。亲戚：[halt-sold-as-one-kind](halt-sold-as-one-kind.md)、[cheap-header-sold-as-free](cheap-header-sold-as-free.md)、[maxtxbytes-sold-as-nested-bound](maxtxbytes-sold-as-nested-bound.md)。

## 一句话

看见每秒几百万交易或节点 OOM，就写成「洪水所以停链」；或不写票不够最终、废弃分叉清不掉，只写 TPS。

## 正确写法

「入站数字不是停链谓词。必须点名：票不够落地 → 更早的块最终不了 → 废弃分叉不回收 → 内存把节点打死。重启后分叉仍超能力不是自动恢复。不要抄官网 TPS。」
