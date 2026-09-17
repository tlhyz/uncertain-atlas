# 反模式：把 height 默认 0 not already fresh / not already tip / not already handshake 正式三事（371 余量） 卖成 已经新鲜 / 已经跟上尖 / 已经是 Info 握手

**层次**：实现 / Query 高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-queryheight-notfresh-vs-bundled.md](../../tracks/implementation/worked-example-queryheight-notfresh-vs-bundled.md)。

官方把 Query 能查当前或过去高度 / height 默认 0 / 这个 height 含 Merkle 根三条核心句写成三件独立的实现事。把它们卖成已经新鲜 / 已经跟上尖 / 已经是 Info 握手，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 默认 0 正式三事（371 余量），必须分开 not already fresh、not already tip、not already handshake 三件事，不要和 371 / 147 / 370 / 384 / 777 / 812 / 814 糊成一句。

## 和相邻反模式

- [queryheight-notstate-sold-as-bundled](queryheight-notstate-sold-as-bundled.md) 是能查单句边界（812 item 1），不是本页默认 0 边界。
- [querycode-notfresh-sold-as-bundled](querycode-notfresh-sold-as-bundled.md) 是 Query 回包 log 就已经新鲜（384/777），不是本页默认 0 边界。
