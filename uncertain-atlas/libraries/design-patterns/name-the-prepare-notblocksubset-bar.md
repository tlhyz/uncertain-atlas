# 模式：把整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**例**：[整池可见 not already block-subset ≠ bundled（345）](../../tracks/implementation/worked-example-prepare-notblocksubset-vs-bundled.md)。

## 三个名字

1. **整池可见 不是 already block-subset：** 看见整池可见 / MaxBytes 写成 -1 把池子都交来 / 池子里所有交易交给 PrepareProposal，不是已经只能看见装得进一块的子集 interchangeable / 已经 block-subset interchangeable / 已经只看见一块子集交差 interchangeable，不是 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable。

2. **能看见全部 不是 already no-cap：** 看见能看见全部 / 池子都交来 / 不是只交一块子集，不是已经没有上限 interchangeable / 已经 no-cap interchangeable / 已经无上限交差 interchangeable，不是 337 maxbytescap interchangeable / 299 evidence-tx interchangeable。

3. **整池都来了 不是 already all-visible-is-uncapped：** 看见整池都来了 / 全部交易在请求里 / -1 把池子交齐，不是已经整包能回 interchangeable / 已经 all-visible-is-uncapped interchangeable / 已经整包交差 interchangeable，不是 789 prepare-notoversize interchangeable / 790 prepare-notenginecut interchangeable。

官方把看见全部、不是没有上限、不是已经能整包交回去写成三个名字。把它们叫成一个「看见整池都给了就已经能整包交回去 interchangeable / 就已经没有上限 interchangeable / 就已经只能看见一块子集 interchangeable」，会把 not already block-subset、not already no-cap、not already all-visible-is-uncapped 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 余量），先数清问的是整池可见 是不是 already block-subset / 345 / preparereturn-sold-as-trimmed，是不是能看见全部 是不是 already no-cap，还是整池都来了 是不是 already all-visible-is-uncapped，再决定要不要同一次发布。345 preparereturn vs pool bundled unbundling 在本页 item 1 启动。
