# 例：看见VoteInfo typically from block 不是已经从本进程抽出不是已经从本进程抽出；看见VoteInfo typically from block is not already extracted from local process不是已经是 Prepare ExtendedVoteInfo；看见VoteInfo typically from block 不是已经从本进程抽出不是已经一定从 local 结构来

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo Usage / ExtendedVoteInfo Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ViAvail VoteInfo typically from block not already local-process / not already Prepare ExtendedVoteInfo / not already 369-path 正式三事（442 余量）/ not 1375 viaext-notblk interchangeable / not 442 viusageavail-vs-extractpath bundled interchangeable」，不是 viusageavail vs extractpath bundled（442），也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369），也不是已经 Validator Usage 四门（449）。不要另写 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。

## 官方三件事

1. **看见VoteInfo typically from block 不是已经从本进程抽出 / 看见VoteInfo typically from block 不是已经从本进程抽出 这份对象 is not already 已经从本进程抽出 interchangeable，也不是已经 viusageavail vs extractpath bundled（442） interchangeable / 1375 viaext-notblk interchangeable / 1374 viaext-notrew interchangeable，也不是已经 ViAvail VoteInfo typically from block not already local-process / not already Prepare ExtendedVoteInfo / not already 369-path 正式三事 bundled（442 item 2 余量） interchangeable / 442 viaext item 2 interchangeable。**  
   官方把VoteInfo typically from block 不是已经从本进程抽出和已经从本进程抽出写成两件。看见VoteInfo typically from block 不是已经从本进程抽出，不是已经从本进程抽出。

2. **看见VoteInfo typically from block is not already extracted from local process / 看见VoteInfo typically from block 不是已经从本进程抽出 / 这份对象 is not already 已经是 Prepare ExtendedVoteInfo interchangeable，也不是已经 viusageavail vs extractpath bundled（442） interchangeable / 1375 viaext-notblk interchangeable / 1376 viaext-notloc interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable / 369 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable。**  
   官方把VoteInfo typically from block is not already extracted from local process和已经是 Prepare ExtendedVoteInfo写成两件。看见VoteInfo typically from block is not already extracted from local process，不是已经是 Prepare ExtendedVoteInfo。

3. **看见VoteInfo typically from block 不是已经从本进程抽出 / 看见VoteInfo typically from block is not already extracted from local process / 这份对象 is not already 已经一定从 local 结构来 interchangeable，也不是已经 viusageavail vs extractpath bundled（442） interchangeable / 1375 viaext-notblk interchangeable / 1374 viaext-notrew interchangeable，也不是已经 Validator Usage 四门 interchangeable / 449 Validator Usage 四门 interchangeable。**  
   官方把VoteInfo typically from block 不是已经从本进程抽出和已经一定从 local 结构来写成两件。看见VoteInfo typically from block 不是已经从本进程抽出，不是已经一定从 local 结构来。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。

## 官方为什么这样拆

- **typically from block 不是已经从本进程抽出 interchangeable：官方把 Process/Finalize 路径和 Prepare 路径分开。**
- **看见 CommitInfo 不是已经是 ExtendedCommitInfo。**
- **看见 typically 不是已经一定从 local 结构来。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经从本进程抽出 | 不是已经从本进程抽出 | 不是已经ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| 已经是 Prepare ExtendedVoteInfo | 不是已经是 Prepare ExtendedVoteInfo | 不是已经Validator Usage 四门（449） |
| 已经一定从 local 结构来 | 不是已经一定从 local 结构来 | 不是已经1374 viaext-notrew |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ViAvail VoteInfo typically from block not already local-process / not already Prepare ExtendedVoteInfo / not already 369-path 正式三事（442 余量），必须分开是不是已经从本进程抽出、是不是已经是 Prepare ExtendedVoteInfo、是不是已经一定从 local 结构来。可以跳过「看见 block_id_flag 就已经奖罚完」。不要另写 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。442 VoteInfo ExtendedVoteInfo availability same-sentence extract-paths bundled unbundling 在本页 item 2 续；续 [`worked-example-viaext-notloc-vs-bundled.md`](worked-example-viaext-notloc-vs-bundled.md)（不变量 1376 item 3）。

## 本页不抄

- 怎样写 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事。
- 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。
