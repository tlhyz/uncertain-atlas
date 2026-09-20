# 例：看见 VoteInfo 与 ExtendedVoteInfo Usage 都写 allowing for rewards based on validator availability 不是已经奖罚完；看见 VoteInfo 通常从拟议块或已决块抽出不是已经从本进程抽出；看见 ExtendedVoteInfo 从本进程 CometBFT 数据结构抽出不是已经 typically extracted from proposed or decided block

**层次**：实现 / VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo Usage / ExtendedVoteInfo Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VoteInfo 与 ExtendedVoteInfo Usage 都写 allowing for rewards based on validator availability 不是已经奖罚完 / VoteInfo 通常从拟议块或已决块抽出不是已经从本进程抽出 / ExtendedVoteInfo 从本进程 CometBFT 数据结构抽出不是已经 typically extracted from proposed or decided block」，不是 VoteInfo 能按到场定奖惩就已经罚没，也不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出。不要另写怎样写 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事。

## 官方三件事

规范把 VoteInfo 与 ExtendedVoteInfo Usage 里同一句 availability、两条不同抽取路径写成三件独立的实现事，不是「看见 block_id_flag 就已经奖罚完、已经从块里抽出、Prepare 和 Process 是同一路」一件事：

1. **看见 VoteInfo 与 ExtendedVoteInfo Usage 都写 allowing for rewards based on validator availability / 看见同一句 不是已经奖罚完，也不是已经交差。**  
   官方写：Indicates whether a validator signed the last block, allowing for rewards based on validator availability. VoteInfo 和 ExtendedVoteInfo 都写这句。看见能按到场定奖惩，不是已经奖罚完。看见有 `block_id_flag`，不是已经交差。看见 Prepare 里也有 availability 信息，不是已经 Finalize 里算完奖惩。
2. **看见 VoteInfo Usage 写 This information is typically extracted from a proposed or decided block / 看见 typically extracted 不是已经从本进程 CometBFT 数据结构抽出，也不是已经是 Prepare 里的 ExtendedVoteInfo。**  
   官方写：This information is typically extracted from a proposed or decided block. 看见从拟议块或已决块抽出，不是已经从本进程 CometBFT 数据结构抽出。看见 Process / Finalize 里的 `CommitInfo`，不是已经是 Prepare 里的 `ExtendedCommitInfo`。看见 typically，不是已经一定从本进程 local 结构来。
3. **看见 ExtendedVoteInfo Usage 写 This information is extracted from CometBFT's data structures in the local process / 看见 extracted from local process 不是已经 typically extracted from proposed or decided block，也不是已经 Process/Finalize 里的 CommitInfo 同一路。**  
   官方写：This information is extracted from CometBFT's data structures in the local process. 看见从本进程抽出，不是已经 typically extracted from proposed or decided block。看见 Prepare 里的 `ExtendedVoteInfo`，不是已经 Process 里的 `VoteInfo` 同一路。看见 local process，不是已经从拟议块或已决块抽出。

怎样写 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事是规范里的做法，本页不抄。VoteInfo 能按到场定奖惩就已经罚没是不变量 365，ExtendedVoteInfo 从本进程抽出就已经从块里抽出是不变量 369，本页不抄。

## 官方为什么这样拆

- **availability 同句 ≠ 已经奖罚完 / 已经交差：** 官方把能定奖惩和已经算完分开。
- **VoteInfo typically from block ≠ ExtendedVoteInfo from local process：** 官方把 Process/Finalize 路径和 Prepare 路径分开。
- **两条 Usage 首句相同 ≠ 抽取异路可互换：** 官方把同一句 availability 和不同抽取路径分开写。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| availability 同句 | 不是已经奖罚完 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| VoteInfo typically from block | 不是已经从本进程抽出 | 不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| ExtendedVoteInfo from local process | 不是已经 typically from block | 不是 ExtendedVoteInfo.block_id_flag 表栏就已经罚没（425） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 block_id_flag 就已经奖罚完、Prepare 和 Process 是同一路、已经从块里抽出」，必须分开 VoteInfo 与 ExtendedVoteInfo Usage 都写 allowing for rewards based on validator availability 是不是已经奖罚完 / 已经交差、VoteInfo 通常从拟议块或已决块抽出是不是已经从本进程抽出 / 已经是 Prepare 里的 ExtendedVoteInfo、ExtendedVoteInfo 从本进程 CometBFT 数据结构抽出是不是已经 typically extracted from proposed or decided block / 已经是 Process/Finalize 里的 CommitInfo 同一路。可以跳过「看见 block_id_flag 就已经奖罚完」。442 VoteInfo ExtendedVoteInfo availability same-sentence extract-paths bundled unbundling 完成（1374 item 1 / 1375 item 2 / 1376 item 3）；精读 [`worked-example-viaext-notrew-vs-bundled.md`](worked-example-viaext-notrew-vs-bundled.md)（不变量 1374 item 1）、[`worked-example-viaext-notblk-vs-bundled.md`](worked-example-viaext-notblk-vs-bundled.md)（不变量 1375 item 2）、[`worked-example-viaext-notloc-vs-bundled.md`](worked-example-viaext-notloc-vs-bundled.md)（不变量 1376 item 3）。不要另写怎样写 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事。

## 本页不抄

- 怎样写 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事。
- VoteInfo 能按到场定奖惩、从拟议块或已决块抽出、按投票权降序排。那是不变量 365。
- ExtendedVoteInfo 从本进程 CometBFT 数据结构抽出、extension_signature 已由引擎验过。那是不变量 369。
- ExtendedVoteInfo.block_id_flag 表栏就已经罚没。那是不变量 425。
