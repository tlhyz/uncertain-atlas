# 模式：把 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**例**：[Proposal + all block parts ≠ 已经只有 hash](../../tracks/implementation/worked-example-finwhenparts-vs-partial.md)。

## 三个名字

1. **Proposal + all block parts 不是已经只有 hash：** 看见 Proposal message with block _v_ and all its block parts 不是已经 hash 栏对上 interchangeable。
2. **2f+1 precommit same id(v) 不是已经 +2/3 prevote ExtendVote：** 看见 Precommit from 2f+1 voting power precommitting same id(_v_) 不是已经 prevote 锁住 ExtendVote interchangeable。
3. **decides block v 不是已经到了这一高就会调 Finalize：** 看见 then decides block _v_ 不是已经 persist outputs / 已经交差 interchangeable。

## 为什么要分开叫

官方把 Proposal + parts、2f+1 precommit、decides block v 和只有 hash、prevote ExtendVote、到了这一高就会调 Finalize 写成三个名字。把它们叫成一个「看见 +2/3 precommit 就已经会调 Finalize」，会把收齐块片、Precommit 门槛、决定 _v_ 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 触发条件，先数清问的是 Proposal + all block parts 是不是已经只有 hash、2f+1 precommit 是不是已经 +2/3 prevote ExtendVote，还是 decides block v 是不是已经到了这一高就会调 Finalize，再决定要不要同一次发布。
