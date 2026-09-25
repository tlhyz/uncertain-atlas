# 反模式：把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事（369 余量）说成已经按原样签 / 已经有重放保护 / 已经必须填

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有签 not already raw ≠ bundled（369）](../../tracks/implementation/worked-example-extvoteinfo-notraw-vs-bundled.md)。

## 卖法

把有签 / `extension_signature` 已由引擎验过、交给应用再处理；扩展启用时两份签都在 / 有 extension_signature 写成已经按原样签 interchangeable / 已经 raw interchangeable / 已经按原样签交差 interchangeable / 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable；把交给应用 / 把签交给应用再处理或再验 / 交给应用 写成已经有重放保护 interchangeable / 已经 protected interchangeable / 已经有重放保护交差 interchangeable；把签了空切片 / 没给 `non_rp_vote_extension` 就签空切片 / 签空切片 写成已经必须填 interchangeable / 已经 must-fill interchangeable / 已经必须填交差 interchangeable，或已经和 369 extvoteinfo bundled / extvoteinfo-sold-as-local interchangeable / 855 extvoteinfo-notraw interchangeable。

## 为什么错

官方把有签、不是已经有重放保护、不是已经必须填写成三件独立的实现事。把它们卖成 already raw interchangeable / already protected interchangeable / already must-fill interchangeable，会把 not already raw、not already protected、not already must-fill 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事（369 余量），必须分开 not already raw、not already protected、not already must-fill 三件事，不要和 369 / 358 / 854 / 856 糊成一句。

## 和相邻反模式

- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 extvoteinfo bundled 全段，不是本页有签 item 2 单句边界。
- [extvoteinfo-notfromblock-sold-as-bundled](extvoteinfo-notfromblock-sold-as-bundled.md) 是从本进程抽出 not already from-block（369 item 1），不是本页 not already raw 边界。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358），不是本页 not already raw 单句。
