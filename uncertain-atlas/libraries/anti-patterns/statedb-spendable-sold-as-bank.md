# 反模式：StateDB 可花余额被写成银行账已经对齐

> 真值：[Cosmos EVM 2026-08](../../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md)、[不变式 115](../invariants/README.md)。亲戚：[oog-sold-as-reverted](oog-sold-as-reverted.md)、[blocked-sold-as-initialized](blocked-sold-as-initialized.md)。

## 一句话

看见 EVM 余额和 x/bank 对过账，或看见主分支已经有静默补丁，就写成归属锁定已经从写回里排除，回绕后的数不能当合法可转。

## 正确写法

「引擎只看见可花时，不得按锁定也算进去的委托额去减这本账。回绕后的数不是银行已经对齐。主分支补丁不是发布线已经打上。」
