# 模式：把 ExtendVote Usage application can choose 0-length extension 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage 0-length 句。  
**例**：[can choose 0-length ≠ bundled](../../tracks/implementation/worked-example-extusage-zerolen-vs-bundled.md)。

## 三个名字

1. **can choose 0-length 不是 won't call ExtendVote：** 看见应用可以选 0 长，不是 437 bundled interchangeable / 524 precommit nil won't call interchangeable / 509 must return non-empty interchangeable。
2. **still calls ExtendVote on non-nil 不是 ExtendVote Usage bundled：** 看见非 nil 仍会 call，不是 437 bundled interchangeable / 524 nil path won't call interchangeable / 361 +2/3 prevote nil ExtendVote interchangeable。
3. **choosing empty not skip Verify 不是 skip Verify：** 看见选了空不是 skip Verify，不是 437 bundled interchangeable / 521 Verify empty still calls interchangeable / 514 0-length invalid interchangeable。

## 为什么要分开叫

官方把 can choose 0-length、still calls ExtendVote on non-nil、choosing empty not skip Verify、ExtendVote Usage bundled（437）、precommit nil won't call（524）、empty extension still calls Verify（521）写成三个名字。把它们叫成一个「看见能空 就已经不会叫 ExtendVote interchangeable、已经跳过 Verify interchangeable」，会把可选 0 长、非 nil 仍会 call、选空不是 skip Verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage application can choose 0-length extension 正式三事，先数清问的是 can choose 0-length 是不是 won't call ExtendVote、still calls on non-nil 是不是 precommit nil won't call、choosing empty 是不是 skip Verify，再决定要不要同一次发布。
