# 反模式：验过头被写成已经能交证据

> 真值：[Alderfly](../../tracks/failure-museum/alderfly.md)、[不变式 66](../invariants/README.md)、[BFT 跳过](../../tracks/light-clients/worked-example-bft-skip.md)。亲戚：[new-set-quorum-as-light-trust](new-set-quorum-as-light-trust.md)、[evidence-equals-slash](evidence-equals-slash.md)。

## 一句话

看见轻客户端 `ValidAndVerified`，就写成已经能提交 `LightClientAttackEvidence`；或把证据形状写成只等「同一高度再出一块冲突块」。

## 正确写法

「收下坏头必须能形成证据。证据不得只依赖同高再出一块。朝前的 lunatic 仍须能问责。验过头 ≠ 已经能提交。安全模型外不是免检。」
