# 反模式：把 ApplySnapshotChunk Usage refetch/ban 正式二事卖成 refetch/ban bundled / 引擎自动 refetch

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[can choose refetch/ban ≠ refetch/ban bundled](../../tracks/implementation/worked-example-applysnapusage-refetch-vs-bundled.md)。

## 卖法

- 「看见 can choose refetch chunks and/or ban P2P peers / 看见 Apply 了 chunk 回包 refetch_chunks / reject_senders 就已经 refetch/ban bundled interchangeable / 已经 RETRY interchangeable / 已经封邻居就交差。」
- 「看见 CometBFT will not do this unless instructed / 看见 refetch_chunks 列了块号就已经引擎自动 refetch interchangeable / 已经 unable retrieve 换快照 interchangeable / 已经齐 interchangeable。」

## 为什么错

官方把 can choose refetch/ban、will not do unless instructed by the application 写成两件独立的实现事。把它们卖成 refetch/ban bundled、引擎自动 refetch，会把 can choose refetch/ban、unless instructed 两条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage refetch/ban 正式二事，必须分开 can choose refetch/ban、will not do unless instructed 两个名字，不要把它们卖成 refetch/ban bundled / 引擎自动 refetch。

## 和相邻反模式

- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch 就已经齐，不是本页 will not do unless instructed 单句专用边界。
- [applysnapusage-sold-as-restored](applysnapusage-sold-as-restored.md) 是 ApplySnapshotChunk Usage verify/Info/unable 正式三事，不是本页 refetch/ban 正式二事。
- [applyretry-sold-as-refetch](applyretry-sold-as-refetch.md) 是 ApplySnapshotChunk Result RETRY bundled 三事，不是本页 can choose refetch/ban 单句专用边界。
