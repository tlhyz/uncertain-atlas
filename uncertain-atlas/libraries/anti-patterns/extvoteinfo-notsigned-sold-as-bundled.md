# 反模式：把 验过的签交给应用 not already signed as-is / not already replay protected / not already must-fill 正式三事（369 余量） 卖成 已经按原样签 / 已经有重放保护 / 已经必须填

**层次**：实现 / ExtendedVoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extvoteinfo-notsigned-vs-bundled.md](../../tracks/implementation/worked-example-extvoteinfo-notsigned-vs-bundled.md)。

官方把 ExtendedVoteInfo 从本进程抽出 / 把验过的签交给应用 / 扩展关掉则字段全空三条核心句写成三件独立的实现事。把它们卖成已经按原样签 / 已经有重放保护 / 已经必须填，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看验过的签交给应用 正式三事（369 余量），必须分开 not already signed as-is、not already replay protected、not already must-fill 三件事，不要和 369 / 358 / 425 / 361 / 818 / 820 糊成一句。

## 和相邻反模式

- [extwhen-canonicalvote-sold-as-bundled](extwhen-canonicalvote-sold-as-bundled.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358），不是本页交给应用边界。
- [extvoteinfo-notblock-sold-as-bundled](extvoteinfo-notblock-sold-as-bundled.md) 是本进程抽出单句边界（818 item 1），不是本页交给应用边界。
