# 反模式：把 FinalizeBlock When instruct Application to persist its state not engine persist tx outputs / AppHash / ResultsHash / not Commit Usage signal bundled / not fincommit bundled 正式三事（590 余量）说成已经引擎 persist 这三份 / 已经 Commit Usage signal bundled / 已经 fincommit bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When instruct Application to persist its state not engine persist ≠ bundled（590）](../../tracks/implementation/worked-example-fincommit-notpersist-vs-bundled.md)。

## 错在哪里

把 to instruct the Application to persist its state / instruct Application to persist its state 写成已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable，或已经 When 第 6 步 persists 这三份 interchangeable；把 instruct persist 写成已经 Signal the Application to persist application state interchangeable，或已经 Commit Usage signal bundled interchangeable；把 When 第 8 步 instruct persist 写成已经是 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590） interchangeable，或已经 fincommit bundled interchangeable，或已经和 calls Commit / after lock mempool / 587 / 481 / 335 / 644 / 646 / 616 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When instruct Application to persist its state not engine persist tx outputs / AppHash / ResultsHash / not Commit Usage signal bundled / not fincommit bundled 正式三事（590 余量），必须分开 not engine persist 这三份、not Commit Usage signal bundled、not fincommit bundled 三件事，不要和 590 / 587 / 481 / 335 / 403 / 632 / 616 / 644 / 646 / 399 糊成一句。

## 和相邻反模式

- [fincommit-sold-as-settled](fincommit-sold-as-settled.md) 是 calls Commit instruct persist（590）专用 bundled，不是本页 590 item 2 单句边界。
- [fincommit-notsettled-sold-as-bundled](fincommit-notsettled-sold-as-bundled.md) 是 590 item 1 余量 / 644 专用，不是本页 instruct persist not engine persist 单句边界。
- [commitnoparam-sold-as-persist](commitnoparam-sold-as-persist.md) 是 Commit 空请求（399）专用，不是本页 not Commit Usage signal 单句边界。
- [finafter-notsettled-sold-as-bundled](finafter-notsettled-sold-as-bundled.md) 是 403 item 1 余量 / 632 专用，不是本页 When 第 8 步 instruct persist 单句边界。
