# 模式：把 SignedMsgType 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) SignedMsgType / Vote / CanonicalVote。  
**例**：[Vote.Type 是这张票的类型 ≠ 已经按那条路径验过](../../tracks/implementation/worked-example-signedmsgtype-vs-verify.md)。

## 三个名字

1. **Vote.Type 是这张票的类型不是已经按那条路径验过：** 看见类型对不是已经验过。
2. **CanonicalVote.Type 是同一个枚举不是已经是同一个对象：** 后者字段顺序不同、含 ChainID，且不会出现在块里。
3. **枚举里写着 PREVOTE 不是已经证明签名只在这一步有效：** 看见枚举在不是已经验过域分离。

## 为什么要分开叫

官方把块里那张 `Vote` 的 `Type`、签名用的 `CanonicalVote` 的 `Type`、以及 `SignedMsgType` 枚举本身写成三件事。把它们叫成一个「看见票上写了 PREVOTE 就已经按 prevote 验过」，会把字段值和验签路径、两个不同序列化的对象、以及域分离是否成立一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见票上写了 PREVOTE 就已经按那条路径验过」，先数清问的是 Vote.Type 是这张票的类型不是已经按那条路径验过、CanonicalVote.Type 是同一个枚举不是已经是同一个对象，还是枚举里写着 PREVOTE 不是已经证明签名只在这一步有效，再决定要不要同一次发布。
