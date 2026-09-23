# 模式：把证据字段可信性三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) DuplicateVoteEvidence / LightClientAttackEvidence。  
**例**：[证据里有 TotalVotingPower ≠ 这些数已经自证](../../tracks/implementation/worked-example-evidencefields-vs-selfcertified.md)。

## 三个名字

1. **证据里有 TotalVotingPower / ValidatorPower 不是这些数已经自证：** 字段在不是值可信。
2. **要求「与本节点自己那份数据相等」不是已经能独立验证：** 校验钉在本地状态上。
3. **Timestamp 是过错那块的凭证时间不是已经由证据自带：** 同样列入「与自己那份相等」。

## 为什么要分开叫

官方把这三个字段的校验都写成**必须与节点自己那份数据相等**（Must be equal to nodes own copy of the data）。把它们叫成一个「看见证据里填了权就已经是证据自带权威」，会把「字段存在」「值可信」「不需要本地状态」三层一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见证据里有这些数就已经是证据自带权威」，先数清问的是证据里有 TotalVotingPower / ValidatorPower 不是这些数已经自证、要求与本节点自己那份数据相等不是已经能独立验证，还是 Timestamp 是过错那块的凭证时间不是已经由证据自带，再决定要不要同一次发布。
