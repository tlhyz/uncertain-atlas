# 例：看见 FinalizeBlockResponse.next_block_delay is not already timeout-commit interchangeable / not already block-interval interchangeable / not already must-det interchangeable

**层次**：实现 / FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事（432 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事（432 余量）/ not 1075 fend-nottimeout interchangeable / not 432 finrespend-vs-params bundled interchangeable」，不是 Finalize 回包末栏 bundled（432），也不是 post-commit 等待已经标成非确定性（52），也不是 ConsensusParams.block 限制块大小和块间隔那种已经是块间隔。不要另写怎样写 Finalize 回包末栏。

## 官方三件事

1. **看见 FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待 / 看见回了 next_block_delay 这份栏 is not already 已经是本地 timeout_commit interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1075 fend-nottimeout interchangeable / 1073 fend-notheffect interchangeable / 432 finrespend item 1 cparam interchangeable，也不是已经 FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事 bundled（432 item 3 余量） interchangeable / 432 finrespend item 3 interchangeable。**  
   官方写：next_block_delay 是 Delay between the time when this block is committed and the next height is started。Deterministic 列是 No。看见回了等待，不是已经本地 timeout_commit 就已经是全网同一份配置 interchangeable——本页从 432 item 3 侧钉 not already timeout-commit 单句。432 finrespend vs params bundled unbundling 在本页 item 3 完成。

2. **看见能指 post-commit 等待 / 看见回了 next_block_delay / 这份栏 is not already 已经是块间隔 interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1075 fend-nottimeout interchangeable / 432 finrespend item 2 app_hash interchangeable / 1074 fend-notapphash interchangeable，也不是已经 post-commit 等待已经标成非确定性 interchangeable / 52 timeout_commit interchangeable。**  
   官方把能指 post-commit 等待和已经是块间隔分开。看见能指 post-commit 等待，不是已经是块间隔 interchangeable。本页钉 not already block-interval 单句。

3. **看见标成非确定 / 看见回了 next_block_delay / 这份栏 is not already 已经像 app_hash 那样必须确定 interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1075 fend-nottimeout interchangeable / 1073 fend-notheffect interchangeable，也不是已经像 app_hash 那样必须确定 interchangeable / 1074 fend-notapphash interchangeable。**  
   官方把标成非确定和已经像 app_hash 那样必须确定分开。看见标成非确定，不是已经像 app_hash 那样必须确定 interchangeable。432 finrespend vs params bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.next_block_delay not already timeout-commit ≠ 已经是本地 timeout_commit interchangeable：** 官方把应用回的 post-commit 等待和配置里的 timeout_commit 分开。
- **看见能指 post-commit 等待 not already block-interval ≠ 已经是块间隔 interchangeable：** 官方把能指 post-commit 等待和已经是块间隔分开。
- **看见标成非确定 not already must-det ≠ 已经像 app_hash 那样必须确定 interchangeable：** 官方把标成非确定和已经像 app_hash 那样必须确定分开；432 finrespend vs params bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待 | 不是已经是本地 timeout_commit | 不是 post-commit 等待已经标成非确定性（52） |
| 看见能指 post-commit 等待 | 不是已经是块间隔 | 不是 ConsensusParams.block 限制块大小和块间隔那种已经是块间隔 |
| 看见标成非确定 | 不是已经像 app_hash 那样必须确定 | 不是 consensus_param_updates 就已经在块 H 生效（1073） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse.next_block_delay not already timeout-commit / not already block-interval / not already must-det 正式三事（432 余量），必须分开是不是已经是本地 timeout_commit、是不是已经是块间隔、是不是已经像 app_hash 那样必须确定。可以跳过「看见回了 Finalize 回包末栏就已经在块 H 生效」。不要另写怎样写 Finalize 回包末栏。432 finrespend vs params bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay。
- Finalize 回包末栏 bundled。那是不变量 432。
- post-commit 等待已经标成非确定性。那是不变量 52。
- ConsensusParams.block 限制块大小和块间隔那种已经是块间隔。那是相邻 ConsensusParams 页，不是本页。
