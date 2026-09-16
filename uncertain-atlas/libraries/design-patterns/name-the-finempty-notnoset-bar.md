# 模式：把 FinalizeBlock empty keep current not changed set / H+1 effective 正式三事（458 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[empty keep current not changed set ≠ bundled（458）](../../tracks/implementation/worked-example-finempty-notnoset-vs-bundled.md)。

## 三个名字

1. **empty keep current set not no set 不是 finempty bundled：** 看见 validator_updates 空着不是已经 empty means no validator set interchangeable，不是 458 finempty interchangeable / 597 notmustprovide interchangeable / 594 not settled interchangeable。
2. **empty keep current not changed set / H+1 不是 459 / 471 / 594：** 看见 may be empty 不是已经 changed validator set / H+1 换人 interchangeable，不是 459 validator_updates interchangeable / 471 fincparam interchangeable / 594 not settled interchangeable。
3. **empty validator_updates keep current not finempty bundled 不是 597 / 458 item 3：** 看见 keep current values 不是已经 finempty bundled interchangeable，不是 597 notmustprovide interchangeable / 596 notempty interchangeable / 458 item 3 consensus_param_updates interchangeable。

## 为什么要分开叫

官方把 empty validator_updates keep current、changed set / H+1 effective 和 finempty bundled 写成三个名字。把它们叫成一个「看见 validator_updates 空着 就已经没有集合 / 已经 keep current 就已经改了集合 interchangeable」，会把 not no set、not changed set / H+1 effective、not finempty bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty keep current not changed set / H+1 effective 正式三事（458 余量），先数清问的是 empty keep current set 是不是 already no validator set / 597 / 458 finempty、是不是 already changed set / H+1 effective / 459 / 471 / 594、还是 already finempty bundled / 596 / 458 item 3，再决定要不要同一次发布。
