# 模式：把 Finalize 回包义务 must provide 四列 not already changed set / settled 正式三事（363 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Finalize must provide 四列 not changed set / settled ≠ bundled（363）](../../tracks/implementation/worked-example-finresp-notsettled-vs-bundled.md)。

## 三个名字

1. **must provide 四列 not changed set / H+1 不是 finresp bundled：** 看见必须回四列不是已经改了集合 interchangeable，不是 363 finresp interchangeable / 471 fincparam interchangeable / 458 finempty interchangeable / 594 not settled interchangeable。
2. **must provide not settled 不是 finresp bundled：** 看见 must provide 四列不是已经 Finalize + Commit 交差 interchangeable，不是 363 finresp interchangeable / 478 finpersist interchangeable / 600 notgates interchangeable / 33 四门已经结算 interchangeable。
3. **must provide not finresp bundled 不是 finasresult / 463：** 看见 must provide 四列不是已经 finresp bundled interchangeable，不是 477 finasresult interchangeable / 463 finreward interchangeable / 597 notmustprovide interchangeable / 460 fincand interchangeable。

## 为什么要分开叫

官方把 must provide 四列、changed set / settled、363 finresp bundled 三事 写成三个名字。把它们叫成一个「看见 must provide 四列 就已经改了集合 / 已经交差 / 已经 finresp bundled interchangeable」，会把 not changed set / H+1、not settled、not finresp bundled / not finasresult bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包义务 must provide 四列 not already changed set / settled 正式三事（363 余量），先数清问的是 must provide 四列是不是 already changed validator set / H+1 effective、是不是 already Finalize + Commit 交差 / persist decision，还是 must provide 是不是 already finresp bundled / finasresult bundled / 463 finreward，再决定要不要同一次发布。
