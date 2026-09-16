# 反模式：把 FinalizeBlockResponse next_block_delay after committing before next height not slot / not final / not finmorepre bundled 正式三事（480 余量）说成已经 slot / 已经 final / 已经 finmorepre bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse next_block_delay after committing before next height not slot ≠ bundled（480）](../../tracks/implementation/worked-example-finmorepre-notaftercommit-vs-bundled.md)。

## 错在哪里

把 how long CometBFT waits after committing a block, before starting the next height / Commit 后再开下一高 写成已经槽位 interchangeable，或已经 ConsensusParams.block 块间隔 interchangeable；把 Set to 0 if you want progress as soon as it has all the precommits and the block has been processed 写成已经决定 / 已经 final interchangeable，或已经 +2/3 precommit 决定 interchangeable；把 after committing before next height 写成已经是 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480） interchangeable，或已经 finmorepre bundled interchangeable，或已经和 includes processing time / more precommits despite 2/3+ / 611 notproctime / 612 notmorepre / Set to constant 1s interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay after committing before next height not slot / not final / not finmorepre bundled 正式三事（480 余量），必须分开 not slot、not final / decided、not finmorepre bundled 三件事，不要和 480 / 385 / 589 / 611 / 612 糊成一句。

## 和相邻反模式

- [finmorepre-sold-as-timeout](finmorepre-sold-as-timeout.md) 是 480 finmorepre bundled 三事专用，不是本页 480 item 3 单句边界。
- [finmorepre-notproctime-sold-as-bundled](finmorepre-notproctime-sold-as-bundled.md) 是 611（480 item 1 余量）专用，不是本页 after committing 单句边界。
- [finmorepre-notmorepre-sold-as-bundled](finmorepre-notmorepre-sold-as-bundled.md) 是 612（480 item 2 余量）专用，不是本页 set to 0 / after committing 单句边界。
- [fndelay-sold-as-slot](fndelay-sold-as-slot.md) 是 589 next_block_delay 非确定三事专用，不是本页 480 item 3 单句边界。
