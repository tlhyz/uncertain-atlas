# 模式：把 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事（326 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**例**：[id 绿了 not already addr-passed ≠ bundled（326）](../../tracks/implementation/worked-example-peerfilter-notaddrpassed-vs-bundled.md)。

## 三个名字

1. **id 绿了 不是 already addr-passed：** 看见 id 绿了 / 发了 `/p2p/filter/id` 绿了 / 第二道绿了，不是已经过了 addr 那一道 interchangeable / 已经 addr 也绿交差 interchangeable，不是 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable。

2. **公钥地址对上 不是 already can-interact：** 看见公钥地址对上 / 对端公钥 Address 对上 / 节点 ID 对上，不是已经能交互 interchangeable / 已经 InitPeer 交互交差 interchangeable，不是 305 initpeer interchangeable / 326 peerfilter item 1 interchangeable。

3. **拒连 不是 already persistent-ban：** 看见拒连 / 任意一道非零码 / CometBFT 拒连，不是已经写进持久封禁表 interchangeable / 已经封禁表交差 interchangeable，不是 50 banlist interchangeable / 326 peerfilter item 3 interchangeable。

官方把 id 绿了单句、already addr-passed、already can-interact、already persistent-ban 写成三个名字。把它们叫成一个「看见 id 过滤查询绿了就已经过了 addr interchangeable / 就已经能交互 interchangeable / 就已经写进持久封禁表 interchangeable」，会把 not already addr-passed、not already can-interact、not already persistent-ban 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事（326 余量），先数清问的是 id 绿了 是不是 already addr-passed / 326 / peerfilter-sold-as-connected，是不是公钥地址对上 是不是 already can-interact，还是拒连 是不是 already persistent-ban，再决定要不要同一次发布。326 peerfilter vs query bundled unbundling 在本页 item 2 续。
