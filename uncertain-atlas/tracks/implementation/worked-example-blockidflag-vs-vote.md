# 例：看见 BlockIDFlag 是这份签对着哪个 BlockID 不是已经投过；看见 ABSENT 是票没收到不是已经投了 nil；看见 UNKNOWN 是错误状态不是另一种缺席

**层次**：实现 / 票标志枚举。  
**分类**：事实（官方枚举）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) BlockIDFlag / CommitSig / ExtendedCommitSig。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「BlockIDFlag 是这份签对着哪个 BlockID 不是已经投过 / ABSENT 是票没收到不是已经投了 nil / UNKNOWN 是错误状态不是另一种缺席」，不是 VoteInfo 能按到场定奖惩就已经罚没，也不是 ExtendedVoteInfo 从本进程抽出就已经带了公钥。不要另写怎样编 BlockIDFlag。

## 官方三件事

规范把 `BlockIDFlag` 定义成「这份签名是**对着哪个 BlockID**」、并把 `ABSENT` 与 `UNKNOWN` 分别标成「票没收到」与「错误状态」，写成三件独立的事实，不是「看见标志就有票、看见 ABSENT 就是投了 nil、看见 UNKNOWN 就是另一种缺席」一件事：

1. **看见 `BlockIDFlag` / 看见标志 不是已经投过，也不是已经计过票。**  
   官方写：`BlockIDFlag` 表示这份签名是**对着哪个 BlockID** 的。看见标志在，不是这个人已经参与过。看见有值，不是已经计进 `+2/3`。看见能填，不是已经交差。
2. **看见 `BLOCK_ID_FLAG_ABSENT`（= 1）/ 看见「票没收到」不是已经投了 nil。**  
   官方在枚举里给 `ABSENT` 的注释是：the vote was not received。看见 `ABSENT`，不是这个人投了 nil。看见没收到，不是已经有反对票。把它当 nil 会计错到场。
3. **看见 `BLOCK_ID_FLAG_UNKNOWN`（= 0）/ 看见「错误状态」不是另一种缺席。**  
   官方给 `UNKNOWN` 的注释是：indicates an error condition。看见 0，不是另一种 `ABSENT`。看见默认值，不是没投票。看见未知，不是已经能按缺席处理。

**另记一条条件校验（属 `ExtendedCommitSig`，不属本枚举）：** 扩展签那一张表里，`Extension` 与 `NonRpExtension` 的校验写成「Length must be zero if BlockIDFlag is not `Commit`」，两个签名的校验写成「valid … if BlockIDFlag is `Commit`, else 0」。**字段能不能非空，取决于标志是不是 `COMMIT`** —— 这又是一层「看见字段在就已经填了」。

怎样编 `BlockIDFlag`、怎样重建票集、怎样算到场是规范里的做法，本页不抄。`VoteInfo` 能按到场定奖惩是不变量 365，本页不抄。`ExtendedVoteInfo` 从本进程抽出是不变量 369/425，本页不抄。

## 官方为什么这样拆

- **标志 ≠ 已经投过：** 它说的是这份签对着哪个 `BlockID`，不是「这个人参与了」。
- **`ABSENT` ≠ 投了 nil：** 一个是没收到，一个是明确反对；到场算法上不是一回事。
- **`UNKNOWN` ≠ 另一种缺席：** 官方把它写成**错误状态**，与正常的 `ABSENT` 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| BlockIDFlag 是这份签对着哪个 BlockID | 不是已经投过 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| ABSENT 是票没收到 | 不是已经投了 nil | 不是 ExtendedVoteInfo 从本进程抽出就已经带了公钥（425） |
| UNKNOWN 是错误状态 | 不是另一种缺席 | 不是 SignedMsgType 枚举值就已经验过域分离（441） |
| 本页不涉及 | — | 不是本头 LastCommit 就是本高已 +2/3（148） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见标志就有票、看见 ABSENT 就是缺席」，必须分开 BlockIDFlag 是这份签对着哪个 BlockID 是不是已经投过、ABSENT 是票没收到是不是已经投了 nil、UNKNOWN 是错误状态是不是另一种缺席。**实现里不得把 `UNKNOWN` 与 `ABSENT` 归成一类**；`ExtendedCommitSig` 的非空校验必须按标志是不是 `COMMIT` 来做。可以跳过「看见标志就有票」。不要另写怎样编 BlockIDFlag。

## 本页不抄

- 怎样编 `BlockIDFlag`、怎样重建票集、怎样算到场。
- `VoteInfo` 能按到场定奖惩。那是不变量 365。
- `ExtendedVoteInfo` 从本进程抽出、扩展签已由引擎验过。那是不变量 369 / 425。
- 本头 `LastCommit` 不是本高已 +2/3。那是不变量 148。
