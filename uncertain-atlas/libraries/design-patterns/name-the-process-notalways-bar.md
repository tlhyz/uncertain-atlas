# 模式：把失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事（351 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[失败时可能对上更早一次或根本不调 not already every-round ≠ bundled（351）](../../tracks/implementation/worked-example-process-notalways-vs-bundled.md)。

## 三个名字

1. **进了这一轮 / 失败时可能对上更早一次或根本不调 不是 already every-round：** 看见进了这一轮 / 失败时可能对上更早一次或根本不调 / 失败时不保证，不是已经每轮都会叫 Process interchangeable / 已经 every-round interchangeable / 已经每轮都会叫交差 interchangeable，不是 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable。

2. **叫了 Process / 可能对上更早一次 不是 already this-prepare：** 看见叫了 Process / `ProcessProposalRequest` 可能对上更早一次 Prepare 的回包 / 对上更早一次，不是已经是这一次刚回的那份 interchangeable / 已经 this-prepare interchangeable / 已经是这一次交差 interchangeable，不是 347 req3coherence interchangeable / 807 process-notguaranteed interchangeable。

3. **失败了 / 根本不调 不是 already crossed：** 看见失败了 / 根本不调 Process / 不调，不是已经交差 interchangeable / 已经 crossed interchangeable / 已经交差交差 interchangeable，不是 806 process-notskip interchangeable / 33 fourgates interchangeable。

官方把失败时不保证、不是已经是这一次刚回的那份、不是已经交差写成三个名字。把它们叫成一个「看见进了这一轮就已经每轮都会叫 interchangeable / 就已经是这一次刚回的那份 interchangeable / 就已经交差 interchangeable」，会把 not already every-round、not already this-prepare、not already crossed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事（351 余量），先数清问的是进了这一轮 / 失败时可能对上更早一次或根本不调 是不是 already every-round / 351 / processalso-sold-as-matched，是不是叫了 Process / 可能对上更早一次 是不是 already this-prepare，还是失败了 / 根本不调 是不是 already crossed，再决定要不要同一次发布。351 processalso vs prepare bundled unbundling 在本页 item 3 完成。
