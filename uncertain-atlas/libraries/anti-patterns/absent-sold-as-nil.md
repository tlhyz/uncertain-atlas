# 反模式：absent-sold-as-nil

**层次**：实现 / 票标志枚举。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) BlockIDFlag / CommitSig / ExtendedCommitSig。  
**例**：[BlockIDFlag 是这份签对着哪个 BlockID ≠ 已经投过](../../tracks/implementation/worked-example-blockidflag-vs-vote.md)。

## 病症

把 `ABSENT`（票没收到）当成投了 nil，或把 `UNKNOWN`（官方注明 indicates an error condition）与 `ABSENT` 归成一类当「没投票」，或把「有 `BlockIDFlag`」写成「这个人参与了共识 / 已经计进 +2/3」，或忽略 `ExtendedCommitSig` 的条件校验（标志不是 `COMMIT` 时 `Extension` / `NonRpExtension` 必须为 0、两个签名必须为 0）。

## 为什么错

官方给枚举的注释把三件事分开了：`ABSENT` = the vote was not received；`COMMIT` = voted for the block that received the majority；`NIL` = voted for nil；而 `UNKNOWN = 0` = **indicates an error condition**。把「没收到」和「错误」都当「没投票」，到场统计就会把错误状态洗成正常缺席。另外 `ExtendedCommitSig` 的字段非空与否**取决于标志是不是 `COMMIT`**，不是无条件可填。

## 正确写法

分开三句：BlockIDFlag 是这份签对着哪个 BlockID 不是已经投过；`ABSENT` 是票没收到不是已经投了 nil；`UNKNOWN` 是错误状态不是另一种缺席。实现按标志做条件校验。

## 边界

不是 [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md)（那是 VoteInfo 能按到场定奖惩就已经罚没，不变量 365），不是 [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md)（那是 ExtendedVoteInfo 从本进程抽出，不变量 425），不是 [signedmsgtype-sold-as-verified](signedmsgtype-sold-as-verified.md)（那是枚举值就已经验过域分离，不变量 441），不是 [lastcommit-sold-as-this-block](lastcommit-sold-as-this-block.md)（那是本头 LastCommit 不是本高已 +2/3，不变量 148）。

## 本页不抄

- 怎样编 `BlockIDFlag`、怎样重建票集、怎样算到场。
- 怎样写利用步骤。
