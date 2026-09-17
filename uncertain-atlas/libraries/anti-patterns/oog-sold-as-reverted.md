# 反模式：out-of-gas 结束被写成空账户删除已经回滚

> 真值：[Ethereum 2016-11-24](../../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md)、[不变式 103](../invariants/README.md)。亲戚：[half-written-state](half-written-state.md)、[local-error-as-consensus-invalid](local-error-as-consensus-invalid.md)、[gas-sold-as-wallclock](gas-sold-as-wallclock.md)。

## 一句话

看见交易气不够倒下，或看见多数客户端在另一条链，就写成失败路径已经撤回空账户删除、两家已经同根。

## 正确写法

「OOG 必须撤回本笔引起的空账户删除。journaling 只记成功不是失败已回滚。跟多数实现不是规范已对齐。」
