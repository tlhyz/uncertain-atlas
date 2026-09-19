# 模式：把 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事（316 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / Specifics of `ExecTxResult`。  
**例**：[标成无效 not already excluded from block ≠ bundled（316）](../../tracks/implementation/worked-example-exectxresult-notexcluded-vs-bundled.md)。

## 三个名字

1. **标成无效 不是 already excluded from block：** 看见 Code ≠ 0 / 标成无效交易，不是已经没进块 interchangeable / 已经从块里删掉 interchangeable，不是 316 exectxresult bundled interchangeable / 33 four gates interchangeable / exectxresult-sold-as-consensus interchangeable。

2. **没索引 不是 already excluded from consensus：** 看见无效交易不建索引 / 不建索引，不是已经没进共识 interchangeable / 已经没进 Agreement 那份 interchangeable，不是 316 exectxresult item 1 interchangeable / 707 exectxresult-notorder interchangeable。

3. **类比 CheckTx 不是 already same as CheckTx gate：** 看见官方把它类比成没过 CheckTx / 类比池门，不是已经和池门同一把尺 interchangeable / 已经和 CheckTx 同一门 interchangeable，不是 316 exectxresult item 3 interchangeable / 709 exectxresult-notheader interchangeable。

官方把标成无效单句、already excluded from block、already excluded from consensus、already same as CheckTx gate 写成三个名字。把它们叫成一个「看见 Code 非零就已经没进块 interchangeable / 就已经没进共识 interchangeable / 就已经和池门同一把尺 interchangeable」，会把 not already excluded from block、not already excluded from consensus、not already same as CheckTx gate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事（316 余量），先数清问的是标成无效 是不是 already excluded from block / 316 / exectxresult-sold-as-consensus，是不是没索引 是不是 already excluded from consensus，还是类比 CheckTx 是不是 already same as CheckTx gate，再决定要不要同一次发布。316 exectxresult vs consensus bundled unbundling 在本页 item 2 完成。
