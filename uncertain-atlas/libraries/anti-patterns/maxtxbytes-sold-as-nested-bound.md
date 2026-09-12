# 反模式：外层交易上限被写成内层解码已有界

> 真值：[ASA-2024-0012 / 0013](../../tracks/failure-museum/asa-2024-0012.md)、[不变式 70](../invariants/README.md)、[编码精读](../../tracks/implementation/worked-example-encoding.md)。亲戚：[maxbytes-sold-as-sla](maxbytes-sold-as-sla.md)、[max-msg-sold-as-recv-quota](max-msg-sold-as-recv-quota.md)。

## 一句话

看见 `max_tx_bytes`，就写成嵌套消息、`UnpackAny`、内部消息已经有界；或只测外层够短，不测解码递归。

## 正确写法

「外层交易字节上限不是内层已有界。解码必须有递归上限。合约或验证者块放出的内部消息必须另写界。」
