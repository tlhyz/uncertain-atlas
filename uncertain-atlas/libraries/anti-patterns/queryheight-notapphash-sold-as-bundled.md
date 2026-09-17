# 反模式：把 height 含根 not already header AppHash / not already proof matched / not already this-height settled 正式三事（371 余量） 卖成 已经印进本头 AppHash / 已经对上 Proof / 已经是本高度交差

**层次**：实现 / Query 高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-queryheight-notapphash-vs-bundled.md](../../tracks/implementation/worked-example-queryheight-notapphash-vs-bundled.md)。

官方把 Query 能查当前或过去高度 / height 默认 0 / 这个 height 含 Merkle 根三条核心句写成三件独立的实现事。把它们卖成已经印进本头 AppHash / 已经对上 Proof / 已经是本高度交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 含根 正式三事（371 余量），必须分开 not already header AppHash、not already proof matched、not already this-height settled 三件事，不要和 371 / 325 / 383 / 781 / 380 / 790 / 812 / 813 糊成一句。

## 和相邻反模式

- [queryheight-notfresh-sold-as-bundled](queryheight-notfresh-sold-as-bundled.md) 是默认 0 单句边界（813 item 2），不是本页含根边界。
- [queryprove-notreqh-sold-as-bundled](queryprove-notreqh-sold-as-bundled.md) 是 Query 证明 height 就已经是请求高度（383/781），不是本页含根边界。
