# 模式：把 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事（351 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[Process 也会在提议者那边叫 not already skip-process ≠ bundled（351）](../../tracks/implementation/worked-example-process-notskip-vs-bundled.md)。

## 三个名字

1. **Process 也会在提议者那边叫 不是 already skip-process：** 看见 `ProcessProposal` 也会在这一轮的提议者那边叫 / 自己刚 Prepare 过 / 自己刚回了 Prepare，不是已经不用再 Process interchangeable / 已经 skip-process interchangeable / 已经跳过 Process 交差 interchangeable，不是 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable。

2. **是提议者 不是 already settled：** 看见是提议者 / 这一轮是自己提议 / 提议者身份，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 33 fourgates interchangeable / 347 req3coherence interchangeable。

3. **列表自己编的 不是 already already-processed：** 看见列表自己编的 / txs 自己刚回 / 自己编的列表，不是已经过了 Process interchangeable / 已经 already-processed interchangeable / 已经过 Process 交差 interchangeable，不是 807 process-notguaranteed interchangeable / 808 process-notalways interchangeable。

官方把 Process 也会在提议者那边叫、不是已经交差、不是已经过了 Process 写成三个名字。把它们叫成一个「看见自己刚 Prepare 过就已经不用再 Process interchangeable / 就已经交差 interchangeable / 就已经过了 Process interchangeable」，会把 not already skip-process、not already settled、not already already-processed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事（351 余量），先数清问的是 Process 也会在提议者那边叫 是不是 already skip-process / 351 / processalso-sold-as-matched，是不是是提议者 是不是 already settled，还是列表自己编的 是不是 already already-processed，再决定要不要同一次发布。351 processalso vs prepare bundled unbundling 在本页 item 1 启动。
