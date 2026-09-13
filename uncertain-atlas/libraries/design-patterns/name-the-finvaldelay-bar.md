# 模式：把 FinalizeBlock validator_updates H+1/H+2/H+3 生效正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[H+1 只更新 Next ≠ 已经在 H+1 计票](../../tracks/implementation/worked-example-finvaldelay-vs-h2vote.md)。

## 三个名字

1. **H+1 只更新 NextValidatorsHash 不是已经在 H+1 计票：** 看见 Next 纳入更新不是已经 ValidatorsHash 已经更新。
2. **H+2 ValidatorsHash 才更新不是已经在 H+1 换人：** 看见 H+2 集合变更才生效不是已经 Next 更新了就已经计票。
3. **H+3 last_commit 才带新集合不是已经 proposed/decided_last_commit 就是新集合：** 看见三门 `*_last_commit` 带 altered validator set 不是已经 H+1/H+2 的 commit 栏就是新集合。

## 为什么要分开叫

官方把块 H 触发的 `validator_updates` 在 H+1、H+2、H+3 各改哪个对象写成三个名字。把它们叫成一个「看见 Finalize 回了 validator_updates 就已经在 H+1 换人」，会把 Next 承诺、ValidatorsHash 计票和 last_commit 延迟一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Next 更新了就已经计票」，先数清问的是 H+1 只更新 Next 是不是已经在 H+1 计票、H+2 ValidatorsHash 才生效是不是已经在 H+1 换人，还是 H+3 last_commit 才带新集合是不是已经 proposed/decided_last_commit 就是新集合，再决定要不要同一次发布。
