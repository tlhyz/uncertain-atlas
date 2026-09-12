# 例：看见 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息不是已经定奖惩；看见 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址不是已经知道本头哈希；看见 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥

**层次**：实现 / ExtendVote 请求末栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.misbehavior 是拟议块里那些过错信息不是已经定奖惩 / ExtendVoteRequest.proposer_address 是造这份提案的验证者地址不是已经知道本头哈希 / VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥」，不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没，也不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希。不要另写怎样写 ExtendVote 请求末栏。

## 官方三件事

规范把 `ExtendVoteRequest.misbehavior` 是拟议块里那些过错信息、`proposer_address` 是造这份提案的验证者地址、`VerifyVoteExtensionRequest.validator_address` 是签了这份扩展的验证者地址写成三件独立的实现事，不是「看见填了 ExtendVote 请求末栏就已经定奖惩、已经知道本头哈希、已经带了公钥」一件事：

1. **看见 `ExtendVoteRequest.misbehavior` 是拟议块里那些过错信息 / 看见填了 misbehavior 不是已经定奖惩，也不是已经罚没。**  
   官方写：`misbehavior` 是拟议块里那些验证者过错信息。看见填了 misbehavior，不是已经 Finalize 可以用 `decided_last_commit` 和 `misbehavior` 定奖惩那种已经罚没。看见拟议块里有过错信息，不是已经交差。看见能指过错，不是已经定了奖惩。
2. **看见 `ExtendVoteRequest.proposer_address` 是造这份提案的验证者地址 / 看见填了 proposer_address 不是已经知道本头哈希，也不是已经交差。**  
   官方写：`proposer_address` 是造这份提案的验证者地址。看见填了 proposer_address，不是已经 Prepare 那种 `height` / `time` / `proposer_address` 对上拟议头就已经知道本头哈希。看见有造提案的人，不是已经字段名对上就已经跑过 Process。看见能指提议者，不是已经交差。
3. **看见 `VerifyVoteExtensionRequest.validator_address` 是签了这份扩展的验证者地址 / 看见填了 validator_address 不是已经带了公钥，也不是已经能验签。**  
   官方写：`validator_address` 是签了这份扩展的验证者地址。看见填了 validator_address，不是已经 `Validator` 用 address 认人那种已经带了公钥。看见能指签扩展的人，不是已经能验签。看见有地址，不是已经交差。

怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address 是规范里的做法，本页不抄。可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没是不变量 363，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.misbehavior 是拟议块里那些过错信息 ≠ 已经定奖惩：** 官方把拟议块里那些过错信息和已经定奖惩分开。
- **ExtendVoteRequest.proposer_address 是造这份提案的验证者地址 ≠ 已经知道本头哈希：** 官方把造这份提案的验证者地址和已经知道本头哈希分开。
- **VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 ≠ 已经带了公钥：** 官方把签了这份扩展的验证者地址和已经带了公钥分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.misbehavior 是拟议块里那些过错信息 | 不是已经定奖惩 | 不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363） |
| ExtendVoteRequest.proposer_address 是造这份提案的验证者地址 | 不是已经知道本头哈希 | 不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359） |
| VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 | 不是已经带了公钥 | 不是 Validator 用 address 认人就已经带了公钥（364） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求末栏就已经定奖惩、已经知道本头哈希、已经带了公钥」，必须分开 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息是不是已经定奖惩、ExtendVoteRequest.proposer_address 是造这份提案的验证者地址是不是已经知道本头哈希、VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址是不是已经带了公钥。可以跳过「看见填了 ExtendVote 请求末栏就已经定奖惩」。不要另写怎样写 ExtendVote 请求末栏。

## 本页不抄

- 怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address。
- 可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没。那是不变量 363。
- Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希。那是不变量 359。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
