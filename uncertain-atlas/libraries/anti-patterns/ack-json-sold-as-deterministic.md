# 反模式：跨链确认的 JSON 被写成已经确定

> 真值：[ISA-2025-001 / ASA-2025-004](../../tracks/failure-museum/isa-2025-001.md)、[不变式 77](../invariants/README.md)、[编码精读](../../tracks/implementation/worked-example-encoding.md)。亲戚：[noncanonical-accepted](noncanonical-accepted.md)、[intdec-sold-as-aligned](intdec-sold-as-aligned.md)。

## 一句话

看见 acknowledgement 意思是成功，就写成反序列化已经确定；或只修 transfer，把其它应用写成已覆盖。

## 正确写法

「跨链确认必须有唯一字节。能开通道的用户是活性对手。只补 transfer 不够。中间件自己编 ack 必须与应用同一 codec。」
