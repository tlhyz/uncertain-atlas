# 反模式：验绿被写成 Fiat-Shamir 已经绑完

> 真值：[Solana 2025-05-02](../../tracks/failure-museum/solana-2025-05-02-elgamal-fiat-shamir.md)、[不变式 95](../invariants/README.md)。亲戚：[proof-ok-equals-no-inflation](proof-ok-equals-no-inflation.md)、[ics23-sold-as-sound](ics23-sold-as-sound.md)。

## 一句话

看见 ZK 证明程序返回接受、或看见 Token 程序不用改、或看见先前审计与未见利用，就写成不可铸、不可偷。

## 正确写法

「验证必须哈希组成该证明的全部代数分量。漏一项，绿牌仍可能是假陈述。应用层未改不是证明层已齐。不要写怎样伪造。」
