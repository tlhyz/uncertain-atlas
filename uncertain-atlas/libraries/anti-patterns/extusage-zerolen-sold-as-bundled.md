# 反模式：把 ExtendVote Usage application can choose 0-length extension 正式三事卖成 ExtendVote Usage bundled / 已经不会叫 ExtendVote / 已经跳过 Verify

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[can choose 0-length ≠ bundled](../../tracks/implementation/worked-example-extusage-zerolen-vs-bundled.md)。

## 卖法

- 「看见应用可以选 0 长扩展 / 看见能空 就已经不会叫 ExtendVote interchangeable / 已经必须填内容 interchangeable。」
- 「看见选了空 就已经 ExtendVote Usage bundled interchangeable / 已经 precommit nil 不会叫 interchangeable。」
- 「看见能空 就已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable。」

## 为什么错

官方把 can choose 0-length、still calls ExtendVote on non-nil Precommit、choosing empty not skip Verify 写成三件独立的实现事。把它们卖成 ExtendVote Usage bundled、已经不会叫 ExtendVote、已经跳过 Verify，会把可选 0 长、非 nil 仍会 call、选空不是 skip Verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage application can choose 0-length extension 正式三事，必须分开 can choose 0-length、still calls ExtendVote on non-nil、choosing empty not skip Verify 三个名字，不要把它们卖成 ExtendVote Usage bundled / 已经不会叫 ExtendVote / 已经跳过 Verify。

## 和相邻反模式

- [extusage-precommitnil-sold-as-bundled](extusage-precommitnil-sold-as-bundled.md) 是 precommit nil won't call 专用；本页是 0-length on non-nil 边界。
- [verifyusage-emptyext-sold-as-bundled](verifyusage-emptyext-sold-as-bundled.md) 是 Verify Usage 0 长仍会 call，不是本页 ExtendVote 侧可选 0 长边界。
- [extusage-sold-as-deterministic](extusage-sold-as-deterministic.md) 是 437 bundled 第三件事专用，不是本页 0-length 边界。
