# 模式：把 Commit Usage retain_height caution 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Use retain_height with caution ≠ retain_height 默认 0 就等于已经在剪](../../tracks/implementation/worked-example-commitretaincaution-vs-kept.md)。

## 三个名字

1. **Use retain_height with caution 不是 retain_height 默认 0 就等于已经在剪：** 看见 Methods Usage 侧 caution 语气，不是 default 0 retain all / blocks below may be removed interchangeable。
2. **all nodes remove historical blocks → permanently lost / no bootstrap unless state sync 不是已经能从创世再装：** 看见全网删历史的后果，不是还能从创世装或已经开了 state sync 就交差 interchangeable。
3. **Historical blocks required for auditing / replay / light client 不是 persist signal bundled interchangeable：** 看见 caution 段里的 other purposes，不是 persist signal 段里 Historical blocks bundled interchangeable。

## 为什么要分开叫

官方把 Commit Usage 里 Use `CommitResponse.retain_height` with caution!、If all nodes remove historical blocks …、Historical blocks may also be required … 和 retain_height 默认全留（366）、persist signal Historical blocks（481）、从创世再装（323）写成三个名字。把它们叫成一个「看见 caution 段落就已经在剪、已经 persist signal 交差、已经能从创世再装」，会把 caution 语气、全网后果、other purposes 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage retain_height caution，先数清问的是 Use retain_height with caution 是不是 retain_height 默认 0 就等于已经在剪、all nodes remove historical blocks 是不是已经能从创世再装 / 已经开了 state sync 就交差、Historical blocks required for auditing / replay / light client 是不是已经 persist signal bundled interchangeable，再决定要不要同一次发布。
