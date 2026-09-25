# 反模式：把 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事（376 余量）说成已经能稍后改裁决 / 已经没进块 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了 REJECT not already later ≠ bundled（376）](../../tracks/implementation/worked-example-proposalstatus-notlater-vs-bundled.md)。

## 卖法

把回了 REJECT / REJECT 表示应用认为提案非法、共识会发 Prevote nil / 回了 REJECT 状态 写成已经能稍后改裁决 interchangeable / 已经 later interchangeable / 已经能稍后改裁决交差 interchangeable / 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable；把发了 nil / 共识会发 Prevote nil / 发了 Prevote nil 写成已经没进块 interchangeable / 已经 outofblock interchangeable / 已经没进块交差 interchangeable；把非法 / 应用认为提案非法 / 非法状态 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 376 proposalstatus bundled / proposalstatus-sold-as-prevote interchangeable / 877 proposalstatus-notlater interchangeable。

## 为什么错

官方把回了 REJECT、不是已经没进块、不是已经交差写成三件独立的实现事。把它们卖成 already later interchangeable / already outofblock interchangeable / already settled interchangeable，会把 not already later、not already outofblock、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事（376 余量），必须分开 not already later、not already outofblock、not already settled 三件事，不要和 376 / 354 / 876 / 875 糊成一句。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 proposalstatus bundled 全段，不是本页回了 REJECT item 3 单句边界。
- [proposalstatus-notfourgates-sold-as-bundled](proposalstatus-notfourgates-sold-as-bundled.md) 是回了 UNKNOWN not already fourgates（376 item 1），不是本页 not already later 边界。
- [proposalstatus-notsettled-sold-as-bundled](proposalstatus-notsettled-sold-as-bundled.md) 是回了 ACCEPT not already settled（376 item 2），不是本页 not already outofblock 边界。
- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 调用是同步的就已经能在返回之后再改裁决（354），不是本页 not already later 单句。
