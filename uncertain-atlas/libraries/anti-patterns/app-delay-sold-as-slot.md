# 反模式：应用回的等待被写成全网槽位

> 真值：[next_block_delay 精读](../../tracks/consensus/worked-example-next-block-delay.md)、[不变式 52](../invariants/README.md)、[abci++ FinalizeBlock](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)。

## 一句话

看见 `next_block_delay`，就写成「应用规定了全网每 N 秒一块」或「等这段才最终」。

## 正确写法

「Commit 已经发生。这是应用回的、非确定性的 post-commit 等待，不是复制状态，不是槽位，也不是最终性。」
