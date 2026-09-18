# 例：看见 ExtendedVoteInfo.block_id_flag is not already slashed interchangeable / not already voteinfo-flag interchangeable / not already settled interchangeable

**层次**：实现 / ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事（425 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事（425 余量）/ not 1053 extvirc-notflag interchangeable / not 425 extvirest-vs-voteinfo bundled interchangeable」，不是 ExtendedVoteInfo 表余栏 bundled（425），也不是 VoteInfo 能按到场定奖惩就已经罚没（365），也不是 PrepareProposalRequest.misbehavior 就已经定奖惩（424）。不要另写怎样写 ExtendedVoteInfo 表余栏。

## 官方三件事

1. **看见 ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票 / 看见填了 block_id_flag 这份栏 is not already 已经罚没 interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1053 extvirc-notflag interchangeable / 1052 extvirc-notkey interchangeable / 425 extvirest item 1 validator interchangeable，也不是已经 ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事 bundled（425 item 2 余量） interchangeable / 425 extvirest item 2 interchangeable。**  
   官方写：block_id_flag 标明这个验证者投了上一块、投了 nil、还是票没收到。看见填了 block_id_flag，不是已经 VoteInfo 标明上一块有没有签、能按到场定奖惩那种已经罚没 interchangeable——本页从 425 item 2 侧钉 not already slashed 单句。425 extvirest vs voteinfo bundled unbundling 在本页 item 2 续。

2. **看见能指没收到 / 看见填了 block_id_flag / 这份栏 is not already 已经是 VoteInfo 的 block_id_flag interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1053 extvirc-notflag interchangeable / 425 extvirest item 3 non_rp_sig interchangeable / 1054 extvirc-notgive interchangeable，也不是已经 VoteInfo 能按到场定奖惩就已经罚没 interchangeable / 365 voteinfo interchangeable。**  
   官方把能指没收到和已经是 VoteInfo 的 block_id_flag 分开。看见能指没收到，不是已经是 VoteInfo 的 block_id_flag interchangeable。本页钉 not already voteinfo-flag 单句。

3. **看见能指 nil / 看见填了 block_id_flag / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1053 extvirc-notflag interchangeable / 1052 extvirc-notkey interchangeable，也不是已经 PrepareProposalRequest.misbehavior 就已经定奖惩 interchangeable / 424 preprestr interchangeable。**  
   官方把能指 nil 和已经交差分开。看见能指 nil，不是已经交差 interchangeable。425 extvirest vs voteinfo bundled unbundling 在本页 item 2 续。

怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo.block_id_flag not already slashed ≠ 已经罚没 interchangeable：** 官方把标明投了上一块、nil、还是没收到票和已经罚没分开。
- **看见能指没收到 not already voteinfo-flag ≠ 已经是 VoteInfo 的 block_id_flag interchangeable：** 官方把能指没收到和已经是 VoteInfo 的 block_id_flag 分开。
- **看见能指 nil not already settled ≠ 已经交差 interchangeable：** 官方把能指 nil 和已经交差分开；425 extvirest vs voteinfo bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票 | 不是已经罚没 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| 看见能指没收到 | 不是已经是 VoteInfo 的 block_id_flag | 不是 PrepareProposalRequest.misbehavior 就已经定奖惩（424） |
| 看见能指 nil | 不是已经交差 | 不是 non_rp_extension_signature 就已经把验过的签交给应用（1054） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事（425 余量），必须分开是不是已经罚没、是不是已经是 VoteInfo 的 block_id_flag、是不是已经交差。可以跳过「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥」。不要另写怎样写 ExtendedVoteInfo 表余栏。425 extvirest vs voteinfo bundled unbundling 在本页 item 2 续；续 [`worked-example-extvirc-notgive-vs-bundled.md`](worked-example-extvirc-notgive-vs-bundled.md)（不变量 1054 item 3）。

## 本页不抄

- 怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag。
- ExtendedVoteInfo 表余栏 bundled。那是不变量 425。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
- PrepareProposalRequest.misbehavior 就已经定奖惩。那是不变量 424。
