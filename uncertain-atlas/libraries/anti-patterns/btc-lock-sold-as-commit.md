# 反模式：Bitcoin 上的锁被写成已经 wrap 或已经租户 commit

> 真值：[BTC 锁 ≠ commit 工作实例](../../tracks/economic/worked-example-btc-lock-vs-commit.md)、[不变式 139](../invariants/README.md)、[Babylon 滤网](../../protocols/babylon/README.md)。亲戚：[backed-sold-as-available](backed-sold-as-available.md)、[leak-sold-as-slash](leak-sold-as-slash.md)、[header-equals-settlement](header-equals-settlement.md)。

## 一句话

看见「BTC 质押」或看见 k-deep 包含证明，就把仍在 Bitcoin 的 UTXO 写成已经 wrap，或写成租户已经 CometBFT commit，或把解绑意图写成已经 k-deep / 浅重组能恢复票权。

## 正确写法

「UTXO 仍在 Bitcoin，不是已经 wrap。k-deep 包含证明给的是票权，不是租户已经 commit。普通解绑看的是已签花费意图，不要求 k-deep；浅重组拿掉解绑交易不会恢复委托。」
