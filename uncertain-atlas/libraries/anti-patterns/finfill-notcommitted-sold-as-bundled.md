# 反模式：把 FinalizeBlock fill all fields not request complete means committed 正式三事（473 余量）卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经交差 / 已经 finfields

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock fill all fields not request complete means committed ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notcommitted-vs-bundled.md)。

## 卖法

- 「看见 all fields / request complete / 请求齐了 就已经 committed interchangeable / 已经 Finalize 改了就已经落盘 interchangeable。」
- 「看见又填一遍 就已经 Finalize 含刚决定那块的字段 interchangeable / 407 finfields interchangeable / 335 finpersist interchangeable。」
- 「看见 request complete 就已经 apply candidate / previously executed interchangeable / 583 refill not request complete means committed interchangeable。」

## 为什么错

官方把 request complete、newly decided block fields / persist decision、apply candidate / refill not committed 写成独立的实现事。把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled、已经交差、已经 finfields，会把 not request complete means committed、not finfields / finpersist、not apply candidate / refill 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not request complete means committed 正式三事（473 余量），必须分开 not request complete means committed、not finfields / finpersist、not apply candidate / refill 三个名字，不要把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经交差 / 已经 finfields。

## 和相邻反模式

- [finfill-sold-as-bundled](finfill-sold-as-bundled.md) 是 473 bundled 三事专用，不是本页 request complete not committed 单句边界。
- [finprocgua-notrefill-sold-as-bundled](finprocgua-notrefill-sold-as-bundled.md) 是 583 refill not request complete means committed 专用，不是本页 473 item 3 单句边界。
