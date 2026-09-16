# 反模式：把 FinalizeBlock When starts consensus for h+1 round 0 正式三事说成已经开下一高交差

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[starts consensus for height h+1 ≠ 已经交差](../../tracks/implementation/worked-example-finh1-vs-round0.md)。

## 错在哪里

把 starts consensus for height h+1 写成已经交差，或已经四门已经结算，或已经 persist decision interchangeable；把 round 0 写成已经继续同一 round，或已经 next_block_delay 槽位，或已经 timeout_commit interchangeable；把 When 第 11 步 after unlock 写成已经 unlocks the mempool，或已经 Finalize 之后 bundled recheck+unlock+h+1，或已经 When trigger 2f+1 precommit interchangeable，或已经和 592 / 403 / 589 / 480 / 479 / 478 / 33 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When starts consensus for h+1 round 0 正式三事，必须分开 starts consensus for height h+1、round 0、When 第 11 步 after unlock 三件事，不要和 592 / 403 / 589 / 480 / 479 / 478 / 33 糊成一句。
