# 例：看见 ValidatorSet.Hash() 是叶子根不是已经含地址；看见叶子只编码 pub_key 与 voting_power 不是已经是整套集合；看见不含提议者优先不是已经不需要交叉核对

**层次**：实现 / ValidatorSet 哈希覆盖面。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) ValidatorSet。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ValidatorSet.Hash() 是叶子根不是已经含地址 / 叶子只编码 pub_key 与 voting_power 不是已经是整套集合 / 不含提议者优先不是已经不需要交叉核对」，不是状态同步装上的 State 必须含提议者选择字段，也不是 `votes` 按投票权降序排。不要另写怎样算 ValidatorSet 哈希。

## 官方三件事

规范把 `ValidatorSet.Hash()` 是 `SimpleValidator` 叶子的默克尔根、每片叶子只编码验证者的 `pub_key` 与 `voting_power`、以及**验证者地址与提议者优先不在这份哈希里**，写成三件独立的事实，不是「看见集合哈希对上就已经是同一套集合、已经含地址、已经不需要另核对」一件事：

1. **看见 `ValidatorSet.Hash()` 是叶子根 / 看见哈希对上 不是已经是整套集合，也不是已经含地址。**  
   官方写：`ValidatorSet.Hash()` 是 `SimpleValidator` 叶子的默克尔根。看见根对上，不是已经覆盖了集合的每一个字段。看见有哈希，不是已经能还原集合。
2. **看见每片叶子是 `pub_key` 与 `voting_power` 的 protobuf 编码 / 看见两样都在 不是已经是完整验证者。**  
   官方写：每片叶子是这个验证者 `pub_key` 与 `voting_power` 的 protobuf 编码。看见叶子里有权与钥，不是已经含了这个人的地址。看见两样，不是已经是 `Validator` 那个对象。
3. **看见地址与提议者优先不在哈希里 / 看见不含 不是已经不需要交叉核对，也不是已经不会认错人。**  
   官方写：**验证者地址与提议者优先不包含在这份哈希里**。看见哈希对上，不是已经含地址。看见哈希对上，不是已经含提议者优先。看见对上，不是已经不需要另拿一份去核对日程。

怎样算 `ValidatorSet.Hash()`、怎样编叶子、怎样种树是规范里的做法，本页不抄。状态同步装上的 State 必须含提议者选择字段是不变量 56，本页不抄。`votes` 按投票权降序排是不变量 365，本页不抄。

## 官方为什么这样拆

- **`ValidatorSet.Hash()` 是叶子根 ≠ 已经是整套集合：** 官方把「根的覆盖面」和「整套集合」分开。
- **叶子只编码 `pub_key` 与 `voting_power` ≠ 已经是完整验证者：** 官方把叶子内容与 `Validator` 对象分开。
- **不含地址与提议者优先 ≠ 已经不需要交叉核对：** 官方把这个缺口写明，正是不变量 56 那条事故的设计根源。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ValidatorSet.Hash() 是叶子根 | 不是已经是整套集合 | 不是状态同步 State 不含提议者选择字段就已经对齐（56） |
| 叶子只编码 pub_key 与 voting_power | 不是已经是完整验证者 | 不是 Validator 用 address 认人就已经带了公钥（364） |
| 不含地址与提议者优先 | 不是已经不需要交叉核对 | 不是 votes 按投票权降序排就已经进了块（365） |
| 本页不涉及 | — | 不是 ValidatorUpdate 就已经改了集合（35） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见集合哈希对上就已经是同一套验证者」，必须分开 ValidatorSet.Hash() 是叶子根是不是已经是整套集合、叶子只编码 pub_key 与 voting_power 是不是已经是完整验证者、不含地址与提议者优先是不是已经不需要交叉核对。可以跳过「看见集合哈希对上就已经是同一套验证者」。不要另写怎样算 ValidatorSet 哈希。

## 本页不抄

- 怎样算 `ValidatorSet.Hash()`、怎样编叶子、怎样种树。
- 状态同步 State 必须含提议者选择字段。那是不变量 56。
- `Validator` 用 address 认人不是已经带了公钥。那是不变量 364。
- `votes` 按投票权降序排。那是不变量 365。
