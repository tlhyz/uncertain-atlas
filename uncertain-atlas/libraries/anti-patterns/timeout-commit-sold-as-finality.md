# 反模式：timeout_commit 被写成还没最终

> 真值：[超时精读](../../tracks/consensus/worked-example-timeouts.md)、[consensus.md](https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md)、[不变式 47](../invariants/README.md#47-本地超时不是最终性)。

## 一句话

看见 `timeout_commit`，就写成「再等一会儿才最终」或「全网必须同一秒数」。看见 `skip_timeout_commit`，就写成第三种最终性。

## 正确写法

「Commit 已经发生。NewHeight 再等是为了多收掉队 precommit。这是本地配置，不是块时间，也不是锁。」
