# 反模式：把 FinalizeBlock When CometBFT calls Commit not already settled / not four gates settled / not fincommit bundled 正式三事（590 余量）说成已经交差 / 已经四门已经结算 / 已经 fincommit bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When CometBFT calls Commit not already settled ≠ bundled（590）](../../tracks/implementation/worked-example-fincommit-notsettled-vs-bundled.md)。

## 错在哪里

把 CometBFT calls Commit / When 第 8 步叫 Commit 写成已经 Finalize + Commit 交差 interchangeable，或已经四门已经结算 interchangeable；把 When 第 8 步 calls Commit 写成已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable，或已经 persist decision interchangeable；把 When 第 8 步叫 Commit 写成已经是 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590） interchangeable，或已经 fincommit bundled interchangeable，或已经和 instruct persist / after lock mempool / 403 / 481 / 587 / 588 / 631 / 645 / 646 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When CometBFT calls Commit not already settled / not four gates settled / not fincommit bundled 正式三事（590 余量），必须分开 not already settled、not four gates settled、not fincommit bundled 三件事，不要和 590 / 403 / 335 / 481 / 587 / 588 / 631 / 645 / 646 / 33 糊成一句。

## 和相邻反模式

- [fincommit-sold-as-settled](fincommit-sold-as-settled.md) 是 calls Commit instruct persist（590）专用 bundled，不是本页 590 item 1 单句边界。
- [finafter-notsettled-sold-as-bundled](finafter-notsettled-sold-as-bundled.md) 是 403 item 1 余量 / 632 专用，不是本页 When 第 8 步 calls Commit not settled 单句边界。
- [finlock-notsettled-sold-as-bundled](finlock-notsettled-sold-as-bundled.md) 是 588 item 1 余量 / 629 专用，不是本页 When 第 8 步 calls Commit 单句边界。
- [commitnoparam-sold-as-persist](commitnoparam-sold-as-persist.md) 是 Commit 空请求（399）专用，不是本页 not already settled 单句边界。
