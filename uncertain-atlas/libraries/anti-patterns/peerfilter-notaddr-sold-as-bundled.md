# 反模式：把 id 过滤查询绿了 not already past-addr / not already interactive / not already settled 正式三事（326 余量） 卖成 已经过了 addr / 已经能交互 / 已经交差

**层次**：实现 / Peer Filtering。  
**分类**：建议（产品）。  
**对应例**：[worked-example-peerfilter-notaddr-vs-bundled.md](../../tracks/implementation/worked-example-peerfilter-notaddr-vs-bundled.md)。

官方把发了 addr 过滤查询 / id 过滤查询绿了 / 有 /store 路径 三条核心句写成三件独立的实现事。把它们卖成已经过了 addr / 已经能交互 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 id 过滤查询绿了 正式三事（326 余量），必须分开 not already past-addr、not already interactive、not already settled 三件事，不要和 326 / 50 / 332 / 944 / 946 糊成一句。

## 和相邻反模式

- [peerfilter-notaccept-sold-as-bundled](peerfilter-notaccept-sold-as-bundled.md) 是发了 addr 仍未收下单句边界（944 item 1），不是本页 id 绿了仍未过 addr 边界。
- 自动封禁表已经有界是不变量 50，不是本页拒连仍未写进持久封禁表边界。
