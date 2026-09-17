# 反模式：把 发了 addr 过滤查询 not already accepted / not already past-id / not already settled 正式三事（326 余量） 卖成 已经收下这个人 / 已经过了 id 那一道 / 已经交差

**层次**：实现 / Peer Filtering。  
**分类**：建议（产品）。  
**对应例**：[worked-example-peerfilter-notaccept-vs-bundled.md](../../tracks/implementation/worked-example-peerfilter-notaccept-vs-bundled.md)。

官方把发了 addr 过滤查询 / id 过滤查询绿了 / 有 /store 路径 三条核心句写成三件独立的实现事。把它们卖成已经收下这个人 / 已经过了 id 那一道 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发了 addr 过滤查询 正式三事（326 余量），必须分开 not already accepted、not already past-id、not already settled 三件事，不要和 326 / 305 / 329 / 945 / 946 糊成一句。

## 和相邻反模式

- [checktx-oscillate-notsameb-sold-as-bundled](checktx-oscillate-notsameb-sold-as-bundled.md) 是本地稳住仍不是全网同一份 b 边界（328/943），不是本页发了 addr 仍未收下边界。
- InitPeer 已经能交互是不变量 305，不是本页 TCP 连上仍未过 Query 边界。
