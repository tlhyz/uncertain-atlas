# 反模式：把 FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事（432 余量） 写成已经 已经是本地 timeout_commit / 已经是块间隔 / 已经像 app_hash 那样必须确定

**层次**：实现 / FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事（432 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-fend-nottimeout-vs-bundled.md`](../tracks/implementation/worked-example-fend-nottimeout-vs-bundled.md)。

把 FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事（432 余量） 写成已经 已经是本地 timeout_commit / 已经是块间隔 / 已经像 app_hash 那样必须确定，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_block_delay 正式三事（432 余量），必须分开 not already timeout-commit、not already block-interval、not already must-det 三件事，不要和 432 / 52 / 1073 / 1074 糊成一句。

也不是：

- [fend-notapphash-sold-as-bundled](fend-notapphash-sold-as-bundled.md) 是 app_hash 仍未写进下一块头单句边界（1074 item 2），不是本页 next_block_delay 仍未是本地 timeout_commit 边界。
- post-commit 等待已经标成非确定性是不变量 52，不是本页能指 post-commit 等待仍未是块间隔边界。
