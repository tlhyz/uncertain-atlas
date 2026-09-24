# 模式：把 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事（359 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[同一套字段 not already ran-process ≠ bundled（359）](../../tracks/implementation/worked-example-prepfields-notprocess-vs-bundled.md)。

## 三个名字

1. **字段名对得上 不是 already ran-process：** 看见字段名对得上 / `txs` / `misbehavior` / `height` / `time` / `next_validators_hash` / `proposer_address` 和 Process / Finalize 同一套 / 同一套字段，不是已经跑过 Process interchangeable / 已经 ran-process interchangeable / 已经叫过 Process 交差 interchangeable，不是 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable。

2. **同一套 不是 already finalize：** 看见同一套 / 和 Process / Finalize 同一套 / 字段名对得上同一套，不是已经 Finalize interchangeable / 已经 finalize interchangeable / 已经 Finalize 交差 interchangeable，不是 351 processalso interchangeable / 831 prepfields-notthissigned interchangeable。

3. **请求在 不是 already settled：** 看见请求在 / Prepare 请求在 / 同一套字段进了请求，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 832 prepfields-nothash interchangeable / 33 fourgates interchangeable。

官方把字段名对得上、不是已经 Finalize、不是已经交差写成三个名字。把它们叫成一个「看见字段名对得上就已经跑过 Process interchangeable / 就已经 Finalize interchangeable / 就已经交差 interchangeable」，会把 not already ran-process、not already finalize、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事（359 余量），先数清问的是字段名对得上 是不是 already ran-process / 359 / preparefields-sold-as-same，是不是同一套 是不是 already finalize，还是请求在 是不是 already settled，再决定要不要同一次发布。359 prepare-fields vs same bundled unbundling 在本页 item 1 启动。
