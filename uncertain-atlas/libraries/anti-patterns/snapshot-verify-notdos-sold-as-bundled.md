# 反模式：把 封禁邻居 not already no snapshot DoS / not already accepted-this-peer / not already settled 正式三事（332 余量） 卖成 已经没有快照 DoS / 已经收下这个人 / 已经交差

**层次**：实现 / Snapshot Verification。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-verify-notdos-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-verify-notdos-vs-bundled.md)。

官方把装完又对上 LastBlockAppHash / 增量验了 chunk / 封禁邻居 三条核心句写成三件独立的实现事。把它们卖成已经没有快照 DoS / 已经收下这个人 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看封禁邻居 正式三事（332 余量），必须分开 not already no snapshot DoS、not already accepted-this-peer、not already settled 三件事，不要和 332 / 326 / 334 / 935 / 936 糊成一句。

## 和相邻反模式

- [snapshot-verify-notanchor-sold-as-bundled](snapshot-verify-notanchor-sold-as-bundled.md) 是增量验仍不是唯一可信锚单句边界（936 item 2），不是本页封禁仍没有消掉快照 DoS 边界。
- 发了 addr 过滤查询已经收下这个人是不变量 326，不是本页封禁仍没有消掉快照 DoS 边界。
