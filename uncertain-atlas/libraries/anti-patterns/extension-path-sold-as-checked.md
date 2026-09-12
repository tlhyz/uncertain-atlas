# 反模式：扩展快路径被写成旧票字段已检查

> 真值：[ASA-2024-011](../../tracks/failure-museum/asa-2024-011.md)、[不变式 57](../invariants/README.md)、[扩展精读](../../tracks/consensus/worked-example-vote-extension.md)。亲戚：[vote-extension-sold-as-block](vote-extension-sold-as-block.md)。

## 一句话

看见实现为 vote extension 另开一条 Precommit 处理，就写成普通票字段已经验过；或把「默认关扩展 / 上游发不出」写成启用后不会 panic。

## 正确写法

「新票路径必须复用旧票的字段检查。会当集合下标的字段，必须在处理扩展之前验完。默认关着只是本条打不进。」
