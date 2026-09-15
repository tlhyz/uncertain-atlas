# 模式：把 PrepareProposal When collect / synchronous / manipulate 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**例**：[collect / synchronous / manipulate ≠ bundled](../../tracks/implementation/worked-example-preparewhen-collect-vs-bundled.md)。

## 三个名字

1. **collect priority / create header 不是 raw proposal bundled：** 看见 When collects from mempool in order of priority，不是 503 Usage raw proposal interchangeable。
2. **synchronous Prepare call 不是能在返回后再改裁决：** 看见 blocks until Application returns，不是 354 Process 同步 interchangeable。
3. **can manipulate transactions 不是 Prepare 改列表 bundled：** 看见 leave/add/remove/modify/reorder，不是 355 改列表 consequences bundled interchangeable。

## 为什么要分开叫

官方把 collect priority、Prepare synchronous call、can manipulate transactions、raw proposal bundled（503）、Prepare 改列表 bundled（355）、validValue 跳过 Prepare（356）写成三个名字。把它们叫成一个「看见自己是提议者就已经 raw proposal bundled interchangeable、已经能在返回后再改裁决、已经 Prepare 改列表 bundled interchangeable」，会把 collect、synchronous、manipulate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事，先数清问的是 collect priority 是不是 raw proposal bundled interchangeable、Prepare synchronous call 是不是能在返回后再改裁决 interchangeable、can manipulate transactions 是不是 Prepare 改列表 bundled interchangeable，再决定要不要同一次发布。
