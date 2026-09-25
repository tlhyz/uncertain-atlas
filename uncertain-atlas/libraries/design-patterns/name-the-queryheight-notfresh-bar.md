# 模式：把 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事（371 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[没填 not already fresh ≠ bundled（371）](../../tracks/implementation/worked-example-queryheight-notfresh-vs-bundled.md)。

## 三个名字

1. **没填 不是 already fresh：** 看见没填 / `height` 默认 0 回最新已提交 / 没填高度，不是已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable，不是 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable。

2. **回了最新已提交 不是 already caught-up：** 看见回了最新已提交 / 回最新已提交那块的数据 / 回了最新，不是已经跟上正在跑的块 interchangeable / 已经 caught-up interchangeable / 已经跟上正在跑的块交差 interchangeable，不是 147 apphash interchangeable / 860 queryheight-notquerystate interchangeable。

3. **默认 0 不是 already info-handshake：** 看见默认 0 / height 默认是 0 / 没填就按 0，不是已经是 Info 握手那两列 interchangeable / 已经 info-handshake interchangeable / 已经是 Info 握手那两列交差 interchangeable，不是 862 queryheight-notapphash interchangeable / 370 info-handshake interchangeable。

官方把没填、不是已经跟上正在跑的块、不是已经是 Info 握手那两列写成三个名字。把它们叫成一个「看见没填就已经新鲜 interchangeable / 就已经跟上正在跑的块 interchangeable / 就已经是 Info 握手那两列 interchangeable」，会把 not already fresh、not already caught-up、not already info-handshake 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事（371 余量），先数清问的是没填 是不是 already fresh / 371 / queryheight-sold-as-committed，是不是回了最新已提交 是不是 already caught-up，还是默认 0 是不是 already info-handshake，再决定要不要同一次发布。371 queryheight-vs-committed bundled unbundling 在本页 item 2 续。
