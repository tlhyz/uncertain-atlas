# 模式：把 CheckTx Usage validates against current state not ExecuteTxState / not about-to-execute / not CheckTxState is ExecuteTxState 正式三事（486 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[validates against current state not ExecuteTxState ≠ bundled（486）](../../tracks/implementation/worked-example-chktxvalidate-notexecstate-vs-bundled.md)。

## 三个名字

1. **validates against current state 不是 ExecuteTxState：** 看见 Methods Usage 对照当前状态验，不是已经按 ExecuteTxState 验过 interchangeable，不是 312 checktxstate-vs-execute interchangeable / 680 chktxvalidate-notexecstate interchangeable。
2. **checking signatures and balances 不是将要执行的那份状态：** 看见验签和余额，不是已经按将要执行的那份状态验过 interchangeable，不是 311 candidate-vs-execute interchangeable。
3. **看见验了 不是 CheckTxState 就是 ExecuteTxState：** 看见 Usage current state，不是已经两份同时在改就等于同一份 interchangeable，不是 312 bundled interchangeable / 314 querystate interchangeable。

官方把 CheckTx Usage current state、ExecuteTxState、将要执行的那份状态写成三个名字。把它们叫成一个「看见跑了 CheckTx 就已经按 ExecuteTxState 验过」，会把 not ExecuteTxState、not about-to-execute、not CheckTxState is ExecuteTxState 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage validates against current state 正式三事（486 余量），先数清问的是 current state 是不是 ExecuteTxState / 312、是不是将要执行的那份状态 / 311，还是看见验了 是不是两份同一份 / 312 bundled，再决定要不要同一次发布。486 chktxvalidate vs apply bundled unbundling 在本页 item 1 启动。
