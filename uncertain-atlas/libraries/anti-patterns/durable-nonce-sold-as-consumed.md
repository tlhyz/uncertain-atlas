# 反模式：失败的 durable nonce 被写成已经消费

> 真值：[Solana 2022-06-01](../../tracks/failure-museum/solana-2022-06-01-durable-nonce.md)、[不变式 85](../invariants/README.md)。亲戚：[local-rng-in-apply](local-rng-in-apply.md)、[ack-json-sold-as-deterministic](ack-json-sold-as-deterministic.md)、[local-clock-sold-as-validatebasic](local-clock-sold-as-validatebasic.md)、[nonce-gap-sold-as-proposal](nonce-gap-sold-as-proposal.md)。

## 一句话

看见 durable nonce 失败进了块、手续费付了，就写成「nonce 已经用过、不能再播」；或把一边收一边拒写成 Tower / PoH 已经一致。

## 正确写法

「失败路径必须与成功路径一样推进或作废同一链上对象。当普通 recent-blockhash 处理、nonce 未推进，不是已消费。近期缓存不是全网同一对象。>33% 接受且不足 66% 对齐是停链，不要抄进不确定法定人数。」
