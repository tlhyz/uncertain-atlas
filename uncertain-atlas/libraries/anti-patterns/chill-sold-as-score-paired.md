# 反模式：改冻结门槛被写成选举地板已经配对

> 真值：[Polkadot 2026-06-30](../../tracks/failure-museum/polkadot-2026-06-election-score-floor.md)、[不变式 110](../invariants/README.md)。亲戚：[enable-height-sold-as-safe](enable-height-sold-as-safe.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)、[validator-update-sold-as-immediate](validator-update-sold-as-immediate.md)。

## 一句话

看见出块还在，或看见质量地板模块还在目录里，就写成改了冷冻门槛之后选举仍能选出下一纪元。

## 正确写法

「会移动可达分的治理变更必须同时带地板。出块继续不是纪元已经转。诚实解低于不可达地板被罚不是提交者作恶。」
