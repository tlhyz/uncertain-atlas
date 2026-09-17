# 反模式：把 Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事（491 余量）说成已经 retain_height 默认 0 全留 / 已经 blocks below may be removed / 已经 persist signal bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notdefaultzero-vs-bundled.md)。

## 卖法

把 Use `CommitResponse.retain_height` with caution! / 要慎用 retain_height 写成已经 retain_height defaults to 0 retain all interchangeable / 366 retain-height bundled interchangeable / 335 finpersist interchangeable / 已经 default 0 全留 interchangeable；把 caution 段落 写成已经 blocks below this height may be removed interchangeable / 366 retain bundled item 2 interchangeable / 已经回了高度就等于已经在剪 interchangeable / 已经 non-zero retain_height 就等于已经在剪 interchangeable；把 with caution 单句 写成已经 Commit Usage persist signal bundled interchangeable / 481 commitpersist bundled interchangeable / 已经 Signal persist application state interchangeable / 已经 caution 已经验完 interchangeable，或已经和 491 commitretaincaution-vs-kept bundled / commitretaincaution-sold-as-pruning interchangeable / 677 commitretaincaution-notdefaultzero interchangeable。

## 为什么错

官方把 Commit Usage caution 语气单句、retain_height defaults to 0 retain all（366）、blocks below height may be removed、Commit Usage persist signal bundled（481）写成三件独立的实现事。把它们卖成 retain_height defaults to 0 retain all interchangeable / blocks below may be removed interchangeable / persist signal bundled interchangeable，会把 not defaults to 0 retain all、not blocks below height may be removed、not Commit Usage persist signal bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事（491 余量），必须分开 not defaults to 0 retain all、not blocks below height may be removed、not Commit Usage persist signal bundled 三件事，不要和 491 / 366 / 481 / 678 / 679 / 323 / 38 / 335 糊成一句。

## 和相邻反模式

- [commitretaincaution-sold-as-pruning](commitretaincaution-sold-as-pruning.md) 是 Commit Usage retain_height caution 正式三事 bundled 全段，不是本页 item 1 with caution 单句边界。
- [retain-sold-as-pruned](retain-sold-as-pruned.md) 是 Commit 保留高度 bundled 全段，不是本页 caution 语气 vs defaults to 0 边界。
- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 persist signal 就等于已经在 Finalize 落了，不是本页 with caution 单句 vs persist signal bundled 边界。
