# 反模式：把 必须 -1 或不超过 100 MB not already default-21 / not already bandwidth-evaluated / not already settled 正式三事（337 余量） 卖成 已经是默认 21 MB / 已经评估过带宽 / 已经交差

**层次**：实现 / BlockParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-cap-not21-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-cap-not21-vs-bundled.md)。

官方把 -1 就按 100 MB 验 / 应用自己卡体积 / 必须 -1 或不超过 100 MB 三条核心句写成三件独立的实现事。把它们卖成已经是默认 21 MB / 已经评估过带宽 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须 -1 或不超过 100 MB 正式三事（337 余量），必须分开 not already default-21、not already bandwidth-evaluated、not already settled 三件事，不要和 337 / 331 / 344 / 917 / 918 糊成一句。

## 和相邻反模式

- [maxbytes-cap-notapp-sold-as-bundled](maxbytes-cap-notapp-sold-as-bundled.md) 是应用自己卡引擎仍管单句边界（918 item 2），不是本页合法范围还不是默认 21 MB 边界。
- 证据 MaxBytes 已经是块 MaxBytes 是不变量 331，不是本页合法范围 / 默认 21 MB 边界。
