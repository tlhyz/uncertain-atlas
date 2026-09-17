# 反模式：把 FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash 正式三事（466 余量）卖成 FinalizeBlock When Application executes block v bundled / 已经 +2/3 precommit decided / 已经 ResultHash / 已经印进本头

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash ≠ bundled（466）](../../tracks/implementation/worked-example-finexecbv-notprecommit-vs-bundled.md)。

## 卖法

- 「看见 Application executes block _v_ / 应用回了 AppHash 和各笔输出 就已经 +2/3 precommit decided interchangeable / 已经 FinalizeBlock When Application executes block v bundled interchangeable。」
- 「看见 Application executes block _v_ 就已经 +2/3 precommit same id(v) decided interchangeable / 362 +2/3 precommit interchangeable。」
- 「看见 ResultHash / 回了 AppHash 就已经印进本头 interchangeable / 335 finpersist interchangeable。」

## 为什么错

官方把 Application executes block _v_、When 流程 +2/3 precommit 决定、ResultHash / AppHash 写成独立的实现事。把它们卖成 FinalizeBlock When Application executes block v bundled、已经 +2/3 precommit decided、已经 ResultHash / 已经印进本头，会把 not +2/3 precommit decided / ResultHash、not 362 bundled、not finpersist / apphash vs this block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash 正式三事（466 余量），必须分开 not +2/3 precommit decided / ResultHash、not +2/3 precommit same id(v) decided、not committed / 本头 AppHash 三个名字，不要把它们卖成 FinalizeBlock When Application executes block v bundled / 已经 +2/3 precommit decided / 已经 ResultHash / 已经印进本头。

## 和相邻反模式

- [finexecbv-sold-as-bundled](finexecbv-sold-as-bundled.md) 是 466 bundled 三事专用，不是本页 not +2/3 precommit decided / ResultHash 单句边界。
- [finexecbv-notpersist-sold-as-bundled](finexecbv-notpersist-sold-as-bundled.md) 是 573（466 item 1 余量）专用，不是本页 466 item 3 单句边界。
- [finalizewhen-sold-as-decided](finalizewhen-sold-as-decided.md) 是 362 When 流程专用，不是本页 466 item 3 单句边界。
