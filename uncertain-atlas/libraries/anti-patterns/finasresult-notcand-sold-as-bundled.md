# 反模式：把 FinalizeBlock must provide values as a result of executing the block not candidate / Process already ran 正式三事（477 余量）说成已经 Process 跑过就不用再执行 / 已经 apply candidate

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[as a result of executing the block not candidate ≠ bundled（477）](../../tracks/implementation/worked-example-finasresult-notcand-vs-bundled.md)。

## 错在哪里

把 as a result of executing the block 写成已经 Process / Prepare candidate 就不需要再在 Finalize 执行，或已经 Process 跑过就不执行 interchangeable；把 must provide as a result of executing 写成已经 apply candidate state 就不需要执行 txs，或已经 ExecuteTxState / may apply candidate interchangeable；把 as a result of executing 写成已经是 FinalizeBlock must provide values bundled（477） interchangeable，或已经 466 executes block v interchangeable，或已经 351 Process also on proposer interchangeable，或已经和 460 / 574 / 584 / 594 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values as a result of executing the block not candidate / Process already ran 正式三事（477 余量），必须分开 as a result of executing not Process already ran、not apply candidate、not 466 / 351 / 594 三件事，不要和 477 / 460 / 574 / 584 / 594 糊成一句。

## 和相邻反模式

- [finasresult-sold-as-candidate](finasresult-sold-as-candidate.md) 是 477 bundled 三事专用，不是本页 not candidate / Process already ran 单句边界。
- [finasresult-notsettled-sold-as-bundled](finasresult-notsettled-sold-as-bundled.md) 是 594（477 item 1 余量）专用，不是本页 as a result of executing 单句边界。
- [finexecbv-notcand-sold-as-bundled](finexecbv-notcand-sold-as-bundled.md) 是 574（466 item 2 余量）专用，不是本页 Usage as a result of executing 单句边界。
