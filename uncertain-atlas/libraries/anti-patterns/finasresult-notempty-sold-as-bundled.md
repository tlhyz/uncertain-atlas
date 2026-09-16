# 反模式：把 FinalizeBlock must provide values provided values not empty keep current / not CheckTx 正式三事（477 余量）说成已经空着就没有义务 / 已经 CheckTx 过了

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[provided values not empty keep current / not CheckTx ≠ bundled（477）](../../tracks/implementation/worked-example-finasresult-notempty-vs-bundled.md)。

## 错在哪里

把 provided values / tx_results 来自执行结果 写成已经空更新就没有 must provide 义务，或已经 empty keep current（458） interchangeable；把 must provide tx_results 写成已经 CheckTx 过了就不需要 Finalize 再回 tx_results，或已经 CheckTx 弱过滤器（339） interchangeable；把 provided values 写成已经是 FinalizeBlock must provide values bundled（477） interchangeable，或已经 finresp bundled（363） interchangeable，或已经和 594 / 595 / 464 / 471 / 459 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values provided values not empty keep current / not CheckTx 正式三事（477 余量），必须分开 provided values not empty keep current、not CheckTx passed、not finasresult bundled 三件事，不要和 477 / 458 / 339 / 464 / 594 / 595 糊成一句。

## 和相邻反模式

- [finasresult-sold-as-candidate](finasresult-sold-as-candidate.md) 是 477 bundled 三事专用，不是本页 provided values 单句边界。
- [finasresult-notsettled-sold-as-bundled](finasresult-notsettled-sold-as-bundled.md) 是 594（477 item 1 余量）专用，不是本页 empty keep current 单句边界。
- [finasresult-notcand-sold-as-bundled](finasresult-notcand-sold-as-bundled.md) 是 595（477 item 2 余量）专用，不是本页 CheckTx passed 单句边界。
