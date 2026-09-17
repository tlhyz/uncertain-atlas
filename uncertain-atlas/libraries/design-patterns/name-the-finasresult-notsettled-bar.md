# 模式：把 FinalizeBlock must provide values not already changed set / settled 正式三事（477 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[must provide 四列 not already changed set / settled ≠ bundled（477）](../../tracks/implementation/worked-example-finasresult-notsettled-vs-bundled.md)。

## 三个名字

1. **must provide 四列 not changed set / H+1 不是 finasresult bundled：** 看见必须回四列不是已经改了集合 interchangeable，不是 477 finasresult interchangeable / 471 fincparam interchangeable / 459 validator_updates interchangeable。
2. **must provide not settled 不是 finresp bundled：** 看见 must provide 不是已经 Finalize + Commit 交差 interchangeable，不是 363 finresp interchangeable / 478 finpersist interchangeable / 33 四门已经结算 interchangeable。
3. **must provide not finasresult bundled 不是 empty keep current：** 看见必须回四列不是已经 finasresult bundled interchangeable，不是 458 finempty interchangeable / 477 item 2 not candidate interchangeable / 460 fincand interchangeable。

## 为什么要分开叫

官方把 must provide values for app_hash / tx_results / validator_updates / consensus_param_updates 和 changed set / settled / finasresult bundled 写成三个名字。把它们叫成一个「看见 must provide 就已经改了集合 / 已经交差 / 已经 finasresult bundled interchangeable」，会把 not changed set / H+1、not settled、not finasresult bundled / not empty keep current 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values not already changed set / settled 正式三事（477 余量），先数清问的是 must provide 四列是不是 already changed validator set / H+1 effective、是不是 already Finalize + Commit 交差 / persist decision，还是 must provide 是不是 already finasresult bundled / empty keep current，再决定要不要同一次发布。
