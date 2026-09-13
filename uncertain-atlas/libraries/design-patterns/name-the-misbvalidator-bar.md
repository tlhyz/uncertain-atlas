# 模式：把 Misbehavior.validator 栏正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**例**：[Misbehavior.validator 是过错验证者 ≠ 已经 slashed](../../tracks/implementation/worked-example-misbvalidator-vs-voteinfo.md)。

## 三个名字

1. **Misbehavior.validator 是过错验证者不是已经 slashed / 已经罚没：** 看见 offending validator 不是已经定了奖惩。
2. **Misbehavior.validator 只是 address+power 的 Validator 结构不是已经 VoteInfo.validator 那种按到场定奖惩：** 看见 Misbehavior 里的 Validator 不是已经 CommitInfo votes 里那份 interchangeable。
3. **Misbehavior.validator 不是已经 ValidatorUpdate 那种已经改了集合：** 看见过错验证者不是已经带了公钥。

## 为什么要分开叫

官方把 Misbehavior 里 `validator` 栏写成三个名字。把它们叫成一个「看见 Misbehavior 里填了 validator 就已经 slashed」，会把 offending validator、VoteInfo.validator 按到场定奖惩、ValidatorUpdate 改集合一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior 里填了 validator 就已经罚没」，先数清问的是 Misbehavior.validator 是不是已经 slashed、Misbehavior.validator 是不是已经 VoteInfo.validator 那种按到场定奖惩，还是 Misbehavior.validator 是不是已经 ValidatorUpdate，再决定要不要同一次发布。
