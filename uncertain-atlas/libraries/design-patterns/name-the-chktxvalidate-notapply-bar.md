# 模式：把 CheckTx Usage does not apply state changes not already mutated / not Finalize executed / not Process candidate committed 正式三事（486 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[does not apply state changes not already mutated ≠ bundled（486）](../../tracks/implementation/worked-example-chktxvalidate-notapply-vs-bundled.md)。

## 三个名字

1. **does not apply state changes 不是已经改了状态：** 看见 Usage 不应用这笔描述的改动，不是已经在 CheckTx 里把余额扣了 interchangeable，不是 681 chktxvalidate-notapply interchangeable。
2. **不应用改动 不是 Finalize 确定执行 txs：** 看见 does not apply，不是已经 Finalize 按应用规则确定执行 txs interchangeable，不是 408 finexec interchangeable。
3. **看见没应用 不是 Process candidate 已提交：** 看见验过 / 没应用，不是已经 Process candidate 就等于已经改了已提交状态 interchangeable，不是 452 proccand interchangeable / 301 forever valid interchangeable。

官方把 CheckTx Usage 不应用改动、Finalize 执行、Process candidate 已提交写成三个名字。把它们叫成一个「看见跑了 CheckTx 就已经改了状态」，会把 not mutated、not Finalize executed、not Process candidate committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage does not apply state changes 正式三事（486 余量），先数清问的是 does not apply 是不是已经改了状态、是不是 Finalize 执行 / 408，还是看见没应用 是不是 Process candidate committed / 452，再决定要不要同一次发布。486 chktxvalidate vs apply bundled unbundling 在本页 item 2 完成。
