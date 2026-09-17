# 反模式：停链交易被写成链已经停

> 真值：[x/crisis 不停链](../../tracks/failure-museum/x-crisis-no-halt.md)、[不变式 73](../invariants/README.md)。亲戚：[endblocker-error-sold-as-skippable](endblocker-error-sold-as-skippable.md)（对照：EndBlocker 出错**会**停）。

## 一句话

看见 `MsgVerifyInvariant` 或模块名叫 crisis，就写成不变量失败后全网已经关机；或把交易内 panic 当成停机谓词已兑现。

## 正确写法

「发停链交易不是链已经停。交易内 panic 可被恢复。真要停，必须写在交易恢复笼外，或写链下协调。」
