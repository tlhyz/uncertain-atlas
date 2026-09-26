# 例：看见应用可以再拉块或封邻居、引擎不自己做不是已经封了；看见 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐；看见 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装

**层次**：实现 / ApplySnapshotChunk 再拉。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「应用可以再拉块或封邻居、引擎不自己做不是已经封了 / refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 / reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装」，不是 Offer 收下就已经装完，也不是封禁邻居就已经没有快照 DoS。不要另写怎样写 ApplySnapshotChunk。378 refetch-vs-restored bundled unbundling 启动（881）；精读 [`worked-example-refetch-notbanned-vs-bundled.md`](worked-example-refetch-notbanned-vs-bundled.md)（不变量 881 item 1）。

## 官方三件事

规范把应用可以再拉块或封邻居而引擎不自己做、`refetch_chunks` 不论 result 都再拉再装、`reject_senders` 不论 Result 都拒这些人写成三件独立的实现事，不是「看见回了再拉就已经封了、已经齐、已经能接着装」一件事：

1. **看见应用可以再拉块或封邻居、引擎不自己做 / 看见能再拉 不是已经封了，也不是已经齐。**  
   官方写：应用可以再拉块，也可以封 P2P 邻居。CometBFT 不会自己做这些，除非应用下了指令。看见能再拉，不是已经封了。看见能封，不是已经齐。看见有指令，不是已经交差。
2. **看见 `refetch_chunks` 不论 `result` 都再拉再装、按顺序 / 看见列了块号 不是已经齐，也不是已经交差。**  
   官方写：`refetch_chunks` 不论 `result` 是什么，都会再拉并列出来的那些块，再按顺序装回去。只拉列出来的那些。看见列了块号，不是已经齐。看见再装，不是已经交差。看见按顺序，不是已经是同一份。
3. **看见 `reject_senders` 不论 `Result` 都拒这些人、已装的不重拉除非点名 / 看见拒了人 不是已经能接着装，也不是已经停。**  
   官方写：`reject_senders` 不论 `Result` 是什么，都拒这些 P2P 发送者。已经装上的块不会重拉，除非明确点名。这些人排队的块会丢掉，新块或其他快照也会拒。看见拒了人，不是已经能接着装。看见丢掉排队，不是已经停。看见已装的还在，不是已经齐。

怎样写 `ApplySnapshotChunk`、怎样再拉、怎样封邻居是规范里的做法，本页不抄。Offer 收下就已经装完是不变量 321，本页不抄。

## 官方为什么这样拆

- **应用可以再拉块或封邻居、引擎不自己做 ≠ 已经封了：** 官方把应用下指令和引擎已经封了分开。
- **refetch_chunks 不论 result 都再拉再装 ≠ 已经齐：** 官方把再拉并列块和已经齐分开。
- **reject_senders 不论 Result 都拒这些人 ≠ 已经能接着装：** 官方把拒发送者和已经能接着装分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用可以再拉块或封邻居、引擎不自己做 | 不是已经封了 | 不是 Offer 收下就已经装完（321） |
| refetch_chunks 不论 result 都再拉再装 | 不是已经齐 | 不是封禁邻居就已经没有快照 DoS（332） |
| reject_senders 不论 Result 都拒这些人 | 不是已经能接着装 | 不是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了再拉就已经封了、已经齐、已经能接着装」，必须分开应用可以再拉块或封邻居、引擎不自己做是不是已经封了、refetch_chunks 不论 result 都再拉再装是不是已经齐、reject_senders 不论 Result 都拒这些人是不是已经能接着装。可以跳过「看见回了再拉就已经封了」。不要另写怎样写 ApplySnapshotChunk。378 refetch-vs-restored bundled unbundling 启动（881）。

## 本页不抄

- 怎样写 `ApplySnapshotChunk`、怎样再拉、怎样封邻居。
- Offer 收下就已经装完。那是不变量 321。
- 封禁邻居就已经没有快照 DoS。那是不变量 332。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
