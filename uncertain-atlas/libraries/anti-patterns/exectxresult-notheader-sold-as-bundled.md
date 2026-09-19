# 反模式：把 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事（316 余量）说成已经印进本头 / 已经进了那份哈希 / 已经是共识字段

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Code / Data not already in this header ≠ bundled（316）](../../tracks/implementation/worked-example-exectxresult-notheader-vs-bundled.md)。

## 卖法

把 Code / Data / 回了 Code 和 Data 写成已经印进本头 interchangeable / 已经 in this header interchangeable / 已经进本头 LastResultsHash interchangeable / 316 exectxresult bundled interchangeable / 147 apphash interchangeable / exectxresult-sold-as-consensus interchangeable；把 Events / 执行里产出了事件 / 按事件查询 写成已经进了那份哈希 interchangeable / 已经 in LastResultsHash interchangeable；把 Info / Log / 调试字段 写成已经是共识字段 interchangeable / 已经 consensus field interchangeable，或已经和 316 exectxresult bundled / exectxresult-sold-as-consensus interchangeable / 709 exectxresult-notheader interchangeable。

## 为什么错

官方把 Code / Data 单句、already in this header、already in LastResultsHash、already consensus field 写成三件独立的实现事。把它们卖成 already in this header interchangeable / already in LastResultsHash interchangeable / already consensus field interchangeable，会把 not already in this header、not already in LastResultsHash、not already consensus field 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事（316 余量），必须分开 not already in this header、not already in LastResultsHash、not already consensus field 三件事，不要和 316 / 147 / 707 / 708 / 33 糊成一句。

## 和相邻反模式

- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 ExecTxResult vs consensus bundled 全段，不是本页 Code/Data item 3 单句边界。
- [exectxresult-notexcluded-sold-as-bundled](exectxresult-notexcluded-sold-as-bundled.md) 是标成无效 item 2，不是本页印进本头边界。
- [exectxlog-sold-as-querylog](exectxlog-sold-as-querylog.md) 是 Log 另一卖法，不是本页 Info/Log 是否共识字段边界。
