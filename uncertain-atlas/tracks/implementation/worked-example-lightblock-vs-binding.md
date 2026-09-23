# 例：看见 LightBlock 有 SignedHeader 不是已经有头；看见两件都在不是已经是同一高；看见绑定的那一句是哈希相等不是已经非 nil 就够

**层次**：实现 / LightBlock 绑定。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) LightBlock / SignedHeader。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「LightBlock 有 SignedHeader 不是已经有头 / 两件都在不是已经是同一高 / 绑定的那一句是哈希相等不是已经非 nil 就够」，不是 ValidatorSet.Hash() 是叶子根就已经是整套集合，也不是三种轻客户端攻击就是穷尽。不要另写怎样构造 LightBlock。

## 官方三件事

规范把 `LightBlock` 是「把验证所需的两个数据结构合起来」、两件都不得为 nil、以及**两句由哈希相等**绑定（`SignedHeader.ValidatorsHash == ValidatorSet.Hash()`），写成三件独立的实现事，不是「看见两件都在就已经是同一高的一份可验对象」一件事：

1. **看见 `LightBlock` 有 `SignedHeader` / 看见有头 不是已经有能验的头，也不是已经有 `Commit`。**  
   官方写：`SignedHeader` 是头**加上**用来证明它的 `Commit`；`Header` 与 `Commit` 各自都不能为 nil 且各自要合规。看见有 `SignedHeader`，不是已经有 `Commit`。看见头在，不是已经验过。看见字段能填，不是已经交差。
2. **看见 `SignedHeader` 与 `ValidatorSet` 都在 / 看见都非 nil 不是已经是同一高，也不是已经能验。**  
   官方写：`LightBlock` 把验证所需的两个数据结构合起来（`SignedHeader` 与 `ValidatorSet`），两个都不得为 nil 并各自合规。看见两件都在，不是已经属于同一高度。看见非 nil，不是已经绑上。
3. **看见绑定写的是 `SignedHeader.ValidatorsHash == ValidatorSet.Hash()` / 看见哈希相等 不是已经非 nil 就够，也不是已经不需要两边都拿。**  
   官方写：`SignedHeader` 与 `ValidatorSet` 由**验证者集合的哈希**连接，即上式相等。看见两件都在，不是已经相等。看见相等是条件，不是已经能省掉一边。看见能拼，不是已经能验。

怎样构造 `LightBlock`、怎样算集合哈希、怎样切 `Header`/`Commit` 是规范里的做法，本页不抄。`ValidatorSet.Hash()` 是叶子根是不变量 444，本页不抄。三种轻客户端攻击就是穷尽见 [`../economic/worked-example-evidence.md`](../economic/worked-example-evidence.md)，本页不抄。

## 官方为什么这样拆

- **有 `SignedHeader` ≠ 已经有能验的头：** 官方把头与 `Commit` 分开，两者各自都要合规。
- **两件都非 nil ≠ 已经是同一高：** 官方把「都在」和「属于同一高度」分开。
- **绑定是哈希相等 ≠ 非 nil 就够：** 官方明写连接条件是 `SignedHeader.ValidatorsHash == ValidatorSet.Hash()`。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| LightBlock 有 SignedHeader | 不是已经有 Commit | 不是集合哈希对上就已经是整套集合（444） |
| 两件都非 nil | 不是已经是同一高 | 不是本头 LastCommit 就是本高已 +2/3（148） |
| 绑定是 ValidatorsHash == ValidatorSet.Hash() | 不是已经非 nil 就够 | 不是 H 的更新已经在 H+1 改 NextValidatorsHash（35） |
| 本页不涉及 | — | 不是三种攻击就是穷尽（见经济证据页） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见两件都在就已经是同一高的一份可验对象」，必须分开 LightBlock 有 SignedHeader 是不是已经有头、两件都在是不是已经是同一高、绑定的那一句是哈希相等是不是已经非 nil 就够。可以跳过「看见两件都在就已经是同一高的一份可验对象」。不要另写怎样构造 LightBlock。

## 本页不抄

- 怎样构造 `LightBlock`、怎样算集合哈希、怎样切 `Header`/`Commit`。
- `ValidatorSet.Hash()` 是叶子根不是已经是整套集合。那是不变量 444。
- 本头 `LastCommit` 不是本高已 +2/3。那是不变量 148。
- 集合更新的 H+1 / H+2 / H+3 延迟。那是不变量 35。
