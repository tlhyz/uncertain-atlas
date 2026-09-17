# 反模式：把 Prepare 和 Process / Finalize 同一套字段 not already ran Process / not already Finalize / not already settled 正式三事（359 余量） 卖成 已经跑过 Process / 已经 Finalize / 已经交差

**层次**：实现 / Prepare 请求字段。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-fields-notrun-vs-bundled.md](../../tracks/implementation/worked-example-prepare-fields-notrun-vs-bundled.md)。

官方把 Prepare 和 Process / Finalize 同一套字段 / local_last_commit 是上一高度的预提交带扩展 / height / time / proposer_address 对上拟议头三条核心句写成三件独立的实现事。把它们卖成已经跑过 Process / 已经 Finalize / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 和 Process / Finalize 同一套字段 正式三事（359 余量），必须分开 not already ran Process、not already Finalize、not already settled 三件事，不要和 359 / 351 / 360 / 473 / 846 / 847 糊成一句。

## 和相邻反模式

- [finprocgua-notallproc-vs-bundled](../../tracks/implementation/worked-example-finprocgua-notallproc-vs-bundled.md) 是 Finalize 时的 Process 保证（360），不是本页同一套字段边界。
- Process 也会在提议者那边叫是不变量 351，不是本页同一套字段边界。
