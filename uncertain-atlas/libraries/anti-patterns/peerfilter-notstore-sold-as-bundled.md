# 反模式：把 有 /store 路径 not already engine-used / not already filtering / not already settled 正式三事（326 余量） 卖成 已经是引擎在用 / 已经是过滤 / 已经交差

**层次**：实现 / Peer Filtering。  
**分类**：建议（产品）。  
**对应例**：[worked-example-peerfilter-notstore-vs-bundled.md](../../tracks/implementation/worked-example-peerfilter-notstore-vs-bundled.md)。

官方把发了 addr 过滤查询 / id 过滤查询绿了 / 有 /store 路径 三条核心句写成三件独立的实现事。把它们卖成已经是引擎在用 / 已经是过滤 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看有 /store 路径 正式三事（326 余量），必须分开 not already engine-used、not already filtering、not already settled 三件事，不要和 326 / 314 / 329 / 944 / 945 糊成一句。

## 和相邻反模式

- [peerfilter-notaddr-sold-as-bundled](peerfilter-notaddr-sold-as-bundled.md) 是 id 绿了仍未过 addr 单句边界（945 item 2），不是本页 /store 仍不是引擎在用边界。
- QueryState 已经是 ExecuteTxState 是不变量 314，不是本页 /store 仍不是过滤边界。
