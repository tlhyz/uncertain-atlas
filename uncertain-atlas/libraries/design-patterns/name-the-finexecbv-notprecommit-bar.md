# 模式：把 FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash 正式三事（466 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**例**：[FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash ≠ bundled（466）](../../tracks/implementation/worked-example-finexecbv-notprecommit-vs-bundled.md)。

## 三个名字

1. **executes block v not +2/3 precommit decided / ResultHash 不是 FinalizeBlock When Application executes block v bundled：** 看见 Application executes block _v_ / 应用回了 AppHash 和各笔输出 不是已经 +2/3 precommit decided / ResultHash interchangeable，不是 466 finexecbv interchangeable / 573 not persist interchangeable / 574 not cand interchangeable。
2. **executes block v not +2/3 precommit decided / ResultHash 不是 +2/3 precommit same id(v) already will Finalize bundled：** 看见 Application executes block _v_ 不是已经 +2/3 precommit same id(v) decided interchangeable，不是 362 +2/3 precommit interchangeable / 335 finpersist interchangeable / 361 ExtendVote when interchangeable。
3. **executes block v not +2/3 precommit decided / ResultHash 不是 finpersist / apphash vs this block：** 看见 ResultHash / 回了 AppHash 不是已经 committed / 本头 AppHash interchangeable，不是 335 finpersist interchangeable / 147 apphash vs this block interchangeable / 407 finfields interchangeable。

## 为什么要分开叫

官方把 Application executes block _v_、应用回了 AppHash 和各笔输出、引擎哈希进 ResultHash 写成三个名字。把它们叫成一个「看见 Application executes block _v_ 就已经 +2/3 precommit decided interchangeable / 已经 466 finexecbv bundled interchangeable / 已经 362 +2/3 precommit interchangeable」，会把 not +2/3 precommit decided / ResultHash、not 362 bundled、not finpersist / apphash vs this block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash 正式三事（466 余量），先数清问的是 executes block v 是不是 already +2/3 precommit decided / ResultHash、是不是 already +2/3 precommit same id(v) decided、是不是 already committed / 本头 AppHash，再决定要不要同一次发布。
