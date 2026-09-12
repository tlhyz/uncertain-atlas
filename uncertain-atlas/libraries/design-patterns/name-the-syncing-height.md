# 模式：把 Finalize 同步高度三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[syncing_to_height 同步或重放时是目标高、否则等于本高 ≠ 已经有完整历史](../../tracks/implementation/worked-example-syncingheight-vs-history.md)。

## 三个名字

1. **syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史：** 看见填了目标不是已经是快照重放。
2. **validator_updates 空则引擎保持当前集合不是已经没有集合：** 看见空着不是已经改了集合。
3. **Finalize 回包 events 标成非确定不是已经必须确定：** 看见回了事件不是已经交差。

## 为什么要分开叫

官方把 `syncing_to_height` 同步或重放时是目标高、否则等于本高、`validator_updates` 空则引擎保持当前集合、Finalize 回包 `events` 标成非确定写成三件事。把它们叫成一个「看见填了同步高度就已经有完整历史」，会把完整历史、空名单和必须确定一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了同步高度就已经有完整历史」，先数清问的是 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史、validator_updates 空则引擎保持当前集合不是已经没有集合，还是 Finalize 回包 events 标成非确定不是已经必须确定，再决定要不要同一次发布。
