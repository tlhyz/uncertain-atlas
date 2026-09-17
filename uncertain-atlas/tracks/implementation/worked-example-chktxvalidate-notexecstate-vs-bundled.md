# 例：看见 CheckTx validates against current state is not already ExecuteTxState interchangeable / not already about-to-execute state interchangeable / not already CheckTxState is ExecuteTxState interchangeable

**层次**：实现 / CheckTx Usage validates against current state not ExecuteTxState / not about-to-execute / not CheckTxState is ExecuteTxState 正式三事（486 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage validates against current state not ExecuteTxState / not about-to-execute / not CheckTxState is ExecuteTxState 正式三事（486 余量）/ not 680 chktxvalidate-notexecstate interchangeable / not 486 chktxvalidate-vs-apply bundled interchangeable」，不是 CheckTx Usage validate-no-apply 正式三事 bundled（486），也不是 CheckTxState 与 ExecuteTxState bundled（312）或 CheckTx 请求余栏 bundled（391）。不要另写怎样实现 CheckTxState、怎样写验签逻辑。

## 官方三件事

规范把 CheckTx Usage 里 validates the transaction against the current state of the application, for example, checking signatures and account balances 和「已经按 ExecuteTxState 验过（312） interchangeable / 已经按将要执行的那份状态验过 interchangeable / 已经 CheckTxState 与 ExecuteTxState 同时在改就等于同一份（312 bundled） interchangeable」分开写成三件独立的实现事，不是「看见 validates against current state 就已经 ExecuteTxState interchangeable / 就已经 about-to-execute interchangeable / 就已经 CheckTxState is ExecuteTxState interchangeable」一件事：

1. **看见 `CheckTx` validates the transaction against the current state of the application, for example, checking signatures and account balances / 看见对照当前状态验、例如验签和余额 / against the current state is not already 已经按 `ExecuteTxState` 验过（312） interchangeable / 312 checktxstate-vs-execute interchangeable / 已经按将要执行的那份状态验过 interchangeable / 已经 Finalize 按应用规则确定执行 txs（408） interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 680 chktxvalidate-notexecstate interchangeable / 681 chktxvalidate-notapply interchangeable / 486 chktxvalidate item 2 does not apply interchangeable，也不是已经 validates against current state not ExecuteTxState / not about-to-execute / not CheckTxState is ExecuteTxState 正式三事 bundled（486 item 1 余量） interchangeable / 486 chktxvalidate item 1 interchangeable。**  
   官方 Usage 写：`CheckTx` validates the transaction against the current state of the application, for example, checking signatures and account balances。看见 against the current state，不是已经按 ExecuteTxState 验过 interchangeable——312 钉 app requirements CheckTxState，本页从 486 item 1 侧钉 not ExecuteTxState 单句。看见 checking signatures and account balances，不是已经 Finalize 按应用规则确定执行 txs interchangeable——408 钉 When 执行，本页钉 Methods CheckTx Usage current state。486 chktxvalidate vs apply bundled unbundling 在本页 item 1 启动。

2. **看见 validates against current state / checking signatures and account balances / 看见对照当前状态验 is not already 已经按将要执行的那份状态验过 interchangeable / 已经 Prepare/Process 立刻执行出候选（311） interchangeable / 已经 candidate 就已经是 ExecuteTxState interchangeable / 已经丢掉就已经永远不用再执行 interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 680 chktxvalidate-notexecstate interchangeable / 486 chktxvalidate item 3 Technically optional interchangeable / 682 chktxvalidate-notoptional interchangeable。**  
   官方把 Usage current state 单句和「将要执行的那份状态 / 候选已经是 ExecuteTxState」路径分开——486 bundled 第一件事常与 311/312 混成「看见对照当前状态验 就已经按将要执行的那份状态验过 interchangeable」，本页钉 not about-to-execute 单句。看见验签和余额，不是已经 candidate vs ExecuteTxState interchangeable——311 钉候选，本页钉 Usage current state。

3. **看见 validates against current state / 看见对照当前状态验 / 看见验了 is not already 已经 CheckTxState 与 ExecuteTxState 同时在改就等于同一份（312 bundled） interchangeable / 312 checktxstate-vs-execute interchangeable / 已经两份同时在改就已经同一份 interchangeable / 已经 QueryState 就是 ExecuteTxState（314） interchangeable / 已经 RECHECK 就已经是新交易 interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 680 chktxvalidate-notexecstate interchangeable / 681 chktxvalidate-notapply interchangeable。**  
   官方把 Usage current state 单句和 CheckTxState 与 ExecuteTxState 同时在改就等于同一份路径分开——486 bundled 第一件事常与 312 bundled 混成「看见验了 就已经两份同一份 interchangeable」，本页钉 not CheckTxState is ExecuteTxState 单句。看见 against the current state，不是已经 QueryState 就是 ExecuteTxState interchangeable——314 另钉 QueryState，本页钉 CheckTx Usage item 1。486 chktxvalidate vs apply bundled unbundling 在本页 item 1 启动。

怎样做验签、怎样维护 CheckTxState、怎样区分 current state 是规范里的做法，本页不抄。CheckTx Usage validate-no-apply 正式三事 bundled（486）、does not apply state changes（486 item 2 余量 / 681）、Technically optional + Code≠0（486 item 3 余量 / 682）、CheckTxState 与 ExecuteTxState（312）、CheckTx 请求余栏（391）是另外那套，本页不抄。

## 官方为什么这样拆

- **validates against current state not ExecuteTxState ≠ 312 checktxstate-vs-execute interchangeable：** 官方把 Methods Usage current state 验和 app requirements CheckTxState / ExecuteTxState 分开。
- **validates against current state not about-to-execute ≠ 311 candidate-vs-execute interchangeable：** 官方把 Usage current state 单句和将要执行的那份状态 / 候选路径分开。
- **validates against current state not CheckTxState is ExecuteTxState ≠ 312 bundled interchangeable：** 官方把 Usage current state 单句和两份同时在改就等于同一份路径分开；486 chktxvalidate vs apply bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| validates against current state | 不是 ExecuteTxState（312） | 不是 does not apply state changes（681/486 item 2） |
| checking signatures and balances | 不是将要执行的那份状态（311） | 不是 CheckTxState bundled（312） |
| 看见验了 | 不是 CheckTxState 就是 ExecuteTxState | 不是 Technically optional + Code≠0（682/486 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage validates against current state not ExecuteTxState / not about-to-execute / not CheckTxState is ExecuteTxState 正式三事（486 余量），必须分开 validates against current state 是不是 ExecuteTxState interchangeable / 312 / 408、checking signatures and balances 是不是将要执行的那份状态 interchangeable / 311、看见验了 是不是 CheckTxState 就是 ExecuteTxState interchangeable / 312 bundled / 314。可以跳过「看见跑了 CheckTx 就已经按 ExecuteTxState 验过」。不要另写怎样实现 CheckTxState。486 chktxvalidate vs apply bundled unbundling 在本页 item 1 启动；续 [`worked-example-chktxvalidate-notapply-vs-bundled.md`](worked-example-chktxvalidate-notapply-vs-bundled.md)（不变量 681 item 2）。

## 本页不抄

- 怎样做验签、怎样维护 CheckTxState、怎样区分 current state。
- CheckTx Usage validate-no-apply 正式三事 bundled。那是不变量 486。
- does not apply state changes。那是不变量 486 item 2 余量 / 681。
- Technically optional + Code≠0。那是不变量 486 item 3 余量 / 682。
- CheckTxState 与 ExecuteTxState / RECHECK。那是不变量 312。
- CheckTx 请求余栏。那是不变量 391。
