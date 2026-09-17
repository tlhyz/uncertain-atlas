# 反模式：本头 LastCommit 被写成本高度已经 +2/3

> 真值：[本头 LastCommit ≠ 本高度已 +2/3](../../tracks/consensus/worked-example-lastcommit-vs-this-block.md)、[不变式 148](../invariants/README.md)、[不变式 65](../invariants/README.md)。亲戚：[quorum-sold-as-all-signed](quorum-sold-as-all-signed.md)、[apphash-sold-as-this-block](apphash-sold-as-this-block.md)。

## 一句话

看见块里有 `LastCommit` 或看见本节点刚凑齐 +2/3，就把本头票写成本高度已经盖章，或把本地那份写成已经是链上 canonical。

## 正确写法

「本块 LastCommit 是上一块的 canonical +2/3，不是本高度已经 +2/3。本地据以进入 Commit 步的那份不必等于下一块提议者写进去的那份。第一块 LastCommit 必须空。」
