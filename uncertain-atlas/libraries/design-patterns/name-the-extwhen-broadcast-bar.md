# 模式：把 ExtendVote When broadcast Precommit 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7。  
**例**：[broadcast Precommit ≠ bundled](../../tracks/implementation/worked-example-extwhen-broadcast-vs-bundled.md)。

## 三个名字

1. **broadcasts Precommit 不是 construct Precommit bundled：** 看见 broadcasts the Precommit message，不是 512 constructs Precommit using both interchangeable。
2. **step 7 after step 6 不是 construct CanonicalVote / fill bundled：** 看见 step 7 after constructs Precommit，不是 511 construct CanonicalVote interchangeable / 510 fill interchangeable。
3. **broadcasts 不是 write into last_commit / Verify late extension：** 看见 broadcasts，不是 438 写进 last_commit interchangeable / Verify 过迟到扩展 interchangeable。

## 为什么要分开叫

官方把 broadcasts Precommit、step 7 顺序、broadcast 与 last_commit/Verify 边界、construct Precommit bundled（512）、ExtendVote When 正式流程 bundled（438）写成三个名字。把它们叫成一个「看见构造了 Precommit 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable、已经 ExtendVote 回了 extension 就已经交差 interchangeable」，会把 broadcast、顺序、后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事，先数清问的是 broadcasts Precommit 是不是 construct Precommit bundled interchangeable、step 7 after step 6 是不是 construct CanonicalVote interchangeable、broadcasts 是不是已经写进 last_commit interchangeable / 已经 Verify 过迟到扩展 interchangeable，再决定要不要同一次发布。
