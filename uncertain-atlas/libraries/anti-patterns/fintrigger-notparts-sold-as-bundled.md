# 反模式：把 FinalizeBlock When trigger Proposal + all block parts not only hash / Process ran 正式三事（479 余量）说成已经 only hash / 已经 Process 跑过 / 已经 fintrigger bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When trigger Proposal + all block parts not only hash ≠ bundled（479）](../../tracks/implementation/worked-example-fintrigger-notparts-vs-bundled.md)。

## 错在哪里

把 Proposal message with block _v_ and all its block parts 写成已经 only `FinalizeBlockRequest.hash` interchangeable，或已经 hash 栏对上 interchangeable，或已经 partial block 就够决定 interchangeable；把 Proposal + all block parts 写成已经 ProcessProposal 跑过 interchangeable，或已经 at least one non-byzantine has run Process interchangeable；把 Proposal + all block parts 写成已经是 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable，或已经 fintrigger bundled interchangeable，或已经和 2f+1 precommit same id(v) / decides block v / 362 finwhen / 361 prevote ExtendVote / 428 finhash / 472 Process guarantee interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger Proposal + all block parts not only hash / Process ran 正式三事（479 余量），必须分开 not only hash、not Process ran、not fintrigger bundled 三件事，不要和 479 / 428 / 472 / 362 / 361 糊成一句。

## 和相邻反模式

- [finwhenparts-sold-as-partial](finwhenparts-sold-as-partial.md) 是 479 fintrigger bundled 三事专用，不是本页 479 item 1 单句边界。
- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页 Proposal + parts not only hash 单句边界。
- [finproc-sold-as-allvalidators](../../libraries/anti-patterns/finproc-sold-as-allvalidators.md) 是 Process guarantee，不是本页 Proposal + parts not Process ran 单句边界。
