# 模式：把 CheckTx Usage validate-no-apply 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[validates current state ≠ ExecuteTxState](../../tracks/implementation/worked-example-chktxvalidate-vs-apply.md)。

## 三个名字

1. **validates against current state / signatures / balances 不是 ExecuteTxState / 将要执行的那份状态：** 看见 Methods Usage 侧对照 current state 验，不是 app requirements CheckTxState vs ExecuteTxState interchangeable。
2. **does not apply state changes 不是已经改了状态 / Finalize 执行 / candidate 已提交 interchangeable：** 看见 CheckTx 不应用改动，不是 Finalize / Process candidate 执行 bundled interchangeable。
3. **Technically optional / Code≠0 rejected 不是四门已经结算 / CheckTx 过了就进块或永远有效：** 看见 optional / mempool guard / Code 语义，不是 optional vs block processing bundled 或 Check 通过就是已进提案 interchangeable。

## 为什么要分开叫

官方把 CheckTx Usage 里 validates against current state、does not apply state changes、Technically optional + Code≠0 拒绝路径，和 CheckTxState（312）、请求余栏 bundled（391）、optional vs block（373）写成三个名字。把它们叫成一个「看见跑了 CheckTx 就已经按 ExecuteTxState 验过、已经改了状态、已经交差」，会把 current state 验、不应用改动、optional/Code 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage validate-no-apply，先数清问的是 validates against current state 是不是 ExecuteTxState、does not apply state changes 是不是已经改了状态、Technically optional / Code≠0 拒绝 是不是四门已经结算 / CheckTx 过了就永远有效，再决定要不要同一次发布。
