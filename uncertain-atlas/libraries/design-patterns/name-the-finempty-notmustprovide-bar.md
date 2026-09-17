# 模式：把 FinalizeBlock empty keep current not no must provide obligation 正式三事（458 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[empty keep current not no must provide ≠ bundled（458）](../../tracks/implementation/worked-example-finempty-notmustprovide-vs-bundled.md)。

## 三个名字

1. **empty keep current not no must provide 不是 finasresult bundled：** 看见 may be empty / keep the current values 不是已经空着就没有 must provide 义务 interchangeable，不是 477 finasresult interchangeable / 596 notempty interchangeable / 363 finresp interchangeable。
2. **empty keep current not finempty bundled 不是 fincparam / validator_updates H+1：** 看见 empty keep current 不是已经 finempty bundled interchangeable，不是 471 fincparam interchangeable / 459 validator_updates interchangeable / 333 ConsensusParams 生效延迟 interchangeable。
3. **empty keep current not nil means do nothing 不是 319 partial update：** 看见 keep current values 不是已经 nil 就什么也不做 interchangeable，不是 319 partial update interchangeable / 432 回包末栏 bundled interchangeable / 335 finpersist interchangeable。

## 为什么要分开叫

官方把 must provide values、may be empty keep current values 和 nil / partial update 写成三个名字。把它们叫成一个「看见空着 就已经没有 must provide 义务 / 已经 keep current 就已经是同一句 bundled interchangeable」，会把 not no must provide obligation、not finempty bundled、not nil means do nothing 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty keep current not no must provide obligation 正式三事（458 余量），先数清问的是 empty keep current 是不是 already no must provide / 477 / 596、是不是 already finempty bundled / 471 / 459、还是 already nil means do nothing / 319 / 432，再决定要不要同一次发布。
