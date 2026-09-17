# 反模式：把 CheckTx Usage Code≠0 rejected not in-pool gossip / not CheckTx guard bundled / not broadcast_tx received 正式三事（489 余量）说成已经流言 / 已经守卫 bundled / 已经别人也会收

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Code≠0 rejected not in-pool gossip ≠ bundled（489）](../../tracks/implementation/worked-example-chktxcodereject-notgossip-vs-bundled.md)。

## 卖法

把 Code≠0 will be rejected / 看见会拒 写成已经进了本地池就开始 P2P 流言 interchangeable / 已经 ProcessProposal REJECT 就等于池门也拒 interchangeable；把看见会拒写成已经 CheckTx 是内存池守卫（405） bundled 就代表 Code 语义已经验完 interchangeable / 405 checktxguard interchangeable；把看见 rejected 写成已经 RPC broadcast_tx 回了就代表别的节点也会收 interchangeable / 301 bundled interchangeable，或已经和 489 chktxcodereject-vs-proposal bundled / chktxcodereject-notgossip-sold-as-bundled interchangeable / 686 chktxcodereject-notgossip interchangeable。

## 为什么错

官方把 CheckTx Usage Code≠0 拒、进池流言、守卫 bundled、broadcast_tx received 写成三件独立的实现事。把它们卖成 gossip interchangeable / guard bundled interchangeable / broadcast_tx received interchangeable，会把 not gossip、not guard bundled、not broadcast_tx received 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Code≠0 rejected 正式三事（489 余量），必须分开 not gossip、not guard bundled、not broadcast_tx received 三件事，不要和 489 / 405 / 301 / 687 / 688 糊成一句。

## 和相邻反模式

- [chktxcodereject-sold-as-proposal](chktxcodereject-sold-as-proposal.md) 是 CheckTx Usage Code≠0 rejected bundled（489），不是本页 item 1 单句边界。
- [chktxcodereject-notproposal-sold-as-bundled](chktxcodereject-notproposal-sold-as-bundled.md) 是 will not be in proposal 单句边界（687 item 2），不是本页 rejected 边界。
