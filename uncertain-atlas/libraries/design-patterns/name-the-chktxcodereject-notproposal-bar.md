# 模式：把 CheckTx Usage will not broadcast or in proposal not Check passed is in proposal / not forever valid / not Finalize Code≠0 still in block 正式三事（489 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[will not be in proposal not Check passed is in proposal ≠ bundled（489）](../../tracks/implementation/worked-example-chktxcodereject-notproposal-vs-bundled.md)。

## 三个名字

1. **will not be included in a proposal block 不是 Check 通过就是已进提案：** 看见 Methods Usage 不会进提案块，不是已经四门已经结算 interchangeable，不是 33 four gates interchangeable / 687 chktxcodereject-notproposal interchangeable。
2. **不会广播 / 不会进提案块 不是 forever valid：** 看见 will not be broadcast，不是已经 CheckTx 过了就永远有效 interchangeable，不是 301 forever valid interchangeable。
3. **看见 Code 非零 不是 Finalize Code≠0 仍在块里：** 看见 Usage 池门 Code，不是已经 Finalize 回执 Code≠0 仍在块里 interchangeable，不是 316 exectxresult interchangeable。

官方把 CheckTx Usage 不会进提案块、四门结算、forever valid、Finalize Code≠0 仍在块里写成三个名字。把它们叫成一个「看见不会进提案块就已经交差」，会把 not Check passed is in proposal、not forever valid、not Finalize Code≠0 still in block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage will not be in proposal 正式三事（489 余量），先数清问的是不会进提案块 是不是 Check 通过就是已进提案 / 33、是不是 forever valid / 301、还是看见 Code 非零 是不是 Finalize Code≠0 仍在块里 / 316，再决定要不要同一次发布。489 chktxcodereject vs proposal bundled unbundling 在本页 item 2 续。
