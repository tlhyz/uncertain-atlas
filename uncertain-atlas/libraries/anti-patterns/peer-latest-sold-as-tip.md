# 反模式：对等节点报的 latest 被写成全网尖

> 真值：[ASA-2025-001](../../tracks/failure-museum/asa-2025-001.md)、[不变式 62](../invariants/README.md)。

## 一句话

看见邻居在 blocksync 里报了一个 `latest`，就写成链已经到了那个高度；或来源断开后仍无限去追这个数字。

## 正确写法

「目标高度必须可归因到仍连着的对等节点。来源改低或断开必须重算。邻居的 latest 不是全网尖。」
