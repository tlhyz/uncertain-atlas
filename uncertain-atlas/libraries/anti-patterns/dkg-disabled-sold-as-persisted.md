# 反模式：DKG 按设计关掉被写成已经落盘

> 真值：[Sui 2026-05 DKG 裁决](../../tracks/failure-museum/sui-2026-05-dkg-verdict-disk.md)、[不变式 93](../invariants/README.md)。亲戚：[durable-nonce-sold-as-consumed](durable-nonce-sold-as-consumed.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)、[cancel-sold-as-no-debit](cancel-sold-as-no-debit.md)。

## 一句话

看见 DKG 参与不够、随机性按设计关掉，或看见用过一次强制关纪元，就写成重启后还记得、换纪元安全模式已经覆盖。

## 正确写法

「失败裁决没写盘，重启就当没关过。依赖随机数的交易既不执行也不取消，队排不空，纪元关不了。一次 force-close 是应急，不是常备能力。不要抄门槛。不要写怎样饿死 DKG。」
