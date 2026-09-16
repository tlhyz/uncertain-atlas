# 反模式：把 FinalizeBlock Contains newly decided block fields not match header 正式三事（474 余量）卖成 FinalizeBlock Contains newly decided block fields bundled / height/time match header 就代表对象已经分清 / fill all fields interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock Contains newly decided block fields not match header ≠ bundled（474）](../../tracks/implementation/worked-example-finnewdec-notmatchheader-vs-bundled.md)。

## 卖法

- 「看见 fields of the newly decided block / 看见刚决定那块的字段 就已经 height/time match header 就代表对象已经分清 interchangeable / 已经 newly decided 和 proposed 对象 interchangeable。」
- 「看见 fields of the newly decided block 就已经 fill all fields even if Prepare/Process passed interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable。」
- 「看见 fields of the newly decided block 就已经 decided_last_commit 和 proposed_last_commit 就可以混用 interchangeable / 已经 height / txs 单栏 interchangeable。」

## 为什么错

官方把 fields of the newly decided block 对象、The height and time values match the values from the header of the proposed block、Currently, CometBFT will fill up all fields 写成三件独立的实现事。把它们卖成 FinalizeBlock Contains newly decided block fields bundled、height/time match header 就代表对象已经分清、fill all fields interchangeable，会把 fields not match header、fields not fill all fields、fields not decided/proposed commit columns 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Contains newly decided block fields not match header 正式三事（474 余量），必须分开 fields not match header means objects separated、fields not fill all fields means newly decided/proposed interchangeable、fields not decided/proposed commit columns interchangeable 三个名字，不要把它们卖成 FinalizeBlock Contains newly decided block fields bundled / height/time match header 就代表对象已经分清 / fill all fields interchangeable。

## 和相邻反模式

- [finnewdec-sold-as-settled](finnewdec-sold-as-settled.md) 是 474 bundled 三事专用，不是本页 fields not match header 单句边界。
- [finnewdec-notsettled-sold-as-bundled](finnewdec-notsettled-sold-as-bundled.md) 是 559 Contains not settled，不是本页 fields vs match header 边界。
- [finnewdec-notproposed-sold-as-bundled](finnewdec-notproposed-sold-as-bundled.md) 是 560 newly decided not proposed，不是本页 474 item 3 边界。
