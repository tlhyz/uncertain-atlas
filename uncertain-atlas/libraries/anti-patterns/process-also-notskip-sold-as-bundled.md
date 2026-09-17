# 反模式：把 Process 也会在提议者那边叫 not already no need to Process again / not already settled / not already this call 正式三事（351 余量） 卖成 已经不用再 Process / 已经交差 / 已经过了 Process

**层次**：实现 / Process 也会在提议者那边叫。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-also-notskip-vs-bundled.md](../../tracks/implementation/worked-example-process-also-notskip-vs-bundled.md)。

官方把 Process 也会在提议者那边叫 / 通常紧跟 Prepare、列表对得上 / 失败时可能对上更早一次或根本不调 三条核心句写成三件独立的实现事。把它们卖成已经不用再 Process / 已经交差 / 已经过了 Process，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 也会在提议者那边叫 正式三事（351 余量），必须分开 not already no need to Process again、not already settled、not already this call 三件事，不要和 351 / 33 / 354 / 857 / 861 / 862 糊成一句。

## 和相邻反模式

- [process-when-notlater-sold-as-bundled](process-when-notlater-sold-as-bundled.md) 是 Process 同步就已经能稍后改裁决（354/857），不是本页提议者也会叫边界。
- 四门已经结算是不变量 33，不是本页提议者也会叫边界。
