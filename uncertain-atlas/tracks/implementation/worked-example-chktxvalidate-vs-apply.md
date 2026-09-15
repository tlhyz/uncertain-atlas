# 例：看见 validates against current state / checking signatures and account balances 不是已经按 ExecuteTxState 验过；看见 does not apply any state changes 不是已经改了状态 / 已经参与处理块；看见 Technically optional / not involved in processing blocks / Code != 0 rejected 不是已经四门已经结算 / CheckTx 过了就永远有效

**层次**：实现 / CheckTx Usage validate-no-apply 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「validates against current state 不是 ExecuteTxState / does not apply state changes 不是已经改了状态 / Technically optional + Code≠0 拒绝 不是四门已经结算 / CheckTx 过了就永远有效」，不是 CheckTx 请求余栏 bundled（391），也不是 CheckTxState 与 ExecuteTxState bundled（312）。不要另写怎样实现 CheckTxState、怎样写验签逻辑。

## 官方三件事

规范把 CheckTx Usage 里 validates against current state、does not apply state changes、Technically optional / not involved in processing blocks 与 Code≠0 拒绝路径，写成三件独立的实现事，不是「看见跑了 CheckTx 就已经按 ExecuteTxState 验过、已经改了状态、已经交差」一件事：

1. **看见 `CheckTx` validates the transaction against the current state of the application, for example, checking signatures and account balances / 看见对照当前状态验、例如验签和余额 不是已经按 `ExecuteTxState` 验过（312） interchangeable，也不是已经按将要执行的那份状态验过，也不是已经 CheckTxState 与 ExecuteTxState 同时在改就等于同一份（312 bundled）。**  
   官方 Usage 写：`CheckTx` validates the transaction against the current state of the application, for example, checking signatures and account balances。看见 against the current state，不是已经按 ExecuteTxState 验过 interchangeable——312 钉 app requirements CheckTxState，本页钉 Methods CheckTx Usage current state。看见 checking signatures and account balances，不是已经 Finalize 按应用规则确定执行 txs（408） interchangeable。看见验了，不是已经 QueryState 就是 ExecuteTxState（314） interchangeable。
2. **看见 but does not apply any of the state changes described in the transaction / 看见不应用这笔描述的任何状态改动 不是已经改了状态 / 已经参与处理块，也不是已经 Finalize 确定执行 txs（408） interchangeable，也不是已经 Process MAY 像 Finalize 整块执行 candidate state（452） interchangeable，也不是已经 CheckTx 过了就永远有效（301）。**  
   官方 Usage 写：but does not apply any of the state changes described in the transaction。看见 does not apply，不是已经在 CheckTx 里把余额扣了 / 状态写了 interchangeable。看见 state changes described in the transaction，不是已经 FinalizeBlock 按应用规则确定执行 txs（408） bundled 第二件事 interchangeable——408 钉 When 执行，本页钉 CheckTx Usage 不应用改动。看见没应用，不是已经 Process candidate state 就等于已经改了已提交状态（452） interchangeable。看见验过，不是已经提案收了 / CheckTx 过了就永远有效（301） interchangeable。
3. **看见 Technically optional - not involved in processing blocks / Guardian of the mempool: every node runs `CheckTx` before letting a transaction into its local mempool / 看见技术上可选、不参与处理块、内存池守卫 不是已经可以不跑 CheckTx / 已经四门已经结算（373） interchangeable；看见 Transactions where `CheckTxResponse.Code != 0` will be rejected - they will not be broadcast to other nodes or included in a proposal block / CometBFT attributes no other value to the response code / 看见 Code≠0 会拒、不会广播、不会进提案块 不是已经 CheckTx 过了就进块（33），也不是已经 CheckTx 过了就永远有效（301），也不是已经 CheckTx 是内存池守卫（405） bundled 就代表 Usage 已经验完 interchangeable。**  
   官方 Usage 写：Technically optional - not involved in processing blocks。看见 optional / not involved in processing blocks，不是已经 CheckTx 技术上可选（373） bundled 第二句 interchangeable——373 钉 optional 与 block processing 分开，本页钉 Usage 侧 validate-no-apply 与 optional 同段语境。看见 Guardian of the mempool / every node runs CheckTx before letting a transaction into its local mempool，不是已经可以不跑 CheckTx interchangeable。官方写：Transactions where `CheckTxResponse.Code != 0` will be rejected … will not be broadcast … or included in a proposal block。CometBFT attributes no other value to the response code。看见 Code≠0 拒，不是已经 Check 通过就是已进提案（33） interchangeable。看见不会进提案块，不是已经 CheckTx 过了就永远有效（301） interchangeable。看见 no other value to the response code，不是已经 CheckTx 是内存池守卫（405） bundled 就代表 optional 已经交差 interchangeable。

怎样做验签、怎样维护 CheckTxState、怎样区分 current state 是规范里的做法，本页不抄。CheckTxState 与 ExecuteTxState（312）是 app requirements 那套，CheckTx 请求余栏 validate-no-apply bundled（391）是 tx / info 那套，CheckTx 技术上可选（373）是 optional vs block processing 那套，本页不抄。

## 官方为什么这样拆

- **validates against current state ≠ ExecuteTxState / 将要执行的那份状态：** 官方把 Methods Usage current state 验和 app requirements CheckTxState 分开。
- **does not apply state changes ≠ 已经改了状态 / Finalize 执行 / candidate 已提交：** 官方把 CheckTx 不应用改动和 Finalize / Process candidate 执行分开。
- **Technically optional + Code≠0 拒绝路径 ≠ 四门已经结算 / CheckTx 过了就进块或永远有效：** 官方把 optional / mempool guard / Code 语义和四门结算、池门 forever valid 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| validates against current state / signatures / balances | 不是 ExecuteTxState | 不是 CheckTxState bundled（312） |
| does not apply state changes | 不是已经改了状态 | 不是 Finalize 确定执行 txs（408） |
| Technically optional / Code≠0 rejected | 不是四门已经结算 | 不是 CheckTx 过了就永远有效（301） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见跑了 CheckTx 就已经按 ExecuteTxState 验过、已经改了状态、已经交差」，必须分开 validates against current state 是不是 ExecuteTxState、does not apply state changes 是不是已经改了状态 / Finalize interchangeable、Technically optional / Code≠0 拒绝 是不是四门已经结算 / CheckTx 过了就永远有效。可以跳过「看见跑了 CheckTx 就已经按 ExecuteTxState 验过」。不要另写怎样实现 CheckTxState。

## 本页不抄

- 怎样做验签、怎样维护 CheckTxState、怎样区分 current state。
- CheckTxState 与 ExecuteTxState / RECHECK 流程。那是不变量 312。
- CheckTx 请求 tx 栏 / Usage validate-no-apply bundled / info。那是不变量 391。
- CheckTx 技术上可选、不参与处理块。那是不变量 373。
- CheckTx 是内存池守卫。那是不变量 405。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
- Finalize 确定执行 txs。那是不变量 408。
- Process candidate 整块执行。那是不变量 452。
