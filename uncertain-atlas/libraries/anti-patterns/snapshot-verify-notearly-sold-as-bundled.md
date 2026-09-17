# 反模式：把 装完又对上 LastBlockAppHash not already incrementally verified / not already in-network / not already settled 正式三事（332 余量） 卖成 已经在装回当中验过 / 已经进了网 / 已经交差

**层次**：实现 / Snapshot Verification。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-verify-notearly-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-verify-notearly-vs-bundled.md)。

官方把装完又对上 LastBlockAppHash / 增量验了 chunk / 封禁邻居 三条核心句写成三件独立的实现事。把它们卖成已经在装回当中验过 / 已经进了网 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完又对上 LastBlockAppHash 正式三事（332 余量），必须分开 not already incrementally verified、not already in-network、not already settled 三件事，不要和 332 / 321 / 323 / 936 / 937 糊成一句。

## 和相邻反模式

- [snapshot-conn-notgone-sold-as-bundled](snapshot-conn-notgone-sold-as-bundled.md) 是可选仍留着 state sync 对象边界（334/934），不是本页装完又对上仍不是早验边界。
- Offer 收下已经装完是不变量 321，不是本页进网前最后一次 Info 仍不是装中验边界。
