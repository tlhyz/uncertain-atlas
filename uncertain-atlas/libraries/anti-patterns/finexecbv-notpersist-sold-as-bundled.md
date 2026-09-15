# 反模式：把 FinalizeBlock When Application executes block v not persist decision / When calling guarantee 正式三事（466 余量）卖成 FinalizeBlock When Application executes block v bundled / 已经 persist decision / 已经 When calling guarantee

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When Application executes block v not persist decision / When calling guarantee ≠ bundled（466）](../../tracks/implementation/worked-example-finexecbv-notpersist-vs-bundled.md)。

## 卖法

- 「看见 Application executes block _v_ / When 第 3 步 executes block _v_ 就已经 persist decision interchangeable / 已经 FinalizeBlock When Application executes block v bundled interchangeable。」
- 「看见 Application executes block _v_ 就已经 When calling guarantee / persist decision interchangeable / 472 finwhen interchangeable。」
- 「看见 When 第 3 步 executes block _v_ 就已经 When calling guarantee not executes block v interchangeable / 572 not execbv interchangeable。」

## 为什么错

官方把 When 第 3 步 Application executes block _v_、Usage When calling guarantee、472 item 3 not executes block v 单句 写成独立的实现事。把它们卖成 FinalizeBlock When Application executes block v bundled、已经 persist decision、已经 When calling guarantee，会把 not persist decision / When calling guarantee、not 472 bundled、not 572 not execbv 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not persist decision / When calling guarantee 正式三事（466 余量），必须分开 not persist decision / When calling guarantee、not When calling guarantee / persist decision、not 572 not execbv 三个名字，不要把它们卖成 FinalizeBlock When Application executes block v bundled / 已经 persist decision / 已经 When calling guarantee。

## 和相邻反模式

- [finexecbv-sold-as-bundled](finexecbv-sold-as-bundled.md) 是 466 bundled 三事专用，不是本页 not persist decision / When calling guarantee 单句边界。
- [finwhen-sold-as-bundled](finwhen-sold-as-bundled.md) 是 472 bundled 三事专用，不是本页 466 item 1 单句边界。
- [finwhen-notexecbv-sold-as-bundled](finwhen-notexecbv-sold-as-bundled.md) 是 572（472 item 3 余量）专用，不是本页 466 item 1 单句边界。
