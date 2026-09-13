# 反模式：把 FinalizeBlock validator_updates H+1/H+2/H+3 生效正式三事说成已经在 H+1 换人

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[H+1 只更新 Next ≠ 已经在 H+1 计票](../../tracks/implementation/worked-example-finvaldelay-vs-h2vote.md)。

## 错在哪里

把 Height H+1: NextValidatorsHash includes the new validator_updates value 写成已经在 H+1 按新集合计票，或已经 ValidatorsHash 已经更新；把 Height H+2: validator set change takes effect and ValidatorsHash is updated 写成已经在 H+1 换人，或已经 Next 更新了就已经计票；把 Height H+3: *_last_commit fields now include the altered validator set 写成已经 proposed_last_commit / decided_last_commit 就是新集合，或已经和 35 / 431 / 333 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock validator_updates H+1/H+2/H+3 生效正式三事，必须分开 H+1 只更新 Next、H+2 ValidatorsHash 才生效、H+3 last_commit 才带新集合三件事，不要和 35 / 431 / 333 / 458 糊成一句。
