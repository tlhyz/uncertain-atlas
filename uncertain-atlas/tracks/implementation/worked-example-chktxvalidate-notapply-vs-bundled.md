# 例：看见 CheckTx does not apply state changes is not already mutated interchangeable / not already Finalize executed interchangeable / not already Process candidate committed interchangeable

**层次**：实现 / CheckTx Usage does not apply state changes not already mutated / not Finalize executed / not Process candidate committed 正式三事（486 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage does not apply state changes not already mutated / not Finalize executed / not Process candidate committed 正式三事（486 余量）/ not 681 chktxvalidate-notapply interchangeable / not 486 chktxvalidate-vs-apply bundled interchangeable」，不是 CheckTx Usage validate-no-apply 正式三事 bundled（486），也不是 CheckTx Usage validates against current state not ExecuteTxState（680）或 Finalize 确定执行 txs（408）。不要另写怎样实现 CheckTxState、怎样写验签逻辑。

## 官方三件事

规范把 CheckTx Usage 里 but does not apply any of the state changes described in the transaction 和「已经在 CheckTx 里把余额扣了 / 状态写了 interchangeable / 已经 Finalize 确定执行 txs（408） interchangeable / 已经 Process candidate 就等于已经改了已提交状态（452） interchangeable / 已经 CheckTx 过了就永远有效（301） interchangeable」分开写成三件独立的实现事，不是「看见 does not apply state changes 就已经 mutated interchangeable / 就已经 Finalize executed interchangeable / 就已经 Process candidate committed interchangeable」一件事：

1. **看见 but does not apply any of the state changes described in the transaction / 看见不应用这笔描述的任何状态改动 / does not apply is not already 已经在 CheckTx 里把余额扣了 / 状态写了 interchangeable / 已经改了状态 interchangeable / 已经参与处理块 interchangeable / 已经 CheckTx 过了就永远有效（301） interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 681 chktxvalidate-notapply interchangeable / 680 chktxvalidate-notexecstate interchangeable / 486 chktxvalidate item 1 current state interchangeable，也不是已经 does not apply state changes not already mutated / not Finalize executed / not Process candidate committed 正式三事 bundled（486 item 2 余量） interchangeable / 486 chktxvalidate item 2 interchangeable。**  
   官方 Usage 写：but does not apply any of the state changes described in the transaction。看见 does not apply，不是已经在 CheckTx 里把余额扣了 interchangeable。看见 state changes described in the transaction，不是已经 CheckTx Usage 正式三事 bundled（486） interchangeable——486 钉 bundled 三事，本页钉 Methods CheckTx Usage 不应用改动单句。486 chktxvalidate vs apply bundled unbundling 在本页 item 2 启动。

2. **看见 does not apply state changes / 不应用这笔描述的状态改动 / 看见没应用 is not already 已经 Finalize 按应用规则确定执行 txs（408） interchangeable / 408 finexec interchangeable / 已经 Finalize 改了就已经交差 interchangeable / 已经印进本头 interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 681 chktxvalidate-notapply interchangeable / 486 chktxvalidate item 3 Technically optional interchangeable / 682 chktxvalidate-notoptional interchangeable。**  
   官方把 Usage 不应用改动单句和 Finalize 确定执行 txs 路径分开——486 bundled 第二件事常与 408 混成「看见不应用改动 就已经 Finalize 执行 interchangeable / 就已经交差 interchangeable」，本页钉 not Finalize executed 单句。看见 does not apply，不是已经 Finalize When 执行 txs interchangeable——408 钉 Finalize 执行，本页钉 CheckTx Usage 不应用。

3. **看见 does not apply state changes / 看见没应用 / 看见验过 is not already 已经 Process MAY 像 Finalize 整块执行 candidate state（452） interchangeable / 452 proccand interchangeable / 已经 candidate 就等于已经改了已提交状态 interchangeable / 已经 Process 回了 Accept 就换工作状态 interchangeable / 已经 CheckTx 过了就永远有效（301） interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 681 chktxvalidate-notapply interchangeable / 680 chktxvalidate-notexecstate interchangeable。**  
   官方把 Usage 不应用改动单句和 Process candidate 已提交路径分开——486 bundled 第二件事常与 452 混成「看见没应用 就已经 Process candidate committed interchangeable」，本页钉 not Process candidate committed 单句。看见验过，不是已经提案收了 / CheckTx 过了就永远有效 interchangeable——301 钉 forever valid，本页钉 Usage 不应用。486 chktxvalidate vs apply bundled unbundling 在本页 item 2 启动。

怎样做验签、怎样维护 CheckTxState、怎样区分 current state 是规范里的做法，本页不抄。CheckTx Usage validate-no-apply 正式三事 bundled（486）、validates against current state not ExecuteTxState（486 item 1 余量 / 680）、Technically optional + Code≠0（486 item 3 余量 / 682）、Finalize 确定执行 txs（408）、Process candidate（452）是另外那套，本页不抄。

## 官方为什么这样拆

- **does not apply state changes not already mutated ≠ 已经改了状态 interchangeable：** 官方把 Methods CheckTx Usage 不应用改动单句和「CheckTx 里已经写状态」路径分开。
- **does not apply state changes not Finalize executed ≠ 408 finexec interchangeable：** 官方把 Usage 不应用改动单句和 Finalize 确定执行 txs 路径分开。
- **does not apply state changes not Process candidate committed ≠ 452 proccand interchangeable：** 官方把 Usage 不应用改动单句和 Process candidate 已提交路径分开；486 chktxvalidate vs apply bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| does not apply state changes | 不是已经改了状态 | 不是 validates against current state（680/486 item 1） |
| 不应用这笔描述的改动 | 不是 Finalize 确定执行 txs（408） | 不是 CheckTx 请求余栏（391） |
| 看见没应用 | 不是 Process candidate 已提交（452） | 不是 Technically optional + Code≠0（682/486 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage does not apply state changes not already mutated / not Finalize executed / not Process candidate committed 正式三事（486 余量），必须分开 does not apply 是不是已经改了状态 interchangeable、不应用改动 是不是 Finalize 执行 interchangeable / 408、看见没应用 是不是 Process candidate committed interchangeable / 452 / 301。可以跳过「看见跑了 CheckTx 就已经改了状态」。不要另写怎样实现 CheckTxState。486 chktxvalidate vs apply bundled unbundling 在本页 item 2 完成；续 [`worked-example-chktxvalidate-notoptional-vs-bundled.md`](worked-example-chktxvalidate-notoptional-vs-bundled.md)（不变量 682 item 3）。

## 本页不抄

- 怎样做验签、怎样维护 CheckTxState、怎样区分 current state。
- CheckTx Usage validate-no-apply 正式三事 bundled。那是不变量 486。
- validates against current state not ExecuteTxState。那是不变量 486 item 1 余量 / 680。
- Technically optional + Code≠0。那是不变量 486 item 3 余量 / 682。
- Finalize 确定执行 txs。那是不变量 408。
- Process candidate 整块执行。那是不变量 452。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
