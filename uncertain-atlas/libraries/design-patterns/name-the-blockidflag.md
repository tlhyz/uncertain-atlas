# 模式：把票标志枚举三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方枚举）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) BlockIDFlag / CommitSig / ExtendedCommitSig。  
**例**：[BlockIDFlag 是这份签对着哪个 BlockID ≠ 已经投过](../../tracks/implementation/worked-example-blockidflag-vs-vote.md)。

## 三个名字

1. **BlockIDFlag 是这份签对着哪个 BlockID 不是已经投过：** 它说的是这份签名对着哪个 `BlockID`。
2. **`ABSENT`（= 1）是「票没收到」不是投了 nil：** 没收到与明确反对不是一回事。
3. **`UNKNOWN`（= 0）是「错误状态」不是另一种缺席：** 官方把它与正常的 `ABSENT` 分开。

**另记一层（`ExtendedCommitSig`）：** `Extension` / `NonRpExtension` 的校验是「BlockIDFlag 不是 `Commit` 时必须为 0」，两个签名则是「是 `Commit` 时有效、否则为 0」。**字段能不能非空取决于标志**。

## 为什么要分开叫

官方把「签对着哪个 BlockID」「没收到」「错误」写成三个不同的枚举值。把它们叫成一个「看见标志就有票 / 看见 ABSENT 就是缺席」，会把到场统计做错 —— `UNKNOWN` 是错误状态，不该和 `ABSENT` 一起当「没投票」；而 `ExtendedCommitSig` 的字段非空与否又依赖标志。三层不能糊。

## 产品

**建议（产品，不是事实）**：实现里**不得把 `UNKNOWN` 与 `ABSENT` 归成一类**；`ExtendedCommitSig` 的非空校验必须按标志是不是 `COMMIT` 来做。产品文案若说「按到场计了奖」，先数清问的是 BlockIDFlag 是这份签对着哪个 BlockID 不是已经投过、ABSENT 是票没收到不是已经投了 nil，还是 UNKNOWN 是错误状态不是另一种缺席。
