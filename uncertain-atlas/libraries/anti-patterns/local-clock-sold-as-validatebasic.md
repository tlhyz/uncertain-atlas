# 反模式：ValidateBasic 读本地钟被写成已经确定

> 真值：[Jackfruit](../../tracks/failure-museum/jackfruit.md)、[不变式 82](../invariants/README.md)。亲戚：[local-rng-in-apply](local-rng-in-apply.md)、[authz-sold-as-validated](authz-sold-as-validated.md)、[pbts-sold-as-mtp](pbts-sold-as-mtp.md)。

## 一句话

看见入门校验在比过期时间，就写成已经确定；或把节点手表写成块时间。

## 正确写法

「状态机里的现在必须是块头时间。ValidateBasic 读本地钟不是已确定。资金安全不是链不会停。漏掉检查（Elderflower）是另一句。」
