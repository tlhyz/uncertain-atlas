# 反模式：把 FinalizeBlockResponse next_block_delay more precommits despite 2/3+ not decided / not 479 fintrigger 正式三事（480 余量）说成已经 decided / 已经 479 fintrigger / 已经 finmorepre bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse next_block_delay more precommits despite 2/3+ not decided ≠ bundled（480）](../../tracks/implementation/worked-example-finmorepre-notmorepre-vs-bundled.md)。

## 错在哪里

把 In CometBFT terms, this interval gives the proposer a chance to receive some more precommits, even though it already has the required 2/3+ 写成已经 has required 2/3+ 就已经决定 / 已经最终 interchangeable，或已经 +2/3 precommit 决定 interchangeable；把 more precommits despite 2/3+ 写成已经 When trigger 2f+1 precommit interchangeable，或已经 479 fintrigger interchangeable；把 more precommits 写成已经是 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480） interchangeable，或已经 finmorepre bundled interchangeable，或已经和 includes processing time / after committing before next height / 362 finwhen / 609 notprecommit / 611 notproctime interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay more precommits despite 2/3+ not decided / not 479 fintrigger 正式三事（480 余量），必须分开 not decided / final、not 479 fintrigger、not finmorepre bundled 三件事，不要和 480 / 362 / 479 / 611 糊成一句。

## 和相邻反模式

- [finmorepre-sold-as-timeout](finmorepre-sold-as-timeout.md) 是 480 finmorepre bundled 三事专用，不是本页 480 item 2 单句边界。
- [finmorepre-notproctime-sold-as-bundled](finmorepre-notproctime-sold-as-bundled.md) 是 611（480 item 1 余量）专用，不是本页 more precommits not decided 单句边界。
- [fintrigger-notprecommit-sold-as-bundled](fintrigger-notprecommit-sold-as-bundled.md) 是 609（479 item 2 余量）专用，不是本页 more precommits despite 2/3+ 单句边界。
- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页 post-commit more precommits 单句边界。
