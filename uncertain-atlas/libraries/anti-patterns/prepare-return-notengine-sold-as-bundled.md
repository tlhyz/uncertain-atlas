# 反模式：把 Req 2 保证回的列表不让块超字节上限 not already engine trims / not already 344 overhead / not already settled 正式三事（345 余量） 卖成 已经是引擎会帮你裁 / 已经扣过头集合证据 / 已经交差

**层次**：实现 / PrepareProposal 回包上限。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-return-notengine-vs-bundled.md](../../tracks/implementation/worked-example-prepare-return-notengine-vs-bundled.md)。

官方把整池可见 / 聚合体积可以超过 max_tx_bytes / Req 2 保证回的列表不让块超字节上限 三条核心句写成三件独立的实现事。把它们卖成已经是引擎会帮你裁 / 已经扣过头集合证据 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 2 保证回的列表不让块超字节上限 正式三事（345 余量），必须分开 not already engine trims、not already 344 overhead、not already settled 三件事，不要和 345 / 344 / 33 / 878 / 879 糊成一句。

## 和相邻反模式

- [prepare-return-notover-sold-as-bundled](prepare-return-notover-sold-as-bundled.md) 是聚合超限单句边界（879 item 2），不是本页回包保证边界。
- MaxBytes 减去头集合证据才是交易上限是不变量 344，不是本页回包保证边界。
