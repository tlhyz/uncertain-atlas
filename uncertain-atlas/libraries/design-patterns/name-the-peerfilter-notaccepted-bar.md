# 模式：把发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事（326 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**例**：[发了 addr not already accepted ≠ bundled（326）](../../tracks/implementation/worked-example-peerfilter-notaccepted-vs-bundled.md)。

## 三个名字

1. **发了 addr 不是 already accepted：** 看见发了 addr / 发了 `/p2p/filter/addr` / 问了 IP 和端口，不是已经收下这个人 interchangeable / 已经收下交差 interchangeable，不是 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable。

2. **TCP 连上 不是 already query-passed：** 看见 TCP 已经连上 / 连上了一个人 / TCP 通了，不是已经过了 Query interchangeable / 已经两道 Query 交差 interchangeable，不是 50 banlist interchangeable / 326 peerfilter item 2 interchangeable。

3. **只问了地址 不是 already id-asked：** 看见只问了地址 / 第一道是 addr / 没有问 id，不是已经问了 id interchangeable / 已经两道都问过交差 interchangeable，不是 314 querystate interchangeable / 326 peerfilter item 3 interchangeable。

官方把发了 addr 单句、already accepted、already query-passed、already id-asked 写成三个名字。把它们叫成一个「看见发了 addr 过滤查询就已经收下 interchangeable / 就已经过了 Query interchangeable / 就已经问了 id interchangeable」，会把 not already accepted、not already query-passed、not already id-asked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事（326 余量），先数清问的是发了 addr 是不是 already accepted / 326 / peerfilter-sold-as-connected，是不是 TCP 连上 是不是 already query-passed，还是只问了地址 是不是 already id-asked，再决定要不要同一次发布。326 peerfilter vs query bundled unbundling 在本页 item 1 启动。
