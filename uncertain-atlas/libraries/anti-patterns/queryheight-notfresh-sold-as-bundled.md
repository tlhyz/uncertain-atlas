# 反模式：把 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事（371 余量）说成已经新鲜 / 已经跟上正在跑的块 / 已经是 Info 握手那两列

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[没填 not already fresh ≠ bundled（371）](../../tracks/implementation/worked-example-queryheight-notfresh-vs-bundled.md)。

## 卖法

把没填 / `height` 默认 0 回最新已提交 / 没填高度 写成已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable / 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable；把回了最新已提交 / 回最新已提交那块的数据 / 回了最新 写成已经跟上正在跑的块 interchangeable / 已经 caught-up interchangeable / 已经跟上正在跑的块交差 interchangeable；把默认 0 / height 默认是 0 / 没填就按 0 写成已经是 Info 握手那两列 interchangeable / 已经 info-handshake interchangeable / 已经是 Info 握手那两列交差 interchangeable，或已经和 371 queryheight bundled / queryheight-sold-as-committed interchangeable / 861 queryheight-notfresh interchangeable。

## 为什么错

官方把没填、不是已经跟上正在跑的块、不是已经是 Info 握手那两列写成三件独立的实现事。把它们卖成 already fresh interchangeable / already caught-up interchangeable / already info-handshake interchangeable，会把 not already fresh、not already caught-up、not already info-handshake 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事（371 余量），必须分开 not already fresh、not already caught-up、not already info-handshake 三件事，不要和 371 / 147 / 860 / 862 糊成一句。

## 和相邻反模式

- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 queryheight bundled 全段，不是本页没填 item 2 单句边界。
- [queryheight-notquerystate-sold-as-bundled](queryheight-notquerystate-sold-as-bundled.md) 是能查 not already querystate（371 item 1），不是本页 not already fresh 边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差（147），不是本页 not already fresh 单句。
