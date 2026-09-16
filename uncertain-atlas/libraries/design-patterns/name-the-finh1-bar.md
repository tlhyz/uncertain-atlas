# 模式：把 FinalizeBlock When starts consensus for h+1 round 0 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 11。  
**例**：[starts consensus for height h+1 ≠ 已经交差](../../tracks/implementation/worked-example-finh1-vs-round0.md)。

## 三个名字

1. **starts consensus for height h+1 不是已经交差：** 看见 When 第 11 步开下一高，不是已经 Finalize + Commit 交差。
2. **round 0 不是已经继续同一 round：** 看见 round 0，不是已经 next_block_delay / timeout_commit interchangeable。
3. **When 第 11 步 after unlock 不是已经 unlock mempool：** 看见开下一高，不是已经 step 10 unlock interchangeable。

## 为什么要分开叫

官方把 When 第 11 步 _p_ starts consensus for height _h+1_, round 0 写成三个名字。把它们叫成一个「看见开下一高了就已经交差 / 已经是 round 0 / 已经 unlock 之后」，会把 starts h+1、round 0 vs delay、step 11 vs step 10 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见开下一高就已经交差」，先数清问的是 starts consensus for height h+1 是不是已经交差 / 已经 persist decision，还是 round 0 是不是已经继续同一 round / 已经 next_block_delay / timeout_commit，还是 When 第 11 步 after unlock 是不是已经 unlocks the mempool / 已经 Finalize 之后 bundled / 已经 When trigger 2f+1 precommit，再决定要不要同一次发布。
