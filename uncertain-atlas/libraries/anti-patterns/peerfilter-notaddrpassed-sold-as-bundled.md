# 反模式：把 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事（326 余量）说成已经过了 addr / 已经能交互 / 已经写进持久封禁表

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[id 绿了 not already addr-passed ≠ bundled（326）](../../tracks/implementation/worked-example-peerfilter-notaddrpassed-vs-bundled.md)。

## 卖法

把 id 绿了 / 发了 `/p2p/filter/id` 绿了 / 第二道绿了 写成已经过了 addr 那一道 interchangeable / 已经 addr-passed interchangeable / 已经 addr 也绿交差 interchangeable / 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable；把公钥地址对上 / 对端公钥 Address 对上 / 节点 ID 对上 写成已经能交互 interchangeable / 已经 can-interact interchangeable；把拒连 / 任意一道非零码 / CometBFT 拒连 写成已经写进持久封禁表 interchangeable / 已经 persistent-ban interchangeable，或已经和 326 peerfilter bundled / peerfilter-sold-as-connected interchangeable / 735 peerfilter-notaddrpassed interchangeable。

## 为什么错

官方把 id 绿了单句、already addr-passed、already can-interact、already persistent-ban 写成三件独立的实现事。把它们卖成 already addr-passed interchangeable / already can-interact interchangeable / already persistent-ban interchangeable，会把 not already addr-passed、not already can-interact、not already persistent-ban 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事（326 余量），必须分开 not already addr-passed、not already can-interact、not already persistent-ban 三件事，不要和 326 / 33 / 734 / 736 / 305 / 50 / 314 糊成一句。

## 和相邻反模式

- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是 Peer Filtering bundled 全段，不是本页 id 第二道 item 2 单句边界。
- [peerfilter-notaccepted-sold-as-bundled](peerfilter-notaccepted-sold-as-bundled.md) 是 addr 第一道 item 1，不是本页 id 绿与 addr 绿边界。
- [initpeer-sold-as-added](initpeer-sold-as-added.md) 是 InitPeer 已经能交互（305），不是本页公钥地址对上边界。
