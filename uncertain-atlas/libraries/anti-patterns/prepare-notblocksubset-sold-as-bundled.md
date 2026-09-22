# 反模式：把整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 余量）说成已经只能看见装得进一块的子集 / 已经没有上限 / 已经整包能回

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[整池可见 not already block-subset ≠ bundled（345）](../../tracks/implementation/worked-example-prepare-notblocksubset-vs-bundled.md)。

## 卖法

把整池可见 / MaxBytes 写成 -1 把池子都交来 / 池子里所有交易交给 PrepareProposal 写成已经只能看见装得进一块的子集 interchangeable / 已经 block-subset interchangeable / 已经只看见一块子集交差 interchangeable / 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable；把能看见全部 / 池子都交来 写成已经没有上限 interchangeable / 已经 no-cap interchangeable / 已经无上限交差 interchangeable；把整池都来了 / 全部交易在请求里 写成已经整包能回 interchangeable / 已经 all-visible-is-uncapped interchangeable / 已经整包交差 interchangeable，或已经和 345 preparereturn bundled / preparereturn-sold-as-trimmed interchangeable / 788 prepare-notblocksubset interchangeable。

## 为什么错

官方把看见全部、不是没有上限、不是已经能整包交回去写成三件独立的实现事。把它们卖成 already block-subset interchangeable / already no-cap interchangeable / already all-visible-is-uncapped interchangeable，会把 not already block-subset、not already no-cap、not already all-visible-is-uncapped 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 余量），必须分开 not already block-subset、not already no-cap、not already all-visible-is-uncapped 三件事，不要和 345 / 299 / 337 / 789 / 790 糊成一句。

## 和相邻反模式

- [preparereturn-sold-as-trimmed](preparereturn-sold-as-trimmed.md) 是 PrepareProposal 回包上限 bundled 全段，不是本页整池可见 item 1 单句边界。
- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 -1 就按 100 MB 验不是已经没有上限（337），不是本页能看见全部 ≠ 无上限 边界。
- [maxbytesoverhead-sold-as-full](maxbytesoverhead-sold-as-full.md) 是 MaxBytes 减去头集合证据才是交易上限（344），不是本页整池可见边界。
