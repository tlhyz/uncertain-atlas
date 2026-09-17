# 反模式：把 16 MB 上限 not already 4 MB snapshot message / not already consensus constant / not already restored 正式三事（375 余量） 卖成 已经是快照报文 4 MB / 已经是共识常数 / 已经装完

**层次**：实现 / LoadSnapshotChunk。  
**分类**：建议（产品）。  
**对应例**：[worked-example-loadchunk-not4mb-vs-bundled.md](../../tracks/implementation/worked-example-loadchunk-not4mb-vs-bundled.md)。

官方把从邻居拉快照块 / 三列认块 / 16 MB 上限三条核心句写成三件独立的实现事。把它们卖成已经是快照报文 4 MB / 已经是共识常数 / 已经装完，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 16 MB 上限 正式三事（375 余量），必须分开 not already 4 MB snapshot message、not already consensus constant、not already restored 三件事，不要和 375 / 321 / 397 / 742 / 501 / 658 / 800 / 801 糊成一句。

## 和相邻反模式

- [loadchunk-notsame-sold-as-bundled](loadchunk-notsame-sold-as-bundled.md) 是三列认块单句边界（801 item 2），不是本页 16 MB 上限边界。
- [applychunk-notoffer-sold-as-bundled](applychunk-notoffer-sold-as-bundled.md) 是 Apply 这块就已经是 Offer（397/742），不是本页 16 MB 上限边界。
