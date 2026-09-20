# 反模式：把本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事（328 余量）说成已经是全局同一高度 / 已经同一份 b / 已经把本地当成全局

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[本地不再振荡 not already same-b ≠ bundled（328）](../../tracks/implementation/worked-example-checktxoscillate-notsameb-vs-bundled.md)。

## 卖法

把本地 h_p,stable / 本节点稳住了 / 只属于进程 p 的稳定高 写成已经是全局同一高度 interchangeable / 已经 global-hstable interchangeable / 已经全网同一高交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable；把本节点不再振荡 / 本地不再振荡 / 本进程 OK 稳住 写成已经各节点同一份 b interchangeable / 已经 same-b interchangeable；把可以把 h_stable 看成 h_p,stable / 实现者本地化 / 一般性不丢 写成已经把本地当成全局 interchangeable / 已经 local-is-global interchangeable，或已经和 328 checktxoscillate bundled / checktxcode-sold-as-stable interchangeable / 742 checktxoscillate-notsameb interchangeable。

## 为什么错

官方把本地 h_p,stable 单句、already global-hstable、already same-b、already local-is-global 写成三件独立的实现事。把它们卖成 already global-hstable interchangeable / already same-b interchangeable / already local-is-global interchangeable，会把 not already global-hstable、not already same-b、not already local-is-global 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地不再振荡不是已经各节点同一份 b not already global-hstable / not already same-b / not already local-is-global 正式三事（328 余量），必须分开 not already global-hstable、not already same-b、not already local-is-global 三件事，不要和 328 / 33 / 313 / 740 / 741 糊成一句。

## 和相邻反模式

- [checktxcode-sold-as-stable](checktxcode-sold-as-stable.md) 是 CheckTx 最终不再振荡 bundled 全段，不是本页同一份 b item 3 单句边界。
- [checktxoscillate-nothstable-sold-as-bundled](checktxoscillate-nothstable-sold-as-bundled.md) 是 h_stable item 2，不是本页本地与全局 / 同一份 b 边界。
- [checktxoscillate-notcode-sold-as-bundled](checktxoscillate-notcode-sold-as-bundled.md) 是有码 item 1，不是本页本地化一般性边界。
