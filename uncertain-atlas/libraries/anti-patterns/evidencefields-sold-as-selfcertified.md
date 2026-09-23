# 反模式：evidencefields-sold-as-selfcertified

**层次**：实现 / 证据字段可信性。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) DuplicateVoteEvidence / LightClientAttackEvidence。  
**例**：[证据里有 TotalVotingPower ≠ 这些数已经自证](../../tracks/implementation/worked-example-evidencefields-vs-selfcertified.md)。

## 病症

把证据里填了 `TotalVotingPower` / `ValidatorPower` 写成这些数已经自带权威、已经能罚，或写成这份证据能独立验证、不需要对照本节点自己那份链状态，或写成证据里的 `Timestamp` 已经自带、已经能自己定。

## 为什么错

规范把这三个字段（`DuplicateVoteEvidence` 的 `TotalVotingPower` / `ValidatorPower` / `Timestamp`，以及 `LightClientAttackEvidence` 的同类字段）的校验都写成**必须与节点自己那份数据相等**（Must be equal to nodes own copy of the data）。也就是说：证据里的数字是**被对照对象**，不是**权威来源**。校验要查本节点自己那份，不是从证据内容里推。

## 正确写法

分开三句：证据里有 TotalVotingPower / ValidatorPower 不是这些数已经自证；要求与本节点自己那份数据相等不是已经能独立验证；Timestamp 是过错那块的凭证时间不是已经由证据自带。

## 边界

不是 [two-votes-sold-as-slash](two-votes-sold-as-slash.md)（那是双签证据形状成立就已经罚没，不变量 21），不是 [evidence-default-sold-as-unbonding](evidence-default-sold-as-unbonding.md)（那是默认证据窗不盖住解绑，不变量 46），不是 [inflight-sold-as-evidence-id](inflight-sold-as-evidence-id.md)（那是证据身份含尚未最终的本地视角字段，不变量 64），不是 [verified-sold-as-evidence](verified-sold-as-evidence.md)（那是收下冲突头不是已经能交证据，不变量 66）。

## 本页不抄

- 怎样构造证据、怎样算投票权、怎样挑时间戳。
- 怎样写利用步骤。
