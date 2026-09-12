# 反模式：授权代发被写成内层消息已经过认证

> 真值：[Elderflower](../../tracks/failure-museum/elderflower.md)、[不变式 81](../invariants/README.md)。亲戚：[local-clock-sold-as-validatebasic](local-clock-sold-as-validatebasic.md)、[blocked-sold-as-initialized](blocked-sold-as-initialized.md)。

## 一句话

看见授权模块替人执行消息，就写成内层已经过 `ValidateBasic`；或把同一天的 Dragonberry 补丁写成认证旁路已修。

## 正确写法

「被代执行的消息必须再跑与直接投递相同的基本校验。授权过了不是内层已合法。打过 ics23 replace 不是本条已补。」
