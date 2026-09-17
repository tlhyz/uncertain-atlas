# 模式：把 CheckTx Usage may come from another node not gossip verified / not removed from pool / not forever valid 正式三事（488 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[may come from another node not removed from pool ≠ bundled（488）](../../tracks/implementation/worked-example-chktxsource-notremoved-vs-bundled.md)。

## 三个名字

1. **may come from another node 不是流言就已经验过：** 看见 Methods Usage 能来自另一节点，不是已经 P2P 流言就代表全网已经验过 interchangeable，不是 684 chktxsource-notremoved interchangeable。
2. **能来自邻居 不是已经从池里删掉：** 看见邻居送来，不是已经提案收了就从池里删掉 interchangeable，不是 301 proposed-vs-removed interchangeable。
3. **看见邻居送来 不是 forever valid：** 看见 Usage 邻居来源，不是已经 CheckTx 过了就永远有效 interchangeable，不是 301 forever valid interchangeable。

官方把 CheckTx Usage 邻居来源、流言验完、从池里删掉、forever valid 写成三个名字。把它们叫成一个「看见邻居送来就已经从池里删掉」，会把 not gossip verified、not removed from pool、not forever valid 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from another node 正式三事（488 余量），先数清问的是 another node 是不是流言就已经验过、是不是已经从池里删掉 / 301、还是看见邻居送来 是不是 forever valid / 301，再决定要不要同一次发布。488 chktxsource vs recheck bundled unbundling 在本页 item 2 续。
