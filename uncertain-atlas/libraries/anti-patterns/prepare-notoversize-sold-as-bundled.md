# 反模式：把聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 余量）说成已经能回超限列表 / 已经按请求裁过 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[聚合体积可以超过 max_tx_bytes not already can-return-oversize ≠ bundled（345）](../../tracks/implementation/worked-example-prepare-notoversize-vs-bundled.md)。

## 卖法

把聚合体积可以超过 `PrepareProposalRequest.max_tx_bytes` / 池子加起来比这次上限大 / 所有交易加起来可以超 写成已经能回超限列表 interchangeable / 已经 can-return-oversize interchangeable / 已经回超限交差 interchangeable / 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable；把请求里带了上限 / `max_tx_bytes` 在请求里 写成已经按这个上限裁过 interchangeable / 已经 request-trimmed interchangeable / 已经裁过交差 interchangeable；把能看见超限的池 / 池子比上限大还交来 写成已经交差 interchangeable / 已经 settled interchangeable / 已经回包交差 interchangeable，或已经和 345 preparereturn bundled / preparereturn-sold-as-trimmed interchangeable / 789 prepare-notoversize interchangeable。

## 为什么错

官方把池子可以超这次上限、请求里写了上限不是已经裁过、能看见超限的池不是已经交差写成三件独立的实现事。把它们卖成 already can-return-oversize interchangeable / already request-trimmed interchangeable / already settled interchangeable，会把 not already can-return-oversize、not already request-trimmed、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 余量），必须分开 not already can-return-oversize、not already request-trimmed、not already settled 三件事，不要和 345 / 299 / 337 / 788 / 790 糊成一句。

## 和相邻反模式

- [preparereturn-sold-as-trimmed](preparereturn-sold-as-trimmed.md) 是 PrepareProposal 回包上限 bundled 全段，不是本页聚合体积可以超过 max_tx_bytes item 2 单句边界。
- [prepare-notblocksubset-sold-as-bundled](prepare-notblocksubset-sold-as-bundled.md) 是整池可见 not already block-subset（345 item 1），不是本页 not already can-return-oversize 边界。
- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 -1 就按 100 MB 验不是已经没有上限（337），不是本页请求里带了上限 ≠ 已经裁过 边界。
