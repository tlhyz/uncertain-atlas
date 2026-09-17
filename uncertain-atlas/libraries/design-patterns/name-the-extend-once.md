# 模式：把一轮一份扩展三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**例**：[一轮最多一张 Precommit ≠ 已经能再签一张](../../tracks/implementation/worked-example-extend-once-vs-round.md)。

## 三个名字

1. **一轮最多一张 Precommit 不是已经能再签一张：** 看见到了 Precommit 步不是已经能再出一张。
2. **ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票：** 看见叫了 ExtendVote 不是已经在签 nil。
3. **一轮只能交出一份扩展不是已经是每一高度一份：** 看见交了一份不是这一高度已经只能有一份。

## 为什么要分开叫

官方把一轮最多一张 Precommit、何时才叫 ExtendVote、一轮只能交出一份扩展写成三件事。把它们叫成一个「看见到了 Precommit 就已经能再签一张」，会把拒收整张预提交、同一块同一份扩展和 Req 6 必须 Accept 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了 Precommit 就已经能再签一张」，先数清问的是一轮最多一张 Precommit 不是已经能再签一张、ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票，还是一轮只能交出一份扩展不是已经是每一高度一份，再决定要不要同一次发布。
