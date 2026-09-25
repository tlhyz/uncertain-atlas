# 反模式：把这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事（371 余量）说成已经印进本头 AppHash / 已经对上 Proof / 已经是本高度交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了高度 not already apphash ≠ bundled（371）](../../tracks/implementation/worked-example-queryheight-notapphash-vs-bundled.md)。

## 卖法

把填了高度 / 这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态 / 填了 height 写成已经印进本头 AppHash interchangeable / 已经 apphash interchangeable / 已经印进本头 AppHash 交差 interchangeable / 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable；把有根 / 有应用 Merkle 根 / 根在 写成已经对上 Proof interchangeable / 已经 proof interchangeable / 已经对上 Proof 交差 interchangeable；把 Height-1 / 代表 Height-1 提交之后的状态 / Height-1 状态 写成已经是本高度交差 interchangeable / 已经 settled interchangeable / 已经是本高度交差交差 interchangeable，或已经和 371 queryheight bundled / queryheight-sold-as-committed interchangeable / 862 queryheight-notapphash interchangeable。

## 为什么错

官方把填了高度、不是已经对上 Proof、不是已经是本高度交差写成三件独立的实现事。把它们卖成 already apphash interchangeable / already proof interchangeable / already settled interchangeable，会把 not already apphash、not already proof、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事（371 余量），必须分开 not already apphash、not already proof、not already settled 三件事，不要和 371 / 147 / 325 / 860 / 861 糊成一句。

## 和相邻反模式

- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 queryheight bundled 全段，不是本页填了高度 item 3 单句边界。
- [queryheight-notquerystate-sold-as-bundled](queryheight-notquerystate-sold-as-bundled.md) 是能查 not already querystate（371 item 1），不是本页 not already apphash 边界。
- [queryheight-notfresh-sold-as-bundled](queryheight-notfresh-sold-as-bundled.md) 是默认 0 not already fresh（371 item 2），不是本页 not already proof 边界。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash（325），不是本页 not already proof 单句。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差（147），不是本页 not already apphash 单句。
