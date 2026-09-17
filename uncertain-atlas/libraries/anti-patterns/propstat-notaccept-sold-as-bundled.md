# 反模式：把 ProposalStatus ACCEPT prevote not settled / not must Accept / not four gates 正式三事（376 余量） 说成已经交差 / 已经必须 Accept / 已经四门齐了

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ACCEPT ≠ bundled（376）](../../tracks/implementation/worked-example-propstat-notaccept-vs-bundled.md)。

## 卖法

把 ProposalStatus 这句写成已经已经交差 / 已经必须 Accept / 已经四门齐了 interchangeable，或已经和 376 proposalstatus-vs-prevote bundled / propstat-notaccept-sold-as-bundled interchangeable。

## 为什么错

官方把 ProposalStatus 三条核心句写成三件独立的实现事。把它们卖成已经交差 / 已经必须 Accept / 已经四门齐了，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus ACCEPT 正式三事（376 余量），必须分开 not settled、not must Accept、not four gates 三件事，不要和 376 / 347 / 33 / 434 / 713 / 715 糊成一句。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus bundled（376），不是本页 item 2 单句边界。
- [propstat-notunknown-sold-as-bundled](propstat-notunknown-sold-as-bundled.md) 是 UNKNOWN 单句边界（713 item 1），不是本页 ACCEPT 边界。
