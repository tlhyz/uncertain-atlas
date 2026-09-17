# 模式：把 Prepare 回包校验 no extra checks not already checked / not app-level replay / not pool dedup 正式三事（357 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[no ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notchecked-vs-bundled.md)。

## 三个名字

1. **no extra checks 不是已经验过重复：** 看见回了提案，不是已经验过重复 interchangeable / 716 prepvalid-notchecked interchangeable。
2. **看见回了提案 不是已经有应用级重放保护：** 看见能提，不是已经有重放保护 interchangeable。
3. **看见没有再验 不是池门去重 / Usage 末尾 no checks：** 看见不再查重复，不是已经 313 / 504 interchangeable。

官方把 Prepare 回包校验三条核心句拆成三个名字。把它们叫成一个「看见回了提案就已经验过重复」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 no extra checks 正式三事（357 余量），先数清问的是没有再验是不是已经验过重复、是不是已经有应用级重放保护、还是看见没有再验是不是 313 / 504，再决定要不要同一次发布。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。
