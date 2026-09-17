# 反模式：把 增量验了 chunk not already the only trusted AppHash / not already unforgeable metadata / not already settled 正式三事（332 余量） 卖成 已经是唯一可信的 AppHash / 已经不能被伪造元数据 / 已经交差

**层次**：实现 / Snapshot Verification。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-verify-notanchor-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-verify-notanchor-vs-bundled.md)。

官方把装完又对上 LastBlockAppHash / 增量验了 chunk / 封禁邻居 三条核心句写成三件独立的实现事。把它们卖成已经是唯一可信的 AppHash / 已经不能被伪造元数据 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看增量验了 chunk 正式三事（332 余量），必须分开 not already the only trusted AppHash、not already unforgeable metadata、not already settled 三件事，不要和 332 / 38 / 334 / 935 / 937 糊成一句。

## 和相邻反模式

- [snapshot-verify-notearly-sold-as-bundled](snapshot-verify-notearly-sold-as-bundled.md) 是装完又对上仍不是早验单句边界（935 item 1），不是本页增量验仍不是唯一可信锚边界。
- 只有 AppHash 可信任是不变量 38，不是本页增量验仍不能代替最后 Info 边界。
