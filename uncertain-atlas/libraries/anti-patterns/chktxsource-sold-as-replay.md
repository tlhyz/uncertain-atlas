# 反模式：把 CheckTx Usage tx source 正式三事卖成 Recheck / 已经从池里删掉 / 已经保证不重放

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[may come from external user ≠ CheckTx_Recheck](../../tracks/implementation/worked-example-chktxsource-vs-recheck.md)。

## 卖法

- 「看见 The transaction may come from an external user / 能来自外部用户 就已经是 CheckTx_Recheck 那种内存池再验 / 已经填了 tx 字节就知道是 New / 已经 RPC broadcast 就代表全网只收一次。」
- 「看见 The transaction may come from another node / 能来自另一节点 就已经流言验过 / 已经从池里删掉 / 提案收了 / CheckTx 过了就永远有效。」
- 「看见 may come from an external user or another node / 送来了 就已经保证不重放 / 已经过了 CheckTx 就有应用级重放保护 / 已经是 CheckTx 守卫余量 bundled 第二句 interchangeable。」

## 为什么错

官方把 may come from external user、may come from another node、external user or another node 写成三件独立的实现事。把它们卖成 Recheck / 已经从池里删掉 / 已经保证不重放，会把 Methods Usage 外部用户来源、邻居来源、不重放保证三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage tx source，必须分开 may come from external user、may come from another node、external user or another node 三个名字，不要把它们卖成 Recheck / 已经从池里删掉 / 已经保证不重放。

## 和相邻反模式

- [chktxtype-sold-as-recheck](chktxtype-sold-as-recheck.md) 是 Request type 就等于 Recheck，不是本页 Usage tx source 全段。
- [checktxguard-sold-as-optional](checktxguard-sold-as-optional.md) 是 CheckTx 守卫余量 bundled，不是本页 Usage tx source 专用三事。
- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是内存池去重就已经保证不重放，不是本页 may come from external user or another node 专用三事。
