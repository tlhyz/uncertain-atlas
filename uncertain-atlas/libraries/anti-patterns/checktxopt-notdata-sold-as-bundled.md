# 反模式：把 回包码不再另有含义 not already Data used / not already consensus order / not already forked 正式三事（373 余量） 卖成 已经被引擎用了 Data / 已经是共识顺序 / 已经分叉

**层次**：实现 / CheckTx 可选。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktxopt-notdata-vs-bundled.md](../../tracks/implementation/worked-example-checktxopt-notdata-vs-bundled.md)。

官方把 CheckTx 技术上可选 / Code ≠ 0 拒收 / 回包码不再另有含义三条核心句写成三件独立的实现事。把它们卖成已经被引擎用了 Data / 已经是共识顺序 / 已经分叉，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包码不再另有含义 正式三事（373 余量），必须分开 not already Data used、not already consensus order、not already forked 三件事，不要和 373 / 317 / 489 / 688 / 381 / 786 / 806 / 807 糊成一句。

## 和相邻反模式

- [checktxopt-notinblock-sold-as-bundled](checktxopt-notinblock-sold-as-bundled.md) 是 Code≠0 拒收单句边界（807 item 2），不是本页回包码边界。
- [chktxcodereject-notothervalue-sold-as-bundled](chktxcodereject-notothervalue-sold-as-bundled.md) 是 Usage no other value 就已经用了 Data（489/688），不是本页回包码边界。
