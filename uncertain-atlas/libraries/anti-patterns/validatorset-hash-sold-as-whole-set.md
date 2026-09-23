# 反模式：validatorset-hash-sold-as-whole-set

**层次**：实现 / ValidatorSet 哈希覆盖面。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) ValidatorSet。  
**例**：[ValidatorSet.Hash() 是叶子根 ≠ 已经是整套集合](../../tracks/implementation/worked-example-validatorset-hash-vs-whole-set.md)。

## 病症

把 `ValidatorSet.Hash()` 对上写成整套验证者集合已经一致（含地址、含提议者日程），或写成叶子里有权与公钥就等于拿到了完整 `Validator`，或写成因为集合哈希验过了所以不需要再交叉核对提议者选择。

## 为什么错

规范明写 `ValidatorSet.Hash()` 是 `SimpleValidator` 叶子的默克尔根，每片叶子只是该验证者 `pub_key` 与 `voting_power` 的 protobuf 编码，并且**验证者地址与提议者优先不包含在这份哈希里**。所以这份根证明的是「钥与权的配对表」，不是「整套集合对象」。地址不同、提议者优先不同的两套集合，可以有同一个根。

## 正确写法

分开三句：ValidatorSet.Hash() 是叶子根不是已经是整套集合；叶子只编码 pub_key 与 voting_power 不是已经是完整验证者；不含地址与提议者优先不是已经不需要交叉核对。

## 边界

不是 [appstate-sold-as-validated](appstate-sold-as-validated.md)（那是状态同步装上的 State 必须含提议者选择字段并交叉核对，不变量 56），不是 [validator-sold-as-update](validator-sold-as-update.md)（那是 `Validator` 用 address 认人不是已经带了公钥，不变量 364），不是 [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md)（那是 H 的更新不是已经在 H+1 计票，不变量 35），不是 `votes` 按投票权降序排（不变量 365）。

## 本页不抄

- 怎样算 `ValidatorSet.Hash()`、怎样编叶子、怎样种树。
- 怎样写利用步骤。
