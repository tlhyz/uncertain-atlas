# 反模式：把 FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts 正式三事（479 余量）说成已经 prevote ExtendVote / 已经 without all block parts / 已经 fintrigger bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote ≠ bundled（479）](../../tracks/implementation/worked-example-fintrigger-notprecommit-vs-bundled.md)。

## 错在哪里

把 Precommit messages from 2f+1 validators' voting power precommitting the same block id(_v_) 写成已经 +2/3 prevote 同一 id(_v_) 才 ExtendVote interchangeable，或已经 prevote 锁住 ExtendVote interchangeable；把 2f+1 precommit same id(v) 写成已经 +2/3 precommit 就可以没有 all block parts interchangeable，或已经 partial block 就够 precommit interchangeable；把 Precommit 门槛 写成已经是 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable，或已经 fintrigger bundled interchangeable，或已经和 decides block v / 362 finwhen / 361 extendwhen / 608 notparts / 428 finhash interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts 正式三事（479 余量），必须分开 not +2/3 prevote ExtendVote、not without all block parts、not fintrigger bundled 三件事，不要和 479 / 361 / 608 / 362 糊成一句。

## 和相邻反模式

- [finwhenparts-sold-as-partial](finwhenparts-sold-as-partial.md) 是 479 fintrigger bundled 三事专用，不是本页 479 item 2 单句边界。
- [fintrigger-notparts-sold-as-bundled](fintrigger-notparts-sold-as-bundled.md) 是 608（479 item 1 余量）专用，不是本页 2f+1 precommit not prevote ExtendVote 单句边界。
- [extendwhen-sold-as-locked](../../libraries/anti-patterns/extendwhen-sold-as-locked.md) 是 +2/3 prevote 才 ExtendVote，不是本页 2f+1 precommit 门槛单句边界。
