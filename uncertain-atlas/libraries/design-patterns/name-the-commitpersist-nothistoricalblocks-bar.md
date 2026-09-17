# 模式：把 Historical blocks required for auditing replay light client not retain_height defaults to 0 retain all / not blocks below height may be removed / not full history in consensus when joined 正式三事（481 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Historical blocks required for auditing replay light client not retain_height defaults to 0 retain all ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-nothistoricalblocks-vs-bundled.md)。

## 三个名字

1. **Historical blocks required 不是 retain_height defaults to 0 retain all：** 看见 Methods Usage 侧 auditing / replay / light client，不是已经 retain_height defaults to 0 retain all interchangeable / 已经 retain_height 默认 0 全留 interchangeable，不是 366 retain-height bundled interchangeable / 677 commitretaincaution-notdefaultzero interchangeable / 335 finpersist interchangeable。

2. **may also be required 不是 blocks below height may be removed：** 看见 Historical blocks may also be required，不是已经 blocks below this height may be removed interchangeable / 已经能剪就等于已经没有历史 interchangeable / 已经 non-zero retain_height 就等于已经在剪 interchangeable，不是 366 retain bundled item 2 interchangeable / 678 commitretaincaution-notbootstrap interchangeable。

3. **other purposes 不是 full history in consensus when joined：** 看见 other purposes / auditing / replay / light client，不是已经切进共识就已经有完整历史 interchangeable / 已经装完切进共识 interchangeable / 已经能从创世再装 interchangeable，不是 323 full-history interchangeable / 38 genesis-replay interchangeable / 681 commitpersist-notendofcall interchangeable。

官方把 Commit Usage Historical blocks may also be required 单句、retain_height defaults to 0 retain all（366）、blocks below height may be removed（366 item 2）、full history in consensus when joined（323）写成三个名字。把它们叫成一个「看见 Historical blocks required 就已经 retain_height 默认 0 全留 interchangeable / 就已经能剪就等于已经没有历史 interchangeable / 就已经切进共识就已经有完整历史 interchangeable」，会把 not retain_height defaults to 0 retain all、not blocks below height may be removed、not full history in consensus when joined 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Historical blocks required for auditing replay light client not retain_height defaults to 0 retain all / not blocks below height may be removed / not full history in consensus when joined 正式三事（481 余量），先数清问的是 Historical blocks required 是不是 retain_height defaults to 0 / 366 / 677，是不是 may also be required 是不是 blocks below may be removed / 366 item 2 / 678，还是 other purposes 是不是 full history in consensus when joined / 323 / 38 / 681，再决定要不要同一次发布。481 commitpersist vs finalize bundled unbundling 在本页 item 3 完成。
