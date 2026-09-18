# 模式：点名 fend-nottimeout 杠

**层次**：实现 / FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事（432 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-fend-nottimeout-vs-bundled.md`](../tracks/implementation/worked-example-fend-nottimeout-vs-bundled.md)。

- **next_block_delay 不是已经是本地 timeout_commit：** 看见回了 next_block_delay，不是已经是本地 timeout_commit interchangeable / 1075 fend-nottimeout interchangeable。
- **看见能指 post-commit 等待 不是已经是块间隔：** 看见能指 post-commit 等待，不是已经是块间隔 interchangeable。
- **看见标成非确定 不是已经像 app_hash 那样必须确定：** 看见标成非确定，不是已经像 app_hash 那样必须确定 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_block_delay 正式三事（432 余量），先数清问的是是不是已经是本地 timeout_commit、是不是已经是块间隔、还是看见标成非确定是不是已经像 app_hash 那样必须确定，再决定要不要同一次发布。432 finrespend vs params bundled unbundling 在本页 item 3 完成。
