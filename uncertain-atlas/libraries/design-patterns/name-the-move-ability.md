# 模式：Move 必须先点名是哪一种能力

**问题：** 产品把「Move 所以钱不能复制 / 写了 store」写成已经解释了资源。用户把 `store` 听成已经上架，或把声明了 `copy` 听成每种实例都能复制。  
**方案：** 每个资源句先点名问的是 `copy`、`drop`、`store` 还是 `key`。`store` 不是顶层资源。`key` 操作只在定义模块。声明了 `has copy` 仍看类型参数。  
**适用：** 经典 Move 全局存储 / Aptos 资源账户。  
**优点：** 用户能指出四扇门不是同一把钥匙。  
**缺点：** 句子变长；不能再用「Move 线性」交差。  
**项目：** 官方 Move Book Abilities。  
**常见 bug：** `store` 写成已经上架；声明写成实例；整数字段写成外层能复制。  
**不确定：** 第一版可以不上 Move。若上，必须写清四扇门。见 [工作实例](../../tracks/state-models/worked-example-ability-vs-resource.md)。
