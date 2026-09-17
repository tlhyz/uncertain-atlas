# 反模式：把 ProposalStatus REJECT prevote nil not can change later / not already not in block / not VerifyStatus REJECT 正式三事（376 余量） 说成已经能稍后改裁决 / 已经没进块 / 已经 Verify REJECT / 已经块非法

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[REJECT ≠ bundled（376）](../../tracks/implementation/worked-example-propstat-notreject-vs-bundled.md)。

## 卖法

把 ProposalStatus 这句写成已经已经能稍后改裁决 / 已经没进块 / 已经 Verify REJECT / 已经块非法 interchangeable，或已经和 376 proposalstatus-vs-prevote bundled / propstat-notreject-sold-as-bundled interchangeable。

## 为什么错

官方把 ProposalStatus 三条核心句写成三件独立的实现事。把它们卖成已经能稍后改裁决 / 已经没进块 / 已经 Verify REJECT / 已经块非法，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus REJECT 正式三事（376 余量），必须分开 not can change later、not already not in block、not VerifyStatus REJECT 三件事，不要和 376 / 354 / 434 / 455 / 713 / 714 糊成一句。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus bundled（376），不是本页 item 3 单句边界。
- [propstat-notaccept-sold-as-bundled](propstat-notaccept-sold-as-bundled.md) 是 ACCEPT 单句边界（714 item 2），不是本页 REJECT 边界。
