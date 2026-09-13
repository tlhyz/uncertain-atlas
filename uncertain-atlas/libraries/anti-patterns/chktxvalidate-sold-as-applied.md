# 反模式：把 CheckTx Usage validate-no-apply 正式三事卖成 ExecuteTxState 验过 / 已经改了状态 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[validates current state ≠ ExecuteTxState](../../tracks/implementation/worked-example-chktxvalidate-vs-apply.md)。

## 卖法

- 「看见 CheckTx validates against current state / checking signatures and account balances / 对照当前状态验 就已经按 ExecuteTxState 验过 / 已经按将要执行的那份状态验过 / 已经 CheckTxState 与 ExecuteTxState 同一份。」
- 「看见 does not apply any state changes / 不应用这笔描述的状态改动 就已经改了状态 / 已经参与处理块 / 已经 Finalize 确定执行 / 已经 Process candidate 交了差 / CheckTx 过了就永远有效。」
- 「看见 Technically optional / not involved in processing blocks / Guardian of the mempool / Code≠0 rejected 就已经四门已经结算 / 可以不跑 CheckTx / CheckTx 过了就进块 / Code OK 就已经 committed。」

## 为什么错

官方把 validates against current state、does not apply state changes、Technically optional + Code≠0 拒绝路径写成三件独立的实现事。把它们卖成 ExecuteTxState 验过 / 已经改了状态 / 已经交差，会把 Methods Usage current state 验、不应用改动、optional/Code 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage validate-no-apply，必须分开 validates against current state、does not apply state changes、Technically optional / Code≠0 拒绝 三个名字，不要把它们卖成 ExecuteTxState 验过 / 已经改了状态 / 已经交差。

## 和相邻反模式

- [chktxtype-sold-as-recheck](chktxtype-sold-as-recheck.md) 是 Request type 就等于 Recheck，不是本页 validate-no-apply Usage。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 optional 就等于四门结算，不是本页 validate-no-apply Usage 全段。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 Check 通过就是已进提案，不是本页 does not apply / Code≠0 拒绝路径。
