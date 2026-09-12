# 反模式：组下标被写成票向量下标

> 真值：[Kusama 2025-08-24](../../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md)、[不变式 98](../invariants/README.md)。亲戚：[part-index-sold-as-proof-index](part-index-sold-as-proof-index.md)、[tx-depth-sold-as-api-depth](tx-depth-sold-as-api-depth.md)、[endblocker-error-sold-as-skippable](endblocker-error-sold-as-skippable.md)。

## 一句话

看见要从组里剔除已禁用的人，或看见 create_inherent 回了 None，就写成票已经按座位号删对、客户端已经报错。

## 正确写法

「组座位号不是信封序号。票可以比组少。API 回 None 必须当失败。生产关日志不是错误已可见。」
