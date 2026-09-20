# 反模式：把发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事（326 余量）说成已经收下 / 已经过了 Query / 已经问了 id

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[发了 addr not already accepted ≠ bundled（326）](../../tracks/implementation/worked-example-peerfilter-notaccepted-vs-bundled.md)。

## 卖法

把发了 addr / 发了 `/p2p/filter/addr` / 问了 IP 和端口 写成已经收下这个人 interchangeable / 已经 accepted interchangeable / 已经收下交差 interchangeable / 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable；把 TCP 已经连上 / 连上了一个人 / TCP 通了 写成已经过了 Query interchangeable / 已经 query-passed interchangeable；把只问了地址 / 第一道是 addr / 没有问 id 写成已经问了 id interchangeable / 已经 id-asked interchangeable，或已经和 326 peerfilter bundled / peerfilter-sold-as-connected interchangeable / 734 peerfilter-notaccepted interchangeable。

## 为什么错

官方把发了 addr 单句、already accepted、already query-passed、already id-asked 写成三件独立的实现事。把它们卖成 already accepted interchangeable / already query-passed interchangeable / already id-asked interchangeable，会把 not already accepted、not already query-passed、not already id-asked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事（326 余量），必须分开 not already accepted、not already query-passed、not already id-asked 三件事，不要和 326 / 33 / 305 / 50 / 314 / 735 / 736 糊成一句。

## 和相邻反模式

- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是 Peer Filtering bundled 全段，不是本页 addr 第一道 item 1 单句边界。
- [initpeer-sold-as-added](initpeer-sold-as-added.md) 是 InitPeer 已经能交互（305），不是本页发了 addr 查询边界。
- [queryproof-notfinalapphash-sold-as-bundled](queryproof-notfinalapphash-sold-as-bundled.md) 是一层 ProofOp 根（325 item 3），不是本页邻居过滤边界。
