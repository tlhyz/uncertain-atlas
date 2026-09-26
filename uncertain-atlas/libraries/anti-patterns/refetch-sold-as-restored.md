# 反模式：看见应用可以再拉块或封邻居、引擎不自己做就当成已经封了 / 看见 refetch_chunks 不论 result 都再拉再装、按顺序就当成已经齐 / 看见 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名就当成已经能接着装

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[应用可以再拉块或封邻居、引擎不自己做 ≠ 已经封了](../../tracks/implementation/worked-example-refetch-vs-restored.md)。

## 塌法

1. 看见应用可以再拉块或封邻居、引擎不自己做 / 看见能再拉，就当成已经封了，或当成已经齐。
2. 看见 `refetch_chunks` 不论 `result` 都再拉再装、按顺序 / 看见列了块号，就当成已经齐，或当成已经交差。
3. 看见 `reject_senders` 不论 `Result` 都拒这些人、已装的不重拉除非点名 / 看见拒了人，就当成已经能接着装，或当成已经停。

## 为什么会出事

官方写：应用可以再拉块，也可以封 P2P 邻居。CometBFT 不会自己做这些，除非应用下了指令。`refetch_chunks` 不论 `result` 是什么，都会再拉并列出来的那些块，再按顺序装回去。`reject_senders` 不论 `Result` 是什么，都拒这些 P2P 发送者。已经装上的块不会重拉，除非明确点名。

## 和相邻反模式

- [refetch-notcomplete-sold-as-bundled](refetch-notcomplete-sold-as-bundled.md) 是 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 item 2），不是本页 bundled 全段 alone。
- [refetch-notbanned-sold-as-bundled](refetch-notbanned-sold-as-bundled.md) 是应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 item 1），不是本页 bundled 全段 alone。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完，不是本页这种应用可以再拉块或封邻居、引擎不自己做不是已经封了。
- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是封禁邻居就已经没有快照 DoS，不是本页这种 refetch_chunks 不论 result 都再拉再装不是已经齐。
- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐，不是本页这种 reject_senders 不论 Result 都拒这些人不是已经能接着装。
